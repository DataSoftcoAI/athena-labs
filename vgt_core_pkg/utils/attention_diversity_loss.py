import torch
import torch.nn as nn

class AttentionDiversityLoss(nn.Module):
    def forward(self, attention_heads):
        H = attention_heads.size(0)
        loss = 0
        for i in range(H):
            for j in range(i+1, H):
                loss += torch.norm(attention_heads[i] - attention_heads[j], p=2)
        return loss / (H * (H - 1) / 2)
