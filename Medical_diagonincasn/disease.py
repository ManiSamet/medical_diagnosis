import csv

from tkinter import *
from tkinter import ttk

# Define global variables for column names, disease data, and result_text
column_names = []
disease_raw = []
combined = []
result_text = None  # Initialize as None

def analyze_symptoms(selected_symptom):
    global result_text  # Access the global result_text variable

    selected_diseases = [disease for disease in combined if selected_symptom in disease]

    # Instead of printing, you can display the results in the GUI
    result_text.delete(1.0, tk.END)  # Clear previous results
    for i in selected_diseases:
        result_text.insert(tk.END, f"{i}\n")

def main():

    # Read and preprocess the CSV data
    with open("/Users/manisamet/Downloads/main.csv", 'r') as testfile:
        data_row = csv.reader(testfile, delimiter=',')

        for r in data_row:
            for c in r:
                if c == 'frequency' or c == 'label':
                    continue
                column_names.append(c.split("_")[-1])
            break

        for r in data_row:
            r.pop(0)
            disease_raw.append(r)

        for r in disease_raw:
            temp = []
            temp.append(r[-1].split("_")[-1])
            for x in range(len(r)):
                if r[x] == '1':
                    temp.append(column_names[x])

            combined.append(temp)

    # the main window
    root = Tk()
    root.title("Symptom Analyzer")
    root.geometry('500x250')

    # dropdown menu
    drop = ttk.Combobox(root, values=column_names)
    drop.grid(column=1, row=5)
    drop.current()
    drop.pack()

    # result text widget to display the analysis results
   # result_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
   # result_text.pack()

  #  def on_dropdown_select():
  #      selected_symptom = dropdown_var.get()
   #     analyze_symptoms(selected_symptom)

    # "Search" button to see the analysis
    #search_button = ttk.Button(root, text="Search", command=on_dropdown_select)
   # search_button.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
