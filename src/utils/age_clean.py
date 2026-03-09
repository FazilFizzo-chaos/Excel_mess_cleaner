import math

from word2number import w2n
import pandas as pd

def clean_word_to_number(val):
    if isinstance(val, (int, float)) and not math.isnan(val):
        return int(val)

    val_str = str(val).strip().lower()
    if val_str in ("nan", "NaN"):
        return None

    try:
        num = pd.to_numeric(val_str, errors='coerce')
        if pd.notna:
         return int(num)
    except:
        pass

    try:
        return w2n.word_to_num(str(val))
    except:
            return None
