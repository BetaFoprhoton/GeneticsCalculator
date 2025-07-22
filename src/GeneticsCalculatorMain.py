from GeneticsData import *
from Util import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.font_manager import FontProperties

gene1 = Gene(
    name = "种子颜色",
    alleles = ["Y", "y"]
)
gene2 = Gene(
    name = "种子形状",
    alleles = ["R", "r"]
)
geno1 = Genotype([gene1, gene2])

#print(geno1.genGamete())
#print(test_cross_geno.genGamete())

env = GeneticsEnv()
env.defAllele(("Y", "y"))
env.defAllele(("R", "r"))
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
print(crowd1.genotype_dict)
print(crowd1.transStrPhenotype(env))
#crowd1.printGenotypeInfo(env)
crowd1.printPhenotypeInfo(env)
crowd = crowd1.transStrPhenotype(env)


a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

plt.rcParams['font.family'] = 'Alibaba PuHuiTi 2.0'  # 替换为你选择的字体
plt.bar(crowd.keys(), crowd.values())
plt.show()