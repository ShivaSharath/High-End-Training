class node:
    def __init__(self,x):
        self.data=x
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_at_end(self,b):
        if self.head==None:
            self.head=node(b)
        else:
            t=self.head
            while (t.next):
                t=t.next
            t.next=node(b)
    def insert_at_beg(self,b):
        if self.head==None:
            self.head=node(b)
        else:
            t=node(b)
            t.next=self.head
            self.head=t
    def delete_at_end(self):
        if self.head==None or self.head.next==None:
            self.head=None
        t=self.head
        while t.next.next:
            t=t.next
        t.next=None
    def delete_at_begin(self):
        if self.head.next==None:
            self.head=None
        else:
            self.head=self.head.next
    def find(self,a):
        if self.head==None:
            return None,None
        t= self.head
        c=0
        while t:
            c+=1
            if t.data==a:
                return True,c
            t=t.next
        return False,None
    def find_middle_node(self):
        if self.head==None:
            return self.head
        else:
            slow=self.head
            fast=self.head
            while  fast and fast.next :
                fast=fast.next.next
                slow=slow.next
            return slow.data 

    def sum_ll(self):
        t=self.head
        s=0
        while t:
            s+=t.data
            t=t.next
        return s
    '''def bubblesort(self):
        t=self.head
        while(t.next!=None):
            v=t.next
            while v!=None:
                if t.data>=v.data:
                    temp=t.data
                    t.data=v.data
                    v.data=temp
                v=v.next'''
    def bubblesort(self):
        c=0
        T=self.head
        p=None
        while(T.next!=None):
            f=0
            t=self.head
            while(t.next!=p):
                if(t.data>t.next.data):
                    f=1
                    t.data, t.next.data=t.next.data, t.data
                t=t.next
            if(f==0):
                break
    def rev(self):
         a=self.head
         b=self.head.next
         c=b.next
    def display(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next
    def sequence(self):
        while (t.next!=node):
            x=t.head
            while(x.next!=node):
                print(t.data,x.data)
    def double_swap(self):
        t=self.head
        s=t.next
        while s!=None:
            temp=t.data
            t.data=s.data
            s.data=temp
            t=t.next.next
            s=s.next.next
        a.display()
a=sll()
a.insert_at_end(10)
a.insert_at_end(20)
a.insert_at_end(40)
a.insert_at_beg(9)
print(a.sum_ll())
a.display()
a.bubblesort()
# a.delete_at_end()
# a.delete_at_begin()
# a.find_middle_node()
44print("\nmiddle node element is " ,a.find_middle_node())
print(a.find(20))
a.double_swap()