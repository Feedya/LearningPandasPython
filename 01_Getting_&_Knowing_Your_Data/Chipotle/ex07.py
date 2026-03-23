import pandas as p

def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    print(data.columns)
    
#columns n est pas une fonction c est un attribut
#elle va renvoyer un objet de type Index
#ou dedans on aura le nom de nos colonnes dans cette exo c est
#Index(['order_id', 'quantity', 'item_name', 'choice_description','item_price'],
#si on renomme avec columns on est obliger de mettre le nom des 5 colonnes

if (__name__ == "__main__"):
    main()