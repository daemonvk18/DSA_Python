class Backtracking:
    def __init__(self) -> None:
        print("constructor instantiated")

    def allpermutations(self,string,string_new,index):
        if len(string)==0:
            print(string_new)
            return
        for i in range(len(string)):
            currentChar = string[i]
            newStr = string[0:i] + string[i+1:]
            self.allpermutations(newStr,string_new + currentChar,index+1)


abc = Backtracking()
abc.allpermutations('ABCD',"",0)             