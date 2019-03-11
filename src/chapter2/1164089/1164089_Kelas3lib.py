class kelas3lib:
    def __init__(self, npm):
        self.npm = npm

#No1
def NPM(npm):
    
    npm = list(str(npm))
    
    angka1 = {"0":" ++++++ ", "1":"  ++", "2":" +++++++ ", "3":" +++++++ ", "4":"     +++", "5":"++++++++", "6":" +++++++ ", "7":"+++++++++", "8":" +++++++ ", "9":" +++++++"}
    angka2 = {"0":"+++  +++", "1":"++++", "2":"++    +++", "3":"++    +++", "4":"   +++++", "5":"++      ", "6":"+++      ", "7":"     +++ ", "8":"+++   +++", "9":"++    +++"}
    angka3 = {"0":"+++  +++", "1":" +++", "2":"     +++ ", "3":"    ++++ ", "4":" +++  ++", "5":"+++++++ ", "6":"++++++++ ", "7":"    +++  ", "8":" +++ +++ ", "9":"++    +++"}
    angka4 = {"0":"+++  +++", "1":" +++", "2":"    +++  ", "3":"    ++++ ", "4":"++++++++", "5":"     +++", "6":"+++   +++", "7":"   +++   ", "8":" +++ +++ ", "9":" ++++++++"}
    angka5 = {"0":"+++  +++", "1":" +++", "2":"  ++++   ", "3":"++    +++", "4":"     +++", "5":"++   +++", "6":"+++   +++", "7":"  +++    ", "8":"+++   +++", "9":"      +++"}
    angka6 = {"0":" ++++++ ", "1":" +++", "2":"++++++++ ", "3":" +++++++ ", "4":"      +++", "5":" ++++++ ", "6":" +++++++ ", "7":" +++     ", "8":" +++++++ ", "9":" +++++++ "}
              
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
              
    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')

#No2
def pengulangan(npm):
    ulang = 1
    while(ulang <= 89):
        print("Halo, "+str(npm)+" apa kabar?")
        ulang += 1

#No3
def pengulangan_089(npm):
    hitung = 0
    npm = str(npm)
    bilangan = npm[4:7]
    
    while(hitung < 17):
        print("Halo, "+bilangan+" apa kabar?")
        hitung = hitung +1

#No4
def perulangan_0(npm):
    npm = str(npm)
    bilangan = npm[-3]  
    print("Halo, "+bilangan+" apa kabar?")

#No5
def down(npm):
    for i in npm:
        print (i)

#No6
def pertambahan(npm):
    nilai = 0
    for i in npm:
        nilai += int(i)
    print(str(nilai)+" Merupakan Hasil Dari Pertambahan NPM Anda")

#No7
def perkalian(npm):
    nilai = 0
    for i in npm:
        nilai *= int(i)
    print(str(nilai)+" Merupakan Hasil Nilai Perkalian NPM Anda")

#No8
def bilgenap():
    npm = [1,1,6,4,0,8,9]
    for i in npm:
        if (i % 2) == 0:
            print("Bilangan Genapnya Dari NPM : "+str(i))

#No9
def bilganjil():
    npm = [1,1,6,4,0,8,9]
    for i in npm:
        if (i%2)==1:
            print("Bilangan Ganjilnya Dari Npm : "+str(i))

#No10
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