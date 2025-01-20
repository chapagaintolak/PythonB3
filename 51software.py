import tkinter as tk
from turtle import onclick

def calculate():
    total_amount  = float(textbox1.get())
    total_person = float(textbox2.get())
    
    amount_per_person = total_amount / total_person
    result_label.config(text=f"Each person need to pay Rs. {amount_per_person:.2f}")
    

root = tk.Tk()
root.title("Bishworaj Bill Split Software")
# Set height and width
root.geometry("500x500")

label1 = tk.Label(root, text="Enter Total Amount: ")
label1.pack()

textbox1 = tk.Entry(root)
textbox1.pack(pady=5)


label2 = tk.Label(root, text="Enter Total People: ")
label2.pack()

textbox2 = tk.Entry(root)
textbox2.pack(pady=5)

button1 = tk.Button(root, text="Calculate",command=calculate)
button1.pack(pady=5)


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()