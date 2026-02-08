# # # a = list(range(1,6))
# # # for i in a:
# # #     print("sanoq " , i)
# # # print(a)
# # # print('kod' , len(a) , 'marta takrorlandi')

# # a = list(range(11,100,2))
# # for kubi in a:
# #     print(kubi**3)

# kinolar = []
# for i in range(1,6):
#     kinolar.append(input( f"{i}-eng sevimli kinolaringizni kiriting:"))
# print(kinolar)

nechta = int(input("bugun nechta odam bilan suhbatlashdingiz: "))
odamlar = []
for odam in range(0,nechta):
    odamlar.append(input(f"{odam+1}- odam ismini kiriting: "))
print("siz suhbatlashgan odamlar: " , odamlar)