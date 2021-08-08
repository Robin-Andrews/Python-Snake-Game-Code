# Global vs. local variables
name = 'Susan'
print(name)


def print_name():
    name = 'Peter'
    print(name)


print_name()
print(name)
