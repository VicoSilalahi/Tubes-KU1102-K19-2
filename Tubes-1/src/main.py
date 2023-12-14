# Nama/NIM
# Alvin Christopher Santausa/19623129
# Anthony Alden Satriabudi/16523185
# Kiyo Lee Tiono/16523003
# Vico A C Silalahi/16523157

# Deskripsi: Program Utama Tugas Besar Simulasi Vending Machine

# Kamus Global
# inventory, userList, credit, totalCred, sum, count, selection: Integer
# Act: Boolean

# Algoritma
# Kumpulan Fungsi

# Fungsi clearScreen()
# Deskripsi: Fungsi untuk membuat newline sebanyak 50, membersihkan cli, bertindak seperti command 'cls' atau 'clear'
def clearScreen():
    for i in range(50):
        print()

# Fungsi initialize()
# Deskripsi: Fungsi untuk menginisialisasi inventory, hanya dilakukan diawal ketika program pertama kali bekerja
def initialize():
    inventory = [["Fanta", "Coca Cola", "Nescafe", "Aqua"], # Item at 0
                 [5000, 7000, 9000, 3000], # Price at 1
                 [10, 8, 12, 15]] # Quantity at 2
    
    userList = [0]*100
    return inventory, userList

# Fungsi displayMenu()
# Deskripsi: Fungsi untuk mengoutput pilihan menu kepada user
def displayMenu(inventory):
    print("1. Input Credit\n2. Pilih Item\n3. Ambil Kembalian dan Tutup Sesi\n4. Matikan Mesin")
    selection = int(input("Masukkan angka opsi: "))
    if(selection>4):
        clearScreen()
        print("Opsi tidak valid!")
    else:
        return selection

# Fungsi inputCredit()
# Deskrispi: Fungsi untuk menambah credit setelah pengisian credit awal
def inputCredit():
    credit = int(input("Masukkan credit (0 untuk kembali): "))
    if(credit<0):
        print("Credit tidak valid!")
        return inputCredit()
    clearScreen()
    return credit

# Fungsi showItem()
# Deskripsi: Fungsi untuk mengoutput item yang tersedia dengan harga dan kuantitas, serta status dari kuantitas tersebut
def showItem():
    print("Item yang tesedia: ")
    for i in range(0, len(inventory[0])):
        print(f"{i+1}. {inventory[0][i]} Harga: {inventory[1][i]} Jumlah: {inventory[2][i]}", end="")
        if(inventory[2][i]==0):
            print(", Habis!", end="")
        print()    

# Fungsi selItem()
# Deskripsi: Fungsi untuk memilih item yang ingin dibeli user, dengan memeriksa jumlah barang, serta sisa credit
def selItem(inventory, sum, credit, count, userList):
    showItem()
    selection = int(input("Nomor item yang ingin dibeli: "))
    if(selection>len(inventory)):
        clearScreen()
        print("Indeks item tidak ada, input item yang valid")
    elif(inventory[2][selection-1]>0):
        if(inventory[1][selection-1]<=credit):
            sum = sum + inventory[1][selection-1]
            count += 1
            userList[count] = selection
            inventory[2][selection-1] -= 1
            clearScreen()
        else:
            clearScreen()
            print("Credit Kurang, pilih item lain, masukkan credit, atau tutup sesi dan ambil kembalian")
    else:
        clearScreen()
        print("Item Habis, pilih item lain")
    return sum, count, userList

# Fungsi checkActivity()
# Deskripsi: Fungsi untuk menutup atau melanjutkan sesi user
def checkActivity():
    print("Tutup Sesi?\n1. Ya, tutup sesi dan ambil kembalian\n2. Tidak, lanjut sesi")
    opt = int(input("Masukkan angka opsi: "))
    if(opt==1):
        act = True
    else:
        act = False
    clearScreen()
    return act

# Fungsi printReceipt()
# Deskripsi: Fungsi untuk mengoutput daftar item yang dibeli user, dan kembalian akhir
def printReceipt(credit, userList):
    i = 0
    check = True
    print(f"Item yang dibeli: ")
    while(check == True):
        i+=1
        print(f"{i}. {inventory[0][userList[i]-1]}")
        if(userList[i+1]==0):
            check = False
    print(f"Total Pembelian : {sum}")
    print(f"Kembalian Credit: {credit}\n\n")
    userList = [0]*100
    

# Fungsi printAscii
# Deskripsi: Fungsi untuk mengoutput ASCII ART sebagai dekorasi interface
def printAscii():
    ascii_art = '''
     __   __           _ _             __  __         _    _          
     \ \ / /__ _ _  __| (_)_ _  __ _  |  \/  |__ _ __| |_ (_)_ _  ___ 
      \ V / -_) ' \/ _` | | ' \/ _` | | |\/| / _` / _| ' \| | ' \/ -_)
       \_/\___|_||_\__,_|_|_||_\__, | |_|  |_\__,_\__|_||_|_|_||_\___|
                               |___/                                  
    '''
    print("\033[1;33;40m", ascii_art)
    print()

# Proses Utama

# Inisialisasi Utama, menghidupkan mesin dan mengisi inventory
state = True
inventory, userList = initialize()

# Program akan diloop hingga user/pemilik mesin mematikan mesin
while(state == 1):
    printAscii()
    credit = inputCredit()
    totalCred = credit
    sum = 0
    Act = True
    count = 0
    while(Act == True):
        printAscii()
        print(f"Credit tersisa: {credit}")
        print(f"Total Pembelian: {sum}")
        selection = displayMenu(inventory)
        if(selection == 1):
            clearScreen()
            printAscii()
            totalCred = totalCred + inputCredit()
            credit = totalCred - sum 
        elif(selection == 2):
            clearScreen()
            printAscii()
            print("Credit tersisa: ", credit)
            sum, count, userList = selItem(inventory, sum, credit, count, userList)
            credit = totalCred - sum
        elif(selection == 3):
            clearScreen()
            printAscii()
            if(checkActivity()):
                printReceipt(credit, userList)
                Act = False
        elif(selection == 4):
            clearScreen()
            printAscii()
            onoff = int(input("Matikan Mesin?\n1. Ya\n2. Tidak"))
            if(onoff==1):
                Act = False
                state = False