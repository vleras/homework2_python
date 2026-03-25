import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print("Execution time:", end - start)
        return result
    return wrapper


@timer
def even_numbers():
    result = []

    for i in range(1, 10):
        if i % 2 == 0:
            result.append(i)

    return result


nums = even_numbers()