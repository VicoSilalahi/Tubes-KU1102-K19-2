# Deskripsi: Program Utama Tugas Besar Simulasi Vending Machine

def clearScreen():
    for i in range(50):
        print()

def initialize():
    inventory = [["Fanta", "Coca Cola", "Nescafe", "Aqua"], # Item at 0
                 [5000, 7000, 9000, 3000], # Price at 1
                 [10, 8, 12, 15]] # Quantity at 2
    userList = [0]*100
    return inventory, userList

def displayMenu(inventory):
    print("1. Input Credit\n2. Pilih Item\n3. Ambil Kembalian dan Tutup Sesi")
    selection = int(input("Masukkan angka opsi: "))
    return selection

def inputCredit():
    credit = int(input("Masukkan credit: "))
    if(credit<=0):
        print("Credit tidak valid!")
        return inputCredit()
    clearScreen()
    return credit

def showItem():
    print("Item yang tesedia: ")
    for i in range(0, len(inventory[0])):
        print(f"{i+1}. {inventory[0][i]} p: {inventory[1][i]} q: {inventory[2][i]}", end="")
        if(inventory[2][i]==0):
            print(" Habis!", end="")
        print()    

def selItem(inventory, sum, credit, count, userList):
    showItem()
    selection = int(input("Nomor item yang ingin dibeli: "))
    # print(credit)
    if(inventory[2][selection-1]>0):
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

def checkActivity():
    print("Tutup Sesi?\n1. Ya, tutup sesi dan ambil kembalian\n2. Tidak, lanjut sesi")
    opt = int(input("Masukkan angka opsi: "))
    if(opt==1):
        act = True
    else:
        act = False
    clearScreen()
    return act

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

while(True):
    print("Ini adalah vending machine minuman, silakan pilih menu")
    inventory, userList = initialize()
    credit = inputCredit()
    totalCred = credit
    sum = 0
    Act = True
    count = 0
    while(Act == True):
        print(f"Credit tersisa: {credit}")
        print(f"Total Pembelian: {sum}")
        selection = displayMenu(inventory)
        if(selection == 1):
            clearScreen()
            totalCred = totalCred + inputCredit()
            credit = totalCred - sum 
        elif(selection == 2):
            clearScreen()
            print("Credit tersisa: ", credit)
            sum, count, userList = selItem(inventory, sum, credit, count, userList)
            credit = totalCred - sum
        elif(selection == 3):
            clearScreen()
            if(checkActivity()):
                printReceipt(credit, userList)
                Act = False