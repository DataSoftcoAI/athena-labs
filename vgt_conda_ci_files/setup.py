from setuptools import setup, find_packages

setup(
    name="vgt_core",
    version="0.3.0",
    packages=find_packages(),
    install_requires=["torch", "numpy", "networkx"],
    author="Dr. Abdulmajeed Nomman",
    description="Multi-head Geometric Attention for Vision Graphs",
)
