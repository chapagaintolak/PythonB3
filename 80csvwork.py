# Read CSV File
import csv
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # to remove header row
    for line in csv_reader:
        print(f"{line[0]} salary is {line[1]} and person is {line[2]} years old.")


### Add Data
with open('data.csv','a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Amit', '20000', '25'])
    
    
        
# Suppose You Are Building Software For Bag Shop.
# You have to add new product
# List the product
# Delete the product
# Update the product
# Search the product