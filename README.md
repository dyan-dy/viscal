<!-- [Read in Chinese](README_zh_cn.md) -->

<!-- <p align="center"> 
  <img src="https://raw.githubusercontent.com/yourusername/viscal/main/docs/assets/viscal_logo.png" alt="viscal Logo" width="300">
</p> -->

<div align="center">
  <a href="https://pypi.org/project/viscal/" target="_blank"><img src="https://img.shields.io/badge/PyPI-0.1.0-blue.svg" height=22px></a>
  <a href="https://github.com/yourusername/viscal" target="_blank"><img src="https://img.shields.io/badge/GitHub-Repo-181717.svg?logo=github" height=22px></a>
  <!-- <a href="https://huggingface.co/spaces/yourusername/viscal-demo" target="_blank"><img src="https://img.shields.io/badge/Demo-🌐-276cb4.svg" height=22px></a> -->
  <!-- <a href="https://yourdocumentationurl.com" target="_blank"><img src="https://img.shields.io/badge/Docs-📖-f0ad4e.svg" height=22px></a> -->
  <!-- <a href="https://discord.gg/yourdiscord" target="_blank"><img src="https://img.shields.io/badge/Discord-7289da.svg?logo=discord" height=22px></a> -->
</div>


# viscal

**Scaling Law Visualization for Model, Dataset, and Compute**

`viscal` is a lightweight Python package designed to visualize **scaling laws** in deep learning. It helps users intuitively understand how **model size, dataset size, and compute** affect training loss. Supports **single-instance and multi-instance comparisons** with relative improvement (%) display.



## Features

- 🔹 Visualize the effect of **model parameters, dataset size, and compute** on loss  
- 🔹 Supports **relative improvement (%)** for intuitive understanding  
- 🔹 Supports **multi-instance comparison** to easily compare different models/configurations  
- 🔹 Annotates key points:
  - 1B parameters
  - Representative datasets (MNIST, CIFAR-10, ImageNet, GPT-3 corpus)
  - Representative FLOPs (BERT/GPT series)



## Installation

```bash
pip install viscal
```
Or for local development:
```bash
git clone https://github.com/yourusername/viscal.git
cd viscal
pip install .
```


## Usage
### Single Instance
```python
from viscal.viz import plot_scaling_curves

instance = [
    {"name": "MyModel", "N": 1e8, "D": 1e6, "C": 1e15}
]

plot_scaling_curves(instance)
```
### Multi-Instance Comparison
```python
from viscal.viz import plot_scaling_curves

instances = [
    {"name": "Small Model", "N": 1e7, "D": 1e6, "C": 1e15},
    {"name": "Medium Model", "N": 1e8, "D": 1e7, "C": 1e16},
    {"name": "Large Model", "N": 1e9, "D": 1e8, "C": 1e17},
]

plot_scaling_curves(instances)
```


## Parameters
| Parameter | Description                          |
| --------- | ------------------------------------ |
| N         | Model parameter count                |
| D         | Dataset size (samples/tokens)        |
| C         | Training FLOPs (forward × 2 × steps) |
| name      | Instance name for legend             |


## Dependencies

Python ≥ 3.8\
numpy\
matplotlib\
torch\
ptflops

```python
pip install numpy matplotlib torch ptflops
```


## Example Output
![loss curve](assets\loss_curve.png "loss curve")
![improvement curve](assets\improve_curve.png "improvement curve")
- Three subplots:
    - Model Size: Loss / Relative Improvement vs N
    - Dataset Size: Loss / Relative Improvement vs D
    - Compute: Loss / Relative Improvement vs C
- Each curve represents one instance
- Supports multi-instance comparison
- Key points annotated (1B params, datasets, FLOPs)

## Contribution

Contributions are welcome:

Support for direct PyTorch model input to automatically compute parameters and FLOPs

Support for dynamic/non-parameterized models with range curves

Improved visualization (marginal gain arrows, gradient bands)

Please submit PRs or open Issues.


## License
MIT License