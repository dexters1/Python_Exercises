""" 
Funkcija koja odredjuje zajednicki delilac dva broja
"""
def zajednicki_delilac(num1, num2):

    while not(num1 == 0 or num2 == 0):
        if(num1 >= num2):
            num1 = num1 - num2
        elif(num2 >= num1):
            num2 = num2 - num1

    if(num1 > num2):
        return num1
    else:
        return num2

"""
Funkcija koja trazi dva broja za trazenje zajednickog delioca
"""
def dodela_delilaca():

    num1 = None
    num2 = None

    while(num1 is None):
        try:
            num1 = int(input())
        except (ValueError, NameError) as e:
            print("Please write an integer for num1")

    while(num2 is None):
        try:
            num2 = int(input())
        except (ValueError, NameError) as e:
            print("Please write an integer for num2")

    print(zajednicki_delilac(num1, num2))

    return zajednicki_delilac(num1, num2)


if __name__ == "__main__":
    dodela_delilaca()