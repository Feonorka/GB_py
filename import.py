from tkinter import *
import tkinter as tk
import sqlite3
from turtle import textinput

# создание базы данных
conn = sqlite3.connect('notes.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT)''')
conn.commit()

def save_note():
    note = textinput('1.0', 'end-1c') # получение текста из текстового поля
    c.execute('INSERT INTO notes (note) VALUES (?)', (note,))
    conn.commit()

# функция чтения списка заметок
def read_notes():
    notes_list.delete(0, 'end') # очистка списка
    c.execute('SELECT * FROM notes')
    notes = c.fetchall()
    for note in notes:
        notes_list.insert('end', note[1])

# функция редактирования заметки
def edit_note():
    selected_note = notes_list.curselection() # получение индекса выбранной заметки
    if selected_note:
        note_id = selected_note[0] + 1 # индекс в списке начинается с 0, а id в базе данных начинается с 1
        updated_note = text_input.get('1.0', 'end-1c')
        c.execute('UPDATE notes SET note = ? WHERE id = ?', (updated_note, note_id))
        conn.commit()
        read_notes()

# функция удаления заметки
def delete_note():
    selected_note = notes_list.curselection() # получение индекса выбранной заметки
    if selected_note:
        note_id = selected_note[0] + 1 # индекс в списке начинается с 0, а id в базе данных начинается с 1
        c.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        conn.commit()
        read_notes()

# создание графического интерфейса
root = tk.Tk()

# текстовое поле для ввода заметки
text_input = tk.Text(root)
text_input.pack(padx=10, pady=10)

# кнопка сохранения заметки
save_button = tk.Button(root, text='Сохранить', command=save_note)
save_button.pack(padx=10, pady=10)

# список заметок
notes_list = tk.Listbox(root)
notes_list.pack(padx=10, pady=10)

# кнопки редактирования и удаления заметки
edit_button = tk.Button(root, text='Редактировать', command=edit_note)
edit_button.pack(padx=10, pady=5)

delete_button = tk.Button(root, text='Удалить', command=delete_note)
delete_button.pack(padx=10, pady=5)

# кнопка обновления списка заметок
read_button = tk.Button(root, text='Обновить список', command=read_notes)
read_button.pack(padx=10, pady=10)

root.mainloop()

# закрытие базы данных после закрытия графического интерфейса
conn.close()