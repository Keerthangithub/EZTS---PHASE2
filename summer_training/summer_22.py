#3121
#1941
#896
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.nxt=None
class dll():
    def __init__(self):
        self.head=None
        self.tail=None
    def addfront(self,x):
        if self.head==None:
            self.head=Node(x)
            self.tail=self.head
        else:
            t=Node(x)
            self.head.prev=t
            t.nxt=self.head
            self.head=self.head.prev
    def addback(self,x):
        if self.head==None:
            self.head=Node(x)
            self.tail=self.head
        else:
            t=Node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
    def search(self,x):
        t=self.head
        f=self.tail
        while t!=f and t!=f.nxt:
            if x==t.data or x==f.data:
                return "Found"
            t=t.nxt
            f=f.prev
        if t.data==x:
            return "Found"
        else:
            return "Not Found"
    def len(self):
        t=self.head
        f=self.tail
        while t!=f and t!=f.nxt:
            t=t.nxt
            f=f.prev
        if t==f:
            return "odd"
        else:
            return "even"
    def palin(self):
        t=self.head
        f=self.tail
        while t!=f and t!=f.nxt:
            if t.data==f.data:
               t=t.nxt
               f=f.prev
            else:
                return "not palindrome"
        if t.data==f.data or t.data==f.nxt.data:
            return "palindrome"
    '''def swap(self):
        t=self.head
        f=self.tail
        c=self.head
        while t!=f:
            t=t.nxt
            f=f.prev
        if t==f:
            c=t
            while t!=None and f!=None:
                print(f.data)
                t=t.prev
                f=f.nxt
            while t!=c:
                print(t.data)
                t=t.nxt
            #print(t.data)'''
    def rev(self):
        t=self.head
        f=self.head.nxt
        while t!=None and f.nxt!=None:
            print(f.data,end="->")
            print(t.data,end="->")
            f=f.nxt.nxt
            t=t.nxt.nxt
        print(f.data,end="->")
        print(t.data,end="->")
        
l1=dll()
#l1.head=Node(5)
#l1.tail=l1.head
l1.addfront(20)
l1.addback(30)
l1.addback(40)
l1.addback(30)
l1.addback(20)
l1.addback(70)
l1.display()
print()
#l1.rev_display()
print(l1.search(5))
print(l1.len())
print(l1.palin())
#l1.swap()
l1.rev()