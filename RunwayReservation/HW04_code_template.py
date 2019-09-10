# coding=UTF-8
import numpy as np

class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None



class BinaryTree:
    def __init__(self):
        self.root = None


    def insert(self,value,):

        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value,self.root)
    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print "value already in tree"

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print str(cur_node.value)
            self._print_tree(cur_node.right_child)

    def insertNode(self,value,k):
        # print k
        if self.root == None:
            self.root=node(value)

        else:
            self._insertNode(self.root,value,k)

    def _insertNode(self,cur_node,value,k):
        if value<self.root.value:
            print "Request at time",value,"is not allowed"
        else:

            if(value <= cur_node.value and (cur_node.value-value) >= k):
                if(cur_node.left_child):
                    self._insertNode(cur_node.left_child,value,k)
                else:
                    cur_node.left_child = node(value)
                    print "Request at time",value,"is allowed"
            elif(value >= cur_node.value and (value - cur_node.value) >= k):
                if(cur_node.right_child):
                    self._insertNode(cur_node.right_child,value,k)
                else:
                    cur_node.right_child = node(value)
                    print "Request at time",value,"is allowed"
            else:
                print "Request at time",value,"is not allowed"







if __name__ == "__main__":
    f = open('./04_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        # Write your code here
        # print npyArray

        tree = BinaryTree()

        k=npyArray[npyArray[0]+1]
        # print k

        for i in range(npyArray[0]):
            tf=tree.insert(npyArray[i+1])

            # print npyArray[i+1]

    # tree.print_tree()


        for j in range(len(npyArray)-npyArray[0]-2):
            # print npyArray[j+npyArray[0]+2]
            n=npyArray[j+npyArray[0]+2]

            tree.insertNode(n,k)

    # print tree.print_tree()
    f.close()


