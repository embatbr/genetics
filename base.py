""" Base code for Mendelian genetics.
"""

import random


class Gene(object):
    """Gene is the super class for all Gene objects.
    """

    def __init__(self, trait: str, allele_1: bool, allele_2: bool,
        possible_phenotypes: tuple):
        """@trait: e.g., color of pea
           @allele_1: true if is dominant, false if recessive
           @allele_2: true if is dominant, false if recessive
           @possible_phenotypes: tuple with possible phenotypes
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
        """Observable characteristic for the trait the Gene object represents.
        Basically, the outcome of the gene.
        """
        raise NotImplementedError()

    def split(self):
        return (self.allele_1, self.allele_2)


class GeneInDominance(Gene):
    """Defines a gene which behavior is of dominance. The possible phenotypes are
    onyle two: (1) dominant (when there is at least one dominant allele) and
    recessive (when both are recessive).
    """

    def __init__(self, trait: str, allele_1: bool, allele_2: bool,
        possible_phenotypes: tuple):
        assert len(possible_phenotypes) == 2, 'Must be in format (recessive, DOMINANT)'

        Gene.__init__(self, trait, allele_1, allele_2, possible_phenotypes)

    @property
    def phenotype(self):
        """Observable characteristic for the trait the Gene object represents.
        Basically, the outcome of the gene.
        """
        return self.possible_phenotypes[int(self.allele_1 or self.allele_2)]


# TODO GeneInCodominance
# TODO GeneInIncompleteDominance


class Genotype(object):
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
    def genome(self):
        """Collection of traits in a specific order form a Genome. Organisms with
        same genome can reproduce.
        """
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

    def reproduce(genotype_1, genotype_2):
        for (gene_1, gene_2) in zip(genotype_1.genes, genotype_2.genes):
            assert gene_1.__class__ == gene_2.__class__, 'Genomes must be the same'
        assert genotype_1.__class__ == genotype_2.__class__, 'Genomes must be the same'
        assert genotype_1.genome == genotype_2.genome, 'Genomes must be the same'

        genotype_1_alleles = random.choice(genotype_1.split())
        genotype_2_alleles = random.choice(genotype_2.split())
        genome = genotype_1.genome
        possible_phenotypes = genotype_1.possible_phenotypes

        zipped = zip(genome, genotype_1_alleles, genotype_2_alleles, possible_phenotypes)

        new_genes = list()
        i = 0
        for (trait, allele_1, allele_2, phenotypes) in zipped:
            gene_class = genotype_1.genes[i].__class__

            new_gene = gene_class(trait, allele_1, allele_2, phenotypes)
            new_genes.append(new_gene)

            i = i + 1

        return Genotype(new_genes)
