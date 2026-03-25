import pandas as p

#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    print(data['item_price'].dtype)
    data['item_price'] = data['item_price'].str.replace('$', '').astype(float)
    print(data['item_price'].dtype)
    
#la fonction dtype va dire c est quoi le type de variable
#qui se trouve dans ma colonne a partir de l index


if (__name__ == "__main__"):    
    main()