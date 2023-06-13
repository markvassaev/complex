import math
from math import atan , sqrt , cos , sin , pi
massiv_chisel = []
def fold_cplx(a,b,c,d):
    i = "i"
    plus = "+"
    result1 = a+c
    result2 = b+d
    result3 = str(result1)+plus+str(result2)+i
    print(result3)

def multiply_cplx(a,b,c,d):

    plus = "+"
    i = "i"
    # x = ""
    result1 = a*c
    result2 = a*d
    result3 = b*c
    result4 = - b*d
    result5 = result1 + result4
    result6 = result2 + result3
    if result6 == 0 :
        x = str(result5)
        massiv_chisel.append(x)

    if str(result6)[0] == "-":
        # print(str(result5) + str(result6) + i)
        x = str(result5) + plus + str(result6) + i
        massiv_chisel.append(x)
    else:
        # print(str(result5)+ plus + str(result6) + i)
        x = str(result5) + plus + str(result6) + i
        massiv_chisel.append(x)



def Exponentiation(a,b,x):
    cornertang = b/a
    corner = atan(cornertang)
    module = sqrt(a**2+b**2)
    number1 = module * cos(x*corner)
    number2 = module * sin(x*corner)
    i = "i"
    plus = "+"
    if str(number2)[0] == "-":
        if number1 - int(number1) < 0.001:
            nubmer3 = str(int(number1)) + str(number2) + i
            print(nubmer3)
        else:
            nubmer3 = str(number1) + str(number2) + i
            print(nubmer3)
    else:
        nubmer3 = str(number1) + plus + str(number2) + i
        print(nubmer3)

def division(a,b,c,d):
    numbers_1 = multiply_cplx(a=a,b=b,c=c,d=-d)
    numbers_2 = multiply_cplx(a=c,b=d,c=c,d=-d)
    print(str(massiv_chisel[0] + "/" + str(massiv_chisel[1])))


Exponentiation(a=5,b=10,x=3)
