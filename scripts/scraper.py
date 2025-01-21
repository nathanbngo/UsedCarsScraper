import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from utils import setup_driver, scrape_car_data, save_to_excel, visualize_data

# Function to scrape data
def start_scraping():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL!")
        return

    try:
        driver = setup_driver()
        car_data = scrape_car_data(driver, url)
        driver.quit()

        # Save to Excel
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                                 filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            save_to_excel(car_data, file_path)
            messagebox.showinfo("Success", f"Data saved to {file_path}")
            load_data(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to load and display data
def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        for row in table.get_children():
            table.delete(row)
        for _, row in df.iterrows():
            table.insert("", tk.END, values=row.to_list())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data: {e}")

# Function to visualize data
def visualize():
    try:
        visualize_data('data/used_cars.xlsx')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to visualize data: {e}")

# Main UI
root = tk.Tk()
root.title("Used Cars Data Scraper")
root.geometry("800x600")

tk.Label(root, text="Enter URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

scrape_button = tk.Button(button_frame, text="Scrape Data", command=start_scraping)
scrape_button.grid(row=0, column=0, padx=10)

visualize_button = tk.Button(button_frame, text="Visualize Data", command=visualize)
visualize_button.grid(row=0, column=1, padx=10)

table_frame = tk.Frame(root)
table_frame.pack(pady=20)

columns = ("Brand", "Year", "Price", "Mileage")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor=tk.CENTER)
table.pack()

root.mainloop()
