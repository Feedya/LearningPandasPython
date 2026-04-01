import pandas as p

def main():
    try:
        data = p.read_csv("product.tsv", sep = '\t', nrows=10)
    except FileNotFoundError:
        print("le chemin du fichier est mauvais")   
        return (0)
    print(data.columns[104])


if __name__ == "__main__":
    main()