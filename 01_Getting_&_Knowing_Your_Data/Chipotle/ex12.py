import pandas as p

#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    tout = data['quantity'].sum()
    print(tout)

#ici on veut savoir la quantite totale dans toute la dataFrame
#donc on indexe la quantity et apres on fait sum pour tout ajouter ensemble

if (__name__ == "__main__"):    
    main()