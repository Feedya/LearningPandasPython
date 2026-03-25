import pandas as p

def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    data = data.groupby('choice_description')
    somme = data.sum()
    somme = somme.sort_values(['quantity'], ascending=False)
    print(somme.head(1))
    
    #index = somme['quantity'].idxmax()
    #print(somme.loc[index])

#ici sort_values on doit lui donner dans quelle colonne on doit faire ud plus petit au plus grand
#et le deuxieme arguments c est sois du plus petit au plus grand sois au plus grand au plus petit
    
if (__name__ == "__main__"):
    main()