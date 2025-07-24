from fractions import *

def unifiedDenominator(input_dict: dict) -> dict:
    """统一传入的字典values的除数以便使其和为1"""
    deno_sum = sum(input_dict.values())
    result = {}
    for name, value in input_dict.items():
        result[name] = Fraction(value, deno_sum)
    return result

def alt_sort_key(s):
    """排序键函数"""
    # 0 - 大写字母, 1 - 小写字母
    case_order = 0 if s.isupper() else 1
    return (s.lower(), case_order)