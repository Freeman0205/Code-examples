

def palindrome(word=input("Введите слово для проверки:")):
    word = word.lower()
    if word[::-1] == word:
        print("Это палиндром!")
    else:
        print("Это не палиндром!")
palindrome()





