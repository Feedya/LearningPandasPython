import pandas as p

def main():
    try:
        data = p.read_csv("product.tsv", sep = '\t', nrows=10)
    except FileNotFoundError:
        print("le chemin du fichier est mauvais")   
        return (0)
    print(data.head(10))

#ici comme on travaille sur un fichier enorme de tout lire prend trop de temps donc
#on ajoute un nouveau champs dans le read_csv qui est nrows qui dis le nombre de ligne a lire

if __name__ == "__main__":
    main()