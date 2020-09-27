number = int(input())

def getDivisor(num):
    div=[]
    for i in range(1,num+1):
        if num % i == 0:
            div.append(i)

    return div

def inputKey(lenth,divisor):
    mydictionary = {}
    count = 0
    while True:
        if count == lenth:
            break
        k = input()
        if mydictionary.__contains__(k) != True: # checking duplicate
            mydictionary[k] = divisor[count]
            count +=1

    return mydictionary


divisor = getDivisor(number)
lenth = len(divisor)

finalDict = inputKey(lenth,divisor)
print(finalDict)
