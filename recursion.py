def sparrows_on_the_roof(bob):
    """ Печатает текст песенки про 99 воробьев на крыше.
        :param bob: Должно быть целым числом.
    """
    if bob < 1:
        print("""Нет воробьев на крыше.
Нет воробьев.""")
        return
    tmp = bob
    bob -= 1
    print("""{} воробьев сидят на крыше. {} воробьев.
Один испугался, с крыши умчался, {} воробьев на крыше осталось.
          """.format(tmp,
                     tmp,
                     bob))
    sparrows_on_the_roof(bob)


sparrows_on_the_roof(99)
