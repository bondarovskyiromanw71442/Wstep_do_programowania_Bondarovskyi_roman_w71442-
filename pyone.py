from random import randint

#Zadanie 1
#
# x  = 1 + 2
# print(type(x))
#
# x = 1 + 4.5
# print(type(x))
#
# x = 3 / 2
# print(type(x))
#
# x = 4 / 2
# print(type(x))
#
# x = 3 // 2
# print(type(x))
#
# x = -3 // 2
# print(type(x))
#
# x = 11 % 2
# print(type(x))
#
# x = 2 ** 10
# print(type(x))
#
# x = 8 ** (1/3)
# print(type(x))
#
# #Zadanie 6
#
# a1 = float(input("Podaj pokonaną odległość : "))
# średnie_spalanie = float(input("Podaj średnie spalanie samochodu: "))
#
# # Cena paliwa w złotówkach za litr
# cena = 6.5
#
# # Obliczanie zużyciu paliwa
# zużyciu_paliwa = (a1 / 100) * średnie_spalanie
# # Obliczanie kosztów podróży
# koszt_podróży = zużyciu_paliwa * cena
#
# # Wyświetlanie wynikóm
# print("Przewidywane zużyciu paliwa: ", zużyciu_paliwa)
# print("Szacowany koszt podróży : ", koszt_podróży)


#Zadanie 7


a1 = randint(a = 1, b = 600)
średnie_spalanie = float(input("Podaj średnie spalanie samochodu: "))

# Cena paliwa w złotówkach za litr
cena = 6.5

# Obliczanie zużyciu paliwa
zużyciu_paliwa = (a1 / 100) * średnie_spalanie
# Obliczanie kosztów podróży
koszt_podróży = zużyciu_paliwa * cena

# Wyświetlanie wynikóm
print("Droga: ", a1, "/ km")
print("Przewidywane zużyciu paliwa: ", zużyciu_paliwa, "/ litry")
print("Szacowany koszt podróży : ", int(koszt_podróży), "/ PLN")

