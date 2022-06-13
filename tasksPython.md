1. На вход дается любое число. Узнать скольки разрядов в числе - оно (1, 2, 3 или более значное), положительное или отрицательное? Например, 25 — это двузначное положительное, а -345 это трехзначное отрицательное, а 2400 это 3х и более значное положительное. 0 учитывать как отдельный вариант, а не как однозначное число.
> ```
> num = 25  
> if num < -99:  
>     print('Отрицательное трехзначное число')  
> elif num >= -99 and num <= -9:  
>     print('Отрицательное двухзначное число')  
> elif num >= -9 and num < 0:  
>     print('Отрицательное однозначное число')  
> elif num >= 1 and num <= 9:  
>     print('Положительное однозначное число')  
> elif num >= 10 and num <= 99:  
>     print('Положительное двухзначное число')  
> elif num >= 100:  
>     print('Положительное трехзначное число')  
> else:  
>     print('Вы ввели 0')

2. Есть список а = [2, 4, 65, 32, 2, 6, 0, -1, 3]. Вывести все значения меньше 5 в консоль.
> ```
> a = [2, 4, 65, 32, 2, 6, 0, -1, 3]
> for i in a:
>    if i < 5:
>        print('Число', i, "меньше 5")

3. Написать систему очереди обслуживания клиентов

> ```
> customers = ["Filip", "Miranda", "Ariah", "Laurence", "Shahid"]
> free_counters = [11, 20, 14, 6, 4]
> customers.sort()
> free_counters.sort()
> customer = customers[0]
> counter = free_counters[0]
> print(customer)
> print("Visit counter:")
> print(counter)

4. “aabbаа” - палиндром. Как это проверить?

> ```
> string = 'aabbaa'
> reversed_string = ''.join(reversed(string))
> print(string == reversed_string)

5. На основании списка a = [‘red’, ‘yellow’, ‘blue’, ‘bread’]. Создать список, в котором будет только слово, лишнее в списке a.

>```
> a = ['red', 'yellow', 'blue', 'bread']
> b = []
> for i in a:
>    if i != 'red' and i != 'yellow' and i != 'blue':
>        removed_element = a.pop()
>        b.append(removed_element)
> print(a)
> print(b)
