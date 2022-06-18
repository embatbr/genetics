"""Mendelian peas
"""

import random

from base import BinaryGene, Genotype


class PeaGenotype(Genotype):
    """Pisum sativum.
    """

    def __init__(self, height: BinaryGene, pod_shape: BinaryGene, seed_shape: BinaryGene,
        peel_color: BinaryGene):
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
            height=BinaryGene(
                'height', gen_allele(), gen_allele(), ('short', 'tall')
            ),
            pod_shape=BinaryGene(
                'pod_shape', gen_allele(), gen_allele(), ('constricted', 'inflated')
            ),
            seed_shape=BinaryGene(
                'seed_shape', gen_allele(), gen_allele(), ('winkled', 'smooth')
            ),
            peel_color=BinaryGene(
                'peel_color', gen_allele(), gen_allele(), ('yellow', 'green')
            )
        )


if __name__ == '__main__':
    pea_1 = PeaGenotype.random()
    pea_2 = PeaGenotype.random()

    print('[pea_1]')
    print(pea_1)

    print()

    print('[pea_2]')
    print(pea_2)

    pea_1_2_child = PeaGenotype.reproduce(pea_1, pea_2)

    print()

    print('[pea_1_2_child]')
    print(pea_1_2_child)
