# Deskripsi: Program Utama Tugas Besar Simulasi Vending Machine

def initialize():
    item = ["Fanta", "Coca Cola", "Nescafe", "Aqua"]
    price = [5000, 7000, 9000, 5000]
    qty = [10, 8, 12, 15]
    return item, price, qty

def newSession():
    credit = 0
    sum = 0
    return credit, sum

def displayMenu(item, price):
    print("Ini adalah vending machine minuman, silakan memilih")
    for i in range(0, len(item)):
        print(f"{i+1}. {item[i]} p: {price[i]} q: {qty[i]}")

# def addItem(item, price, qty, sum, credit):
#     done = False
#         selection = int(input("Nomor item yang ingin dibeli: "))
#         if(price[selection-1]<=credit-sum and sum > 0):
#             sum = sum + price[selection-1]
#             credit 
        
#     return sum





credit = 20000
# n = 5
# item, price, qty = [0] * n, [0] * n, [0] * n

item, price, qty = initialize()
credit, sum = newSession()
displayMenu(item, price)
