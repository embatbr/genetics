"""Mendelian peas
"""

import random

from base import BinaryGene, Genome, GenomeCarrier


class Pea(GenomeCarrier):
    """Pisum sativum.
    """

    def __init__(self, height: BinaryGene, pod_shape: BinaryGene, seed_shape: BinaryGene,
        peel_color: BinaryGene):
        GenomeCarrier.__init__(
            self,
            Genome([height, pod_shape, seed_shape, peel_color])
        )

    def classname(self):
        return 'Pea'

    @classmethod
    def random(cls):
        gen_allele = lambda: random.choice((True, False))

        return Pea(
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
    pea_1 = Pea.random()
    pea_2 = Pea.random()

    print('[pea_1]')
    print(pea_1)

    print('[pea_2]')
    print(pea_2)

    # pea_1_2_child = Pea.reproduce(pea_1, pea_2)
