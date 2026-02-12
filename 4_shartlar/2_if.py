# # # # # # juft = int(input('juft son kiriting: '))
# # # # # # if juft%2 == 0: print('rahmat') 
# # # # # # else: print('bu juft son emas')

# # # # # yosh = int(input("yoshingiz nechida: "))
# # # # # if yosh < 4 :
# # # # #     print("bepul")
# # # # # elif yosh < 18:
# # # # #     print("10 000 so'm")
# # # # # elif yosh > 60:
# # # # #     print("bepul")
# # # # # elif yosh > 18:
# # # # #     print("20 000 so'm")

# # # # a = int(input('son kiriting: '))
# # # # b = int(input('ikkinchi sonni kiriting: '))
# # # # if a==b:
# # # #     print(a , "teng" , b , "ga")
# # # # elif a > b :
# # # #     print(a , ">" , b)
# # # # else:
# # # #     print(a , "<" , b)

# mahsulotlar = ['a' , 'b' , 'c' , 'd' , "e" , 'f' , 'g' , 'h' , 'm' , 'n']
# mahsulot = []
# n =1
# for i in range(0,5):
#     mahsulot.append(input(f'{i+1}-mahsulotni kiriting: '))
# print("----------------------")
# for k in mahsulot:
#     if k in mahsulotlar:
#         print(f'{n}-mahsulot {k} bor')
#         n = n+1
#     else:
#         print(f'{n}-mahsulot: {k} yoq')
#         n = n+1

# # # mahsulotlar = ['a' , 'b' , 'c' , 'd' , "e" , 'f' , 'g' , 'h' , 'm' , 'n']
# # # mahsulot = []
# # # bor_mahsulatlar = []
# # # mavjud_emas = []
# # # for i in range(0,5):
# # #     mahsulot.append(input(f'{i+1}-mahsulotni kiriting: '))
# # # print("----------------------")
# # # for k in mahsulot:
# # #     if k in mahsulotlar:
# # #         bor_mahsulatlar.append(k)
# # #     else:
# # #         mavjud_emas.append(k)
# # # if len(mavjud_emas) == 0:
# # #     print('siz soragan barchasi bor')
# # # else :
# # #     print('quyidagi mahsulotlar dokonimizda yoq: ' , mavjud_emas)

# # foydalanuvchilar = ['admin' , 'sardor' , 'sarvar' , 'umsh' , 'asl']
# # foydalamuvchi = input("login kiriting: ")
# # if foydalamuvchi in foydalanuvchilar:
# #     print('bunday foyalanuvchi nomi band, iltimos boshqa login kiriting')
# # else:
# #     print('hush kelibsiz yangi foydalanuvchi')

a = int(input("biror butun son kiriting: "))
for k in range(2,11):
    if a%k==0:
        print(k , "ga bolinganida qoldiqsiz")