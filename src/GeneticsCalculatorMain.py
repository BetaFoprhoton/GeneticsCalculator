from GeneticsData import *
from Util import *
import matplotlib.pyplot as plt
import numpy as np

gene1 = Gene(
    name = "test",
    alleles = ["A", "a"]
)
gene2 = Gene(
    name = "test2",
    alleles = ["B", "b"]
)
gene3 = Gene(
    name = "test3",
    alleles = ["C", "c"]
)
geno1 = Genotype([gene1, gene2])
test_cross_geno = Genotype([
    Gene(["a", "a"]),
    Gene(["b", "b"])
])

print(geno1.genGamete())
print(test_cross_geno.genGamete())

env = GeneticsEnv()
env.defAllele(("A", "a"))
env.defAllele(("B", "b"))
def lethanl1(geno_str_list) -> Fraction:
    if "a" in geno_str_list and "b" in geno_str_list:
        return Fraction(1, 2)
    else:
        return Fraction(1, 1)
def lethanl2(geno_str_list) -> Fraction:
    if "A" in geno_str_list and "A" in geno_str_list:
        return Fraction(1, 2)
    else:
        return Fraction(1, 1)
env.defGenotypeLethal(lethanl1, lethanl2)
crowd1 = selfing(geno1, env)
print(crowd1.genotype_dict)
crowd1.printGenotypeInfo(env)
crowd = crowd1.transStrGenotype(env)

plt.bar(crowd.keys(), crowd.values())
plt.show()