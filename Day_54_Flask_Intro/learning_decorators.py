import time


def delay_function(function):
    def wrapper_function():
        time.sleep(3)
        function()
        function()
        time.sleep(2)

    return wrapper_function


@delay_function
def say_hello():
    print("Hello")

@delay_function
def say_bye():
    print("bye")


def say_paaji():
    print("paaji")


say_hello()
say_bye()

# delayed_funciton = delay_function(say_paaji)
# delayed_funciton()