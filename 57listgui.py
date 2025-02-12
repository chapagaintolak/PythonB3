import tkinter as tk

def add_item():
    item_name = entry.get().strip()
    if item_name:
        var = tk.IntVar()
        shopping_cart.append({'name': item_name, 'var': var})
        cb = tk.Checkbutton(scrollable_frame, text=item_name, variable=var, anchor='w')
        cb.pack(fill='x', padx=5, pady=2)
        entry.delete(0, tk.END)

def show_items():
    items_text = "All Items:\n"
    for item in shopping_cart:
        status = "Checked" if item['var'].get() == 1 else "Unchecked"
        items_text += f"{item['name']} - {status}\n"
    display_label.config(text=items_text)

shopping_cart = []

root = tk.Tk()
root.title("Shopping Cart")
root.geometry("400x500")

# Top section for adding items
top_frame = tk.Frame(root)
top_frame.pack(padx=10, pady=10, fill='x')

entry = tk.Entry(top_frame)
entry.pack(side='left', expand=True, fill='x', padx=5)

add_button = tk.Button(top_frame, text="Add Item", command=add_item)
add_button.pack(side='left')

# Scrollable area for checkboxes
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

# Bottom section for displaying results
bottom_frame = tk.Frame(root)
bottom_frame.pack(padx=10, pady=10, fill='x')

show_button = tk.Button(bottom_frame, text="Show All Items", command=show_items)
show_button.pack()

display_label = tk.Label(root, text="", justify='left', wraplength=380)
display_label.pack(padx=10, pady=10, fill='both')

# Handle Enter key for adding items
entry.bind('<Return>', lambda event: add_item())

root.mainloop()