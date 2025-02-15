import csv
import os
from datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk

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
        messagebox.showerror("Error", f"Error loading visitors: {e}")
    return visitors

# Save visitors to CSV
def save_visitors(visitors):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Name", "Purpose"])
        for visitor in visitors:
            writer.writerow([visitor["ID"], visitor["Date"], visitor["Name"], visitor["Purpose"]])

# Get today's date automatically
def get_visit_date():
    return datetime.today().strftime("%Y-%m-%d")

# Add visitor with optional ID input
def add_visitor():
    def save():
        id_option = id_choice.get()
        visitor_id = id_entry.get().strip()
        name = name_entry.get().strip()
        purpose = purpose_entry.get().strip()
        date = date_entry.get().strip()

        if not name or not purpose:
            messagebox.showwarning("Input Error", "Name and Purpose fields are required!")
            return

        visitors = load_visitors()

        if id_option == "manual":
            if not visitor_id:
                messagebox.showwarning("Input Error", "Please enter an ID!")
                return
            if any(v["ID"] == visitor_id for v in visitors):
                messagebox.showwarning("Input Error", "ID already exists! Please use a unique ID.")
                return
        else:
            visitor_id = str(len(visitors) + 1)  # Auto-generate ID

        visitors.append({"ID": visitor_id, "Date": date, "Name": name, "Purpose": purpose})
        save_visitors(visitors)
        messagebox.showinfo("Success", f"Visitor {name} added successfully with ID: {visitor_id}!")
        add_window.destroy()
        refresh_table()

    add_window = Toplevel(root)
    add_window.title("Add Visitor")
    add_window.geometry("400x300")

    Label(add_window, text="ID Option:").grid(row=0, column=0, padx=10, pady=10)
    id_choice = StringVar(value="auto")
    Radiobutton(add_window, text="Auto-generate ID", variable=id_choice, value="auto").grid(row=0, column=1, sticky=W)
    Radiobutton(add_window, text="Manual ID", variable=id_choice, value="manual").grid(row=1, column=1, sticky=W)

    Label(add_window, text="ID:").grid(row=2, column=0, padx=10, pady=10)
    id_entry = Entry(add_window)
    id_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(add_window, text="Name:").grid(row=3, column=0, padx=10, pady=10)
    name_entry = Entry(add_window)
    name_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(add_window, text="Purpose:").grid(row=4, column=0, padx=10, pady=10)
    purpose_entry = Entry(add_window)
    purpose_entry.grid(row=4, column=1, padx=10, pady=10)

    Label(add_window, text="Date:").grid(row=5, column=0, padx=10, pady=10)
    date_entry = Entry(add_window)
    date_entry.insert(0, get_visit_date())
    date_entry.grid(row=5, column=1, padx=10, pady=10)

    Button(add_window, text="Save", command=save).grid(row=6, column=1, pady=20)

# List visitors in a table (MISSING FUNCTION)
def list_visitors():
    visitors = load_visitors()
    if not visitors:
        messagebox.showinfo("Info", "No visitors found.")
        return

    table_window = Toplevel(root)
    table_window.title("Visitor List")
    table_window.geometry("600x400")

    columns = ("ID", "Date", "Name", "Purpose")
    tree = ttk.Treeview(table_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill=BOTH, expand=True)

    for visitor in visitors:
        tree.insert("", END, values=(visitor["ID"], visitor["Date"], visitor["Name"], visitor["Purpose"]))


# Delete visitor by ID
def delete_visitor():
    def delete():
        visitor_id = id_entry.get().strip()
        if not visitor_id:
            messagebox.showwarning("Input Error", "Please enter an ID!")
            return

        visitors = load_visitors()
        updated_visitors = [v for v in visitors if v["ID"] != visitor_id]
        if len(updated_visitors) < len(visitors):
            save_visitors(updated_visitors)
            messagebox.showinfo("Success", "Visitor deleted successfully!")
            delete_window.destroy()
            refresh_table()
        else:
            messagebox.showwarning("Error", "Visitor ID not found!")

    delete_window = Toplevel(root)
    delete_window.title("Delete Visitor")
    delete_window.geometry("300x150")

    Label(delete_window, text="Enter Visitor ID:").pack(pady=10)
    id_entry = Entry(delete_window)
    id_entry.pack(pady=10)

    Button(delete_window, text="Delete", command=delete).pack(pady=20)

# Update visitor details with old/new comparison
def update_visitor():
    def load_visitor_data():
        visitor_id = id_entry.get().strip()
        if not visitor_id:
            messagebox.showwarning("Input Error", "Please enter an ID!")
            return

        visitors = load_visitors()
        found = [v for v in visitors if v["ID"] == visitor_id]
        
        if not found:
            messagebox.showwarning("Error", "Visitor ID not found!")
            return
        
        global original_data
        original_data = found[0]
        
        # Populate fields with existing data
        old_id_label.config(text=original_data["ID"])
        old_date_label.config(text=original_data["Date"])
        old_name_label.config(text=original_data["Name"])
        old_purpose_label.config(text=original_data["Purpose"])
        
        date_entry.delete(0, END)
        date_entry.insert(0, original_data["Date"])
        name_entry.delete(0, END)
        name_entry.insert(0, original_data["Name"])
        purpose_entry.delete(0, END)
        purpose_entry.insert(0, original_data["Purpose"])

    def save_changes():
        new_id = id_entry.get().strip()
        new_date = date_entry.get().strip()
        new_name = name_entry.get().strip()
        new_purpose = purpose_entry.get().strip()

        if not all([new_id, new_date, new_name, new_purpose]):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        visitors = load_visitors()
        
        # Check if ID was changed and validate uniqueness
        if new_id != original_data["ID"]:
            if any(v["ID"] == new_id for v in visitors):
                messagebox.showwarning("Error", "New ID already exists!")
                return

        # Update the visitor record
        for visitor in visitors:
            if visitor["ID"] == original_data["ID"]:
                visitor["ID"] = new_id
                visitor["Date"] = new_date
                visitor["Name"] = new_name
                visitor["Purpose"] = new_purpose
                break

        save_visitors(visitors)
        messagebox.showinfo("Success", "Visitor updated successfully!")
        update_window.destroy()
        refresh_table()

    update_window = Toplevel(root)
    update_window.title("Update Visitor")
    update_window.geometry("800x400")

    # Old Data Frame
    old_frame = LabelFrame(update_window, text="Original Data")
    old_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N)

    Label(old_frame, text="ID:").grid(row=0, column=0, sticky=W)
    old_id_label = Label(old_frame, text="", fg="gray")
    old_id_label.grid(row=0, column=1, sticky=W)

    Label(old_frame, text="Date:").grid(row=1, column=0, sticky=W)
    old_date_label = Label(old_frame, text="", fg="gray")
    old_date_label.grid(row=1, column=1, sticky=W)

    Label(old_frame, text="Name:").grid(row=2, column=0, sticky=W)
    old_name_label = Label(old_frame, text="", fg="gray")
    old_name_label.grid(row=2, column=1, sticky=W)

    Label(old_frame, text="Purpose:").grid(row=3, column=0, sticky=W)
    old_purpose_label = Label(old_frame, text="", fg="gray")
    old_purpose_label.grid(row=3, column=1, sticky=W)

    # New Data Frame
    new_frame = LabelFrame(update_window, text="New Data")
    new_frame.grid(row=0, column=1, padx=10, pady=10, sticky=N)

    Label(new_frame, text="ID:").grid(row=0, column=0, sticky=W)
    id_entry = Entry(new_frame)
    id_entry.grid(row=0, column=1, sticky=W)

    Label(new_frame, text="Date:").grid(row=1, column=0, sticky=W)
    date_entry = Entry(new_frame)
    date_entry.grid(row=1, column=1, sticky=W)

    Label(new_frame, text="Name:").grid(row=2, column=0, sticky=W)
    name_entry = Entry(new_frame)
    name_entry.grid(row=2, column=1, sticky=W)

    Label(new_frame, text="Purpose:").grid(row=3, column=0, sticky=W)
    purpose_entry = Entry(new_frame)
    purpose_entry.grid(row=3, column=1, sticky=W)

    # Control Buttons
    Button(update_window, text="Load Data", command=load_visitor_data).grid(row=1, column=0, pady=10)
    Button(update_window, text="Save Changes", command=save_changes).grid(row=1, column=1, pady=10)

# Search visitor by ID, name, date, or purpose
def search_visitor():
    def search():
        search_term = search_entry.get().strip()
        if not search_term:
            messagebox.showwarning("Input Error", "Search term cannot be empty!")
            return

        visitors = load_visitors()
        found = []
        for v in visitors:
            if (search_term == v["ID"] or
                search_term.lower() in v["Name"].lower() or
                search_term in v["Date"] or
                search_term.lower() in v["Purpose"].lower()):
                found.append(v)

        if found:
            table_window = Toplevel(root)
            table_window.title("Search Results")
            table_window.geometry("600x400")

            columns = ("ID", "Date", "Name", "Purpose")
            tree = ttk.Treeview(table_window, columns=columns, show="headings")
            for col in columns:
                tree.heading(col, text=col)
            tree.pack(fill=BOTH, expand=True)

            for visitor in found:
                tree.insert("", END, values=(visitor["ID"], visitor["Date"], visitor["Name"], visitor["Purpose"]))
        else:
            messagebox.showinfo("Info", "No matching visitors found.")

    search_window = Toplevel(root)
    search_window.title("Search Visitor")
    search_window.geometry("300x150")

    Label(search_window, text="Enter Search Term:").pack(pady=10)
    search_entry = Entry(search_window)
    search_entry.pack(pady=10)

    Button(search_window, text="Search", command=search).pack(pady=20)

# Refresh the table in the main window
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    visitors = load_visitors()
    for visitor in visitors:
        tree.insert("", END, values=(visitor["ID"], visitor["Date"], visitor["Name"], visitor["Purpose"]))

# Main GUI setup
root = Tk()
root.title("Visitor Entry System")
root.geometry("400x300")

# Main table
columns = ("ID", "Date", "Name", "Purpose")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill=BOTH, expand=True)

# Buttons
Button(root, text="Add Visitor", command=add_visitor).pack(side=LEFT, padx=10, pady=10)
Button(root, text="List Visitors", command=list_visitors).pack(side=LEFT, padx=10, pady=10)
Button(root, text="Delete Visitor", command=delete_visitor).pack(side=LEFT, padx=10, pady=10)
Button(root, text="Update Visitor", command=update_visitor).pack(side=LEFT, padx=10, pady=10)
Button(root, text="Search Visitor", command=search_visitor).pack(side=LEFT, padx=10, pady=10)

# Load initial data
refresh_table()

# Run the application
root.mainloop()