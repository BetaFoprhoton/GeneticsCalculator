from fractions import *

def unifiedDenominator(input_dict: dict) -> dict:
    deno_sum = sum(input_dict.values())
    result = {}
    for name, value in input_dict.items():
        result[name] = Fraction(value, deno_sum)
    return result