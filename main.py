# 1-misol
sonlar = (3, 7, 2, 9, 5)
yigindi = 0

for son in sonlar:
    yigindi += son

print("Yig'indisi:", yigindi)

# 2-misol
sonlar = eval(input("Tuple kiriting: "))

eng_katta = sonlar[0]

for son in sonlar:
    if son > eng_katta:
        eng_katta = son

print("Eng katta element:", eng_katta)

# 3-misol
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

yangi_list = []

for element in (tuple1 + tuple2):
    yangi_list.append(element)

yangi_tuple = tuple(yangi_list)
print("Yangi tuple:", yangi_tuple)

# 4-misol
sonlar = (3, 8, 5, 10, 2, 7, 6)

juftlar = []

for son in sonlar:
    if son % 2 == 0:
        juftlar.append(son)

print("Juft sonlar:", juftlar)

# 5-misol
sonlar = (1, 2, 3, 4, 5)

teskari = []

for son in sonlar:
    teskari.insert(0, son)

yangi_tuple = tuple(teskari)

print("Teskari tuple:", yangi_tuple)
