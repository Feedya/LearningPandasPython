import pandas as p

def main():
    try:
        data = p.read_csv("chipotle.tsv", sep = '\t')
    except FileNotFoundError:
        print("nom du fichier est mauvais")
        return (0)
    print(data.index)
    
#l attribut index vas nous dire sur les index en horizontale
#start = ou on commence
#stop = ou c est la fin
#step = c est combien on saut entre chaque ligne
#le step sera la majoriter du temps a 1

if (__name__ == "__main__"):
    main()