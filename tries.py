class node:
    def _init_(self):
        self.d={}
        self.flag=0    
class tries:
    def _init_(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:return False
    def prefix(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    
    def print_words_with_prefix(self):
        t=self.root
        i=0
        while t.flag==1:
            print(t.d[i])
            t=t.d[i]
            i+=1
        
t1=tries()

n=int(input())
for i in range(n):
    a,s=input().split(" ")
    if a=="1":
        t1.insert(s)
    if a=="2":
        print(t1.search(s))
    if a=="3":
        print(t1.prefix(s))