import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import random
import webbrowser

def upload_and_analyze():
    file_path = filedialog.askopenfilename()
    if file_path:
        df = pd.read_csv(file_path)
        # User Ranking
        message_counts = df.groupby('Author')['Content'].count().reset_index(name='Messages')
        ranked_authors = message_counts.sort_values(by='Messages', ascending=False).reset_index(drop=True)
        
        for i in user_tree.get_children():
            user_tree.delete(i)
        
        for index, row in ranked_authors.iterrows():
            user_tree.insert("", tk.END, values=(index + 1, row['Author'], row['Messages']))
        
        # Date Ranking
        date_counts = df.groupby('Date')['Content'].count().reset_index(name='Messages')
        ranked_dates = date_counts.sort_values(by='Messages', ascending=False).reset_index(drop=True)
        
        for i in date_tree.get_children():
            date_tree.delete(i)
        
        for index, row in ranked_dates.iterrows():
            date_tree.insert("", tk.END, values=(index + 1, row['Date'], row['Messages']))

def draw_stars(canvas, number_of_stars):
    for _ in range(number_of_stars):
        x1 = random.randint(0, 200)
        y1 = random.randint(0, 100)
        size = random.randint(1, 3)
        canvas.create_oval(x1, y1, x1 + size, y1 + size, fill="white")

def on_tab_selected(event):
    selected_tab = event.widget.tab(event.widget.select(), "text")
    if selected_tab == "Help":
        webbrowser.open('https://github.com/diligencefrozen')

root = tk.Tk()
root.title("DiscordChatAnalyzer")
root.geometry("800x600")
root.iconbitmap('icofile.ico')

tab_control = ttk.Notebook(root)

main_tab = ttk.Frame(tab_control)
tab_control.add(main_tab, text='Home')

main_label = tk.Label(main_tab, text="Give magical data analysis a try here! Based on users' chat histories, we'll rank them for you!", wraplength=400, justify="center")
main_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")
main_tab.columnconfigure(0, weight=1)

ranking_tab = ttk.Frame(tab_control)
date_ranking_tab = ttk.Frame(tab_control)  
about_tab = ttk.Frame(tab_control)

tab_control.add(main_tab, text='Home')
tab_control.add(ranking_tab, text='User Ranking')
tab_control.add(date_ranking_tab, text='Date Ranking')  
tab_control.add(about_tab, text='Help')

tab_control.bind("<<NotebookTabChanged>>", on_tab_selected)

# User Ranking
user_columns = ('#1', '#2', '#3')
user_tree = ttk.Treeview(ranking_tab, columns=user_columns, show='headings')
user_tree.heading('#1', text='Rank')
user_tree.heading('#2', text='User')
user_tree.heading('#3', text='Messages')
user_tree.column('#1', anchor=tk.CENTER, width=100)
user_tree.column('#2', anchor=tk.W, width=250)
user_tree.column('#3', anchor=tk.CENTER, width=100)
user_tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Date Ranking
date_columns = ('#1', '#2', '#3')
date_tree = ttk.Treeview(date_ranking_tab, columns=date_columns, show='headings')
date_tree.heading('#1', text='Rank')
date_tree.heading('#2', text='Date')
date_tree.heading('#3', text='Messages')
date_tree.column('#1', anchor=tk.CENTER, width=100)
date_tree.column('#2', anchor=tk.W, width=250)
date_tree.column('#3', anchor=tk.CENTER, width=100)
date_tree.pack(pady=10, fill=tk.BOTH, expand=True)

upload_button = tk.Button(ranking_tab, text="Upload CSV File", command=upload_and_analyze)
upload_button.pack(pady=10)

about_label = tk.Label(about_tab, text="For more detailed information, please visit my GitHub. Thank you sincerely for using my program.", padx=20, pady=20)
about_label.pack()

tab_control.pack(expand=1, fill="both")

tab_control.select(main_tab)

root.mainloop()
