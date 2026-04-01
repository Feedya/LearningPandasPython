import pandas as p

def main():
    try:
        data = p.read_csv("product.tsv", sep = '\t', nrows=10)
    except FileNotFoundError:
        print("le chemin du fichier est mauvais")   
        return (0)
    nom_colonne = data.columns[104]
    print(data.dtypes[nom_colonne])

#ici on doit trouver quelle valeur se trouve dans la 104 colonne dans 
#notre dataFrame 
#donc premierement on prend le nom de la colonne
#apres avec dtypes et le nom de la colonne on a se
#qui se trouve a l interieur


if __name__ == "__main__":
    main()