import pandas as p

#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    chaque_commande_mis_ensemble = data.order_id.value_counts()
    total = chaque_commande_mis_ensemble.count()
    print(f"total de commandes : {total}")

if (__name__ == "__main__"):
    main()