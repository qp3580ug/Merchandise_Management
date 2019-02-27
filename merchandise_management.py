import sqlite3
import os
import sys

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
        add_new_merchandise(cur)
    if num == 2:
        update_merchandiseInventory(cur)
    if num == 3:
        add_new_tour_date_town(cur)
    if num == 4:
        add_new_receipt(cur)
    if num == 5:
        show_inventory(cur)


def add_new_merchandise(cur):
    merchName = input('Enter type of Merchandise to add: ')
    merchAmount = input('Enter total number of Merchandise in stock: ')
    cur.execute('insert into merchandiseInventory values (?, ?)', (merchName, merchAmount))
    os.execl(sys.executable, sys.executable, *sys.argv)

def update_merchandiseInventory(cur):
    merchName = input('Enter merchandise you would like to change: ')
    merchAmount = input('Enter new total of merchandise: ')
    cur.execute('update merchandiseInventory where merchName=? set merchAmount=?', (merchName, merchAmount))
    os.execl(sys.executable, sys.executable, *sys.argv)

def add_new_tour_date_town(cur):
    townName = input('Please add a town name for the tour: ')
    dateVisited = input('Please add the date this town was visited: ')
    cur.execute('insert into tourLocations values (?, ?)', (townName, dateVisited))
    os.execl(sys.executable, sys.executable, *sys.argv)

def add_new_receipt(cur):
    merchName = input('Please enter merchandise on receipt: ')
    townName = input('Please enter the receipt town name where purchased: ')
    merchSold = int(input('Please enter total of this merchandise sold: '))
    cur.execute('insert into merchPurchased values (?, ?, ?)', (merchName, townName, merchSold))
    os.execl(sys.executable, sys.executable, *sys.argv)

def show_inventory(cur):
    for row in cur.execute('select * from merchandiseInventory'):
        print(row)
    os.execl(sys.executable, sys.executable, *sys.argv)

main()