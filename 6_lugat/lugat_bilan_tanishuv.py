# # otam = {'ismi': 'Azamat', 'yoshi': 50, 'kasbi': 'muhandis'}
# # print(f"Otamning ismi {otam['ismi']}, yoshi {otam['yoshi']} da, kasbi {otam['kasbi']}.")

# oilam = {'otam': 'osh', 'onam': 'mastava', 'ukam': 'baliiq', 'singlim': 'shirinlik'}
# print(f"Otamning sevimli taomi {oilam['otam']}, onamning sevimli taomi {oilam['onam']}, ukamning sevimli taomi {oilam['ukam']} va singlimning sevimli taomi {oilam['singlim']}.")

atamalar = {
    'integer': 'butun son',
    'float': 'haqiqiy son',
    'string': 'matn',
    'int': 'butun son',
    'str': 'matn',
    'if': 'shart operatori',
    'elif': 'aks holda shart operatori',
    'else': 'aks holda shart operatori',
    'append': 'ro\'yxatga element qo\'shish',
    'insert': 'ro\'yxatga element qo\'shish',
    'del': 'ro\'yxatdan element o\'chirish',
    'pop': 'ro\'yxatdan element o\'chirish',
}
# a = input("biror atama kiriting: ")
# if a in atamalar:
#     print(f"{a} so\'zi {atamalar[a]} degani")
# else:    
#     print(f"kechirasiz, {a} so\'zi lug\'atimizda mavjud emas")

b = input("biron atama kiriting: ")
print(atamalar.get(b, f"kechirasiz, {b} so\'zi lug\'atimizda mavjud emas"))