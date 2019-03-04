NPM = 1174043
char = "#"
if NPM%3 == 0:
    char = "*"
if NPM%3 == 1:
    char = "#"
if NPM%3 == 2:
    char = "+"
baris = []
baris.append("   ##      ##   ######## ##          #####   ##         #######  ")
baris.append(" ####    ####   ##    ## ##    ##   ##   ##  ##    ##  ##     ## ")
baris.append("   ##      ##       ##   ##    ##  ##     ## ##    ##         ## ")
baris.append("   ##      ##      ##    ##    ##  ##     ## ##    ##   #######  ")
baris.append("   ##      ##     ##     ######### ##     ## #########        ## ")
baris.append("   ##      ##     ##           ##   ##   ##        ##  ##     ## ")
baris.append(" ######  ######   ##           ##    #####         ##   #######  ")   
a = 0
for x in baris:
    print(baris[a].replace("#", char))
    a+=1