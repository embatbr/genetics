"""Mendelian peas
"""

import random

from base import GeneInDominance, Genotype


class PeaGenotype(Genotype):
    """Pisum sativum.
    """

    def __init__(self, height: GeneInDominance, pod_shape: GeneInDominance, seed_shape: GeneInDominance,
        peel_color: GeneInDominance):
        Genotype.__init__(
            self,
            [height, pod_shape, seed_shape, peel_color]
        )

    def classname(self):
        return 'PeaGenotype'

    @classmethod
    def random(cls):
        gen_allele = lambda: random.choice((True, False))

        return PeaGenotype(
            height=GeneInDominance(
                'height', gen_allele(), gen_allele(), ('short', 'tall')
            ),
            pod_shape=GeneInDominance(
                'pod_shape', gen_allele(), gen_allele(), ('constricted', 'inflated')
            ),
            seed_shape=GeneInDominance(
                'seed_shape', gen_allele(), gen_allele(), ('winkled', 'smooth')
            ),
            peel_color=GeneInDominance(
                'peel_color', gen_allele(), gen_allele(), ('yellow', 'green')
            )
        )


if __name__ == '__main__':
    pea_1 = PeaGenotype.random()
    pea_2 = PeaGenotype.random()

    print('[pea_1]')
    print('genome:', pea_1.genome)
    print(pea_1)

    print()

    print('[pea_2]')
    print('genome:', pea_2.genome)
    print(pea_2)

    pea_1_2_child = PeaGenotype.reproduce(pea_1, pea_2)

    print()

    print('[pea_1_2_child]')
    print('genome:', pea_1_2_child.genome)
    print(pea_1_2_child)
