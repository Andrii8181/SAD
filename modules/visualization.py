import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplot(df, value_col, factor_col):
    """
    Побудова boxplot-графіка для показника по рівнях фактора.
    Повертає matplotlib-фігуру.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x=factor_col, y=value_col, data=df, ax=ax)
    ax.set_title(f"Розподіл показника '{value_col}' по фактору '{factor_col}'", fontsize=14)
    ax.set_xlabel(factor_col, fontsize=12)
    ax.set_ylabel(value_col, fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig
