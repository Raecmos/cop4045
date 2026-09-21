def line_number(filein:str, fileout:str) -> None:

    try:
        fin = open(filein,"r")
        fout = open(fileout, "w")

        count = 1
        for line in fin:
            fout.write("{}. {}".format(count, line))
            count += 1
        fin.close()
        fout.close()
    except FileNotFoundError as exc:
        print("File Error {} \n".format(filein))
        raise exc
    except IOError as exc:
        print(" IOError : {} and {}.\n".format(filein, fileout))
        raise exc


#b)
def parse_functions(pyfile:str) -> tuple:


    def remove_comment_empty(line:str) -> str:
       
        comment = ""
        for i in range(len(line)):
            ch = line[i]
            if comment != "":
                if ch == comment:
                    comment = ""
            elif ch == '"' or ch == "'":
                comment = ch
            elif ch == "#":
                return line[:i]
        return line

    def parse_line(line:str, prev_fun:bool):
       
    try:

        fin = open(pyfile, "r")
        func_dict = {}

        in_function = False
        count = 0
        fun_text = ""
        fun_name = ""
        fun_args = ""
        fun_count = 0
        for line in fin:
            count += 1
          
    except FileNotFoundError as exc:
        print("Error: input file {} not found.\n")
        raise exc
    except IOError as exc:
        print("Error: IOError while working with file {}.\n")
        raise exc
    except ValueError as exc:
        print("Error: could not parse file {}.\n")
        raise exc


def main():
   

if __name__ == "__main__":
    main()