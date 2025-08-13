import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import scikit_posthocs as sp

def run_analysis(df, value_col, factor_col, method):
    """
    Виконує статистичний аналіз залежно від вибраного методу.
    Повертає таблицю результатів та силу впливу факторів.
    """
    result = {}

    # ANOVA
    model = ols(f'{value_col} ~ C({factor_col})', data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    result["table"] = anova_table

    # Сила впливу η²
    eta_sq = anova_table["sum_sq"][:-1] / anova_table["sum_sq"].sum()
    result["effect_size"] = pd.DataFrame({
        "Фактор": eta_sq.index,
        "η²": eta_sq.values
    })

    # Пост-хок тести
    if method == "Тест Тьюкі":
        tukey = pairwise_tukeyhsd(endog=df[value_col], groups=df[factor_col], alpha=0.05)
        result["table"] = pd.DataFrame(data=tukey.summary().data[1:], columns=tukey.summary().data[0])

    elif method == "НІР (LSD)":
        from statsmodels.stats.multicomp import MultiComparison
        mc = MultiComparison(df[value_col], df[factor_col])
        lsd_result = mc.allpairtest(sm.stats.ttest_ind, method='bonf')[0]
        result["table"] = pd.DataFrame(lsd_result.data[1:], columns=lsd_result.data[0])

    elif method == "Тест Данкана":
        result["table"] = sp.posthoc_duncan(df, val_col=value_col, group_col=factor_col)

    elif method == "Бонфероні":
        result["table"] = sp.posthoc_conover(df, val_col=value_col, group_col=factor_col, p_adjust="bonferroni")

    return result
