# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 20:27:19 2021

"""
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def init__(self):
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self,data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head #this will goes to zero
        while itr.next: #till next become zero
            itr = itr.next #incrementing
            itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
            if node.next:
                node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index, no):
        for i in range(no):
            if index<0 or index>self.get_length():
                raise Exception('Invalid Index')
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
                return
            count = 0
            itr = self.head
            while itr:
                if count == index: #Remove = 2 count = 2
                    itr.prev.next = itr.next
                    if itr.next:
                        itr.next.prev = itr.prev
                    break
                itr = itr.next
                count += 1
                
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def print_list(self):
        if self.head == None:
            print("Doubly linked list is empty")
            return
        itr = self.head()
        lstr = " "
        while itr:
            lstr += str(itr.data)
            itr = itr.next
            
        print(lstr)
        
def main():
    f=open("inputDLL.rtf")
    content = f.read()
    print(content)
    dict = {content.split(":")}
    print(lines,'\n')
    
    
if _name_ == "__main__":
    dllist = DoublyLinkedList()
    dllist.insert_values([])
    dllist.insert_at_beginning('Dave')
    dllist.print_list()
    dllist.insert_at_end('Ricky')
    dllist.print_list()
    dllist.insert_at(1, 'Harry')
    dllist.print_list()
    dllist.insert_at_end('Adam')
    dllist.print_list()
    dllist.insert_at(0,'Jerry')
    dllist.print_list()
    dllist.insert_at(1,'Rob')
    dllist.print_list()
    dllist.remove_at(1,2)
    dllist.print_list()

