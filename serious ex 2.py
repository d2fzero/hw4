prices = {}
prices["banana"]= 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

purchased_items = {
"banana": 5,
"pear": 3

}
total= 0
for i in prices :
    for j in purchased_items :
        if i == j :
            print(i,",""quantity:" ,purchased_items[j],"prices : ",prices[i])
            total=total+purchased_items[j]*prices[i]



print("the total money is: ",total)