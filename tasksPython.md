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

6. Есть 2 множества A = {3, 5, 11, 7, 4 -3}, B = {11, 5, 8, 1, 10, 7}. Вывести в консоль элементы A, которых нет в B.

>```
> A = {3, 5, 11, 7, 4, -3}
> B = {11, 5, 8, 1, 10, 7}
> print(A.difference(B))

7. Есть строка a = “a14b6fh”, как узнать, что все символы уникальны, используя множества и списки?

> ```
> a = 'a14b6fh'
> b = set(a)
> if len(a) == len(b):
>     print('В строке нет повторяющихся символов.')
> else:
>     print('Есть повторяющиеся символы.')

8. Есть словарь: d = {‘a’:3, ‘b’:0, ‘c’:4, ‘d’:-3}. Найти самое большое число из значений словаря.

> ```
> d = {'a': 3, 'b': 0, 'c': 4, 'd': -3}
> values = d.values()
> big_number = d['a']
> for i in values:
>    if i > big_number:
>         big_number = i
> print(big_number)

9. Есть словарь: d = {‘a’:3, ‘b’:hello, ‘c’:4, ‘d’:-3}. Найти самое большое число из значений словаря.

> ```
> d = {'a': 3, 'b': 'hello', 'c': 4, 'd': -3}
> values = d.values()
> big_number = d['a']
> for i in values:
>     if type(i) == int:
>         if i > big_number:
>             big_number = i
> print(big_number)
