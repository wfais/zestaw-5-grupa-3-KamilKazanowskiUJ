from itertools import product

def flatten_tuple(nested_tuple):
    result = []
    for item in nested_tuple:
        if isinstance(item, tuple):
            result.extend(flatten_tuple(item))
        else:
            result.append(item) 
    return result


def hyperproduct(lists):
    if len(lists) == 1:
        c = []
        for num in lists[0]:
            c.append((num, 0))    
        return c

    a = lists[0]
    for i in range(1, len(lists)):
        a = list(product(a, lists[i]))

    b = []
    for item in a:
        b.append(tuple(flatten_tuple(item)))
    return b


def S_function(iterable, M):
    sum = 0
    for item in iterable:
        sum += item**2
    
    return sum % M


def maximize_expression(K, M, lists):
    products = hyperproduct(lists)
    max_expr = 0
    for item in products:
        n = S_function(item, M)
        if n > max_expr:
            max_expr = n
    
    return max_expr


if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
