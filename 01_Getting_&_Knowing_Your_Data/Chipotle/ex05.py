import pandas as p

def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    print(data.shape(0))

if __name__ == "__main__":
    main()