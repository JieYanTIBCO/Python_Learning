class capchar:
    def __init__(self,paragrah):
        self.paragrah=paragrah
    
    def capchar(self) -> str:
        flag_capnext= True
        return_list=[]
        for char in self.paragrah:
            if char.isalpha() and flag_capnext:
                return_list.append(char.upper())
                flag_capnext=False
            elif char in '.?!':
                return_list.append(char)
                flag_capnext= True
            else:  
                return_list.append(char)
        return ''.join(return_list)


cap=capchar("this is test paragraph. do not take this as formal documentation! and I love you all? no? yes")


print(cap.capchar())
