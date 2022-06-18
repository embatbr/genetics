"""Mendelian peas
"""

import random

from base import BinaryGene, Genome


class PeaGenome(Genome):
    """Pisum sativum.
    """

    def __init__(self, height: BinaryGene, pod_shape: BinaryGene, seed_shape: BinaryGene,
        peel_color: BinaryGene):
        Genome.__init__(
            self,
            [height, pod_shape, seed_shape, peel_color]
        )

    def classname(self):
        return 'PeaGenome'

    @classmethod
    def random(cls):
        gen_allele = lambda: random.choice((True, False))

        return PeaGenome(
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
    pea_1 = PeaGenome.random()
    pea_2 = PeaGenome.random()

    print('[pea_1]')
    print(pea_1)

    print()

    print('[pea_2]')
    print(pea_2)

    pea_1_2_child = PeaGenome.reproduce(pea_1, pea_2)

    print()

    print('[pea_1_2_child]')
    print(pea_1_2_child)
