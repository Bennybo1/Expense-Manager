import os
import datetime
import time
import customtkinter as ctk
from tkinter import messagebox
import sys
print("Transaction----Management----Program----Output")

#Option functions

def quit():
	sys.exit()



def budget_edit():
	global budget
	clear_options()
	Heading.configure(text='Edit Monthly Budget', padx=37,pady=30)
	Budget_Label.grid(row=1, column=0)
	new_budget_entry.grid(row=2, column=0)
	budget_enter_button.grid(row=3, column=0, pady=20)
	cancel_button.grid(row=4, column=0, pady=5)
	

def new_budget_entered():
	global budget
	global new_budget
	with open(os.path.join('Expense Manager Database', 'File_Budget.txt'), 'r') as file:
		budget = file.read().strip()
	new_budget = new_budget_entry.get()
	if new_budget == '':
		messagebox.showwarning(title='No input', message='You must enter a budget to update your current one')
	else:
		try:
			float(new_budget)
			if float(new_budget) <= 0:
				messagebox.showwarning(title='Budget Error', message='Your new budget cannot be 0 or less than 0')
			else:
				budget = new_budget
				with open(os.path.join('Expense Manager Database', 'File_Budget.txt'), 'w') as file:
					file.write(budget)
				messagebox.showinfo(title='Budget Set', message='Budget was successfully updated!')
				print("New budget was set!")
				main_window()

		except ValueError:
			messagebox.showwarning(title='Input Error', message='You must enter a valid number')


def new_transaction():
	clear_options()
	cancel_button.grid(row=6, column=0, pady=5)
	transaction_price_entry.grid(row=2, column=0)
	Price_Label.grid(row=1, column=0)
	Catagory_Label.grid(row=3, column=0,)
	transaction_catagory_entry.grid(row=4, column=0)
	transaction_enter_button.grid(row=5, column=0, pady=20)
	Heading.configure(text='New Transaction', padx=90, pady=30)

	

def view_transactions():
	global budget
	global fixed_total
	global transactions_text
	#Preparing window
	clear_options()
	Heading.configure(text='View Transactions')
	text_frame.grid(row=1, column=0, padx=15)
	close_button.grid(row=2, column=0, pady=10)
	window.geometry('650x450')
	#Getting the transactions and total
	with open(os.path.join('Expense Manager Database','Transactions.txt'), 'r') as file:
		ttext = file.read()
	transactions_text.configure(text=ttext)
	add_total()
	total_text.configure(text=f'\n***The total amount spent is ${fixed_total}***\n\n\n')
	
		

	#reading the budget and calculating it
	with open(os.path.join('Expense Manager Database','File_Budget.txt'), 'r') as file:
		budget = file.read().strip()
		fixed_budget = "{:.2f}".format(float(budget))
		daily_budget = float(fixed_budget) / 30
		fixed_daily_budget = "{:.2f}".format(float(daily_budget))
		weekly_budget = float(fixed_daily_budget) * 7
		fixed_weekly_budget = "{:.2f}".format(float(weekly_budget))
	budget_text.configure(text=f'~~~To stay within your budget of ${fixed_budget} you\nwould need to spend approximately ${fixed_weekly_budget} a week\nor ${fixed_daily_budget} a day~~~')
		
		
		
		

	

def transaction_entered():
	today = datetime.date.today()
	amount = transaction_price_entry.get()
	if amount == '':
		messagebox.showwarning(title='No input', message='You must enter the cost to add a transaction')
	else:
		try:
			number = float(amount)
			if number > 0:
				fixed_number = "{:.2f}".format(number)
				catagory = transaction_catagory_entry.get()
				catagory_length = len(catagory)
				if catagory_length > 15:
					messagebox.showwarning(title='Catagory Error', message='Your catagory cannot be longer than 15 characters')
				else:
					if catagory == '':
						if messagebox.askokcancel(title='No catagory entered', message='Are you sure you do not want a catagory for your transaction?'):
							catagory='Undefined'
							with open(os.path.join('Expense Manager Database','Transactions.txt'), 'a') as file:
								file.write(f'--Transaction Date: {today}, Amount Spent: ${fixed_number} Catagory: {catagory}--\n\n')
							with open(os.path.join('Expense Manager Database','File_Count.txt'), 'a') as file:
								file.write(f"{amount}\n")
							messagebox.showinfo(title='Transaction State', message='Transaction was successfully added!')
							main_window()
							
							
						else:
							pass
					else:
						catagory = transaction_catagory_entry.get()
						with open(os.path.join('Expense Manager Database','Transactions.txt'), 'a') as file:
							file.write(f'--Transaction Date: {today}, Amount Spent: ${fixed_number} Catagory: {catagory}--\n\n')
						with open(os.path.join('Expense Manager Database','File_Count.txt'), 'a') as file:
							file.write(f"{amount}\n")
						messagebox.showinfo(title='Transaction State', message='Transaction was successfully added!')
						main_window()
						

			else:
				messagebox.showwarning(title='Value Error', message='Transactions must be greater than 0')

		except ValueError:
			messagebox.showwarning(title='Input Error', message='Input was not a valid number')


def add_total():
	global fixed_total
	total = 0
	try:
		with open(os.path.join('Expense Manager Database', 'File_Count.txt'), 'r') as file:
			for line in file:
				total += round(float(line.strip()), 2)
		fixed_total = "{:.2f}".format(float(total))
	except FileNotFoundError:
		print("File not found.")		
	except ValueError:
		print("Invalid data in file.")

def clear_options():
	new_transaction_button.grid_forget()
	view_transactions_button.grid_forget()
	budget_edit_button.grid_forget()
	quit_button.grid_forget()
	settings_button.grid_forget()

def clear_window():
	for widget in window.grid_slaves():
		widget.grid_forget()
	


def main_window():
	cancel_button.configure(text='Close Transactions')
	clear_window()
	window.geometry("350x450")

	Heading.configure(text='Transaction Manager', padx=15, pady=0)

	Heading.grid(row=0, column=0)
	new_transaction_button.grid(row=1, column=0, pady=20, padx=0)
	view_transactions_button.grid(row=2, column=0, pady=20, padx=0)
	budget_edit_button.grid(row=3, column=0, pady=20, padx=0)
	quit_button.grid(row=4, column=0, pady=20, padx=0)
	settings_button.grid(row=5, column=0, pady=20)

def login():
	global name
	global budget
	clear_options()
	clear_window()
	Heading.grid(row=0, column=0, padx=65, pady=10)
	Heading.configure(text='Fill in the info')
	Name_Label.grid(row=1, column=0)
	name_entry.grid(row=2, column=0)
	Budget_Label.grid(row=3, column=0)
	budget_entry.grid(row=4, column=0)
	submit_button.grid(row=5, column=0, pady=30)


def check_info():
	global name
	global budget
	name = name_entry.get()
	budget = budget_entry.get()
	if name == '':
		messagebox.showwarning(title='Name Error', message='You must enter a name')
	if budget == '':
		messagebox.showwarning(title='Budget Error', message='You must enter a monthly budget')
		
	else:
		try:
			float(budget)
			if float(budget) <= 0:
				messagebox.showwarning(title="Budget Error", message='Budget cannot be 0 or less than 0')
			else:
				os.makedirs('Expense Manager Database')
				with open(os.path.join('Expense Manager Database', 'Transactions.txt'), 'w') as file:
					file.write(f"{name}'s Transactions list:\n\n")
				with open(os.path.join('Expense Manager Database', 'File_Count.txt'), 'w') as file:
					file.write("")
				with open(os.path.join('Expense Manager Database', 'File_Budget.txt'), 'w') as file:
					file.write(budget)
				with open(os.path.join('Expense Manager Database', 'Name.txt'), 'w') as file:
					file.write(name)
				
				print('4 paths were created')
				main_window()
		except ValueError:
			messagebox.showwarning(title='Budget Error', message='Budget must be a valid number')



def settings():
	clear_options()
	Name_Label.configure(text='Update your name\nhere', pady=25)
	Heading.configure(text='Settings')
	Name_Label.grid(row=1, column=0, padx=100)
	name_entry.grid(row=2, column=0)
	new_name_enter.grid(row=3, column=0, pady=10)
	dark_mode.grid(row=4, column=0, pady=25)
	light_mode.grid(row=5, column=0, pady=25)
	close_button.configure(text='Close Settings')
	close_button.grid(row=6, column=0, pady=20)



def new_name():
	new_name = name_entry.get()
	with open(os.path.join('Expense Manager Database', 'Name.txt'), 'r') as file:
		name = file.read().strip()

	if new_name == '':
		messagebox.showwarning(title='New Name Error', message='You must enter a name to change your current name')
	else:
		name = new_name
		new_name_style = f"{name}'s Transactions list:\n\n"
		print(name)
		with open(os.path.join('Expense Manager Database', 'Name.txt'), 'w') as file:
			file.write(name)
		with open(os.path.join('Expense Manager Database', 'Transactions.txt'), 'r') as file:
			content = file.readlines()
		content.insert(0, new_name_style)
		with open(os.path.join('Expense Manager Database', 'Transactions.txt'), 'w') as file:
			file.writelines(new_name_style)
# Insert the new line at the start
			
			messagebox.showinfo(title='New Name', message='Name Update was Successfully')


def dark_mode():
	ctk.set_appearance_mode('dark')
def light_mode():
	ctk.set_appearance_mode('light')

window = ctk.CTk()
window.title("Transaction Manager")
window.geometry("350x450")
window.resizable(False,False)
ctk.set_appearance_mode('system')


#CTk Widgets
#Labels

Heading = ctk.CTkLabel(window, text="Transaction Manager", font=('Comfortaa', 35), padx=15)
Price_Label = ctk.CTkLabel(window, text='Price Of Transaction', font=('Times New Roman', 20))
Catagory_Label = ctk.CTkLabel(window, text='Catagory Of Transaction', font=('Times New Roman', 20))
Budget_Label = ctk.CTkLabel(window, text='Enter your monthly budget', font=('Times New Roman', 20))
Name_Label = ctk.CTkLabel(window, text='Enter your name', font=('Times New Roman', 20))


#Buttons

new_transaction_button = ctk.CTkButton(window, text='New Transaction', font=('Comfortaa', 25), height=40, width=150, fg_color='#1b6f89',hover_color='#00526c', command=new_transaction)

view_transactions_button = ctk.CTkButton(window, text='View Transactions', font=('Comfortaa', 25), height=40, width=150, hover_color='#440352', fg_color='#6c0783', command=view_transactions)

budget_edit_button = ctk.CTkButton(window, text='Edit Monthly Budget', font=('Comfortaa', 25), height=40, width=150, fg_color='#9e2c04', hover_color='#661b01', command=budget_edit)

quit_button = ctk.CTkButton(window, text='Quit Program', font=('Comfortaa', 25), height=40, width=150, fg_color='#424242', hover_color='#2c2c2c', command=quit)

settings_button = ctk.CTkButton(window, text='⚙️', height=30, width=30, font=('Comfortaa', 32), command=settings)

transaction_enter_button = ctk.CTkButton(window, text='Enter Transaction', height=30, width=150, font=('Comfortaa', 20), command=transaction_entered)

budget_enter_button = ctk.CTkButton(window, text='Enter New Budget', height=30, width=150, font=('Comfortaa', 20), command=new_budget_entered)

cancel_button = ctk.CTkButton(window, text='Cancel', font=('Comfortaa', 20), height=30, width=75, fg_color='#c40000', hover_color='#830000', command=main_window)

submit_button = ctk.CTkButton(window, text='        Enter        ', height=30, width=106, font=('Comfortaa', 20), command=check_info)

close_button = ctk.CTkButton(window, text='Close Transactions', font=('Comfortaa', 20), height=30, width=105, command=main_window)

dark_mode = ctk.CTkButton(window, text='Dark Mode', font=('Comfortaa', 20), height=30, width=75, command=dark_mode, fg_color='#1b1b1b', hover_color='#000000')

light_mode = ctk.CTkButton(window, text='Light Mode', font=('Comfortaa', 20), height=30, width=75, command=light_mode, fg_color='#8aacb6', hover_color='#4f6f79')

new_name_enter = ctk.CTkButton(window, text='Enter New Name', font=('Comfortaa', 20), height=30, width=75, command=new_name)
#Entrys

transaction_price_entry = ctk.CTkEntry(window, font=('Comfortaa', 15), height=30, width=90)
new_budget_entry = ctk.CTkEntry(window, font=('Comfortaa', 15), height=30, width=90)
transaction_catagory_entry = ctk.CTkEntry(window, font=('Comfortaa', 15), height=30, width=110)


name_entry = ctk.CTkEntry(window, font=('Comfortaa', 15), height=30, width=90)
budget_entry = ctk.CTkEntry(window, font=('Comfortaa', 15), height=30, width=90)

#Scroll frame widgets

text_frame = ctk.CTkScrollableFrame(window, width=600, height=350)
transactions_text = ctk.CTkLabel(text_frame, text='')
transactions_text.pack()
total_text = ctk.CTkLabel(text_frame, text='')
total_text.pack()
budget_text = ctk.CTkLabel(text_frame, text='')
budget_text.pack()


#Checking if the text file exists
if os.path.isdir('Expense Manager Database'):
	print("File paths are there, running program")
	main_window()

else:
	login()
	print("Files path are not all there")
	
window.mainloop()