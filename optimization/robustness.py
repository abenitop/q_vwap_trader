import numpy as np

def monte_carlo_sqn(returns, iterations=1000):
    if len(returns) < 20: return 0.0
    sqns = []
    for _ in range(iterations):
        sample = np.random.choice(returns, size=len(returns), replace=True)
        avg_r = np.mean(sample)
        std_r = np.std(sample)
        sqn = (avg_r / std_r) * np.sqrt(len(sample)) if std_r > 0 else 0
        sqns.append(sqn)
    return np.percentile(sqns, 5)
