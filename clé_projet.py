def ouverture_fichier():
    with open("clé_texte_projet.txt","r",encoding="utf-8") as fichier:
        l=fichier.read()
    return(l)


def recherche(contenu,clé,liste):
    clé="the"
    a=0
    for i in range(len(contenu)):
        if contenu[i]==clé[a]:
            a=a+1
            if a==len(clé):
                liste.append(i-a+1)
                a=0
        else:
            a=0
    return(liste)

liste=[]
contenu=ouverture_fichier()
resultat=recherche(contenu,"the",liste)
print(ouverture_fichier())
print(resultat)