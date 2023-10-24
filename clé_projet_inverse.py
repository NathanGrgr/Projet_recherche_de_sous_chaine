def ouverture_fichier():
    with open("clé_texte_projet.txt","r",encoding="utf-8") as fichier:
        l=fichier.read()
    return(l)


def recherche(contenu,clé,liste):
    a=(len(clé)-1)
    c=a
    b=len(clé)
    for i in reversed(range(len(contenu))):
        if contenu[i]==clé[a]:
            print(contenu[i],clé[a])
            a=a-1
            if a==c-b:
                liste.append(i)
                a=(len(clé)-1)
        else:
            a=(len(clé)-1)
    liste.sort()
    return(liste)

liste=[]
contenu="medicament"
#clé=input("clé")
resultat=recherche(contenu,"tartine",liste)

print(contenu)
print(resultat)