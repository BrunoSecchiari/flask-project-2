from datetime import date
from typing import Tuple


def get_current_date(current_date: date = date.today()) -> Tuple:
    month = current_date.strftime("%m")
    quarter = (int(month) - 1) // 3 + 1
    year = current_date.strftime("%Y")

    return current_date, month, quarter, year
