"""Mendelian peas
"""

import random

from base import Gene, Genome


class Pea(object):
    """Pisum sativum.
    """

    def __init__(self, height: Gene, pod_shape: Gene, seed_shape: Gene,
        peel_color: Gene):
        self.genome = Genome([height, pod_shape, seed_shape, peel_color])

    def __str__(self):
        return 'Pea\n{}'.format(str(self.genome))

    def traits_shown(self):
        return self.genome.traits_shown()

    @classmethod
    def random(cls):
        gen_allele = lambda: random.choice((True, False))

        return Pea(
            height=Gene(
                'height', gen_allele(), gen_allele(), ('short', 'tall')
            ),
            pod_shape=Gene(
                'pod_shape', gen_allele(), gen_allele(), ('constricted', 'inflated')
            ),
            seed_shape=Gene(
                'seed_shape', gen_allele(), gen_allele(), ('winkled', 'smooth')
            ),
            peel_color=Gene(
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
