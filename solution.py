import pandas as pd
import numpy as np

import statsmodels.stats.weightstats as w

chat_id = 531503618 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:

    alpha = 0.04

    _, p_value = proportions_ztest(

        [x_success, y_success], [x_cnt, y_cnt], alternative="smaller"

    )

    return p_value <= alpha
