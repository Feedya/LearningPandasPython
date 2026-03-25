import pandas as p

def main():
    try:
        data = p.read_csv("product.tsv", sep = '\t')
    except FileNotFoundError:
        print("le chemin du fichier est mauvais")   
        return (0)
    print(data.index)


if __name__ == "__main__":
    main()