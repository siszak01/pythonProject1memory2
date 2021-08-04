def f(*args, **kwargs):
    s = 0

    list_args = list(args) + list(kwargs.values())

    for i in list_args:
        # if isinstance(i, int) or isinstance(i, float):
        if type(i) in [int, float]:
            s += i
        elif type(i) == list:
            s += f(*i)

    return s


print(f(1, 1, 1, 1, ))


def g(n):
     if n == 0:
         return 0, 0, 0

     total_sum, even_sum, odd_sum =g(n - 1)
     total_sum += n
     if n % 2 == 0:
         even_sum += n
     else:
         odd_sum += n

     return total_sum, even_sum, odd_sum


print(g(5))



def pirnt_integer(a):

    if a is int(a):
        return (a)

    else:
        return (0)

print (pirnt_integer(2.3))







