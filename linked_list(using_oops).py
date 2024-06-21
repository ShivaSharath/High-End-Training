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
    def display(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next
a=sll()
a.insert_at_end(10)
a.insert_at_end(20)
a.insert_at_end(40)
a.insert_at_beg(9)
print(a.sum_ll())
a.display()
# a.delete_at_end()
# a.delete_at_begin()
# a.find_middle_node()
print("\nmiddle node element is " ,a.find_middle_node())
print(a.find(20))

