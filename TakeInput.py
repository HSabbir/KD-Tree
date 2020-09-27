
def take_input():
    dimension = int(input("Enter Number Of Dimension: "))
    numberOfNode = int(input("Enter Number Of Node: "))
    inputNode = []
    print("Enter Your Node Data: ")
    for i in range(numberOfNode):
        node = input()
        node = reformating(node,',')
        inputNode.append(node)

    all_input = [dimension,numberOfNode,inputNode]

    return all_input
def reformating(data,delimeter):

    return data.split(delimeter)
