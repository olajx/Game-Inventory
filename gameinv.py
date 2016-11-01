inv = OrderedDict = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 

# DISPLAY INVENTORY(step 1)
def display_inventory(inventory): 
    print()
    print("Inventory:")
    total_items = 0

    #k = key(i.e.: rope), v = value(i.e.: 1)
    for k, v in inventory.items():                          
        print(str(v) + ' ' + k)
        total_items += v
    print("Total number of items: " + str(total_items))

display_inventory(inv)

#ADD TO INVENTORY(step 2)
def add_to_inventory(inventory, added_items):

    # This method returns the key value available in the dictionary
    for i in range(len(added_items)):            
          inventory.setdefault(added_items[i],0)            
          inventory[added_items[i]] +=  1
    return inventory
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)

print()

#DISPLAY TABLE ORDERED BY COUNT(step 3)
def print_table(order=None):
    from collections import OrderedDict

    total_items = 0

    print("Inventory:")
    print(" count    item name")
    print("--------------------")

    # the table is unordered
    if order == None:
        new_inv = OrderedDict(inv.items())
        
    # the table is ordered by count in ascending order
    if order == "count,asc":
        new_inv = OrderedDict(sorted(inv.items(), key=lambda x: x[1]))

    # the table is ordered by count in descending order
    if order == "count,desc":
        new_inv = OrderedDict(sorted(inv.items(), key=lambda x: -x[1]))

    for k, v in new_inv.items():
            total_items += v
            print(str(v).rjust(6), k.rjust(12))

    print("-------------------")
    print("Total number of items: " + str(total_items))
    
print_table("count,desc")

#IMPORT NEW INVENTORY ITEMS FROM A FILE (step 4)
def import_inventory(filename):
    from collections import OrderedDict
    imTable = OrderedDict(inv.items())
    total_items = 0
    import csv
    with open('import_inventory.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['item_name'] in imTable:
                imTable[row['item_name']] =  int(imTable[row['item_name']]) + int(row['count'])
            else:
                imTable[row['item_name']] = row['count']
    return imTable

inv = import_inventory('import_inventory.csv')

display_inventory(inv)

#EXPORT ALL INVENTORY ITEMS TO A FILE (step 5)
def export_inventory(filename):
    import csv
    input_file=open(filename, "a")
    for k, v in inv.items():
        line = '{}, {}'.format(k, v) 
        print(line, file=input_file)        
    input_file.close()
print('filename: ')

export_inventory(input() or 'export_inventory.csv')
 
#WORK WITH SPECIAL CHARACTERS (step 6)
def __init__(self, f, dialect='import_inventory.csv', encoding="utf-8", **kwds):
    f = UTF8Recoder(f, encoding)
    self.reader = 'import_inventory.csv'.reader(f, dialect=dialect, **kwds)

def next(self):
    row = self.reader.next()
    return [unicode(s, "utf-8") for s in row]

def __iter__(self):
    return self
