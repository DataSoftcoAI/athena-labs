import matplotlib.pyplot as plt
import networkx as nx

class AttentionVisualizer:
    def plot_attention(self, G, pos, attn_matrix, head_idx):
        plt.figure(figsize=(8,8))
        weights = attn_matrix[head_idx].detach().numpy()
        nx.draw_networkx_nodes(G, pos, node_size=10)
        nx.draw_networkx_edges(G, pos, width=1,
            edge_color=weights.flatten(), edge_cmap=plt.cm.inferno)
        plt.title(f"Head {head_idx} Attention")
        plt.axis('off')
        plt.show()
