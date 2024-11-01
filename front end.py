import tkinter as tk
import dayfinder

def enter_date(year, month):
    
    if month == 2:  
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            maximum_days = 29  
        else:
            maximum_days = 28
    elif month in {1, 3, 5, 7, 8, 10, 12}:  
        maximum_days = 31
    elif month in {4, 6, 9, 11}:  
        maximum_days = 30
    else:
        return "invalid" 
    
    return maximum_days

def calculate_day():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        
        if not (1600 <= year <= 2400):
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "Year must be between 1600 to 2400.")
            return
        if not (1 <= month <= 12):
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "Month must be between 1 to 12.")
            return
        
        maximum_days = enter_date(year, month)
        if maximum_days == "invalid":
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "Invalid month entered.")
            return
        
        date = int(date_entry.get())
        
        if not (1 <= date <= maximum_days):
            output_entry.delete(0, tk.END)
            output_entry.insert(0, f"Date must be between 1 to {maximum_days}.")
            return
        
        result_day = dayfinder.result(year, month, date)
        output_entry.delete(0, tk.END)
        output_entry.insert(0, result_day)        
    except ValueError:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Please enter valid numbers.")

root = tk.Tk()
root.title("DayFinder: Discover Your Day of the Week")
root.geometry("900x600")
root.configure(bg="lightblue")

title_label = tk.Label(root, text="BHAVAN'S  DAY  FINDER  APPLICATION", font=("Times New Roman", 24, "bold"), bg="lightblue")
title_label.place(relx=0.5, rely=0.1, anchor="center")

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

year_label = tk.Label(root, text="Enter Year:",font=("Times New Roman", 16,"bold"),fg="darkblue")
year_label.grid(row=0, column=0, padx=70, pady=(150,20))
year_entry = tk.Entry(root,font=("Times New Roman", 20,"bold"), width=25,fg="darkgreen")
year_entry.grid(row=0, column=1, padx=10, pady=(150,20))

month_label = tk.Label(root, text="Enter Month (1-12):",font=("Times New Roman", 16,"bold"),fg="darkblue")
month_label.grid(row=1, column=0, padx=10, pady=20)
month_entry = tk.Entry(root,font=("Times New Roman", 20,"bold"), width=25,fg="darkgreen")
month_entry.grid(row=1, column=1, padx=10, pady=20)

date_label = tk.Label(root, text="Enter Date:",font=("Times New Roman", 16,"bold"),fg="darkblue")
date_label.grid(row=2, column=0, padx=10, pady=20)
date_entry = tk.Entry(root,font=("Times New Roman", 20,"bold"), width=25,fg="darkgreen")
date_entry.grid(row=2, column=1, padx=10, pady=20)

calculate_button = tk.Button(root, text="Find Day",bg="yellow", command=calculate_day)
calculate_button.grid(row=3, column=0, columnspan=2, pady=50)

output_label = tk.Label(root, text="The day is:",font=("Times New Roman", 16,"bold"),fg="darkblue")
output_label.grid(row=4, column=0, padx=30, pady=20)
output_entry = tk.Entry(root, font=("Times New Roman", 20,"bold"), width=40,fg="darkgreen")
output_entry.grid(row=4, column=1, padx=10, pady=20)

root.mainloop()
