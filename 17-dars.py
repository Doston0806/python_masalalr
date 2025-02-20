
                        # 17-dars: WHILE TSIKLI
                        # amaliy masalalar
#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating


# books="Svimli kitobinizni nomini kiriting\n>>>"
# qiymat=''
# while True:
#     if qiymat!='stop':
#         qiymat=input(books)
#
#     else:
#         break
# print("Dastur tugadi")

# name="ismingizni kiriting\n>>>"
# yosh="yoshingizni kiriting\n>>>"
# # name=input(name)
# qiymat=''
# while True:
#     qiymat=(input(yosh))
#     if (qiymat)=='exit':
#         break
#     # if (name=='Doston') :
#     #     print("Ismingiz chiroyli ekan sizga kirish tekin")
#     elif ( int(qiymat)>0 and int(qiymat)<=7):
#         print("Sizga muzeyga kirish 2000 so'm bo'ladi")
#     elif int(qiymat)>7 and int(qiymat)<18:
#         print("Sizga muzeyga kirish 3000 so'm bo'ladi")
#     elif int(qiymat)>=18 and int(qiymat)<65:
#         print("Sizga muzeyga kirish 10000 so'm bo'ladi")
#     elif int(qiymat)>=65:
#         print("Sizga muzeyga kirish tekin bemalol kirib aylanavering")
#
#
# print("Dastur to'xtadi")


# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = (input(savol))
#     if qiymat=='exit':
#         break
#     elif int(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
#
# print("Dastur to'xtadi")


              # 18-dars: WHILE, RO'YXATLAR VA LUG'ATLAR
                   # amaliyot masalalar

 # Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

# buyurtma=[]
# n=1
# while True:
#     buyurtma.append(input("Mahsulotlar nomini kiriting= "))
#     javob=input("Yana mahsulot qo'shishni xoxlaysizmi>>>")
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
#
# print(buyurtma)


e_bozor={}
ishora=True
while ishora:
    mahsulot=input("Mahsulot nomini kiriting=")
    narx=int(input(f"{mahsulot}ning narxini kiriting="))
    e_bozor[mahsulot]=narx
    savol=input("Yana mahsulot kiritishni xoxlaysizmi=")
    if savol=='yo\'q':
        ishora=False

print(e_bozor)

buyurtma=[]
n=1
while True:
    buyurtma.append(input("Mahsulotlar nomini kiriting= "))
    javob=input("Yana mahsulot qo'shishni xoxlaysizmi>>>")
    if javob=='ha':
        n+=1
        continue
    else:
        break

print(buyurtma)

for narsa, qiymat in e_bozor.items():
    if narsa in buyurtma:
        print(f"{narsa}ning narxi {qiymat}")
    else:
        print(f"Bizda {narsa} yo\'q")

# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}
#
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")