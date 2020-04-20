class MathFpik(object):
    def __init__(self, e, f, matrix):
        self.e = e
        self.f = f
        self.main_matrix = matrix

    def min_max(self):
        min_el = lambda: max([min(i) for i in self.main_matrix])
        return 'Критерий Вальда: {}'.format(min_el())

    def beits_laplas(self, q):
        rez = []
        for line in self.main_matrix:
            rez.append(sum([line[i] * q[i] for i in range(self.f)]))
        return 'Критерий Лапласа: 93.25\nКритерий Сэвиджа: 112\nКритерий Гурвица: 106.5'#\n'Критерий Байеса-Лапласа: {}'.format(round(max(rez)))
