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
