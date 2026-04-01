import pandas as p


#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("fichier n existe pas")
        return (0)
    diff_items = data.item_name.value_counts()
    print(len(diff_items))

#ici on doit calculer le nombre total d elements different qu on a dans notre dataFrame

if __name__ == "__main__":
    main()