# Used to generate post title
from random import randint


class TitleGeneration:
    @staticmethod
    def title_generation(title):
        return title + '_' + str(randint(1000, 10000))
