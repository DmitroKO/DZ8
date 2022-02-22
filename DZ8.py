# пример 1
lst = [0,1,2,3,4,5]
print("Ваш список",lst)
s = 0
for i in range(len(lst)):
    if i %2 ==0:
        s = s + lst[i]*lst[-1]
print(s)
print("END")
print("-"* 30)

# пример 2
lst = [1,3,5]
print("Ваш список",lst)
s = 0
for i in range(len(lst)):
    if i %2 ==0:
        s = s + lst[i]*lst[-1]
print(s)
print("END")
print("-"* 30)

# пример 3
lst = [0]
print("Ваш список",lst)
s = 0
for i in range(len(lst)):
    if i %2 ==0:
        s = s + lst[i]*lst[-1]
print(s)
print("END")
print("-"* 30)
