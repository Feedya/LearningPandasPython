import pandas as p

#What is the age with least occurrence?
#['user_id', 'age', 'gender', 'occupation', 'zip_code']
def main():
    try:
        data = p.read_csv("occupation.user", sep = '|')
    except FileNotFoundError:
        print("le chemin n est pas bon du fichier")
        return (0)
    group = data.groupby('age')
    taille = group.size()
    taille_ascending = taille.sort_values()
    print(taille_ascending.head(10))
    
if __name__ == "__main__":
    main()