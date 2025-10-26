from GeneticsCalculatorLib import *
from Util import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import Visualization

gene1 = Gene("Y", "y")
gene2 = Gene("R", "r")
geno1 = Genotype(gene1, gene2)

#print(geno1.genGamete())
#print(test_cross_geno.genGamete())

env = GeneticsEnv()
env.defAllele("Y", "y")
env.defAllele("R", "r")
def lethanl1(geno_str_list) -> Fraction:
    if "a" in geno_str_list and "b" in geno_str_list:
        return Fraction(1, 2)
    else:
        return Fraction(1, 1)
def pheno1(pheno_str_list) -> str:
    if "Y" in pheno_str_list:
        return "黄色"
    elif "y" in pheno_str_list:
        return "绿色"
def pheno2(pheno_str_list) -> str:
    if "R" in pheno_str_list:
        return "圆粒"
    elif "r" in pheno_str_list:
        return "皱粒"
#env.defGenotypeLethal(lethanl1, lethanl2)
#env.defGenotypeLethal(lethanl1)
env.defPhenotypeTransLaw(pheno1, pheno2)
crowd1 = selfing(geno1, env)
#print(crowd1.genotype_dict)
#print(crowd1.transStrPhenotype(env))
#crowd1.printGenotypeInfo(env)

crowd1.printPhenotypeInfo(env)
crowd1.printGenotypeInfo(env)
pheno_dict = crowd1.transStrPhenotype(env)

Visualization.ShowGrapgh(pheno_dict)

#print(Gender.Female == Gender.Male)

env = GeneticsEnv()
env.defAllele("A", "a")
env.defAllele("X", "Y")
def pheno_gender(str_list):
    if str_list.count("X") == 2:
        return Gender.Female.value
    elif str_list.count("X") == 1 and str_list.count("Y") == 1:
        return Gender.Male.value
    else:
        return Gender.Unknown.value
def pheno_normal(str_list):
    if "A" in str_list:
        return "显性"
    else:
        return "隐性"
env.defPhenotypeTransLaw(pheno_gender)
env.defPhenotypeTransLaw(pheno_normal)
gender_fe = Genotype(Gene("A", "a"), Gene("X", "X"))
gender_ma = Genotype(Gene("A", "a"), Gene("X", "Y"))
crowd_gender = cross(gender_fe, gender_ma, env)
#Visualization.ShowGrapgh(crowd_gender.transStrPhenotype(env))

gene_sex = Gene("A", sex_chromosome = "X")
gene_normal = Gene("B", "b")
dict_sitest = Genotype(gene_sex, gene_normal).genGamete()

test = str(SexGeneGroup("X", ["A", "a"]))
test2 = str(SexGeneGroup("Y", []))
print(str(SexGeneGroup.fromString(test)))
print(str(SexGeneGroup.fromString(test2)))