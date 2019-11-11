listy = [2, 5, 76, -4, 200, 0, 9, 2, -3, 5]

def sumnums(a_list):
    tally = 0
    for i in a_list:
        tally += i
    print(tally)
print("sum the numbers")
sumnums(listy)

def largest(a_list):
    big = a_list[0]
    for  i in a_list:
        if i > big:
            big = i
    print(big)
print("largest number")
largest(listy)

def smallest(a_list):
    small = a_list[0]
    for i in a_list:
        if i < small:
            small = i
    print(small)
print("Smallest Number")
smallest(listy)

def even(a_list):
    for i in a_list:
        if i % 2 == 0:
            print(i)
print("Even Numbers")
even(listy)

def positive(a_list):
    for i in a_list:
        if i > 0:
            print(i)
print("Positive numbers printed")
positive(listy)



def positive2(a_list):
    new_list = []
    for i in a_list:
        if i > 0:
            new_list.append(i)
    return new_list
print("Positive numbers (returned as a list)")
print(positive2(listy))

def multiply_list(a_list, factor):
    new_list = []
    for i in a_list:
        new_list.append(i * factor)
    return new_list

print("Multiply a list")
print(multiply_list(listy, 5))

def mult_vectors(a_list, b_list):
    new_list = []
    if len(a_list) != len(b_list):
        print("Lists must be the same length")
        return
    for i in range(len(a_list)):
        new_list.append(a_list[i] * b_list[i])
    return new_list

print("Multiply Vectors")
print(mult_vectors(listy, listy))

def matrixAdd(a_list, b_list):
    new_list = []
    for i in range(len(a_list)):
        new_new = []
        for j in range(len(a_list[i])):
            new_new.append(a_list[i][j] + b_list[i][j])
        new_list.append(new_new)
    return new_list

print("Matrix addition 2")
print(matrixAdd([[1,2], [3,4]], [[5, 6], [7,8]]))


