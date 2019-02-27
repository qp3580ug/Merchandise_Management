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
        add_new_merchandise(num, cur)
    if num == 2:
        update_merchandiseInventory(num)
    if num == 3:
        add_new_tour_date_town(num)
    if num == 4:
        add_new_receipt(num)
    if num == 5:
        show_inventory(num, cur)


def add_new_merchandise(num, cur):
    merchName = input('Enter type of Merchandise to add: ')
    merchAmount = input('Enter total number of Merchandise in stock: ')
    cur.execute('insert into merchandiseInventory values (?, ?)', (merchName, merchAmount))
    os.execl(sys.executable, sys.executable, *sys.argv)

def update_merchandiseInventory(num):
    num = 0
    return num

def add_new_tour_date_town(num):
    num = 0
    return num

def add_new_receipt(num):
    num = 0
    return num

def show_inventory(num, cur):
    for row in cur.execute('select * from merchandiseInventory'):
        print(row)
    num = 0
    return num

main()