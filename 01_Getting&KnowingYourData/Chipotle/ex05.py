import pandas as p

def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    print(data.shape[0])
    print(data.shape[1])

#ici on va montrer combien de lignes j ai
#chaque lignes c est des donnees par rapport a un truque
#ici les commandes chipotle
#chaque lignes ca sera se que la personne a commander
#avec ce qu elle a payer
#et l id de sa commandes
#shape n est pas une fonction donc on lui met pas de ()
#shape est un attribut
#elle va renvoyer un tuple qui va nous dire les dimension de notre 
#dataFrame
#ici on travaille sur une dataFrame a 2 dimension
#donc shape[1] le nombre de lignes
#shape[2] le nombre de colonnes

if __name__ == "__main__":
    main()