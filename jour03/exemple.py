def modifier(liste):
    liste.append(99)

ma_liste = [1,2,3]
ma_liste2 = ma_liste
modifier(ma_liste)
print(ma_liste)