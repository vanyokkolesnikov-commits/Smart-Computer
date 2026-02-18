import tkinter as tk
from tkinter import ttk
import os
import time
import random

a = [
    "— Моя девушка порвала со мной, и я забрал ее кресло-каталку. Угадайте, кто приполз ко мне на коленях?",
    "Акробат умер на батуте, но еще какое-то время продолжал радовать публику.",
    "Зеленский заявил, что после войны в Украине будет как в Швейцарии. Нейтралитет, часы и счета в иностранных банках.",
    "Мой друг спросил, как быстро похудеть. Я предложил ампутацию. Он не оценил шутку, зато теперь весит на 10 кг меньше.",
    "— Что было раньше: курица или яйцо?\n— Сначала было яйцо...\n...а внутри него лежала инструкция по сборке шведской стенки.",
    "Зеленский: Дайте..."
]
joke = random.choice(a)

root = tk.Tk()
root.title("микруха")
root.geometry("430x330")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)




console_text1 = tk.Text(frame1, height=15, width=50, bg='black', fg='white')
console_text1.pack(padx=10, pady=10)

console_text1.insert('end', ">>> Добро пожаловать в диспетчер!\n")
console_text1.insert('end', ">>> Введите help для справки\n")

console_entry1 = ttk.Entry(frame1, width=50)
console_entry1.place(x=10, y=270)

def on_enter(event):
    cmd = console_entry1.get()
    console_text1.insert('end', f"\n>>> {cmd}\n")
    if cmd == "help":
        console_text1.insert('end', "Доступные команды:\nhelp - команды\nclear - отчистка\nexit - выход\nginfo - графическое окно\n"
                                    "info - информация о пк\ndisp - диспетчер\nmonitor - монитор ресурсов")
    elif cmd == "clear":
        console_text1.delete('1.0', 'end')
    elif cmd == "exit":
        root.quit()
    elif cmd == "ginfo":
        os.system('msinfo32')
    elif cmd == "info":
        os.system("dxdiag")
    elif cmd == "disp":
        os.system("perfmon")
    elif cmd == "monitor":
        os.system("resmon")
    else:
        console_text1.insert('end', f"Неизвестная команда: {cmd}\n")
    console_entry1.delete(0, 'end')
    console_text1.see('end')


console_entry1.bind('<Return>', on_enter)
console_entry1.focus()





console_text = tk.Text(frame2, height=15, width=50, bg='black', fg='white')
console_text.pack(padx=10, pady=10)

console_text.insert('end', ">>> Добро пожаловать в консоль!\n")
console_text.insert('end', ">>> Введите help для справки\n")

console_entry = ttk.Entry(frame2, width=50)
console_entry.place(x=10, y=270)

def on_enter(event):
    cmd = console_entry.get()
    console_text.insert('end', f"\n>>> {cmd}\n")
    if cmd == "help":
        console_text.insert('end', "Доступные команды:\nhelp - команды\nclear - отчистка\nexit - выход\nshutdown - выключить компьютер"
                                   "\ntime - время\nsite - сайты\nsounds - выкл/вкл звуки\ngames - игры\nversion - версия\njoke - шутка\nmaid - фронтальная камера")
    elif cmd == "clear":
        console_text.delete('1.0', 'end')
    elif cmd == "exit":
        root.quit()
    elif cmd == "shutdown":
        os.system("shutdown /s /t 1")
    elif cmd == "site":
        console_text.insert('end', "google\nyoutube\ntwitch\nxxx\n")
    elif cmd == "google":
        os.system('start https://google.com')
    elif cmd == "youtube":
        os.system('start https://www.youtube.com/')
    elif cmd == "twitch":
        os.system('start https://www.twitch.tv/')
    elif cmd == "xxx":
        os.system('start https://hot.noodlemagazine.com/video/аниме')
    elif cmd == "sounds":
        os.system('powershell -c "(New-Object -ComObject wscript.shell).SendKeys([char]173)"')
    elif cmd == "time":
        console_text.insert('end', time.ctime())
    elif cmd == "games":
        console_text.insert('end', "Dota\nPhasmophobia\nTerraria\nForest\nDST\ntmodloader")
    elif cmd == "dota":
        os.system("start steam://run/570")
    elif cmd == "phasmophobia":
        os.system("start steam://run/739630")
    elif cmd == "terraria":
        os.system("start steam://run/105600")
    elif cmd == "forest":
        os.system("start steam://run/242760")
    elif cmd == "dst":
        os.system("start steam://run/322330")
    elif cmd == "tmodloader":
        os.system("start steam://run/1281930")
    elif cmd == "joke":
        console_text.insert('end', random.choice(a))
    elif cmd == "version":
        console_text.insert('end', "Version: 1.0.1")
    elif cmd == "maid":
        console_text.insert('end', "⣿⣿⣷⡁⢆⠈⠕⢕⢂⢕⢂⢕⢂⢔⢂⢕⢄⠂⣂⠂⠆⢂⢕⢂⢕⢂⢕⢂⢕⢂"
                                   "\n⣿⣿⣿⡷⠊⡢⡹⣦⡑⢂⢕⢂⢕⢂⢕⢂⠕⠔⠌⠝⠛⠶⠶⢶⣦⣄⢂⢕⢂⢕"
                                   "\n⣿⣿⠏⣠⣾⣦⡐⢌⢿⣷⣦⣅⡑⠕⠡⠐⢿⠿⣛⠟⠛⠛⠛⠛⠡⢷⡈⢂⢕⢂"
                                   "\n⠟⣡⣾⣿⣿⣿⣿⣦⣑⠝⢿⣿⣿⣿⣿⣿⡵⢁⣤⣶⣶⣿⢿⢿⢿⡟⢻⣤⢑⢂"
                                   "\n⣾⣿⣿⡿⢟⣛⣻⣿⣿⣿⣦⣬⣙⣻⣿⣿⣷⣿⣿⢟⢝⢕⢕⢕⢕⢽⣿⣿⣷⣔"
                                   "\n⣿⣿⠵⠚⠉⢀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⢕⢕⢕⢕⢕⢕⣽⣿⣿⣿⣿"
                                   "\n⢷⣂⣠⣴⣾⡿⡿⡻⡻⣿⣿⣴⣿⣿⣿⣿⣿⣿⣷⣵⣵⣵⣷⣿⣿⣿⣿⣿⣿⡿"
                                   "\n⢌⠻⣿⡿⡫⡪⡪⡪⡪⣺⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃"
                                   "\n⠣⡁⠹⡪⡪⡪⡪⣪⣾⣿⣿⣿⣿⠋⠐⢉⢍⢄⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⠏⠈"
                                   "\n⡣⡘⢄⠙⣾⣾⣾⣿⣿⣿⣿⣿⣿⡀⢐⢕⢕⢕⢕⢕⡘⣿⣿⣿⣿⣿⣿⠏⠠⠈"
                                   "\n⠌⢊⢂⢣⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢐⢕⢕⢕⢕⢕⢅⣿⣿⣿⣿⡿⢋⢜⠠⠈"
                                   "\n⠄⠁⠕⢝⡢⠈⠻⣿⣿⣿⣿⣿⣿⣿⣷⣕⣑⣑⣑⣵⣿⣿⣿⡿⢋⢔⢕⣿⠠⠈"
                                   "\n⠨⡂⡀⢑⢕⡅⠂⠄⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⢔⢕⢕⣿⣿⠠⠈"
                                   "\n⠄⠪⣂⠁⢕⠆⠄⠂⠄⠁⡀⠂⡀⠄⢈⠉⢍⢛⢛⢛⢋⢔⢕⢕⢕⣽⣿⣿⠠")
    else:
        console_text.insert('end', f"Неизвестная команда: {cmd}\n")
    console_entry.delete(0, 'end')
    console_text.see('end')

console_entry.bind('<Return>', on_enter)
console_entry.focus()

notebook.add(frame1, text='Диспетчер')
notebook.add(frame2, text='Консоль')
notebook.add(frame3, text='3')
notebook.add(frame4, text='4')

label3 = ttk.Label(frame3, text="Третья вкладка")
label3.pack(pady=20)

root.mainloop()
