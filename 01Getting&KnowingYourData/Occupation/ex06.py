import pandas as p

#['user_id', 'age', 'gender', 'occupation', 'zip_code']
def main():
    try:
        data = p.read_csv("occupation.user", sep = '|')
    except FileNotFoundError:
        print("le chemin n est pas bon du fichier")
        return (0)
    print(data.describe(include = "all"))
    
    # la ici on va utiliser un flag pour inclure tout les infos
    #meme les string
    #ceux qui peut donner des resultats assez speciaux mais 
    #interessant quand meme
    
if __name__ == "__main__":
    main()