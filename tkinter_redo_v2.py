import tkinter as tk
from tkinter import ttk, messagebox

MONTH_DAYS = 30

class Car:
    def __init__(self, mpg, principle_cost, repair):
        self.mpg = mpg
        self.principle_cost = principle_cost
        self.repair = repair

# Car instances
car_classes = {
    'compact': Car(32, 23839, 887),
    'sedan': Car(31.7, 31758, 887),
    'hatchback': Car(30, 33795, 1064),
    'coupe': Car(24, 51770, 1064),
    'sports': Car(25, 32961, 1200),
    'luxury': Car(21, 42040, 1064),
    'wagon': Car(30, 25678, 1064),
    'large suv': Car(20, 54520, 1064),
    'pickup': Car(22, 37895, 1200)
}

def calculate_fuel_cost(daily_distance, mpg, gas_cost=5.55):
    return (daily_distance * MONTH_DAYS) / mpg * gas_cost

def calculate_loan_cost(loan_amount, loan_term, interest_rate=0.0663):
    monthly_interest_rate = interest_rate / 12
    monthly_payment = (monthly_interest_rate * loan_amount) / (1 - (1 + monthly_interest_rate) ** -loan_term)
    return monthly_payment

def handle_calculate():
    try:
        selected_car_a = car_classes[car_selection_a.get()]
        selected_car_b = car_classes[car_selection_b.get()]
        daily_distance_a = float(entry_daily_distance_a.get())
        daily_distance_b = float(entry_daily_distance_b.get())
        down_payment_percentage_a = float(entry_down_payment_a.get()) / 100
        down_payment_percentage_b = float(entry_down_payment_b.get()) / 100
        loan_term_a = int(entry_loan_term_a.get())
        loan_term_b = int(entry_loan_term_b.get())

        adjusted_principle_cost_a = selected_car_a.principle_cost - (selected_car_a.principle_cost * down_payment_percentage_a)
        adjusted_principle_cost_b = selected_car_b.principle_cost - (selected_car_b.principle_cost * down_payment_percentage_b)

        monthly_payment_a = calculate_loan_cost(adjusted_principle_cost_a, loan_term_a)
        monthly_payment_b = calculate_loan_cost(adjusted_principle_cost_b, loan_term_b)

        fuel_cost_a = calculate_fuel_cost(daily_distance_a, selected_car_a.mpg)
        fuel_cost_b = calculate_fuel_cost(daily_distance_b, selected_car_b.mpg)

        entry_fuel_cost_a.delete(0, tk.END)
        entry_fuel_cost_a.insert(0, f"${fuel_cost_a:.2f}")
        entry_monthly_payment_a.delete(0, tk.END)
        entry_monthly_payment_a.insert(0, f"${monthly_payment_a:.2f}")

        entry_fuel_cost_b.delete(0, tk.END)
        entry_fuel_cost_b.insert(0, f"${fuel_cost_b:.2f}")
        entry_monthly_payment_b.delete(0, tk.END)
        entry_monthly_payment_b.insert(0, f"${monthly_payment_b:.2f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Tkinter GUI setup
root = tk.Tk()
root.configure(bg="#f0f0f0")  # Light gray background
root.title("Vehicle Decisions Made Easy")

# Set window size and center it
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Main frame for centered layout
center_frame = ttk.Frame(root, padding=20, style='My.TFrame')
center_frame.place(relx=0.5, rely=0.5, anchor='center')

style = ttk.Style()
style.configure('My.TFrame', background='#f0f0f0')

header_label = ttk.Label(center_frame, text="Vehicle Decisions Made Easy", font=('Helvetica', 23, 'bold'), background="#f0f0f0")
header_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="w")

# Dropdown menus for car selection
car_selection_a = ttk.Combobox(center_frame, values=list(car_classes.keys()), width=30)
car_selection_a.grid(row=1, column=0, pady=(5, 0))
car_selection_a.set("Select Car A")
car_selection_b = ttk.Combobox(center_frame, values=list(car_classes.keys()), width=30)
car_selection_b.grid(row=1, column=1, pady=(5, 0))
car_selection_b.set("Select Car B")

# Entry widgets and labels for Car A
label_daily_distance_a = ttk.Label(center_frame, text="Daily Distance (in miles)", background="#f0f0f0")
label_daily_distance_a.grid(row=2, column=0, sticky="w")
entry_daily_distance_a = ttk.Entry(center_frame, width=30)
entry_daily_distance_a.grid(row=3, column=0)

label_down_payment_a = ttk.Label(center_frame, text="Down Payment (%)", background="#f0f0f0")
label_down_payment_a.grid(row=4, column=0, sticky="w")
entry_down_payment_a = ttk.Entry(center_frame, width=30)
entry_down_payment_a.grid(row=5, column=0)

label_loan_term_a = ttk.Label(center_frame, text="Loan Term (months)", background="#f0f0f0")
label_loan_term_a.grid(row=6, column=0, sticky="w")
entry_loan_term_a = ttk.Entry(center_frame, width=30)
entry_loan_term_a.grid(row=7, column=0)

# Calculate button
btn_calculate = ttk.Button(center_frame, text="Calculate", command=handle_calculate)
btn_calculate.grid(row=8, column=0, columnspan=2, pady=10)

# Entry widgets and labels for Monthly Costs for Car A
label_fuel_cost_a = ttk.Label(center_frame, text="Monthly Fuel Principle Cost", background="#f0f0f0")
label_fuel_cost_a.grid(row=9, column=0, sticky="w")
entry_fuel_cost_a = ttk.Entry(center_frame, width=30)
entry_fuel_cost_a.grid(row=10, column=0)

label_monthly_payment_a = ttk.Label(center_frame, text="Monthly Loan Payment", background="#f0f0f0")
label_monthly_payment_a.grid(row=11, column=0, sticky="w")
entry_monthly_payment_a = ttk.Entry(center_frame, width=30)
entry_monthly_payment_a.grid(row=12, column=0)

# Entry widgets and labels for Car B
label_daily_distance_b = ttk.Label(center_frame, text="Daily Distance (in miles)", background="#f0f0f0")
label_daily_distance_b.grid(row=2, column=1, sticky="w")
entry_daily_distance_b = ttk.Entry(center_frame, width=30)
entry_daily_distance_b.grid(row=3, column=1)

label_down_payment_b = ttk.Label(center_frame, text="Down Payment (%)", background="#f0f0f0")
label_down_payment_b.grid(row=4, column=1, sticky="w")
entry_down_payment_b = ttk.Entry(center_frame, width=30)
entry_down_payment_b.grid(row=5, column=1)

label_loan_term_b = ttk.Label(center_frame, text="Loan Term (months)", background="#f0f0f0")
label_loan_term_b.grid(row=6, column=1, sticky="w")
entry_loan_term_b = ttk.Entry(center_frame, width=30)
entry_loan_term_b.grid(row=7, column=1)

# Entry widgets and labels for Monthly Costs for Car B
label_fuel_cost_b = ttk.Label(center_frame, text="Monthly Fuel Principle Cost", background="#f0f0f0")
label_fuel_cost_b.grid(row=9, column=1, sticky="w")
entry_fuel_cost_b = ttk.Entry(center_frame, width=30)
entry_fuel_cost_b.grid(row=10, column=1)

label_monthly_payment_b = ttk.Label(center_frame, text="Monthly Loan Payment", background="#f0f0f0")
label_monthly_payment_b.grid(row=11, column=1, sticky="w")
entry_monthly_payment_b = ttk.Entry(center_frame, width=30)
entry_monthly_payment_b.grid(row=12, column=1)

# Equation label under Car A and B Monthly Loan Payment 
label_loan_formula_b = ttk.Label(center_frame, text="Monthly payment = (loan amount) × (interest rate / 12) / \n(1 − (1 + (interest rate / 12)) ^ (-loan term))", justify=tk.CENTER, background="#f0f0f0", font=('Helvetica', 20, 'bold'))
label_loan_formula_b.grid(row=13, column=0, columnspan=2, sticky="s")

root.mainloop()
