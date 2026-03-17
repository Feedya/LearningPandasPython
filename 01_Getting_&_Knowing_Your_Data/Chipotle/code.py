import pandas as p


#ici data sera une DataFrame
def main():
    chemin = "chipotle.tsv"
    #creer la dataframe
    data = p.read_csv(chemin, sep='\t')
    #voire l info de la variable le nom de la variable
    print("variable ")
    print(type(data))

if __name__ == "__main__":
    main()