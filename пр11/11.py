import json
import requests
username = "rust-lang"
url = f"https://api.github.com/users/{username}"
def F():
    f_json = requests.get(url).json()
    v = name.get()
    inf = dict((key, data[key]) for key in ['company', 'created_at', 'email', 'id', 'name', 'url'] if key in data)


    if v == 'rust-lang':
        with open('C:\\Prog file\\Вывод.json', 'w') as file:
            json.dump(inf, file)


    else:
        print('Данное имя не задано')



import tkinter as tk
window = tk.Tk()
window.geometry('400x300')
window.title("json")
name = tk.Entry(window)
name.grid(padx=120, pady=15)
btn = tk.Button(window, text="click", command=F)
btn.grid(padx=90, pady=15)
window.mainloop()
F()
