import torch

class EdgeNormalizer:
    def __init__(self, eps=1e-5):
        self.eps = eps

    def normalize(self, edge_feats):
        dist = edge_feats[..., 0]
        dist = (dist - dist.mean()) / (dist.std() + self.eps)
        edge_feats[..., 0] = dist
        return edge_feats
