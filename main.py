# 1. dodanie checkboxa wielkie litery oraz cyfry
import random
import secrets
import string
from importlib.metadata import files
from tkinter import *

from tkinter import filedialog


# sprawdzenie czy pole dlugosc hasla to int
def contains_number(value):
    for character in value:
        if character.isdigit():
            return True
    return False

# zamiana listy na string
def list_to_string(array):
    string = ""
    for a in array:
        string += a
    return string


# generowanie hasła
def new_rand():
    received_pass.delete(0, END)
    i = 0
    password = []

    # sprawdzanie dlugosci wpisanego int
    if length_pass.get() == "":
        length = 0
    elif not contains_number(length_pass.get()):
        length = 0
    else:
        length = int(length_pass.get())

    #sprawdzanie czy hasło zostalo juz wygenerowane
    while length > len(password):
        if not checkChar.get():
            chars = string.ascii_letters + string.digits
        else:
            chars = string.ascii_letters + string.digits + string.punctuation

        char = list(chars)  # lista znakow
        rand = secrets.choice(char) #Generowanie losowego znaku przez moduł "secrets" - najbezpieczniejsza metoda, która wybiera losowy znak
        password += rand  # tworzenie hasla-dodawania losowego znaku

        if length == 1:  # sprawdzanie czy haslo mac tylko jeden znak jesli tak, zakoncz proram
            break
        i += 1
        if len(password) == 1:
            rand2 = secrets.choice(char)
            password += rand2  # dodawanie drugiego znaku (pierwszy w tablicy)(potrzebne do sprawdzenia czy się nie powtarza ze znakiem poprzednim)

        # Sprawdzanie czy obok siebie nie ma tego samego znaku, jesli tak usuniecie go
        if len(password) > 1:
            if password[i] == password[i - 1]:
                print("zduplikowane: ", password[i], password[i - 1])
                del password[i}
                i -= 1

    received_pass.insert(0, list_to_string(password))


# kopiowanie do schowka
def copy():
    root.clipboard_clear()
    root.clipboard_append(received_pass.get())
    pass


# zapis do pliku .txt
def save():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text document", "*.txt"), ("All Files", "*.*")),
                                        defaultextension=files)
        f = open(getattr(path, "name"), "w")
        f.write(received_pass.get())
        f.close()
    except AttributeError:
        pass


root = Tk()

root.title("Generator silnego hasła!")
root.geometry("600x400")
root.configure(bg="#D3D3D3")

label_frame = LabelFrame(root, text="Podaj długość hasła", font=20)
label_frame.pack(pady=20)
label_frame.configure(bg="gray")

length_pass = Entry(label_frame, font=("Verdana", 17))
length_pass.pack(pady=20, padx=50)

label_frame2 = LabelFrame(root, text="Otrzymane hasło", font=20)
label_frame2.pack(pady=30)
label_frame2.configure(bg="orange")

received_pass = Entry(label_frame2, text="", font=("Verdana", 15), bd=0, bg="systembuttonface")
received_pass.pack(pady=20, padx=40)

checkChar = BooleanVar(value=True)
check_box = Checkbutton(root, text="Znaki specjalne", onvalue=True, offvalue=False, variable=checkChar)
check_box.pack()

my_frame = Frame(root)
my_frame.pack(pady=20)
my_frame.configure(bg="#D3D3D3")

generate_button = Button(my_frame, borderwidth='0', text="Generuj", font=22, command=new_rand,
                         activebackground="orange", width=7)
generate_button.grid(row=0, column=0)
generate_button.configure(bg="gray", font=("calibri", 12, "bold"))

copy_button = Button(my_frame, borderwidth='0', text="Skopiuj", font=22, command=copy, activebackground="orange",
                     width=7)
copy_button.grid(row=0, column=1, padx=10)
copy_button.configure(bg="gray", font=("calibri", 12, "bold"))

save_button = Button(my_frame, borderwidth="0", text="Zapisz", font=22, command=save, activebackground="orange",
                     width=7)
save_button.grid(row=0, column=2)
save_button.configure(bg="gray", font=("calibri", 12, "bold"))

root.mainloop()
