from fractions import Fraction
from itertools import product
from functools import reduce
from operator import mul
from Util import *

class Allele:
    def __init__(self, name: str):
        self.name = name

    def gen(self) -> Fraction:
        if self.name == "a":
            return Fraction(1, 2)
        return Fraction(1, 1)

class Gene:
    def __init__(self, alleles: list[Allele], name: str, description: str = ""):
        self.name = name
        self.alleles = alleles
        
    def gen(self) -> dict:   
        group = {}
        for allele in self.alleles:
            proportion = allele.gen()
            if proportion > 1:
                raise ValueError("proportion cannot bigger than 1")
            if group.get(allele.name, "null") == "null":
                group[allele.name] = proportion
            else:
                group[allele.name] += proportion
        return unifiedDenominator(group)
        
class Genotype:
    def __init__(self, genes: list[Gene]):
        self.genes = genes
    
    def __hash__(self):
        return hash(frozenset((g, tuple(sorted(alleles))) for g, alleles in self.genes.items()))
    
    def __eq__(self, other):
        return self.genes == other.genes
        
    def genGamete(self) -> dict:
        dicts = [gene.gen() for gene in self.genes]
    
        # 1. 准备每个字典的键值对列表（保持顺序）
        result = {}
        items_list = []
        for d in dicts:
            # 对每个字典，转换为(键, 值)元组列表
            # 注意：这里使用sorted()确保顺序一致性
            items_list.append(sorted(d.items()))
        
        # 2. 计算所有字典项的笛卡尔积
        for combination in product(*items_list):
            # combination是元组
            
            # 3. 提取键列表和值列表
            keys = [item[0] for item in combination]  # ['A', 'X', 'P']
            values = [item[1] for item in combination]  # [Fraction(1,2), ...]
            
            # 4. 计算所有Fraction的乘积
            product_value = reduce(mul, values, Fraction(1, 1))
            
            # 5. 使用元组作为键（列表不可哈希）
            result[tuple(keys)] = product_value
        return result

    def cross(self, other: Genotype):
        pass
        