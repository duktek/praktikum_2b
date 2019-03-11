def bilprima(npm):
    npm = str(npm)
    nilai = npm[2]
    num = int(nilai)
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                print("Bukan Bilangan Prima")
                break
            else:
                print("Merupakan Bilangan Primanya :"+str(num))
    else:
        print("Tidak Ada Bilangan Prima")
bilprima(int(input("Masukan NPM : ")))