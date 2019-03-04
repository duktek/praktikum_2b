NPM = 1164081
char = "#"
if NPM%3 == 0:
    char = "*"
if NPM%3 == 1:
    char = "#"
if NPM%3 == 2:
    char = "+"
row = []
row.append("   ##      ##   ######## ##          #####   ########      ## ")   
row.append(" ####    ####   ##       ##    ##   ##   ##  ##    ##    #### ")  
row.append("   ##      ##   ##       ##    ##  ##     ## ##    ##      ## ") 
row.append("   ##      ##   ######## ##    ##  ##     ## ########      ## ") 
row.append("   ##      ##   ##    ## ######### ##     ## ##    ##      ## ") 
row.append("   ##      ##   ##    ##       ##   ##   ##  ##    ##      ## ") 
row.append(" ######  ###### ########       ##    #####   ########    ###### ")
a = 0
for x in row:
    print(row[a].replace("#", char))
    a+=1