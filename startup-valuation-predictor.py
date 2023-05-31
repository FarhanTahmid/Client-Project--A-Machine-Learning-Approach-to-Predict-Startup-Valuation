import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter.font import Font


filename = 'E:\cse 498r\svm.pkl'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Create the main window
window = tk.Tk()
window.title("Startup Valuation Predictor")
window.geometry("800x400")
window.configure(background='sky blue')

# Increase font size
font = Font(size=12)

# Create a frame to center the input fields
center_frame = tk.Frame(window, bg='sky blue')
center_frame.pack(expand=True)



# Create input fields
entry_fields = []

duration_label = tk.Label(center_frame, text=f"Enter Duration:", font=font, bg='sky blue')
duration_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
duration_entry = tk.Entry(center_frame, width=10, font=font)
duration_entry.grid(row=0, column=1, padx=5, pady=5)
entry_fields.append(duration_entry)

operational_cost_label = tk.Label(center_frame, text=f"Operational Cost:", font=font, bg='sky blue')
operational_cost_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
operational_cost_entry = tk.Entry(center_frame, width=10, font=font)
operational_cost_entry.grid(row=1, column=1, padx=5, pady=5)
entry_fields.append(operational_cost_entry)

total_fund_label = tk.Label(center_frame, text=f"Total Fund:", font=font, bg='sky blue')
total_fund_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
total_fund_entry = tk.Entry(center_frame, width=10, font=font)
total_fund_entry.grid(row=2, column=1, padx=5, pady=5)
entry_fields.append(total_fund_entry)

revenue_label = tk.Label(center_frame, text=f"Revenue:", font=font, bg='sky blue')
revenue_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
revenue_entry = tk.Entry(center_frame, width=10, font=font)
revenue_entry.grid(row=3, column=1, padx=5, pady=5)
entry_fields.append(revenue_entry)

profit_label = tk.Label(center_frame, text=f"Profit:", font=font, bg='sky blue')
profit_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
profit_entry = tk.Entry(center_frame, width=10, font=font)
profit_entry.grid(row=4, column=1, padx=5, pady=5)
entry_fields.append(profit_entry)

nfm_label = tk.Label(center_frame, text=f"Net Profit Margin:", font=font, bg='sky blue')
nfm_label.grid(row=5, column=0, padx=5, pady=5, sticky='e')
nfm_entry = tk.Entry(center_frame, width=10, font=font)
nfm_entry.grid(row=5, column=1, padx=5, pady=5)
entry_fields.append(nfm_entry)

user_base_label = tk.Label(center_frame, text=f"User Base:", font=font, bg='sky blue')
user_base_label.grid(row=6, column=0, padx=5, pady=5, sticky='e')
user_base_entry = tk.Entry(center_frame, width=10, font=font)
user_base_entry.grid(row=6, column=1, padx=5, pady=5)
entry_fields.append(user_base_entry)

dau_label = tk.Label(center_frame, text=f"Daily Active User:", font=font, bg='sky blue')
dau_label.grid(row=7, column=0, padx=5, pady=5, sticky='e')
dau_entry = tk.Entry(center_frame, width=10, font=font)
dau_entry.grid(row=7, column=1, padx=5, pady=5)
entry_fields.append(dau_entry)





title_label = tk.Label(window, text="Generate Predictions for valuation of your Startup ", font=font, bg='sky blue')
title_label.pack(pady=5)

# Create a button to generate the graph
generate_button = tk.Button(window, text="Generate Graph", font=font)
generate_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()