class Sequence:

    def __init__(self, name, seq):
        self._name = name
        self._seq = seq
        if not hasattr(self, '_alphabet'):#hastter
            self._alphabet = dict(zip(set(seq), [0] * len(set(seq))))

    # будет возращать частоту  встречаемости символов в последовательности
    def frequencies(self):
        self._frequencies = {sym: self._seq.count(sym) for sym in self._alphabet}
        return self._frequencies

    # возвращает название последовательности, string
    def name1(self):
        return self._name

    # возвращает последовательность, string
    def sequence(self):
        return self._seq

    # возвращает длину последовательности, int
    def __len__(self):
        return len(self._seq)

    def __getitem__(self, key):
        return self._seq[key]

    # Задание !!!!!! (11) #

    def change1(self, rule):
        self._seq = ''.join(list(map(rule, self._seq)))

                    # Задание !!!!!!!!!!(12) #

    def change2(self, rule):
        self.__new_seq = []
        for i in range(len(self._seq)):
            self.__new_seq.extend(rule(self._seq[i - 1], self[i]))
        self._seq = ''.join(self.__new_seq)
        del self.__new_seq
