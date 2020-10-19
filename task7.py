def fact(a):
    result = 1
    for i in range(1, a + 1):
        yield result
        result *= i
    yield result
for el in fact(0):
    print(el)




from functools import reduce

#fact = int(input("Введите число: "))

#def my_func(prev_el, i):
#    return prev_el * i

#print(reduce(my_func, range(1,fact + 1)))