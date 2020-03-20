sad=[1,2,3]
funny=[5,2,6]
for fun in funny:         #для ключей
    for key in sad:       #для значений
        if key==fun:      #сравнение
            print (fun, 'Найдено')
            break
    else:
        print(fun, 'ничего не найдено')
            
