import csv

def read_ranking(f):
 
    rdr = csv.reader(f)
    next(rdr)  
    t_lst = [(int(ls[0]), ls[1], int(ls[2]), float(ls[3].replace("$", "").replace(",", "")))
             for ls in rdr]
    t_dct = {(ls[1], ls[2]): (ls[0], ls[3]) for ls in t_lst}

    t_ranked_lst = sorted([(ls[0], (ls[1], ls[2]), ls[3]) for ls in t_lst])
    return (t_dct, t_ranked_lst)



def read_casts(f):
   
    rdr = csv.reader(f)
   
    casts_dct = {(ml[0], int(ml[1])): (ml[2], ml[3], ml[4], ml[5], ml[6], ml[7])
                 for ml in rdr}
    return casts_dct



def display_slice(msg:str, lst:list, n:int) -> None:

    print(msg)
    for x in lst[:n]:
        print(x)


# a)

def top_collaborations(ranked_lst:list, cast_dct:dict) -> list:
   

def display_top_collaborations(ranked_lst:list, cast_dct:dict) -> None:
  

# b)

def top_grossing_actors(top_gross_lst:list, cast_dct:dict) -> list:
    "
    


def display_top_actors(top_gross_lst:list, cast_dct:dict) -> None:
    
# c)
def main():

    cast_f = None
    topranked_f = None
    topgrossing_f = None
    try:
    

if __name__ == "__main__":
    main()