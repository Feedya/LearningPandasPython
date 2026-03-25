import pandas as p

#['user_id', 'age', 'gender', 'occupation', 'zip_code']
def main():
    try:
        data = p.read_csv("occupation.user", sep = '|')
    except FileNotFoundError:
        print("le chemin n est pas bon du fichier")
        return (0)
    print(data.describe())
    
    #c est une fonction tres forte qui va calculer plein de truque 
    #mais que avec des informations qui sont des nombres
    
if __name__ == "__main__":
    main()