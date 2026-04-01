import pandas as p

#HOW MANY DIFF OCCUPATION ARE IN THE DATAFRAME
#['user_id', 'age', 'gender', 'occupation', 'zip_code']
def main():
    try:
        data = p.read_csv("occupation.user", sep = '|')
    except FileNotFoundError:
        print("le chemin n est pas bon du fichier")
        return (0)
    g = data.value_counts('occupation')
    print(g.count())
    group = data.groupby('occupation')
    print(len(group))
    
    
if __name__ == "__main__":
    main()