import torch
import torch.nn as nn
import torch.nn.functional as F

class GeometryDisentangler(nn.Module):
    """
    وحدة تفكيك الأنماط الهندسية داخل الرأس.
    تتعلم التمييز بين: القرب، الزاوية، التكرار، التماثل...
    """
    def __init__(self, edge_dim=4, hidden_dim=8):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(edge_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )

    def forward(self, edge_features):
        return self.mlp(edge_features).squeeze(-1)  # [N, N]

class VGTCoreV03(nn.Module):
    """
    VGT-Core v0.3: Multi-Head Geometric Attention with Geometry Disentanglers
    """
    def __init__(self, embed_dim=16, num_heads=4, edge_dim=4, disentangle=True):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        self.disentangle = disentangle

        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)

        self.edge_mlps = nn.ModuleList([
            GeometryDisentangler(edge_dim=edge_dim, hidden_dim=8)
            if disentangle else nn.Sequential(
                nn.Linear(edge_dim, 8),
                nn.ReLU(),
                nn.Linear(8, 1)
            )
            for _ in range(num_heads)
        ])

        self.output_proj = nn.Linear(embed_dim, embed_dim)
        self.dropout = nn.Dropout(0.1)
        self.layer_norm = nn.LayerNorm(embed_dim)

    def forward(self, node_features, edge_features, adj_mask):
        N = node_features.size(0)
        Q = self.q_proj(node_features).view(N, self.num_heads, self.head_dim)
        K = self.k_proj(node_features).view(N, self.num_heads, self.head_dim)
        V = self.v_proj(node_features).view(N, self.num_heads, self.head_dim)

        attention_weights = []
        head_outputs = []

        for h in range(self.num_heads):
            qh = Q[:, h]  # [N, D/H]
            kh = K[:, h]
            vh = V[:, h]

            attn_scores = torch.matmul(qh, kh.T) / (self.head_dim ** 0.5)
            edge_scores = self.edge_mlps[h](edge_features)  # [N, N]
            total_scores = attn_scores + edge_scores

            # Masking
            masked_scores = total_scores * adj_mask - 1e10 * (1 - adj_mask)
            attn = F.softmax(masked_scores, dim=-1)
            attention_weights.append(attn)

            out = torch.matmul(attn, vh)  # [N, D/H]
            head_outputs.append(out)

        combined = torch.cat(head_outputs, dim=-1)
        output = self.output_proj(combined)
        output = self.dropout(self.layer_norm(output))

        return output, torch.stack(attention_weights)
