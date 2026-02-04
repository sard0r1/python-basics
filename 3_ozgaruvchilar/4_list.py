ismlar = ["Umsh" , "Asl" , "Bekki"]
print("salom " + ismlar[0] + " salom " + ismlar[1] + " salom " + ismlar[2])

sonlar = [1 , -2 , 3.3]
sonlar[0] = 2
sonlar[1] = sonlar[1] * -1
del sonlar[0]
print(sonlar)


t_shaxslar = ["Ali" , "Vali" , "Hasan" , "Husan"]
z_shaxslar = ["Asl" , "Bekki" , "Umsh"]
a = t_shaxslar.pop(0)
b = z_shaxslar.pop(0)
print(" Men " + a + " bilan " + b + " ni tanishtiraman ")



friends = []
friends.append("Ali")
friends.append("Vali")
friends.append("Hasan")
print(friends)
friends.remove("Vali")
friends.append("Husan")
friends.insert(0 , "Asl")
print(friends)


mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
print(mehmonlar)