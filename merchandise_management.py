import sqlite3

num = 0

def main():
    db = sqlite3.connect('critical_roll_tour_merch.db')
    cur = db.cursor()
    cur.execute('create table if not exists merchandiseInventory (merchName text, merchAmount int)')
    cur.execute('create table if not exists tourLocations (townName text, dateVisited text)')
    cur.execute('create table if not exists merchPurchased (merchName text, townName text, merchSold int)')

    print('Please select an option from the ones below\n1. Add New Merch To Merchandise Inventory\n2. Change Inventory\n3. Add New Show Date and Town\n4. Add Receipt of Merchandise Purchased at Each Location\n5. Check Merchandise Inventory')
    num = int(input('Enter number here: '))

    if num == 1:
        add_new_merchandise()
    if num == 2:
        update_merchandiseInventory()
    if num == 3:
        add_new_tour_date_town()
    if num == 4:
        add_new_receipt()
    if num == 5:
        show_inventory()


def add_new_merchandise():

def update_merchandiseInventory():
    
def add_new_tour_date_town():

def add_new_receipt():

def show_inventory():


main()