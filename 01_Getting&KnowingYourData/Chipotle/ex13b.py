import pandas as p

#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    put_float = lambda x : float(x[1:-1])
    print(data['item_price'].dtype)
    data['item_price'] = data['item_price'].apply(put_float)   
    print(data['item_price'].dtype)
    

#ici on va creer une fonction lamba
#et on va utiliser APPLY
#APPLY est tres IMPORTANTS il va utiliser une fonction qu on a creer sur les elements de
#notre dataFrame, elle est tres utiles
#elle va se balader toute seule du premier index au dernier et appliquer la fonciton


if (__name__ == "__main__"):
    main()