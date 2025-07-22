from fractions import Fraction
from itertools import product
from functools import *
import functools
from operator import mul
from Util import *

class Gene:
    def __init__(self, alleles: list[str], name: str = "", description: str = ""):
        self.name = name
        self.alleles = alleles
        
    def gen(self) -> dict:   
        group = {}
        for allele in self.alleles:
            proportion = 1 #暂时
            if proportion > 1:
                raise ValueError("proportion cannot bigger than 1")
            if group.get(allele, "null") == "null":
                group[allele] = proportion
            else:
                group[allele] += proportion
        return unifiedDenominator(group)
        
class Genotype:
    def __init__(self, genes: tuple[Gene]):
        self.genes = genes
    
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


class GeneticsEnv:
    def __init__(self):
        self.alleles_dom_info = [] #相对显隐性关系
        self.alleles_group_info = {} #等位基因关系
        self.lethal_func_info = []
        self.pheno_func_info = []
        self.group_count = 0

    def printAllelesInfo(self):
        print("Relative hidden relationship between alleles:")
        for allele_dom in self.alleles_dom_info:
            print("( ", end = "")
            for allele in allele_dom.keys():
                print(allele, end = " ")
            print(")", end = "\n")

    def defAllele(self, alleles: tuple[str]):
        count = 0
        dom_dict = {}
        for allele in alleles:
            dom_dict[allele] = count
            self.alleles_group_info[allele] = self.group_count
            count += 1
        self.alleles_dom_info.append(dom_dict)
        self.group_count += 1

    def defGenotypeLethal(self, *func):
        self.lethal_func_info += func

    def defPhenotypeTransLaw(self, *func):
        self.pheno_func_info += func

    def toPhenotype(self, str_gene_list: list[str]) -> tuple[str]:
        pheno_list = []
        for pheno_func in self.pheno_func_info:
            pheno_list.append(pheno_func(str_gene_list))
        return tuple(sorted(pheno_list))

    def genGenotypeLethanlChance(self, str_gene_list: list[str]) -> float:
        shrink = Fraction(1, 1)
        for lethanl_func in self.lethal_func_info:
            shrink *= lethanl_func(str_gene_list)
            #print("Genotype: ", str_gene_list, " has change its proprotion to: ", str(shrink))
        return shrink

    def domCmp(self, a, b):
        if self.isRelativeDominant(a, b):
            return -1
        else:
            return 1

    def isRelativeDominant(self, allele1: str, allele2: str):
        for reg_alleles in self.alleles_dom_info:
            if (allele1 in reg_alleles.keys()) and (allele2 in reg_alleles.keys()):
                return reg_alleles[allele1] < reg_alleles[allele2]
        return "Not Allele"
        
    def toGenotype(self, geno_str_list: list[str]) -> Genotype:
        grouped_geno_list = [[] for _ in range(10)]
        for geno_str in geno_str_list:
            index = self.alleles_group_info.get(geno_str, "null")
            if index == "null":
                raise ValueError("Cannot find allele: \"" + geno_str + "\" in this environment.")
            grouped_geno_list[index].append(geno_str)
        result = []
        for group in grouped_geno_list:
            if (group != []):
                result.append(Gene(sorted(group, key = functools.cmp_to_key(self.domCmp))))
        return Genotype(result)

    def toGenotypeString(self, genotype: Genotype) -> str:
        str_geno = ""
        for gene in genotype.genes:
            #print(gene.alleles)
            for allele in gene.alleles:
                #print(allele, end = " ")
                if len(allele) > 1:
                    str_geno += "(" + allele + ")"
                else:
                    str_geno += allele
        return str_geno

    def toPhenotypeString(self, genotype: Genotype) -> str:
        gene_list = []
        for gene in genotype.genes:
            gene_list += gene.alleles
        if gene_list == []:
            return "Unknown"
        return "".join(self.toGenotype(gene_list))

class Population:
    genotype_dict = {}
    def __init__(self, genotype_dict):
        self.genotype_dict = genotype_dict
    
    def transStrGenotype(self, env: GeneticsEnv) -> dict:
        new_dict = {}
        for geno_item in self.genotype_dict.items():
            geno_str = env.toGenotypeString(env.toGenotype(geno_item[0]))
            new_dict[geno_str] = geno_item[1]
        return new_dict

    def transStrPhenotype(self, env: GeneticsEnv) -> dict:
        pheno_dict = {}
        for geno_item in self.genotype_dict.items():
            phenotype = env.toPhenotype(geno_item[0])
            phenotype = "".join(phenotype)
            if pheno_dict.get(phenotype, "null") == "null":
                pheno_dict[phenotype] = geno_item[1]
            else:
                pheno_dict[phenotype] += geno_item[1]
        return pheno_dict
    
    def printGenotypeInfo(self, env: GeneticsEnv):
        geno_dict = self.transStrGenotype(env)
        for genotype in geno_dict.items():
            print(genotype[0], ": ", genotype[1].numerator, "/", genotype[1].denominator, end = "\t")

    def printPhenotypeInfo(self, env: GeneticsEnv):
        pheno_dict = self.transStrPhenotype(env)
        for phenotype in pheno_dict.items():
            print(phenotype[0], ": ", phenotype[1].numerator, "/", phenotype[1].denominator, end = "\t")

def alt_sort_key(s) -> tuple:
    # 0 - 大写字母, 1 - 小写字母
    case_order = 0 if s.isupper() else 1
    return (s.lower(), case_order)

def cross(geno1: Genotype, geno2: Genotype, env: GeneticsEnv) -> Population:
    gamete_dict1 = geno1.genGamete()
    gamete_dict2 = geno2.genGamete()
    crowd = {}
    for gamete_item1 in gamete_dict1.items():
        for gamete_item2 in gamete_dict2.items():
            genotype = tuple(sorted(list(gamete_item1[0]) + list(gamete_item2[0]), key = alt_sort_key))
            proportion = gamete_item1[1] * gamete_item2[1]
            if crowd.get(genotype, "null") == "null":
                crowd[genotype] = proportion
            else:
                crowd[genotype] += proportion
    result = {}
    for geno_item in crowd.items():
        new_chance = geno_item[1] * env.genGenotypeLethanlChance(geno_item[0])
        if new_chance != 0:
            result[geno_item[0]] = new_chance
        else:
            if result.get(geno_item[0], "null") != "null":
                result.pop(geno_item[0])
    return Population(unifiedDenominator(result))

def selfing(genotype: Genotype, env: GeneticsEnv) -> Population:
    return cross(genotype, genotype, env)