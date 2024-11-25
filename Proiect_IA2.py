import tkinter as tk
from tkinter import messagebox

def explain_python():
    # Fereastră principală
    root = tk.Tk()
    root.title("python helper")
    root.geometry("640x480")
    
    # Eticheta cu introducerea
    intro_label = tk.Label(root, text=(
        "Bună ziua! Astăzi o să vă arăt ce este Python și cu ce se ocupă.\n\n"
        "Python este un limbaj de programare interpretat, open-source, de nivel înalt, "
        "folosit pentru dezvoltarea rapidă de programe si scripturi.\n\n"
        "Câteva caracteristici principale ale Python:\n"
        "1. Sintaxă ușor de înțeles.\n"
        "2. O comunitate mare de utilizatori și multe biblioteci gata de utilizare.\n"
        "3. Poate fi folosit pentru diverse aplicații: web, data science, automatizări, "
        "inteligență artificială și multe altele."
    ), wraplength=480, justify="left")
    intro_label.pack(pady=10)

    # Butoane pentru diferite secțiuni
    learn_button = tk.Button(root, text="Cum pot învăța Python?", command=ask_about_learning)
    learn_button.pack(pady=5)

    usage_button = tk.Button(root, text="Care sunt utilizările Python?", command=ask_about_usage)
    usage_button.pack(pady=5)

    jobs_button = tk.Button(root, text="Ce joburi pot avea dacă știu Python?", command=ask_about_jobs)
    jobs_button.pack(pady=5)

    advantages_button = tk.Button(root, text="Avantajele Python față de alte limbaje", command=ask_about_advantages)
    advantages_button.pack(pady=5)

    # Buton pentru ieșire
    exit_button = tk.Button(root, text="Ieșire", command=root.destroy)
    exit_button.pack(pady=10)

    # Rulăm fereastra principală
    root.mainloop()


def ask_about_learning():
    messagebox.showinfo(
        "Cum să înveți Python",
        (
            "Poți învăța Python pe site-uri precum Python.org, cursuri de specialitate sau prin tutoriale online.\n"
            "Ca sa înveti python mai usor incepe prin a scrie câteva programe simple!"
        )
    )


def ask_about_usage():
    messagebox.showinfo(
        "Utilizările Python",
        (
            "Python are o gamă largă de utilizări, inclusiv:\n"
            "- Dezvoltare web (ex. Flask, Django)\n"
            "- Analiză de date și machine learning (ex. Pandas, NumPy, TensorFlow)\n"
            "- Automatizare și scripting (ex. scriere de scripturi automate)\n"
            "- Crearea de jocuri (ex. Pygame)"
        )
    )


def ask_about_jobs():
    messagebox.showinfo(
        "Joburi pentru cunoscătorii de Python",
        (
            "Cunoașterea Python îți poate deschide uși către multe cariere, inclusiv:\n"
            "- Dezvoltator software/web\n"
            "- Inginer de machine learning\n"
            "- Automatizare \n"
            "- Data Scientist\n"
            "- Tester automatizat (QA Engineer)\n"
            "- Cercetător în domeniul AI/ML\n\n"
            "Python este folosit de companii de top precum Google, Facebook, Amazon și multe altele."
        )
    )


def ask_about_advantages():
    messagebox.showinfo(
        "Avantajele Python față de alte limbaje",
        (
            "Uitati câteva avantaje ale Python față de alte limbaje de programare:\n\n"
            "-Ușor de învățat: Sintaxa sa este mai simplă și mai intuitivă decât limbaje precum C++ sau Java.\n"
            "-Comunitate mare și biblioteci extinse**: Există resurse aproape pentru orice nevoie, ceea ce nu e întotdeauna cazul cu alte limbaje.\n"
            "-Versatilitate: Python este folosit în multiple domenii, de la web development la AI și data science.\n"
            "-Portabilitate: Codul Python poate rula pe diferite platforme fără modificări majore.\n"
            -"Productivitate ridicată: Python permite dezvoltarea rapidă a aplicațiilor, reducând timpul necesar pentru prototipuri.\n\n"
            "Toate acestea fac Python un limbaj atractiv pentru toti programatorii de la incepatori pana la avansati."
        )
    )


if __name__ == "__main__":
    explain_python()
    
