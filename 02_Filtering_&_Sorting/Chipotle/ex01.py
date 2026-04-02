import pandas as p

#Index(['order_id', 'quantity', 'item_name', 'choice_description','item_price'],

def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("le chemin est mauvais")
        return (0)
    #on transforme les prix en float
    data.item_price = data.item_price.str.replace("$", "").astype(float)

    #on va creer le prix par 1 seul produit
    data["prix_uniter"] = data.item_price / data.quantity

    #on enleves les doublons
    data_unique = data.drop_duplicates(["item_name", "choice_description"])

    #les doubles crochets [[]] les premier c est pour choisir ce qu on veut
    #les deuxieme c est pour dire qu on creer une nouvelle data frame
    liste = data_unique[["item_name", "choice_description", "prix_uniter"]]

    print(liste)
    


if __name__ == "__main__":
    main()