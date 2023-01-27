"""decorator that counts how many times function has been called"""


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        return func(*args, **kwargs)
    wrapper.num_calls = 0
    return wrapper


@count_calls
def test_function():
    pass


test_function()
test_function()
print(test_function.num_calls)
