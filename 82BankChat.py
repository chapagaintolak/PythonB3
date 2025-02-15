import csv
import os
from datetime import datetime
from tabulate import tabulate  # Import tabulate for pretty tables

# File to store visitor data
FILE_NAME = "visitorInfo.csv"

# Ensure CSV file exists with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Name", "Purpose"])

# Load existing visitors from CSV
def load_visitors():
    visitors = []
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                visitors.append(row)
    except Exception as e:
        print(f"Error loading visitors: {e}")
    return visitors

# Save visitors to CSV
def save_visitors(visitors):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Name", "Purpose"])
        for visitor in visitors:
            writer.writerow([visitor["ID"], visitor["Date"], visitor["Name"], visitor["Purpose"]])

# Get today's date automatically, allowing editing
def get_visit_date():
    today_date = datetime.today().strftime("%Y-%m-%d")
    edit_date = input(f"Visit Date (Default: {today_date}, press Enter to keep): ").strip()
    return edit_date if edit_date else today_date

# Add visitor with optional ID input
def add_visitor(visitors):
    print("\n➕ Add Visitor")
    id_option = input("Do you want to input an ID manually? (y/n): ").strip().lower()
    if id_option == "y":
        while True:
            visitor_id = input("Enter visitor ID: ").strip()
            # Check if ID already exists
            if any(v["ID"] == visitor_id for v in visitors):
                print("\n⚠️ ID already exists! Please use a unique ID.\n")
            else:
                break
    else:
        # Auto-generate ID (next available number)
        visitor_id = str(len(visitors) + 1)
        print(f"Auto-generated ID: {visitor_id}")

    date = get_visit_date()
    name = input("Enter visitor name: ").strip()
    purpose = input("Enter visit purpose: ").strip()
    visitors.append({"ID": visitor_id, "Date": date, "Name": name, "Purpose": purpose})
    save_visitors(visitors)
    print(f"\n✅ Visitor {name} added successfully with ID: {visitor_id}!\n")

# List visitors (Pretty Table)
def list_visitors(visitors):
    if not visitors:
        print("\n⚠️ No visitors found.\n")
        return

    table_data = [[v["ID"], v["Date"], v["Name"], v["Purpose"]] for v in visitors]
    print("\n📜 Visitor List:\n")
    print(tabulate(table_data, headers=["ID", "Date", "Name", "Purpose"], tablefmt="grid"))
    print()

# Delete visitor
def delete_visitor(visitors):
    visitor_id = input("Enter visitor ID to delete: ").strip()
    updated_visitors = [v for v in visitors if v["ID"] != visitor_id]
    if len(updated_visitors) < len(visitors):
        save_visitors(updated_visitors)
        print("\n✅ Visitor deleted successfully!\n")
    else:
        print("\n⚠️ Visitor ID not found!\n")

# Update visitor with flexible fields
def update_visitor(visitors):
    visitor_id = input("Enter visitor ID to update: ").strip()
    for visitor in visitors:
        if visitor["ID"] == visitor_id:
            print("\n👤 Current Visitor Details:")
            print(tabulate([[visitor["ID"], visitor["Date"], visitor["Name"], visitor["Purpose"]]], headers=["ID", "Date", "Name", "Purpose"], tablefmt="grid"))
            print()

            # Update ID
            update_id = input("Do you want to update the ID? (y/n): ").strip().lower()
            if update_id == "y":
                while True:
                    new_id = input("Enter new ID: ").strip()
                    if any(v["ID"] == new_id for v in visitors):
                        print("\n⚠️ ID already exists! Please use a unique ID.\n")
                    else:
                        visitor["ID"] = new_id
                        break

            # Update Date
            update_date = input("Do you want to update the date? (y/n): ").strip().lower()
            if update_date == "y":
                visitor["Date"] = get_visit_date()

            # Update Name
            update_name = input("Do you want to update the name? (y/n): ").strip().lower()
            if update_name == "y":
                visitor["Name"] = input("Enter new name: ").strip()

            # Update Purpose
            update_purpose = input("Do you want to update the purpose? (y/n): ").strip().lower()
            if update_purpose == "y":
                visitor["Purpose"] = input("Enter new purpose: ").strip()

            save_visitors(visitors)
            print("\n✅ Visitor updated successfully!\n")
            return
    print("\n⚠️ Visitor ID not found!\n")

# Search visitor by ID, first name word, date, or purpose
def search_visitor(visitors):
    search_term = input("Enter search term (ID, name's first word, date, or purpose): ").strip()
    if not search_term:
        print("\n⚠️ Search term cannot be empty!\n")
        return

    found = []
    for v in visitors:
        # Check ID exact match
        if v["ID"] == search_term:
            found.append(v)
            continue
        # Check first word of name (case-insensitive)
        name_parts = v["Name"].strip().split()
        name_first_word = name_parts[0].lower() if name_parts else ''
        if name_first_word == search_term.lower():
            found.append(v)
            continue
        # Check date contains search_term
        if search_term in v["Date"]:
            found.append(v)
            continue
        # Check purpose contains search_term (case-insensitive)
        if search_term.lower() in v["Purpose"].lower():
            found.append(v)
            continue

    print(f"\n🔎 Found {len(found)} matching visitors:")
    if found:
        table_data = [[v["ID"], v["Date"], v["Name"], v["Purpose"]] for v in found]
        print(tabulate(table_data, headers=["ID", "Date", "Name", "Purpose"], tablefmt="grid"))
    else:
        print("No visitors found.")
    print()

# Show visitor by ID
def show_visitor_by_id(visitors):
    visitor_id = input("Enter visitor ID to view details: ").strip()
    for v in visitors:
        if v["ID"] == visitor_id:
            print("\n👤 Visitor Details:\n")
            print(tabulate([[v["ID"], v["Date"], v["Name"], v["Purpose"]]], headers=["ID", "Date", "Name", "Purpose"], tablefmt="grid"))
            print()
            return
    print("\n⚠️ Visitor ID not found!\n")

# Main program loop
def main():
    visitors = load_visitors()
    while True:
        print("\n📌 Visitor Entry System")
        print("1. Add Visitor")
        print("2. List Visitors")
        print("3. Delete Visitor")
        print("4. Update Visitor")
        print("5. Search Visitor")
        print("6. Show Visitor by ID")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_visitor(visitors)
        elif choice == "2":
            visitors = load_visitors()  # Reload visitors from CSV before listing
            list_visitors(visitors)
        elif choice == "3":
            delete_visitor(visitors)
        elif choice == "4":
            update_visitor(visitors)
        elif choice == "5":
            search_visitor(visitors)
        elif choice == "6":
            show_visitor_by_id(visitors)
        elif choice == "7":
            print("\n👋 Exiting program. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()