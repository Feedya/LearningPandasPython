import pandas as p

def main():
    chemin = "Chipotle.tsv"
    try:
        data = p.read_csv(chemin, sep='\t')
    except FileExistsError:
        print("le chemin est mauvais")
    print(data)


if (__name__ == "__main__"):
    main()