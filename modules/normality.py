import scipy.stats as stats

def check_normality(series):
    """
    Перевірка нормальності розподілу даних за тестом Шапіро-Вілка.
    Повертає словник з результатом і рекомендаціями.
    """
    stat, p = stats.shapiro(series.dropna())
    is_normal = p >= 0.05

    recommendation = """
    **Що це означає?**  
    Розподіл показника значно відхиляється від нормального.  
    **Рекомендації:**  
    - Використати непараметричні методи (Краскел-Уолліса, Манна-Уїтні)  
    - Провести трансформацію даних (логарифмування, ранжування)
    """

    return {
        "is_normal": is_normal,
        "p_value": p,
        "recommendation": recommendation if not is_normal else ""
    }
