# CS50P week 0 - lecture 0, part 4 (2026-11-21)
# def, parameters, default values, main(), scope


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
