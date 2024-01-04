import tkinter as tk
from tkinter import ttk

def create_dark_gray_rectangle(parent, row, column, text, multiline_text=None):
    dark_gray_frame = ttk.Frame(parent, style="DarkerGray.TFrame")
    dark_gray_frame.grid(row=row, column=column, padx=5, pady=5, sticky="w")

    label_frame = ttk.Frame(dark_gray_frame, style="DarkerGray.TFrame")
    label_frame.grid(row=0, column=0, padx=(5, 10), pady=5, sticky="w")

    label = ttk.Label(label_frame, text=text, background="dark gray", anchor="w", padding=(5, 5))
    label.grid(row=0, column=0, sticky="w")

    if multiline_text:
        text_widget = tk.Text(dark_gray_frame, wrap=tk.WORD, background="dark gray", height=2, width=30)
        text_widget.insert("1.0", multiline_text)
        text_widget.config(state=tk.DISABLED)
        text_widget.grid(row=1, column=0, padx=(5, 10), pady=5, sticky="w")

    rectangle_shape = ttk.Frame(dark_gray_frame, style="DarkerGray.TFrame", height=5)
    rectangle_shape.grid(row=2, column=0, padx=5, pady=5, sticky="w")

def create_separator(parent, row, column, rowspan):
    separator = ttk.Separator(parent, orient='vertical')
    separator.grid(row=row, column=column, rowspan=rowspan, sticky='ns')

root = tk.Tk()
root.configure(bg="white")
root.title("Vehicle Decisions Made Easy")

style_darker_gray = ttk.Style()
style_darker_gray.configure("DarkerGray.TFrame", background="dark gray")

frm = ttk.Frame(root, padding=10)
frm.grid()

header_label = ttk.Label(frm, text="Vehicle Decisions Made Easy", font=('Helvetica', 16, 'bold'))
header_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="w")

text_column1 = ['Vehicle A Brand', 'Loan Amount A', 'Term Length A', 'Interest Rate A', 'City Efficiency A', 'Hwy Efficiency A', 'Weekly City Miles']
text_column2 = ['Vehicle B Brand', 'Loan B Amount', 'Term Length B', 'Interest Rate B', 'City Efficiency B', 'Hwy Efficiency B', 'Weekly Highway Miles']

for i, text in enumerate(text_column1):
    create_dark_gray_rectangle(frm, i+1, 0, text)

# Create a separator between the columns
create_separator(frm, 1, 1, len(text_column1))

for i, text in enumerate(text_column2):
    create_dark_gray_rectangle(frm, i+1, 2, text)

third_column_headings = ['Monthly Maintenance Cost', 'Monthly Interest Charges', 'Monthly Loan Charges', 'Final Monthly Cost', 'Car To Buy', 'Total Car Cost of Ownership']

monthly_maintenance_multiline_text = "Car A $250\nCar B $350"
monthly_interest_multiline_text = "Car A $150\nCar B $200"  # Multiline text for Monthly Interest Charges
monthly_loan_charges_multiline_text = "Car A $350\nCar B $400"  # Multiline text for Monthly Loan Charges
final_monthly_cost_multiline_text = "Car A $750\nCar B $900"  # Multiline text for Final Monthly Cost

# Adjusted creation of dark gray rectangles in the third column
def create_dark_gray_rectangle(parent, row, column, text, multiline_text=None, is_special_text=False):
    dark_gray_frame = ttk.Frame(parent, style="DarkerGray.TFrame")
    dark_gray_frame.grid(row=row, column=column, padx=5, pady=5, sticky="w")

    label_frame = ttk.Frame(dark_gray_frame, style="DarkerGray.TFrame")
    label_frame.grid(row=0, column=0, padx=(5, 10), pady=5, sticky="w")

    label = ttk.Label(label_frame, text=text, background="dark gray", anchor="w", padding=(5, 5))
    label.grid(row=0, column=0, sticky="w")

    if multiline_text:
        if is_special_text:
            # Use a label for special text
            special_label = ttk.Label(dark_gray_frame, text=multiline_text, background="dark gray", anchor="w")
            special_label.grid(row=1, column=0, padx=(5, 10), pady=5, sticky="w")
        else:
            # Use text widget for multiline text
            text_widget = tk.Text(dark_gray_frame, wrap=tk.WORD, background="dark gray", height=2, width=30)
            text_widget.insert("1.0", multiline_text)
            text_widget.config(state=tk.DISABLED)
            text_widget.grid(row=1, column=0, padx=(5, 10), pady=5, sticky="w")



total_cost_ownership_formula = "Principal + Tax + Interest + (Term x Yearly Ownership Cost)"

# Adjusted creation of dark gray rectangles in the third column
create_dark_gray_rectangle(frm, 1, 3, third_column_headings[0], monthly_maintenance_multiline_text)

for i, text in enumerate(third_column_headings[1:]):
    if text == "Total Car Cost of Ownership":
        create_dark_gray_rectangle(frm, i+2, 3, text, total_cost_ownership_formula, is_special_text=True)
    elif text == "Monthly Interest Charges":
        create_dark_gray_rectangle(frm, i+2, 3, text, monthly_interest_multiline_text)
    elif text == "Monthly Loan Charges":
        create_dark_gray_rectangle(frm, i+2, 3, text, monthly_loan_charges_multiline_text)
    elif text == "Final Monthly Cost":
        create_dark_gray_rectangle(frm, i+2, 3, text, final_monthly_cost_multiline_text)
    else:
        create_dark_gray_rectangle(frm, i+2, 3, text)

root.mainloop()

