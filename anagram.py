def anagram(w1, w2):
        w1 = w1.lower()    # Исключаем влияние регистра
        w2 = w2.lower()
        return  sorted(w1) == sorted(w2) # сортируем слова по алфавиту и сравниваем значения(Try если слова анаграммы)
print(anagram("Капот", "тапок"))
print(anagram("summer", "spring"))
