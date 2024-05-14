# currency converter gui using tkinter. very quick and small project to become familiar
from tkinter import *

# root window
root = Tk()
root.title("Currency Converter")
root.geometry('550x400')
root.resizable(width=False, height=False)

title = Label(root, text="Currency Converter", font=("Arial", 25))
title.pack(side=TOP, pady=20)

usd = Label(root, text="USD $", font=("Arial", 20), fg="green")
usd.place(x=50, y=100)

arrow_down = Label(root, text="\u2193", font=("Arial", 30))
arrow_down.place(x=80, y=160)

target = Label(root, text="Won ₩", font=("Arial", 20), fg="red")
target.place(x=50, y=250)

output = Label(root, font=("Arial", 20), text="")
output.place(x=330, y=250)

# Dropdown menu button with down arrow symbol
dropdown_button = Button(root, text="\u02c5", font=("Arial", 8), width=2, relief=FLAT)
dropdown_button.place(x=175, y=250)


# Function to update the display of target currency
def make_selection(value):
    user_select.set(value)
    target.configure(text=value)
    dropdown_button.configure(relief=FLAT)


# Function to create and display the dropdown menu
def display_menu(event):
    menu = Menu(root, tearoff=0)
    for currency in currencies:
        menu.add_command(label=currency, command=lambda value=currency: make_selection(value))
    menu.tk_popup(event.x_root, event.y_root)


# Bind the custom dropdown button to the function
dropdown_button.bind("<Button-1>", display_menu)  # button 1 is the lmb

# Currency conversion dictionary
currencies = {
    "Won ₩": 1378.09,
    "Yen ¥": 157.90,
    "NTD NT$": 32.60
}

currency_names = list(currencies.keys())

# user selected options
user_select = StringVar(root)
user_select.set(currency_names[0])


# Entry field event function
def enter(event):
    dollars = float(user_input.get())
    # print(dollars)
    target_currency = user_select.get()
    # bprint(target_currency)
    conversion_rate = currencies[target_currency]
    # print(conversion_rate)
    converted_amount = f"{dollars * conversion_rate:.2f}"
    output.configure(text=f"{converted_amount} {target_currency.split(' ')[-1]}")


# Create entry field
user_input = Entry(root, width=10, font=("Arial", 20))
user_input.place(x=330, y=105)
user_input.bind("<Return>", enter)

root.mainloop()
