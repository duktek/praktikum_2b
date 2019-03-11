def pertambahan(npm):
    nilai = 0
    for i in npm:
        nilai += int(i)
    print(str(nilai)+" Merupakan Hasil Dari Pertambahan NPM Anda")

pertambahan(input("Masukan NPM : "))