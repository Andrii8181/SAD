import json
import pandas as pd

def save_project(df, value_col, factor_col, method, filename="SAD_Проєкт.sadproj"):
    """
    Зберігає проєкт у форматі JSON.
    """
    project_data = {
        "data": df.to_dict(orient="list"),
        "value_col": value_col,
        "factor_col": factor_col,
        "method": method
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(project_data, f, ensure_ascii=False, indent=4)

def load_project(filename="SAD_Проєкт.sadproj"):
    """
    Завантажує проєкт з JSON-файлу.
    Повертає DataFrame і параметри.
    """
    with open(filename, "r", encoding="utf-8") as f:
        project_data = json.load(f)
    df = pd.DataFrame(project_data["data"])
    value_col = project_data["value_col"]
    factor_col = project_data["factor_col"]
    method = project_data["method"]
    return df, value_col, factor_col, method
