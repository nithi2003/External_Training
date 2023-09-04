class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class ll:
    def __init__(self):
        self.head = None
        self.head1 = None
    def insert(self,val):
        new = node(val)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    def insert2(self,val):
        new = node(val)
        if self.head1 is None:
            self.head1 = new
        else:
            temp = self.head1
            while temp.next:
                temp = temp.next
            temp.next = new
    def sort(self):
        l = []
        temp = self.head
        temp2 = self.head1
        if self.head is None and self.head1 is not None:
            return self.head1
        if self.head is not None and self.head1 is None:
            return self.head
        if self.head is None and self.head1 is None:
            return self.head
        while temp:
            l.append(temp.data)
            temp = temp.next
        while temp2:
            l.append(temp2.data)
            temp2 = temp2.next
        l.sort()
        i = 0
        temp = self.head
        while temp:
            if temp.data!=l[i]:
                temp.data,l[i]=l[i],temp.data
            i+=1
            temp = temp.next
        temp = self.head
        while temp.next:
            temp = temp.next
        while i<len(l):
            temp.next = node(l[i])
            i+=1
            temp = temp.next
        temp3 = self.head
        while temp3:
            print(temp3.data,end=" ")
            temp3 = temp3.next
    def some(self,left,right):
        temp = self.head
        l = []
        for i in range(left-1):
            temp = temp.next
        for j in range(left,right+1):
            l.append(temp.data)
            temp = temp.next
        l = l[::-1]
        temp2 = self.head
        j = 0
        for i in range(left-1):
            temp2 = temp2.next
        for i in range(left,right+1):
            temp2.data,l[j]=l[j],temp2.data
            temp2 = temp2.next
            j+=1
        temp3 = self.head
        while temp3:
            print(temp3.data,end=" ")
            temp3 = temp3.next
                

o = ll()
o.insert(1)
o.insert(2)
o.insert(3)
o.insert(4)
o.insert(5)
#o.sort()
o.some(2,4)
