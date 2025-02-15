import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

class BagShopApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bag Shop Management System")
        self.geometry("1000x700")

        # Create CSV file with header if not exists
        if not os.path.isfile('bag_shop_data.csv'):
            with open('bag_shop_data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["ID", "Name", "Qty", "Price"])

        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create left frame for buttons
        left_frame = tk.Frame(self, width=150, bg="#f0f0f0")
        left_frame.grid(row=0, column=0, sticky="nswe")

        # Create buttons
        buttons = [
            ("Add Product", AddFrame),
            ("List Products", ListFrame),
            ("Delete Product", DeleteFrame),
            ("Update Product", UpdateFrame),
            ("Search Product", SearchFrame)
        ]

        for text, frame_class in buttons:
            btn = tk.Button(left_frame, text=text, width=15,
                            command=lambda fc=frame_class: self.show_frame(fc))
            btn.pack(pady=5, padx=5, fill=tk.X)

        # Create container frame
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Initialize frames
        self.frames = {}
        for F in (AddFrame, ListFrame, DeleteFrame, UpdateFrame, SearchFrame):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ListFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if hasattr(frame, 'on_show'):
            frame.on_show()

class AddFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        form_frame = tk.Frame(self)
        form_frame.pack(pady=20)

        fields = [
            ("Product ID:", "id_entry"),
            ("Product Name:", "name_entry"),
            ("Quantity:", "qty_entry"),
            ("Price:", "price_entry")
        ]

        self.entries = {}
        for i, (text, name) in enumerate(fields):
            label = tk.Label(form_frame, text=text)
            entry = tk.Entry(form_frame, width=30)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[name] = entry

        submit_btn = tk.Button(form_frame, text="Add Product", command=self.add_product)
        submit_btn.grid(row=4, columnspan=2, pady=10)

    def add_product(self):
        entries = {k: v.get().strip() for k, v in self.entries.items()}
        if any(not v for v in entries.values()):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            qty = int(entries["qty_entry"])
            price = float(entries["price_entry"])
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity or price format!")
            return

        # Check ID uniqueness
        with open('bag_shop_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                if row and row[0] == entries["id_entry"]:
                    messagebox.showerror("Error", "ID already exists!")
                    return

        # Add to CSV
        with open('bag_shop_data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                entries["id_entry"],
                entries["name_entry"],
                qty,
                price
            ])
            messagebox.showinfo("Success", "Product added successfully!")
            for entry in self.entries.values():
                entry.delete(0, tk.END)

class ListFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Qty", "Price", "Total"), show="headings")
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(fill=tk.BOTH, expand=True)

        headings = [
            ("ID", 100),
            ("Name", 200),
            ("Qty", 80),
            ("Price", 100),
            ("Total", 150)
        ]
        for hdr, width in headings:
            self.tree.heading(hdr, text=hdr)
            self.tree.column(hdr, width=width, anchor=tk.CENTER)

    def on_show(self):
        self.refresh_data()

    def refresh_data(self):
        self.tree.delete(*self.tree.get_children())
        with open('bag_shop_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                if row:
                    total = float(row[2]) * float(row[3])
                    self.tree.insert("", tk.END, values=(
                        row[0],
                        row[1],
                        row[2],
                        f"${float(row[3]):.2f}",
                        f"${total:.2f}"
                    ))

class DeleteFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        form_frame = tk.Frame(self)
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Product ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(form_frame, width=30)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        delete_btn = tk.Button(form_frame, text="Delete Product", command=self.delete_product)
        delete_btn.grid(row=1, columnspan=2, pady=10)

    def delete_product(self):
        product_id = self.id_entry.get().strip()
        if not product_id:
            messagebox.showerror("Error", "Please enter Product ID!")
            return

        rows = []
        found = False
        with open('bag_shop_data.csv', 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            rows.append(header)
            for row in reader:
                if row and row[0] == product_id:
                    found = True
                else:
                    if row:  # Skip empty rows
                        rows.append(row)

        if not found:
            messagebox.showerror("Error", "Product ID not found!")
            return

        with open('bag_shop_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        messagebox.showinfo("Success", "Product deleted successfully!")
        self.id_entry.delete(0, tk.END)

class UpdateFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.current_id = None
        
        form_frame = tk.Frame(self)
        form_frame.pack(pady=20)

        self.entries = {}
        fields = [
            ("Product ID:", "id_entry"),
            ("Name:", "name_entry"),
            ("Quantity:", "qty_entry"),
            ("Price:", "price_entry")
        ]

        for i, (text, name) in enumerate(fields):
            label = tk.Label(form_frame, text=text)
            entry = tk.Entry(form_frame, width=30)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[name] = entry

        fetch_btn = tk.Button(form_frame, text="Fetch Product", command=self.fetch_product)
        fetch_btn.grid(row=0, column=2, padx=10)
        
        update_btn = tk.Button(form_frame, text="Update Product", command=self.update_product)
        update_btn.grid(row=4, columnspan=3, pady=10)

    def fetch_product(self):
        product_id = self.entries["id_entry"].get().strip()
        if not product_id:
            messagebox.showerror("Error", "Please enter Product ID!")
            return

        with open('bag_shop_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row and row[0] == product_id:
                    self.current_id = product_id
                    self.entries["name_entry"].delete(0, tk.END)
                    self.entries["name_entry"].insert(0, row[1])
                    self.entries["qty_entry"].delete(0, tk.END)
                    self.entries["qty_entry"].insert(0, row[2])
                    self.entries["price_entry"].delete(0, tk.END)
                    self.entries["price_entry"].insert(0, row[3])
                    return
            
        messagebox.showerror("Error", "Product ID not found!")

    def update_product(self):
        if not self.current_id:
            messagebox.showerror("Error", "Please fetch a product first!")
            return

        entries = {k: v.get().strip() for k, v in self.entries.items()}
        if not all(entries.values()):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            qty = int(entries["qty_entry"])
            price = float(entries["price_entry"])
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity or price format!")
            return

        rows = []
        with open('bag_shop_data.csv', 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            rows.append(header)
            for row in reader:
                if row and row[0] == self.current_id:
                    rows.append([self.current_id, entries["name_entry"], qty, price])
                else:
                    if row:
                        rows.append(row)

        with open('bag_shop_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        messagebox.showinfo("Success", "Product updated successfully!")
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.current_id = None

class SearchFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10)
        
        tk.Label(search_frame, text="Search by name initial:").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        search_btn = tk.Button(search_frame, text="Search", command=self.search)
        search_btn.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Qty", "Price", "Total"), show="headings")
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(fill=tk.BOTH, expand=True)

        headings = [
            ("ID", 100),
            ("Name", 200),
            ("Qty", 80),
            ("Price", 100),
            ("Total", 150)
        ]
        for hdr, width in headings:
            self.tree.heading(hdr, text=hdr)
            self.tree.column(hdr, width=width, anchor=tk.CENTER)

    def search(self):
        initial = self.search_entry.get().strip().upper()
        if not initial:
            messagebox.showerror("Error", "Please enter a search initial!")
            return
        
        self.tree.delete(*self.tree.get_children())
        with open('bag_shop_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row and row[1] and row[1][0].upper() == initial[0]:
                    total = float(row[2]) * float(row[3])
                    self.tree.insert("", tk.END, values=(
                        row[0],
                        row[1],
                        row[2],
                        f"${float(row[3]):.2f}",
                        f"${total:.2f}"
                    ))

if __name__ == "__main__":
    app = BagShopApp()
    app.mainloop()