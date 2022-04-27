import tkinter.filedialog
from tkinter import *
from tkinter import ttk


class NotePad(Tk):
    def __init__(self):
        super().__init__()
        self.title('Bloco de notas - Make in Python V1.0')
        self.resizable(False, False)
        self.menubar = Menu(self)
        self.file_menu = Menu(self.menubar, tearoff=0)

    def elements(self):
        def open_file():
            file_path = tkinter.filedialog.askopenfile()
            if file_path is not None:
                with open(file_path.name, 'r', encoding='utf-8') as file:
                    content = file.read()
                    box_text.insert(1.0, content)
            else:
                pass

        def save_file():
            value = box_text.get(1.0, 'end')
            try:
                f = open(tkinter.filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension='.txt'), 'w')
                f.write(value)
                f.close()
            except FileNotFoundError:
                pass

        def close_file():
            box_text.delete(0.0, 'end')

        def close_program():
            self.destroy()

        # Elementos do menu
        self.file_menu.add_command(label="Abrir", command=open_file)
        self.file_menu.add_command(label="Salvar como...", command=save_file)
        self.file_menu.add_command(label="Fechar", command=close_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=close_program)
        self.menubar.add_cascade(label="Arquivo", menu=self.file_menu)
        editmenu = Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Undo", command='1')
        self.config(menu=self.menubar)

        # Container
        frame = Frame(self)
        frame.grid(rowspan=10, columnspan=10)

        # Área de escrita
        box_text = Text(frame, width=125, height=30, font=('Arial', 11, 'bold'))
        box_text.grid(row=0, column=0)

        scroll = ttk.Scrollbar(frame, orient='vertical', command=box_text.yview)
        scroll.grid(row=0, column=1, sticky='ns')
        box_text['yscrollcommand'] = scroll.set


if __name__ == '__main__':
    app = NotePad()
    app.elements()
    app.mainloop()
