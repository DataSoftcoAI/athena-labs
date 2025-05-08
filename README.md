# 🔷 VGT-Core: Multi-Head Geometric Attention for Vision Graphs

> Developed by Dr. Abdulmajeed Nomman & Athena AGI Research Lab – Stanford University

**VGT-Core** is a Python module that implements **multi-head geometric attention** over graphs extracted from visual data (e.g., images, scenes). It features flexible edge modeling, geometric disentanglers, and scalable architecture for learning structured patterns in vision.

---

## 🚀 Features

- ✅ Multi-head attention with independent geometric edge modules
- 🧠 GeometryDisentangler for per-head pattern specialization
- 🔍 Modular utility toolkit: edge normalization, attention diversity loss, visualization
- ⚙️ Ready for PyTorch training pipelines
- 🔁 Designed for explainability and fine-grained pattern analysis

---

## 📦 Installation

```bash
pip install vgt-core
```

Or from source:

```bash
git clone https://github.com/DataSoftcoAI/athena-labs
cd vgt_core_pkg
pip install .
```

---

## 🧪 Quick Example

```python
from vgt_core.core.vgt_core_v0_3 import VGTCoreV03
import torch

# Sample inputs
N, D, H = 12, 16, 4
node_features = torch.randn(N, D)
edge_features = torch.randn(N, N, 4)
adj_mask = torch.ones(N, N)

# Initialize model
model = VGTCoreV03(embed_dim=D, num_heads=H, disentangle=True)

# Forward pass
output, attn_weights = model(node_features, edge_features, adj_mask)
```

---

## 🛠 Utilities

| Module | Function |
|--------|----------|
| `EdgeNormalizer` | Normalize distance/angle edge features |
| `AttentionDiversityLoss` | Enforce head-level specialization |
| `GeometryDataSynthesizer` | Generate synthetic geometric test images |
| `AttentionVisualizer` | Render head-wise graph attention maps |

---

## 🧠 Citation / Academic Use

If used in research, cite as:

```
@inproceedings{nomman2025vgt,
  title={Disentangled Geometric Attention for Structured Visual Reasoning},
  author={Nomman, Abdulmajeed and Athena AGI Team},
  year={2025},
  note={Preprint: arXiv & CVPR 2026 Submission}
}
```

---

## 📜 License

Apache 2.0 — Free for academic and commercial use with attribution.

---

**“Every pattern in nature has geometry. Every geometry tells a story worth learning by machines.” — Athena**



---
## Mini SDK:

## 🧪 Quick Start SDK

We provide a minimal package for experimentation and prototyping.

🔗 [Download Mini SDK (.zip)](https://github.com/DataSoftcoAI/athena-labs/releases/download/v0.3.0/vgt_core_mini_sdk.zip)

It includes:
- ✅ Core multi-head attention model
- ⚙️ Edge normalization utility
- 🧪 Minimal test script

> Perfect for research notebooks, classroom demos, or prototyping new attention heads.








---

##Old Version:

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
