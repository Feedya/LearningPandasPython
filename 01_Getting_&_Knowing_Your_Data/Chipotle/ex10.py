import pandas as p

#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    group = data.groupby('item_name')
    group = group.sum()
    
    index = group['quantity'].idxmax()
    print(group.loc[index])

if (__name__ == "__main__"):    
    main()
