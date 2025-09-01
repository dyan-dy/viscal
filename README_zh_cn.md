<!-- [Read in English](README_en.md)

<p align="center"> 
  <img src="https://raw.githubusercontent.com/yourusername/viscal/main/docs/assets/viscal_logo.png" alt="viscal Logo" width="300">
</p>

<div align="center">
  <a href="https://pypi.org/project/viscal/" target="_blank"><img src="https://img.shields.io/badge/PyPI-0.1.0-blue.svg" height=22px></a>
  <a href="https://github.com/yourusername/viscal" target="_blank"><img src="https://img.shields.io/badge/GitHub-Repo-181717.svg?logo=github" height=22px></a>
  <!-- <a href="https://huggingface.co/spaces/yourusername/viscal-demo" target="_blank"><img src="https://img.shields.io/badge/Demo-🌐-276cb4.svg" height=22px></a>
  <a href="https://yourdocumentationurl.com" target="_blank"><img src="https://img.shields.io/badge/Docs-📖-f0ad4e.svg" height=22px></a>
  <a href="https://discord.gg/yourdiscord" target="_blank"><img src="https://img.shields.io/badge/Discord-7289da.svg?logo=discord" height=22px></a> -->
</div>

---

# viscal

**模型、数据集与计算量的 Scaling Law 可视化工具**

`viscal` 是一个轻量级 Python 包，用于可视化深度学习中的 **scaling law**。它可以帮助用户直观理解 **模型大小、数据量和计算量** 对训练损失的影响。支持 **单实例和多实例对比**，并可以显示 **相对改善百分比 (%)**。

---

## 功能

- 🔹 可视化 **模型参数、数据量和计算量** 对损失的影响  
- 🔹 支持 **相对改善 (%)** 显示，更直观理解收益  
- 🔹 支持 **多实例对比**，轻松比较不同模型/配置  
- 🔹 标注关键节点：
  - 10亿参数（1B）  
  - 代表性数据集（MNIST、CIFAR-10、ImageNet、GPT-3 语料）  
  - 代表性 FLOPs（BERT/GPT 系列）

---

## 安装

```bash
pip install viscal -->
