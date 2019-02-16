#Emily Wilson
#12-5-18
#HW7- Advanced Algorithms

#Using python 3

import sys

def parseFile(filename):
    weights = []
    values = []
    intro = []
    isOne = True
    
    if filename[5] == "1":
        isOne = True 
    else:
        isOne = False
    
    infile = open(filename, 'r')
                
    line = infile.readline() #first line
    line = line.strip()
    pieces = line.split(" ") 
    for x in pieces:
        intro.append(x)
    maxWeight = int(intro[1])
    
    line = infile.readline() #weights
    line = line.strip()
    pieces = line.split(" ") 
    for x in pieces:
        weights.append(int(x))
    
    line = infile.readline() #values
    line = line.strip()
    pieces = line.split(" ") 
    for x in pieces:
        values.append(int(x))

    infile.close()
    knapsack(values, weights, maxWeight, isOne)    

def knapsack(vals, wts, w, isOne):
    
    h=len(vals)

    table = [[0 for x in range(w + 1)] for i in range(len(vals) + 1)]

    # First iterate over the items (rows)
    # second iterate over the columns which represent weights

    for i in range(1,h+1):
        for x in range(1,w+1):
            currWeight=wts[i-1]
            currValue=vals[i-1]
          
            if currWeight > x:   #case 1
                table[i][x] = table[i-1][x]
                
            else:
                 #we can fit the item in the sack and now we have to figure out
                #if it's worth swiping it
                
                # if the value of the item < capacity
                dont_bring= table[i-1][x]
                # val of current item  + val of remaining weight
                do_bring_it = currValue + table[i-1][x - currWeight]

                table[i][x] = max(dont_bring, do_bring_it)

    solution_arr = []

    for x in table:
        for y in x:
            solution_arr.append(y)

    result = []
    weightLimit = w
    for i in range(h, 0, -1):
           
        if table[i][weightLimit] != table[i-1][weightLimit]:
            item = (i-1, wts[i-1],vals[i-1])
            result.append(item)
            weightLimit -= wts[i-1]
    
    finalItems = []
    finalWeight = 0
    finalValue = 0
    for x in result:
        finalItems.append(x[0])
        finalWeight += x[1]
        finalValue += x[2]
    
    if isOne:
        infile = open("output1.txt", "w")
        infile.write("List of items (indices) in final knapsack: %s\n" %(finalItems))
        infile.writelines("Total weight: %s\n" %(finalWeight))
        infile.writelines("Total value: %s\n" %(finalValue))
        infile.close()
    else:
        infile = open("output2.txt", "w")
        infile.write("List of items (indices) in final knapsack: %s \n" %(finalItems))
        infile.writelines("Total weight: %s\n" %(finalWeight))
        infile.writelines("Total value: %s\n" %(finalValue))
        infile.close()
    
def main():
    
   # fileName = input("enter file ")
    fileName = sys.argv[1]
    fileName = parseFile(fileName)
        
main()
    
    
    
