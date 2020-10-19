#count

from itertools import count

try:
    start = int(input("Введите любое целое число: "))
    stop = int(input("Введите завершающее целое число: "))

except ValueError:
    print("Это не число. Выходите")
    exit(1)

if start > stop:
    for el in count(start, -1):
        if el < stop:
            break
        print(el)

for el in count(start):
   if el > stop:
       break
   else:
    print(el)



#cycle

from itertools import cycle

my_list = [123, False, True, "QAZ", "123"]
count_ = 0
for el in cycle(my_list):
    if count_ > 14:
        break
    print(el)
    count_ += 1



