# пример 1
lst = [0,1,2,3,4,5]
print("Ваш список",lst)
summa = 0
for i in range(len(lst)):
    if i %2 ==0:
        summa = summa + lst[i]
        number = lst[-1]
        summa1 =summa * number
print(summa1)
print("END")
print("-"* 30)

# пример 2
lst = [1,3,5]
print("Ваш список",lst)
summa = 0
for i in range(len(lst)):
    if i %2 ==0:
        summa = summa + lst[i]
        number = lst[-1]
        summa1 = summa * number
print(summa1)
print("END")
print("-"* 30)

# пример 4
lst = [6]
print("Ваш список",lst)
summa = 0
for i in range(len(lst)):
    if i %2 ==0:
        summa = summa + lst[i]
        number = lst[-1]
        summa1 = summa * number
print(summa1)
print("END")
print("-"* 30)

# пример 5
lst = []
print("Ваш список",lst)
summa = 0
for i in range(len(lst)):
    if i %2 == 0:
        summa = summa + lst[i]
        number = lst[-1]
        summa1 = summa * number
    print(summa1)
print("END")
print("-"* 30)
