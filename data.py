# def full_name(fName, lName):
#     a = fName + " " + lName
#     return a

# fullName = full_name("Dilshod", "Murtazoyev")

# print(f"Men {fullName} => Wepro o'quv markazida Back-End yo'nalishida dars olaman.")


# from pickletools import read_int4


# def pluse(a, b):
#     return a + b

# def minuse(a, b):
#     return a - b

# def kopaytma(a, b):
#     return a * b

# def bolish(a, b):
#     return a / b

# while True:
#     a = input("Birinchi sonni kiriting: ")
#     a = int(a)

#     amal = input("Amalni tanlang ( + /\ - /\ * /\ (/) ): ")

#     b = input("Ikkinchi sonni kiriting: ")
#     b = int(b)

#     if amal == "+":
#         natija = pluse(a, b)
#     elif amal == "*":
#         natija = kopaytma(a, b)
#     elif amal == "-":
#         natija = minuse(a, b)
#     else:
#         natija = bolish(a,b)

#     print(natija)

#     done = input("Davom etamizmi? (y/n)")
#     if done == "y":
#         continue
#     else:
#         break


# print("Salom dunyo")

# def hello(a):
#     return f"{a} ta olma oldim"

# natija = hello(12)
# print(natija)


# ismlar = ['ali', 'vali', 'hasan', 'husan']


# def katta_harf(event):
#     for i in range(len(event)):
#         # print(i)
#         ismlar[i] = ismlar[i].title()

# katta_harf(ismlar)
# print(ismlar)



# ismlar = ['ali', 'vali', 'hasan', 'husan']


# def katta_harf(event):
#     for i in range(len(event)):
#         # print(i)
#         event[i] = event[i].title()
#     return event    
# natija = katta_harf(ismlar[:])
# print(ismlar)



# def bahola(ismlar):
#     baholar = {}
    
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)


# 22.1
# def kopaytma(*sonlar):
#     natija = 1
#     for i in sonlar:
#         natija*=i
#     return natija

# print(kopaytma(1,2,3,6,1,2,3,4))


# 22.2
# def talaba(ism, familiya, **qolganlari):
#     qolganlari['ism']=ism
#     qolganlari['familiya']=familiya
#     return qolganlari 

# talaba1 = talaba("Dilshod", "Murtazoyev", yoshi=22, qayerdan="Bukhara")
# print(talaba1)


# 23.1


# barcha_sonlar = list(range(11))

# dastur_oylagan_son = r.choice(barcha_sonlar)
# men_oylagan_son = input("Salom son topish o'yinini o'ynaymiizmi men o'ylagan sonni topingchi?? \n >>>")
# men_oylagan_son = int(men_oylagan_son) 

# mening_urunishlar_sonim = 0

# if dastur_oylagan_son > men_oylagan_son:
#     mening_urunishlar_sonim+=1
#     men_oylagan_son = input("men o'ylagan son kattaroq... \n >>>")


# def son_top():

import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:", end="")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:", end="")
        else:
            break
        
    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar
    

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
            
play()

class User:
    def __int__(self,name,username,email):
        self.name = name
        self.uname = username
        self.mail = email
    
    def describe():
        pass
    
    def get_email():
        pass








    class Talaba:
        """Talaba nomli klass yaratamiz"""
        def __init__(self,ism,familiya,tyil):
            """Talabaning xususiyatlari"""
            self.ism = ism
            self.familiya = familiya
            self.tyil = tyil
        
        def get_name(self):
            """Talabaning ismini qaytaradi"""
            return self.ism
        
        def get_lastname(self):
            """Talabaning familiyasini qaytaradi"""
            return self.familiya
        
        def get_fullname(self):
            """Talabaning ism-familiyasini qaytaradi"""
            return f"{self.ism} {self.familiya}"
        
        def get_age(self,yil):
            """Talabaning yoshini qaytaradi"""
            return yil-self.tyil
        
        def tanishtir(self):
            print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")