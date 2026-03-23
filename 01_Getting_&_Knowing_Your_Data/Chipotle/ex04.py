import pandas as p

def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except (FileNotFoundError):
        print("le chemin est mauvais")
        return (0)
    print(data.head(10))

#la fonction head c est la fonction de chaque data scientist qui se respecte
#et qui ne chie pas la ou il dort
#cette fonction prend un nombre en parametre
#ca sera le nombre des premieres lignes de la dataFrame qu on va voir
#si on met un nombre negatifs par exemple -5
#ca va nous montrer toute les lignes sauf les 5 derniers

if __name__ == "__main__":
    main()