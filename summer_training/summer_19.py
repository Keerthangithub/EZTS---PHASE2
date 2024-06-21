class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t.nxt!=None):
            print(t.data,end="->")
            t=t.nxt
    def search(self,x):
        t=self.head
        c=0
        while(t!=None):
            if x==t.data:
                c=1
                print("Found")
                break
            else:
                c=0
                t=t.nxt
        if c==0:
            print("Not found")
    '''def mn(self):
        c=1
        f=0
        while t!=None:
            c+=1
            t=t.nxt
        if c%2==0:
            for i in range((c//2)-1):
                f=f.nxt
     def addback(self,x):
        t=self.head
        while(t!=None):
            t=t.nxt
        t.nxt=node(x)'''
    def len(self):
        t=self.head
        c=1
        while(t!=None and t.nxt!=None):
            c+=2
            t=t.nxt.nxt
        if c%2!=0:
            print(c-1)
        else:
            print(c+1)
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if t.data%2==0:
                s+=t.data
        print(s)
    def ls(self):
        t=self.head
        while t.nxt!=None:
            t1=t.nxt
            while t1!=None:
                print(t.data,end="")
                print(t1.data)
                t1=t1.nxt
            t=t.nxt
    def bubsort():
        
l1=sll()
#l2=sll()
l1.head=node(10)
l1.head.nxt=node(20)
l1.head.nxt.nxt=node(30)
l1.head.nxt.nxt.nxt=node(40)
l1.ls()
#l1.head.nxt.nxt.nxt=node(40)
l1.len()
#l1.addback(20)
#l1.addback(35)
l1.display()
#l1.addeven()
#l1.search(20)
'''l2.head=node(55)
l2.node(50)
l2.head.nxt=node(60)
l2.head.nxt.nxt=node(70)
l2.display()
l2.addeven()'''