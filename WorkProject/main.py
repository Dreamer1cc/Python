from tkinter import *
import read as r
import tkinter.filedialog as fdialog

'''Создание окна приложения'''
window = Tk()
window.title('WorkProject')
window.geometry('300x200')

'''Оформление окна'''
canvas = Canvas(window, width=300, height=200)
# canvas.pack(side='right')

'''Надпись на экране(ярлык)'''
label = Label(window, text='Путь к файлу: ')
label.place(x=0, y=10)

'''Поле для ввода данных'''
entry_text = Entry(window)
entry_text.place(x=85, y=10)

'''Кнопка запуска программы'''
btn_go = Button(window, text='GO!')
btn_go.bind('<Button-1>', lambda event: r.read_logs(entry_text.get()))
btn_go.place(x=85, y=60)

'''Браузер файлов'''
btn_brws = Button(window, text='BROWSE')
btn_brws.bind('<Button-1>', lambda event: r.read_logs(fdialog.askopenfilename()))
btn_brws.place(x=125, y=60)

window.mainloop()
