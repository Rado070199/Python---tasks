import logging
import traceback
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import PhotoImage

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('calcForm.log'),
        logging.StreamHandler()
    ]
)

number1 = None
operation = None

#TODO obsługa operacji(narazie działa tylko /)
def on_button_click(event):
    try:
        global operation, number1
        button_text = event.widget.cget("text")
        
        match button_text:
            case '%':
                messagebox.showinfo("%", button_text)
            case 'CE':
                messagebox.showinfo("CE", button_text)
            case 'C':
                messagebox.showinfo("C", button_text)
            case 'X':
                text_box.delete("end-2c", tk.END)
            case '1/x':
                messagebox.showinfo("1/x", button_text)
            case 'x2':
                messagebox.showinfo("x2", button_text)
            case 'Pie':
                messagebox.showinfo("Pie", button_text)
            case '/':
                if operation is None:
                    operation = '/'
                    number1 = float(text_box.get("1.0", tk.END).strip())
                    text_box.delete("1.0", tk.END)
                else:
                    get_sum()
            case '*':
                messagebox.showinfo("*", button_text)
            case '-':
                messagebox.showinfo("-", button_text)
            case '+':
                messagebox.showinfo("+", button_text)
            case '+/z':
                messagebox.showinfo("+/z", button_text)
            case ',':
                messagebox.showinfo(",", button_text)
            case '=':
                messagebox.showinfo("=", button_text)
            case _:
                text_box.insert(tk.END, button_text)
    except Exception as e:
        logging.error(f'error: {e}')
        logging.error("Traceback:\n%s", traceback.format_exc())
        exit()
        
def get_sum():
    global operation, number1
    number2 = float(text_box.get("1.0", tk.END).strip())
    text_box.delete("1.0", tk.END)
    expression = f"{number1} {operation} {number2}"
    result = eval(expression)
    text_box.insert("1.0", f'{result}')

#Budowanie formularza
try:
    root = tk.Tk()
    root.title('Calculator')

    #Aby ustawić ikonę dla okna aplikacji w tkinter, możesz użyć metody iconbitmap() (dla plików .ico) lub PhotoImage() (dla plików .png, .gif, itp.).
    '''
    # Ustaw ikonę z pliku .png
    icon = PhotoImage(file='ikona.png')
    root.iconphoto(True, icon)

    # Ustaw ikonę z pliku .ico
    root.iconbitmap('ikona.ico')
    '''
    icon = PhotoImage(file='Resources/Calculator32.png')
    root.iconphoto(True, icon)
    # Wymiary startowe formularza.
    root.geometry('400x350')

    # Pole typu textBox jako ekran wyświetlacza.
    text_frame = tk.Frame(root)
    text_frame.pack(padx=10, pady=10)
    font_style = font.Font(family='Halvetica', size=24)

    text_box = tk.Text(text_frame, height=1, width=40, font=font_style)
    text_box.pack(padx=10, pady=10)



    # Utwórz ramkę na siatkę.
    grid_frame = tk.Frame(root)
    grid_frame.pack(padx=10, pady=10, fill=tk.BOTH,)

    # Dodaj przyciski do siatki 4 kolumny x 6 wierszy
    texts = [
        "%", "CE", "C", "X",
        "1/x", "x2", "Pie", "/",
        "7", "8", "9", "*",
        "4", "5", "6", "-",
        "1", "2", "3", "+",
        "+/z", "0", ",", "="
    ]
    for row in range(6):
        for col in range(4):
            text = texts[row * 4 + col]
            if text == "=":
                btn = tk.Button(grid_frame, text=text, bg="blue", fg="white")
            else:
                btn = tk.Button(grid_frame, text=text)
            
            btn.bind("<Button-1>", on_button_click)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # Ustaw proporcje kolumn i wierszy, aby przyciski rozciągały się
    for i in range(4):
        grid_frame.columnconfigure(i, weight=1)
    for i in range(6):
        grid_frame.rowconfigure(i, weight=1)

    root.mainloop()
except Exception as e:
    logging.error('error: {e}')
    logging.error("Traceback:\n%s", traceback.format_exc())
    exit()
