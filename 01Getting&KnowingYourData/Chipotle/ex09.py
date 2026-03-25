import pandas as p

#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    #on va changer le itemPrice en float
    #premierement on enleves le $ en transformant en str et en utilisant replace
    #apres on utilise astype pour changer en float comme il n y a plus de charactere
    data['item_price'] = data['item_price'].str.replace('$', '').astype(float)
    
    group = data.groupby('item_name')
    sum_group = group.sum()
    #on va faire des groupes de produits en utilisant groupby
    #apres on va faire sum pour ajouter tout les nombres ensemble
    #comme ca on a un constats sur chaque item
    
    index = sum_group['quantity'].idxmax()
    print(sum_group.loc[[index]])
    
    #va donner l index de la valeur la plus grande
    #et loc vas nous renvoyer la ligne assosier a cette index
    #si on met qu une seule paire de [] ca va nous renvoyer comme une liste
    #si on met 2 [[]] ca va nous renvoyer la ligne tant que dataFrame
    
if (__name__ == "__main__"):
    main()