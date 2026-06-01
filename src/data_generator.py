import numpy as np
import pandas as pd

def generate_ab_test_data(n_control=1000, n_treatment=1000, 
                          control_mean=50, treatment_mean=55,
                          control_std=10, treatment_std=10,
                          random_seed=42):
    np.random.seed(random_seed)
    control_group = np.random.normal(control_mean, control_std, n_control)
    treatment_group = np.random.normal(treatment_mean, treatment_std, n_treatment)
    df = pd.DataFrame({
        'user_id': range(n_control + n_treatment),
        'group': ['control'] * n_control + ['treatment'] * n_treatment,
        'metric_value': np.concatenate([control_group, treatment_group])
    })
    return df

def generate_categorical_data(n_samples=500):
    np.random.seed(42)
    data = {
        'converted': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
        'version': np.random.choice(['A', 'B'], n_samples, p=[0.5, 0.5])
    }
    return pd.DataFrame(data)