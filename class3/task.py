for i in range(101):
    output = str(i)
    if i % 3 == 0: 
        output += " foo"
    if i % 5 == 0:
        output += " bar"  
    if i % 10 == 0:
        output += " buzz"       
    print(output)
