import pandas as p
import numpy as n

#'product_name'
def main():
    try:
        data = p.read_csv("product.tsv", sep = '\t', nrows=100)
    except FileNotFoundError:
        print("le chemin du fichier est mauvais")   
        return (0)
    index_name = data.columns.get_loc('product_name')
    print(data.values[18][index_name])

#ici on va utiliser get_loc qui nous renvoie l index de se qu on cherche
#et on va utiliser la fonction values qui vient de numpy
#donc on combine le monde de pandas avec celui de numpy

if __name__ == "__main__":
    main()