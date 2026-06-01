import numpy as np
from scipy import stats

def t_test_two_sample(control_data, treatment_data, alpha=0.05):
    t_stat, p_value = stats.ttest_ind(control_data, treatment_data)
    pooled_std = np.sqrt((np.var(control_data) + np.var(treatment_data)) / 2)
    cohens_d = (np.mean(treatment_data) - np.mean(control_data)) / pooled_std
    result = {
        'test_name': 'Two-Sample T-Test',
        't_statistic': t_stat,
        'p_value': p_value,
        'alpha': alpha,
        'reject_null': p_value < alpha,
        'effect_size_cohens_d': cohens_d,
        'control_mean': np.mean(control_data),
        'treatment_mean': np.mean(treatment_data),
    }
    return result

def chi_square_test(contingency_table, alpha=0.05):
    chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    result = {
        'test_name': 'Chi-Square Test',
        'chi2_statistic': chi2_stat,
        'p_value': p_value,
        'degrees_of_freedom': dof,
        'alpha': alpha,
        'reject_null': p_value < alpha,
    }
    return result

def interpret_result(result):
    print(f"\n{'='*50}")
    print(f"Test: {result['test_name']}")
    print(f"{'='*50}")
    print(f"P-value: {result['p_value']:.6f}")
    if result['reject_null']:
        print(f"\n✅ REJECT null hypothesis - Significant difference found")
    else:
        print(f"\n❌ FAIL TO REJECT null hypothesis - No significant difference")