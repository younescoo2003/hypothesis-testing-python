import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_distributions(control_data, treatment_data, save_path=None):
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.hist(control_data, alpha=0.5, label='Control', bins=30, density=True)
    plt.hist(treatment_data, alpha=0.5, label='Treatment', bins=30, density=True)
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title('Distribution Comparison')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.boxplot([control_data, treatment_data], labels=['Control', 'Treatment'])
    plt.ylabel('Value')
    plt.title('Box Plot Comparison')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()