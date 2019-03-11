def pengulangan_089(npm):
    hitung = 0
    npm = str(npm)
    bilangan = npm[4:7]
    
    while(hitung < 17):
        print("Halo, "+bilangan+" apa kabar?")
        hitung = hitung +1

pengulangan_089(int(input("Masukan NPM : ")))