import pandas as p

#order_id', 'quantity', 'item_name', 'choice_description','item_price'],
def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("chemin n est pas bon")
        return (0)
    #on met les price en float
    put_float = lambda x : float(x[1:-1])
    data.item_price = data.item_price.apply(put_float)
    #on creer un tableau mis tout ensemble
    id_data = data.groupby('order_id')
    
    data['revenue'] = data['quantity'] * data['item_price']
    
    result_price = id_data.revenue.sum()

    print(result_price.mean())
    
    #dans pandas on peut creer une nouvelle colonne dans la dataFrame
    #tres facilement juste en fesant ['nouveau'] et ca va en creer pour chaque ligne
    
    #ici on a appris une nouvelle fonction
    #MEAN
    #cette fonciton va compter la moyenne d un int de toute les lignes de la dataFrame

if __name__ == "__main__":
    main()