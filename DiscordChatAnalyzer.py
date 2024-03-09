import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import random

def upload_and_analyze():
    file_path = filedialog.askopenfilename()
    if file_path:
        df = pd.read_csv(file_path)
        message_counts = df.groupby('Author')['Content'].count().reset_index(name='Messages')
        ranked_authors = message_counts.sort_values(by='Messages', ascending=False).reset_index(drop=True)
        
        for i in tree.get_children():
            tree.delete(i)
        
        for index, row in ranked_authors.iterrows():
            tree.insert("", tk.END, values=(index + 1, row['Author'], row['Messages']))

def draw_stars(canvas, number_of_stars):
    for _ in range(number_of_stars):
        x1 = random.randint(0, 200)
        y1 = random.randint(0, 100)
        size = random.randint(1, 3)
        canvas.create_oval(x1, y1, x1 + size, y1 + size, fill="white")

root = tk.Tk()
root.title("Discord Chat Analyzer")
root.geometry("800x600")

tab_control = ttk.Notebook(root)

main_tab = ttk.Frame(tab_control)
tab_control.add(main_tab, text='Main')

ranking_tab = ttk.Frame(tab_control)
tab_control.add(ranking_tab, text='User Ranking')

main_label = tk.Label(main_tab, text="Hello, here you can try magical data analysis!", padx=20, pady=20)
main_label.pack()

canvas = tk.Canvas(main_tab, width=200, height=100, bg="black")
canvas.pack()
draw_stars(canvas, 50)  

upload_button = tk.Button(ranking_tab, text="Upload CSV File", command=upload_and_analyze)
upload_button.pack(pady=10)

columns = ('#1', '#2', '#3')
tree = ttk.Treeview(ranking_tab, columns=columns, show='headings')
tree.heading('#1', text='Rank')
tree.heading('#2', text='User')
tree.heading('#3', text='Messages')
tree.column('#1', anchor=tk.CENTER, width=100)
tree.column('#2', anchor=tk.W, width=250)
tree.column('#3', anchor=tk.CENTER, width=100)
tree.pack(pady=10, fill=tk.BOTH, expand=True)

tab_control.pack(expand=1, fill="both")

# Run the UI
root.mainloop()
