import pandas as p

#how many products cost more than 10 dollars

#Index(['order_id', 'quantity', 'item_name', 'choice_description','item_price'],

    #    data['item_price'] = data['item_price'].str.replace('$', '').astype(float)
      
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("le chemin est mauvais")
        return (0)
    #on change le type de item_price en float
    data.item_price = data.item_price.str.replace("$", "").astype(float)

    #on va compter et afficher le nombre de commandes du meme articles
    #qui depasse 10 $
    data['price_per_article'] = data['item_price'] / data['quantity']
    print("price plus de 10 par meme articles acheter au meme temps")
    print((data.price_per_article > 10).sum())


    #on va afficher le nombre d articles qui depasse les 10
    print("le nombre d article acheter seul qui depasse les 10")
    print((data.item_price > 10).sum())

    #le nombre d articles qui font plus de 10$ qui sont unique en choice description
    print("le nombre d articles unique qui font plus de 10 en comptant les choix differents")
    duplicates = data.drop_duplicates(["item_name", "choice_description"])
    print((duplicates.price_per_article > 10).sum())

if __name__ == "__main__":
    main()