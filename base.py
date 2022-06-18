""" Base code for Mendelian genetics.
"""

import random


class BinaryGene(object):
    """A BinaryGene object is composed of the particular trait it defines, its
    two alleles and the traits shown (with only two options).
    """

    def __init__(self, trait: str, allele_1: bool, allele_2: bool,
        traits_shown: tuple):
        """@trait: e.g., color of pea (green or yellow)
           @allele_1: true if is dominant, false if recessive
           @allele_2: true if is dominant, false if recessive
           @traits_shown: tuple with traits in format (recessive, DOMINANT)
        """
        self.trait = trait
        self.allele_1 = allele_1
        self.allele_2 = allele_2
        self.traits_shown = traits_shown

    def __str__(self):
        return '{} ({},{}) {}'.format(self.trait, self.allele_1, self.allele_2,
            self.trait_shown())

    def trait_shown(self):
        return self.traits_shown[int(self.allele_1 or self.allele_2)]

    def split(self):
        return (self.allele_1, self.allele_2)


class Genome(object):
    """A collection of Gene objects.
    """

    def __init__(self, genes: list):
        self.genes = genes

    def __str__(self):
        ret = ''

        traits_shown = self.traits_shown()

        for gene in self.genes:
            ret = '{}{}\n'.format(ret, str(gene))

        return ret

    def traits_shown(self):
        return {
            gene.trait: gene.trait_shown()
            for gene in self.genes
        }

    # TODO fix: add 'trait'
    # def split(self):
    #     """Independent assortment.
    #     """
    #     splitted_genes = [
    #         random.sample(gene.split(), 2)
    #         for gene in self.genes
    #     ]

    #     alleles_1 = list(map(lambda x: x[0], splitted_genes))
    #     alleles_2 = list(map(lambda x: x[1], splitted_genes))

    #     return (alleles_1, alleles_2)


class GenomeCarrier(object):
    """Base object that carries a genome.
    """

    def __init__(self, genome: Genome):
        self.genome = genome

    def classname(self):
        raise NotImplementedError()

    def __str__(self):
        return '{}\n{}'.format(self.classname(), str(self.genome))

    def traits_shown(self):
        return self.genome.traits_shown()

# TODO create a class GenomeCarrier, with methods "reproduce" and "random", and
# serving as base for all carriers (e.g., Pea class).
