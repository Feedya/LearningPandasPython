import pandas as p

#['user_id', 'age', 'gender', 'occupation', 'zip_code']
def main():
    try:
        data = p.read_csv("occupation.user", sep = '|')
    except FileNotFoundError:
        print("le chemin n est pas bon du fichier")
        return (0)
    
    #on va regrouper notre dataFrame par l occupation
    group = data.groupby('occupation')
    
    #on va compter comvbien de lignes a chaque occupation
    taille = group.size()
    print(taille)
    
    #on va sortir celle qui a la plus de lignes dedans
    index = taille.idxmax()
    print(index)

if __name__ == "__main__":
    main()