def fizz_buzz():
    for x in range (101):

        if x%3==0 and x%5==0:
            print(x, "fizzbuzz")

        elif x%3==0:
            print (x, "fizz")
        elif x%5==0:
            print (x, "buzz")

        else:
            print (x, 'Не подходит под условия')

fizz_buzz()
