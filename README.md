# athena-labs
Athena labs(AGI)

# VGT - Vision Geometry Transformer

**Multi-Head Geometric Attention for Vision-based Graph Models**  
Developed by [Dr. Abdulmajeed Nomman](https://github.com/DataSoftcoAI/athena-labs) and Athena Research Team

---

## 📌 Overview

VGT is a PyTorch module implementing a **Multi-Head Geometric Attention** mechanism. It is designed for graph-based computer vision models that represent images as spatial graphs (keypoints and geometric relations).

This package is part of the VGT-Core v0.2 project.

---

## 🔍 Key Features

- Multi-head attention over image-based graphs
- Learnable edge embeddings (distance, angle, orientation)
- LayerNorm + Dropout for stability
- Modular design, easy integration with GNN pipelines
- Ideal for shape analysis, sketch recognition, or structural vision tasks

---

## 🛠 Installation

```bash
pip install vgt
```

Or from source:

```bash
git clone https://github.com/DataSoftcoAI/athena-labs/VGT-Core-v0.2
cd VGT-Core-v0.2
pip install .
```

---

## 🚀 Usage

```python
from vgt.multihead_geometric_attention import MultiHeadGeometricAttention

model = MultiHeadGeometricAttention(embed_dim=16, num_heads=4)

output, attn_weights = model(
    node_features,      # Tensor [N, D]
    edge_features,      # Tensor [N, N, 4]
    adj_mask            # Tensor [N, N] (binary mask)
)
```

---

## 📊 Input Format

- `node_features`: Features for each keypoint/node in the image.
- `edge_features`: Geometric relations (distance, angle, cos, sin).
- `adj_mask`: Binary adjacency matrix representing graph connectivity.

---

## 🧠 Research Applications

- Structural image classification
- Sketch-based search and retrieval
- Scene graph modeling
- Robotics: object part understanding
- Human pose as graph with geometric links

---

## 📚 Citation

If you use this package in your research, please cite:

```
@software{vgt2025,
  author = {Abdulmajeed Nomman , Athena (AGI) Team},
  title = {VGT - Vision Geometry Transformer},
  year = {2025},
  url = {https://github.com/DataSoftcoAI/athena-labs/VGT-Core-v0.2}
}
```

---

## 🔗 Project Repository

[GitHub Repository → VGT-Core v0.2](https://github.com/DataSoftcoAI/athena-labs/VGT-Core-v0.2)

---
*"لكل عين صناعية... عدسة ترى من زاوية مختلفة، ومعًا نرى بوضوح أكثر." — أثينا*
