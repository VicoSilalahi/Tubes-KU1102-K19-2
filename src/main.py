# Deskripsi: Program Utama Tugas Besar Simulasi Vending Machine
# Test commit

def clearScreen():
    for i in range(20):
        print()

def initialize():
    inventory = [["Fanta", "Coca Cola", "Nescafe", "Aqua"], # Item at 0
                 [5000, 7000, 9000, 3000], # Price at 1
                 [10, 8, 12, 15]] # Quantity at 2
    userList = [0]*100
    return inventory, userList

def displayMenu(inventory):
    print("1. Input Credit\n2. Pilih Barang\n3. Ambil Kembalian dan Tutup Sesi")
    selection = int(input("Masukkan angka opsi: "))
    return selection
    

def inputCredit():
    credit = int(input("Masukkan credit: "))
    if(credit<=0):
        print("Credit tidak valid!")
        return inputCredit()
    return credit

def showItem():
    print("Item yang tesedia: ")
    for i in range(0, len(inventory[0])):
        print(f"{i+1}. {inventory[0][i]} p: {inventory[1][i]} q: {inventory[2][i]}", end="")
        if(inventory[2][i]==0):
            print(" Habis!")
        print()
        

def selItem(inventory, sum, credit, count, userList):
    showItem()
    selection = int(input("Nomor item yang ingin dibeli: "))
    if(inventory[1][selection-1]<=credit-sum):
        sum = sum + inventory[1][selection-1]
        count += 1
        userList[count] = selection
    else:
        print("Credit Kurang, pilih barang lain, masukkan credit, atau tutup sesi dan ambil kembalian")
    return sum, count, userList

def checkActivity():
    print("Lanjut sesi?\n1. Ya\n2. Tidak, tutup sesi, dan ambil kembalian")
    opt = int(input("Masukkan angka opsi: "))
    if(opt==1):
        act = True
    else:
        act = False
    return act

def printReceipt(credit, userList):
    i = 0
    check = True
    while(check == True):
        i+=1
        print(inventory[0][userList[i]-1])
        if(userList[i+1]==0):
            check = False
    print(credit)

while(True):
    print("Ini adalah vending machine minuman, silakan pilih menu")
    inventory, userList = initialize()
    credit = inputCredit()
    initCredit = credit
    sum = 0
    Act = True
    count = 0
    while(Act == True):
        print("Credit tersisa: ", credit)
        print("Total Pembelian: ", sum)
        selection = displayMenu(inventory)
        if(selection == 1):
            credit = credit + inputCredit()
        elif(selection == 2):
            print("Credit tersisa: ", credit)
            sum, count, userList = selItem(inventory, sum, credit, count, userList)
            credit = initCredit - sum
        elif(selection == 3):
            if(checkActivity()):
                printReceipt(credit, userList)
                Act = False