


# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/
def A(char):
    print("")
    for i in range(7):
        for j in range(5):
            if ((j == 0 or j == 4) and i != 0) or ((i == 0 or i == 3) and (j > 0 and j < 4)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def B(char):
    print("")
    for i in range(7):
        for j in range(5):
            if (j == 0) or (j == 4 and (i != 0 and i != 3 and i != 6)) or ((i == 0 or i == 3 or i == 6) and (j > 0 and j < 4)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def C(char):
    print("")
    for i in range(7):
        for j in range(5):
            if (j == 0 and (i != 0 and i != 6)) or ((i == 0 or i == 6) and (j < 4 and j > 0)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def D(char):
    print("")
    for i in range(7):
        for j in range(5):
            if (j == 0) or (j == 4 and (i != 0 and i != 6)) or ((i == 0 or i == 6) and (j > 0 and j < 4)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def E(char):
    print("")
    for i in range(7):
        for j in range(5):
            if j == 0 or i == 0 or i == 3 or i == 6:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def F(char):
    print("")
    for i in range(7):
        for j in range(5):
            if j == 0 or i == 0 or i == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def G(char):
    print("")
    for i in range(7):
        for j in range(6):
            if j == 0 or (j == 4 and (i !=1 and i != 2)) or ((i == 0 or i == 6) and (j > 0 and j < 5)) or (i == 3 and (j != 1 and j != 2)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def H(char):
    print("")
    for i in range(7):
        for j in range(5):
            if (j == 0 or j == 4) or i == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def I(char):
    print("")
    for i in range(7):
        for j in range(5):
            if j == 2 or ((i == 0 or i == 6) and j != 2):
                print("*", end="  ")
            else:
                print(" ", end="  ")
        print("")

def J(char):
    print("")
    for i in range(7):
        for j in range(5):
            if j == 2 or i == 0 or (j == 1 and i == 6) or (j == 0 and (i == 5 or i == 4)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def K(char):
    print("")
    for i in range(7):
        for j in range(5):
            if j == 0 or (j == 1 and i == 3) or (j == 2 and (i == 2 or i == 4)) or (j == 3 and (i == 1 or i == 5)) or (j == 4 and (i == 0 or i == 6)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def L(char):
    print("")
    for i in range(7):
        for j in range(5):
            if j == 0 or i == 6:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def M(char):
    print("")
    for i in range(6):
        for j in range(5):
            if j == 0 or j == 4 or (i == 1 and (j == 1 or j == 3)) or (i == 2 and j == 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def N(char):
    print("")
    for i in range(6):
        for j in range(6):
            if (j == 0 or j == 5) or ((i == 1 and j == 1) or (i == 2 and j == 2) or (i == 3 and j == 3) or (i == 4 and j == 4) or (i == 5 and j == 5)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def O(char):
    print("")
    for i in range(7):
        for j in range(5):
            if ((j == 0 or j == 4) and (i != 0 and i != 6)) or ((i == 0 or i == 6) and (j < 4 and j > 0)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def P(char):
    print("")
    for i in range(7):
        for j in range(5):
            if j == 0 or ((i == 0 or i == 3) and (j != 4)) or ((j == 4) and (i == 1 or i == 2)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def Q(char):
    print("")
    for i in range(8):
        for j in range(6):
            if ((j == 0 or j == 4) and (i > 0 and i < 6)) or ((i == 0 or i == 6) and (j < 4 and j > 0)) or (i == 5 and j == 2) or (i == 7 and j == 4):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def R(char):
    print("")
    for i in range(8):
        for j in range(5):
            if j == 0 or ((i == 0 or i == 3) and (j != 4)) or ((j == 4) and (i == 1 or i == 2)) or (i == 4 and j == 1) or (i == 5 and j == 2) or (i == 6 and j == 3) or (i == 7 and j == 4):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def S(char):
    print("")
    for i in range(7):
        for j in range(5):
            if (i == 0 and j != 0) or (j == 0 and (i == 1 or i == 2)) or (i == 3 and (j != 0 and j != 4)) or (j == 4 and (i == 4 or i == 5)) or (i == 6 and j != 4):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def T(char):
    print("")
    for i in range(7):
        for j in range(5):
            if j == 2 or i == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def U(char):
    print("")
    for i in range(7):
        for j in range(5):
            if ((j == 0 or j == 4) and i != 6 ) or (i == 6 and (j > 0 and j < 4)):
                print("*", end="  ")
            else:
                print(" ",end="  ")
        print("")

def V(char):
    print("")
    for i in range(5):
        for j in range(9):
            if (i == 0 and (j == 0 or j == 8)) or (i == 1 and (j == 1 or j == 7)) or (i == 2 and (j == 2 or j == 6)) or (i == 3 and (j == 3 or j == 5)) or (i == 4 and (j == 4)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def W(char):
    print("")
    for i in range(6):
        for j in range(5):
            if j == 0 or j == 4 or (i ==4  and (j == 1 or j == 3)) or (i == 3 and j == 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def X(char):
    print("")
    for i in range(7):
        for j in range(7):
            if (i == 0 and (j == 0 or j == 6)) \
            or (i == 1 and (j == 1 or j == 5)) \
            or (i == 2 and (j == 2 or j == 4)) \
            or (i == 3 and j == 3) \
            or (i == 4 and (j == 2 or j == 4)) \
            or (i == 5 and (j == 1 or j == 5)) \
            or (i == 6 and (j == 0 or j == 6)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def Y(char):
    print("")
    for i in range(8):
        for j in range(7):
            if (j == 3 and (i != 0 and i != 1 and i != 2)) or (i == 0 and (j == 0 or j == 6)) or (i == 1 and (j == 1 or j == 5)) or (i == 2 and (j == 2 or j == 4)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def Z(char):
    print("")
    for i in range(6):
        for j in range(6):
            if (i == 0 or i == 5) or (i == 1 and j == 4) or (i == 2 and j == 3) or (i == 3 and j == 2) or (i == 4 and j == 1) or (i == 5 and j == 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")


name = input("Enter your name: ")
print('Program Developed By Shailendra:-')
char = []
for i in name:
    char.append(i.upper())

for j in char:
    if j == "A":
        A(char)

    if j == "B":
        B(char)

    if j == "C":
        C(char)

    if j == "D":
        D(char)

    if j == "E":
        E(char)

    if j == "F":
        F(char)

    if j == "G":
        G(char)

    if j == "H":
        H(char)

    if j == "I":
        I(char)

    if j == "J":
        J(char)

    if j == "K":
        K(char)

    if j == "L":
        L(char)

    if j == "M":
        M(char)

    if j == "N":
        N(char)

    if j == "O":
        O(char)

    if j == "P":
        P(char)

    if j == "Q":
        Q(char)

    if j == "R":
        R(char)

    if j == "S":
        S(char)

    if j == "T":
        T(char)

    if j == "U":
       U(char)

    if j == "V":
        V(char)

    if j == "W":
        W(char)

    if j == "X":
        X(char)

    if j == "Y":
        Y(char)

    if j == "Z":
        Z(char)

input()