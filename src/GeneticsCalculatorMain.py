from GeneticsData import *
from Util import *

f1 = Fraction(3, 2)
f2 = Fraction(f1, 3)
print(f2)

tuple1 = (2, 3)
print(tuple1[1])
Allele("a")

gene1 = Gene(
    name = "test",
    alleles = [Allele("A"), Allele("a"), Allele("a")]
)
gene2 = Gene(
    name = "test2",
    alleles = [Allele("B"), Allele("b")]
)
gene3 = Gene(
    name = "test3",
    alleles = [Allele("C"), Allele("Cx"), Allele("c")]
)
geno1 = Genotype([gene1, gene2])

print(geno1.genGamete())

dict1 = {
    "A": Fraction(1, 5),
    "b": Fraction(2, 4),
    "C": Fraction(3, 9)
}
print(unifiedDenominator(dict1))