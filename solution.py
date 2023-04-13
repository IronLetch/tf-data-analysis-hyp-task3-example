import pandas as pd
import numpy as np


chat_id = 531503618 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:  # Одна или две выборке на входе, заполняется исходя из условия

    _, pvalue = w.ztest(x, y, value=500, alternative='larger')

    return pvalue <= 0.04
