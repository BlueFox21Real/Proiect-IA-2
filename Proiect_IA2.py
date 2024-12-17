import tkinter as tk
from tkinter import messagebox
import pygame

def explain_python():
   
    pygame.mixer.init()

    def play_sound(file):
        pygame.mixer.Sound(file).play()

    
    root = tk.Tk()
    root.title("python helper")
    root.geometry("640x480")

    
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

    
    def on_learn_button():
        play_sound("sunetselectie.mp3")
        ask_about_learning()

    def on_usage_button():
        play_sound("sunetselectie.mp3")
        ask_about_usage()

    def on_jobs_button():
        play_sound("sunetselectie.mp3")
        ask_about_jobs()

    def on_advantages_button():
        play_sound("sunetselectie.mp3")
        ask_about_advantages()

    def on_exit_button():
        play_sound("sunetiesire.mp3")
        root.destroy()

   
    learn_button = tk.Button(root, text="Cum pot învăța Python?", command=on_learn_button)
    learn_button.pack(pady=5)

    usage_button = tk.Button(root, text="Care sunt utilizările Python?", command=on_usage_button)
    usage_button.pack(pady=5)

    jobs_button = tk.Button(root, text="Ce joburi pot avea dacă știu Python?", command=on_jobs_button)
    jobs_button.pack(pady=5)

    advantages_button = tk.Button(root, text="Avantajele Python față de alte limbaje", command=on_advantages_button)
    advantages_button.pack(pady=5)

   
    exit_button = tk.Button(root, text="Ieșire", command=on_exit_button)
    exit_button.pack(pady=10)

    
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
            "Cunoașterea Python îti poate deschide uși către multe cariere, inclusiv:\n"
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
            "-Productivitate ridicată: Python permite dezvoltarea rapidă a aplicațiilor, reducând timpul necesar pentru prototipuri.\n\n"
            "Toate acestea fac Python un limbaj atractiv pentru toti programatorii de la incepatori pana la avansati."
        )
    )

if __name__ == "__main__":
    explain_python()
