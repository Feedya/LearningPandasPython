import pandas as p

def main():
    try:
        data = p.read_csv("product.tsv", sep = '\t')
    except FileNotFoundError:
        print("le chemin du fichier est mauvais")   
        return (0)
    print(data.shape)

#ici on travaille avec un tableau qui a 163 colonnes et 356027 lignes
#ce qui est assez grand mais restes tres petit avec des encore plus grosse donnes


if __name__ == "__main__":
    main()