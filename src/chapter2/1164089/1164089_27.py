def perkalian(npm):
    nilai = 0
    for i in npm:
        nilai *= int(i)
    print(str(nilai)+" Merupakan Hasil Nilai Perkalian NPM Anda")

perkalian(input("Masukan NPM : "))