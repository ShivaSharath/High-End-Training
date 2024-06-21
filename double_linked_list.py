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
        c=0                         #q=self.tail
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
    def palindrome(self):
        h=self.head
        t=self.tail
        while t!=h:
            if h.data!=t.data:
                return "not palindrome"
            h=h.next
            t=t.prev
        return "palindrome"
    def half_exchange(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            f=f.next.next
            s=s.next
        h=self.head
        t=s
        while t!=None:
            t.data,h.data=h.data,t.data
            t=t.next
            h=h.next
        a.display()
    def paranthesis_check(self):
        b=list()
        t=self.head
        c=1
        flag=1
        while t.next:
            if t.data in ']})':
                flag=0
                break
            if t.data in '({[':
                b.append(t.data)
            elif t.data == ')' and '(' == b[-1]:
                b.pop()
            elif t.data == ']' and '[' == b[-1]:
                b.pop()
            elif t.data == '}' and '{' == b[-1]:
                b.pop()
            elif t.data !=b[-1]:
                break
            t=t.next
            c+=1
        return -1 if len(b)==0 and flag==1 else c
    def evod(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.evod(t.next,es,os)
    def prime_count(self,t,c):
        if(self.head==None):
            return c
        def pnt(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return pnt(s+1,n)
        if(pnt(2,t.data)):
            c=c+1
        return self.prime_count(t.next,c)
a=dll()
a.addback(10)
a.addfront(10)
a.addback(30)
a.display()
a.revdisplay()
print(a.linearsearch(10))
print(a.even_odd())
print(a.palindrome())
a.evod(a.head,0,0)
a.half_exchange()
a.paranthesis_check()

a.prime_count(t)