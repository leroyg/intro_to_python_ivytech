# subroutines here
import csv 

def readCSV(csvFile):
    phone_dir = {} 
    with open(csvFile, mode='r') as infile:
        reader = csv.reader(infile, delimiter=',')
        first_line = True
        for row in reader:
            if first_line:
                 first_line = False
            else:    
                phone_dir[row[0]] = row[1]
    return phone_dir 
    
# Function to write to csv
def writeCSV(csvFile, phone_dir, column1, column2):
    with open(csvFile, mode='w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        writer.writerow([column1, column2])
        for item in phone_dir:
            writer.writerow([item, phone_dir[item]])

# list contacts
def show_contacts(p_list):
    print("Show Contacts")
    print("Name\tNumber")
    for item in p_list:
        print(item + "\t" + p_list[item])

    
# add contacts
def add_contact(p_list):
    print("Add Contact")
    name = input("Contact name? ")
    phone = input("Phone number? ")
    p_list[name] = phone
    
# update contcts
def update_contact(phone_dir):
    print("Update Contact")
    name = input("Name: ")
    if (name in phone_dir):
        phone = input("New Number: ")
        phone_dir[name] = phone
        print(name, "Updated.")
    else:
        print(name, "Not found.")   

# delete contacts
def delete_contact(phone_dir):
    print("Delete Contact")    
    name = input("Name: ")
    if (name in phone_dir):
        del phone_dir[name]
        print(name, "Deleted.")
    else:
        print(name, "Not found.")

# ** MAIN PROGRAM **
print("Python Rolodex")
command = -1

phone_list_filepath = "./phone_list.csv"
phone_dir = readCSV(phone_list_filepath)

# while not exiting...
while command != 0:
    print("1 - Show Contact List")
    print("2 - Add to Contact List")
    print("3 - Update Contact Phone Number")
    print("4 - Delete Contact")        
    print("0 - Exit")
    command = int(input("Command? "))
    if command == 1:
        show_contacts(phone_dir)
    elif command == 2:
        add_contact(phone_dir)
    elif command == 3:
        update_contact(phone_dir)
    elif command == 4:
        delete_contact(phone_dir)

#Update database with changes
writeCSV(phone_list_filepath, phone_dir, "name", "number")

print("End of program.")


