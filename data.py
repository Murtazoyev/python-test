# def full_name(fName, lName):
#     a = fName + " " + lName
#     return a

# fullName = full_name("Dilshod", "Murtazoyev")

# print(f"Men {fullName} => Wepro o'quv markazida Back-End yo'nalishida dars olaman.")


from pickletools import read_int4


def pluse(a, b):
    return a + b

def minuse(a, b):
    return a - b

def kopaytma(a, b):
    return a * b

def bolish(a, b):
    return a / b

while True:
    a = input("Birinchi sonni kiriting: ")
    a = int(a)

    amal = input("Amalni tanlang ( + /\ - /\ * /\ (/) ): ")

    b = input("Ikkinchi sonni kiriting: ")
    b = int(b)

    if amal == "+":
        natija = pluse(a, b)
    elif amal == "*":
        natija = kopaytma(a, b)
    elif amal == "-":
        natija = minuse(a, b)
    else:
        natija = bolish(a,b)

    print(natija)

    done = input("Davom etamizmi? (y/n)")
    if done == "y":
        continue
    else:
        break


print("Salom dunyo")

def hello(a):
    return f"{a} ta olma oldim"

natija = hello(12)
print(natija)