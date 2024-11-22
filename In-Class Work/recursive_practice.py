# Recursive Practice 11-22-24

# Question 2 - First Rule Break Index
def r_frbi(lista, listb, index):
    if index == len(lista):
        return -1
    if index % 3 == 0 and lista[index] in listb:
        return index
    if index % 3 == 1 and lista[index] not in listb:
        return index
    if index % 3 == 2 and lista[index] != lista[index]:
        return index
    else:
        return r_frbi(lista, listb, index + 1)

def defsettings_r_frbi(lista, listb):
    return r_frbi(lista, listb, 0)

# print(defsettings_r_frbi(list_a, list_b))

# Test 1 - PASS!
# list_a = [8, 4, 3, 5, 1, 6]
# list_b = [1, 2, 3, 4, 5, 6]
# Returns 3

# Test 2 - PASS!
# list_a = [1, 2, 3]
# list_b = [9, 2, 3]
# Returns -1


# Question 1 - Double Digits
def r_doubledigits(s, index):
    if index == len(s):
        return ""
    if s[index].isdigit():
        return s[index] + s[index] + r_doubledigits(s, index + 1)
    else:
        return s[index] + r_doubledigits(s, index + 1)

def defsettings_r_doubledigits(s):
    return r_doubledigits(s, 0)

# Test 1 - PASS!
# str = "ab34c5"
# Returns "ab3344c55"

# Test 2 - PASS!
# str = "1test2test3"
# Returns "11test22test33"

# print(defsettings_r_doubledigits(str))
