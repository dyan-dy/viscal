import numpy as np
import matplotlib.pyplot as plt
from .utils import relative_improvement

def scaling_loss(N, D, C, L_inf=0.05, A=10.0, alpha=0.3, B=5.0, beta=0.2, C0=2.0, gamma=0.25):
    return L_inf + A/N**alpha + B/D**beta + C0/C**gamma

def plot_scaling_curves(instances, show_relative=True):
    """
    Plot three subplots: Model Size / Dataset Size / Compute
    instances: list of dicts, each with keys:
        - name: str
        - N: int
        - D: int
        - C: float
    """
    plt.figure(figsize=(18,5))
    colors = ['blue','orange','green','red','purple','brown']

    # Model Size
    plt.subplot(1,3,1)
    for i, inst in enumerate(instances):
        N_values = np.logspace(6, 10, 50)
        loss_curve = scaling_loss(N_values, inst["D"], inst["C"])
        y = relative_improvement(loss_curve) if show_relative else loss_curve
        plt.plot(N_values, y, marker='o', linestyle='-', color=colors[i%len(colors)], label=inst["name"])
    plt.xscale('log')
    plt.xlabel("Model Parameters N (count)")
    plt.ylabel("Relative Improvement (%)" if show_relative else "Loss")
    plt.title("Model Size")
    plt.grid(True)
    plt.axvline(x=1e9, color='red', linestyle='--')
    plt.text(1e9*1.05, 10, "1B parameters", color='red', rotation=90, va='bottom')
    plt.legend()

    # Dataset Size
    plt.subplot(1,3,2)
    for i, inst in enumerate(instances):
        D_values = np.logspace(4, 12, 50)
        loss_curve = scaling_loss(inst["N"], D_values, inst["C"])
        y = relative_improvement(loss_curve) if show_relative else loss_curve
        plt.plot(D_values, y, marker='s', linestyle='-', color=colors[i%len(colors)], label=inst["name"])
    plt.xscale('log')
    plt.xlabel("Dataset Size D (samples/tokens)")
    plt.ylabel("Relative Improvement (%)" if show_relative else "Loss")
    plt.title("Dataset Size")
    plt.grid(True)

    key_datasets = {"MNIST":6e4, "CIFAR-10":5e4, "ImageNet":1.2e6, "OpenWebText":4e7, "GPT-3 corpus":3e11}
    offsets = [2,5,0,0,0]
    for (name, val), off in zip(key_datasets.items(), offsets):
        plt.axvline(x=val, color='purple', linestyle='--')
        plt.text(val*1.05, off, name, color='purple', rotation=90, va='bottom')

    plt.legend()

    # Compute
    plt.subplot(1,3,3)
    for i, inst in enumerate(instances):
        C_values = np.logspace(12, 24, 50)
        loss_curve = scaling_loss(inst["N"], inst["D"], C_values)
        y = relative_improvement(loss_curve) if show_relative else loss_curve
        plt.plot(C_values, y, marker='^', linestyle='-', color=colors[i%len(colors)], label=inst["name"])
    plt.xscale('log')
    plt.xlabel("Compute C (FLOPs)")
    plt.ylabel("Relative Improvement (%)" if show_relative else "Loss")
    plt.title("Compute")
    plt.grid(True)

    key_FLOPs = {"BERT-base":1e20, "GPT-2":3e21, "GPT-3":3e23}
    for name, val in key_FLOPs.items():
        plt.axvline(x=val, color='purple', linestyle='--')
        plt.text(val*1.1, 10, name, color='purple', rotation=90, va='bottom')

    plt.legend()
    plt.tight_layout()
    plt.show()
