import pandas as p

#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    #on change en float
    put_float = lambda x : float(x[1:-1])
    data['item_price'] = data['item_price'].apply(put_float)
    
    #on calcule tout
    sum_of_price = data['item_price'] * data['quantity']
    print(sum_of_price.dtype)
    all_price = sum_of_price.sum()
    print(f"somme total : {all_price}")

#ici on va calculer combien d argent ils ont fait en total dans cette dataFrame



if (__name__ == "__main__"):
    main()