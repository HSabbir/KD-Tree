from TakeInput import *
from Node import Node

details = take_input()

dimension = details[0]

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,val):

        if self.root == None:
            self.root = Node(val)

        else:
            global dimension
            level = 0
            current = self.root
            while True:
                compareIndex = level % dimension
                level +=1
                if int(val[compareIndex]) < int(current.data[compareIndex]):
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif int(val[compareIndex]) > int(current.data[compareIndex]):
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    def search(self,node,val,level):

        if node == None or node.data == val:
            return node

        global dimension
        compareIndex = level % dimension

        if int(val[compareIndex]) < int(node.data[compareIndex]):
            return self.search(node.left,val,level+1)

        return self.search( node.right, val, level + 1)
        '''else:
            

            while True:
                
                level += 1
                if int(val[compareIndex]) < int(current.data[compareIndex]):
                    if current.left and current.left.data == val:
                        return True
                    else:
                        current.left = Node(val)
                        break
                elif int(val[compareIndex]) > int(current.data[compareIndex]):
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break'''

    def inorder(self, node):
        if node is not None:
            print(node.data)
            self.inorder(node.left)

            self.inorder(node.right)







numberOfNode = details[1]
data = details[2]
t = Tree()
for i in range(numberOfNode):
    t.insert(data[i])

while True:
    print('1.insert')
    print('2.search')
    print('3.print')
    print('4.exit')
    choice = int(input())
    if choice == 1:
        insertdata = input('enter insert data')
        insertdata = reformating(insertdata,',')
        t.insert(insertdata)
    elif choice == 2:
        searchdata = input('enter search data')
        searchdata = reformating(searchdata,',')
        s = t.search(t.root,searchdata,0)
        if s :
            print('Exists')
        else:
            print('Does not exists')
    elif choice == 3:
        t.inorder(t.root)

    elif choice == 4:
        break
    else:
        print('wrong choice..try again')