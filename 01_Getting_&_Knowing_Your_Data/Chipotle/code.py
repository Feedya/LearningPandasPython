import pandas as p


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
    index = data['quantity']
    print(data["quantity"].max())
    
    print("\nla ligne avec la plus grosse quantity")
    data_du_record = data[data['quantity'] == data['quantity'].max()]
    print(data[data['quantity'] == data['quantity'].max()])
    
    print("\ncombien de order coutait plus de 10 francs")
    data['item_price'] = data["item_price"].str.replace("$", "").astype(float)
    nombre_de_lignes_plus_de_10_francs = data[data['item_price'] > 10]
    print(len(nombre_de_lignes_plus_de_10_francs))
    
if __name__ == "__main__":
    main()