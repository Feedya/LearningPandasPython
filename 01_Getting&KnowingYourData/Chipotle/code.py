import pandas as p
import numpy as np


#ici data sera une DataFrame
def main():
    chemin = "chipotle.tsv"
    #creer la dataframe
    data = p.read_csv(chemin, sep='\t')
    
    #voire l info de la variable le nom de la variable
    print("///////////////////////////")
    print("type variable ")
    #ecrire le type de la variable
    print(type(data))
    
    #ecrire a les lignes a partir du debut
    print("///////////////////////////")
    print("ligne depuis le haut")
    print(data.head(1))
    print("///////////////////////////\n")

    #ecrire les lignes a partir de la fin
    print("///////////////////////////")
    print("ligne depuis le bas")
    print(data.tail(1))
    print("///////////////////////////\n")

    #ecrire toute les informations sur la DataFrame
    print("///////////////////////////")
    print("Info sur tout la DataFrame")
    print(data.info())
    print("///////////////////////////\n")

    #ecrire un resumer sur la dataFrame
    print("///////////////////////////")
    print("resume statistique sur la data frame")
    print(data.describe())
    print("///////////////////////////\n")

    print("Combien d obesrvation on a dans notre DataFrame")
    print(len(data))

    print("\nCombien de colonne on a dans notre DataFrame")
    print(data.shape)
    
    print("\nEcrire le nom des colonnes")
    print(data.columns)
    
    print("\n How is the dataset indexed?")
    print(data.index)
    
    print("\nla plus grosse quantity orderer")
    #index = data['quantity']
    print(data["quantity"].max())
    
    print("\nla ligne avec la plus grosse quantity")
    data_du_record = data[data['quantity'] == data['quantity'].max()]
    print(data[data['quantity'] == data['quantity'].max()])
    
    print("\ncombien de order coutait plus de 10 francs")
    data['item_price'] = data["item_price"].str.replace("$", "").astype(float)
    nombre_de_lignes_plus_de_10_francs = data[data['item_price'] > 10]
    print(len(nombre_de_lignes_plus_de_10_francs))
    
    print("\nvoir le type de chaque colonne")
    print(data.dtypes) 
    
    print("\nle nombre d arcticles moin de 10 francs?")
    data_moin_de_10_francs = data[data['item_price'] <= 10]
    print(len(data_moin_de_10_francs))
    
    print("\nle nombres article avec le nom plus long que 10 charactere")
    nom_plus_long_que_10 = data[data['item_name'].str.len() > 10]
    print(len(nom_plus_long_que_10))
    
    print("\nle nombre d article qui ont le nom plus petit que 10 charactere")
    nom_plus_petit_que_10 = data[data['item_name'].str.len() < 10]
    print(len(nom_plus_petit_que_10))
    
    print("\nle nombres d articles qui ont le nom egale a 10 charactere")
    nom_egale_a_10 = data[data['item_name'].str.len() == 10]
    print(len(nom_egale_a_10))

    print("\nCombien de quantity differentes il y a?")
    plats = data.groupby('quantity')
    print(plats.groups.keys())
    
    print("\nSomme de commande pour chaque plats")
    plats = data.groupby('item_name')
    somme_par_plats = plats['quantity'].sum()
    print(somme_par_plats)
    
    print("\nall quantity")
    all_order = data['quantity'].sum()
    print(all_order)
    
    print("\nle choix le plus pris dans choice_description")
    most_bought = data.groupby('choice_description').sum().sort_values(['quantity'], ascending=False)
    print(most_bought.head(1))
    
    
    print("\nle nombre de items acheter au total")    
    total = data.quantity.sum()
    print(total)
    
    revenue = (data['quantity']* data['item_price']).sum()

    print('Revenue was: $' + str(np.round(revenue,2)))

if __name__ == "__main__":
    main()