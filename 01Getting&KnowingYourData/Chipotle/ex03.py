import pandas as p

def main():
    chemin = "chipotle.tsv"
    try:
        data = p.read_csv(chemin, sep='\t')
    except FileNotFoundError:
        print("le chemin est mauvais")
        return (0)
    print(data)
    
#on va utiliser la fonction read_csv pour lire le fichier
#cette fonction prend en parametre le nom du fichier et
#le PLUS IMPORTANT le separateur. En gros c est comment elle va diviser
#notre fichier pour creer la DataFrame
#
#un truque en plus c est que si on a un mauvais nom de fichier on aura
#une erreur de compilation
#et avec le except FileNotFoundError
#on va attraper cette erreur et on aura pas d erreur de compilation
#IMPORT faut sortir dans le except sinon ca va continuer dans le programme
#et on peut avoir encore des erreurs

if (__name__ == "__main__"):
    main()