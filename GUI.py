import tkinter as tk
from tkinter import messagebox
from chatbot import selskaper_for_teknologi

def hent_selskaper():
    kategori = e.get()  
    if not kategori:
        messagebox.showwarning("Advarsel", "Vennligst skriv inn en kategori!")
        return

    try:
        selskaper = selskaper_for_teknologi(kategori)
        if not selskaper:
            messagebox.showinfo("Ingen data", f"Ingen selskaper funnet i kategorien {kategori}.")
        else:
            vis_resultat(selskaper)
    except ValueError as ve:
        messagebox.showerror("Feil", str(ve))
    except sqlite3.OperationalError as oe:
        messagebox.showerror("Feil", f"Databasefeil: {oe}")

def vis_resultat(selskaper):
    resultat_vindu = tk.Toplevel(root)
    resultat_vindu.title("Resultater")
    resultat_vindu.geometry("400x300")
    resultat_vindu.configure(bg="darkblue")

    tk.Label(resultat_vindu, text="Selskaper:", bg="darkblue", fg="white").pack(pady=10)
    for selskap in selskaper:
        tk.Label(resultat_vindu, text=selskap, bg="darkblue", fg="white").pack()


root = tk.Tk()
root.geometry("400x300")
root.configure(bg="darkblue")


myLabel = tk.Label(root, text="Hei, velkommen til DIGIN letebot", padx=50, pady=20, bg="darkblue", fg="white")
myLabel.place(relx=0.5, rely=0.1, anchor="center")


e = tk.Entry(root, width=50, borderwidth=5)
e.place(relx=0.5, rely=0.5, anchor="center")


btn = tk.Button(root, text="Søk", command=hent_selskaper)
btn.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()