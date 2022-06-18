""" Base code for Mendelian genetics.
"""

import random


class BinaryGene(object):
    """A BinaryGene object is composed of the particular trait it defines, its
    two alleles and the possible phenotypes (with only two options).
    """

    def __init__(self, trait: str, allele_1: bool, allele_2: bool,
        possible_phenotypes: tuple):
        """@trait: e.g., color of pea
           @allele_1: true if is dominant, false if recessive
           @allele_2: true if is dominant, false if recessive
           @possible_phenotypes: tuple with possible phenotypes in format
           (recessive, DOMINANT), e.g., green or yellow
        """
        self.trait = trait
        self.allele_1 = allele_1
        self.allele_2 = allele_2
        self.possible_phenotypes = possible_phenotypes

    def __str__(self):
        return '{} ({},{}) {}'.format(self.trait, self.allele_1, self.allele_2,
            self.phenotype)

    @property
    def phenotype(self):
        """Observable characteristic for the trait the BinaryGene object represents.
        Basically, the outcome of the gene.
        """
        return self.possible_phenotypes[int(self.allele_1 or self.allele_2)]

    def split(self):
        return (self.allele_1, self.allele_2)


class Genome(object):
    """A collection of Gene objects.
    """

    def __init__(self, genes: list):
        self.genes = genes

    def __str__(self):
        ret = [str(gene) for gene in self.genes]
        return '\n'.join(ret)

    @property
    def possible_phenotypes(self):
        return [gene.possible_phenotypes for gene in self.genes]

    @property
    def phenotype(self):
        return [gene.phenotype for gene in self.genes]

    @property
    def traits(self):
        return [gene.trait for gene in self.genes]

    def split(self):
        """Independent assortment.
        """
        splitted_genes = [
            random.sample(gene.split(), 2)
            for gene in self.genes
        ]

        alleles_1 = list(map(lambda x: x[0], splitted_genes))
        alleles_2 = list(map(lambda x: x[1], splitted_genes))

        return (alleles_1, alleles_2)

    def reproduce(genome_1, genome_2):
        assert genome_1.traits == genome_2.traits, 'Genomes must have same traits'

        genome_1_alleles = random.choice(genome_1.split())
        genome_2_alleles = random.choice(genome_2.split())
        traits = genome_1.traits
        possible_phenotypes = genome_1.possible_phenotypes

        zipped = zip(traits, genome_1_alleles, genome_2_alleles, possible_phenotypes)

        new_genes = list()
        for (trait, allele_1, allele_2, phenotypes) in zipped:
            new_gene = BinaryGene(trait, allele_1, allele_2, phenotypes)
            new_genes.append(new_gene)

        return Genome(new_genes)
