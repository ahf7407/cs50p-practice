# CS50P week 0 - lecture 0, part 2 (2026-11-18)
# print parameters (end, sep), quotes, f-strings, strip/title, split

# 1. end: stay on the same line
print("hello, ", end="")
print("world")

# 2. sep: choose what goes between values
print("a", "b", "c", sep="-")

# 3. quotes inside quotes
print('hello, "friend"')      # outer single, inner double
print("hello, \"friend\"")    # escape with backslash

# 4. f-string
name = "amir"
age = 19
print(f"{name} is {age} years old")

# 5. clean up user input
name = input("what's your name? ").strip().title()
print(f"hello, {name}")

# 6. split a full name and greet by first name
full_name = input("full name? ").strip().title()
first, last = full_name.split(" ")
print(f"hello, {first}")
