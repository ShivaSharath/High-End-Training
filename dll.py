class node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)                 #self.tail.next=node(x)
            self.tail.next=t          #self.tail.next.prev=self.tail
            t.prev=self.tail          #self.tail=self.tail.next
            self.tail=self.tail.next
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)  
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def revdisplay(self):
        t=self.tail
        print()
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def even_odd(self):
        t=self.head
        c=0
        while(t!=None):             #while(t!=q and t!=q.next):
            c+=1                    #	t=t.next
            t=t.next                #	q=q.prev
        if(c%2==0):                 #if(t==q):
            return "Even"           #	return "odd"
        else:                       #else: return "even"
            return "Odd"
    def linearsearch(self,x):
        if self.head==None:
            return None,None
        else:
            c=1
            b=1
            t=self.head
            q=self.tail
            while t!=q and t!=q.next:
                c+=1
                b-=1
                if t.data==x:
                    return "yes",c
                if  q.data==x:
                    return "yes",b
                t=t.next
                q=q.prev
            if(t.data==x):
                return 1
            else:
                return 0
    def pal(self):
        
a=dll()
a.addback(10)
a.addfront(20)
a.addback(30)
a.display()
a.revdisplay()
print(a.linearsearch(20))
print(a.even_odd())
