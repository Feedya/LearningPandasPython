import pandas as p

#['user_id', 'age', 'gender', 'occupation', 'zip_code']
def main():
    try:
        data = p.read_csv("occupation.user", sep = '|')
    except FileNotFoundError:
        print("le chemin n est pas bon du fichier")
        return (0)
    moyen = data.age.mean()
    print(moyen)
    
    #compter l age moyen dans la DataFram
    
if __name__ == "__main__":
    main()