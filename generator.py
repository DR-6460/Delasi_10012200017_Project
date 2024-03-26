from random import choice


def generate(length: int, alphabet: bool, number: bool, symbol: bool):
    """
    Returns a randomly generated password with the specified number of words and the specified type of characters.
    :param length: The length of the generated password
    :param alphabet: Whether alphabets should be part of the password
    :param number: Whether numbers should be part of the password
    :param symbol: Whether symbols should be part of the password
    """

    values = [i for i in range(33, 126)]
    values.remove(96)
    values.remove(124)

    values_alpha = []
    values_num = []
    values_sym = []

    for x in range(0, 89):
        if chr(values[x]).isalpha():
            values_alpha.append(values[x])

    for x in range(0, 89):
        if chr(values[x]).isnumeric():
            values_num.append(values[x])

    for x in range(0, 91):
        if values[x] not in values_num:
            if values[x] not in values_alpha:
                values_sym.append(values[x])

    password = ""

    sym_limit = 0

    for x in range(0, length):
        pool = []
        if alphabet:
            pool.extend(values_alpha)

        if number:
            pool.extend(values_num)

        if symbol and sym_limit < (length // 3):
            pool.extend(values_sym)
        elif not alphabet and not number:
            pool.extend(values_sym)

        var = choice(pool)
        password += chr(var)

        if var in values_sym:
            sym_limit += 1

    return password


print(generate(length=5, alphabet=False, number=False, symbol=True))

"""
print("Alpha")
list_alpha = []
for x in values_alpha:
    list_alpha.append(chr(x))
print(values_alpha)
print(list_alpha)

print("Num")
list_num = []
for x in values_num:
    list_num.append(chr(x))
print(values_num)
print(list_num)

print("Sym")
print(values_sym)
print("[", end="")
for x in values_sym:
    print(f"'{chr(x)}'", end=", ")
print("]")

print("All")
print(values)

var1 = list(range(33, 127, 1))
# var1.pop(index)
# var1.remove(value)
var = random.choice(var1)
print(var)
print(chr(var))
"""
