from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk, ImageDraw


class WorkArea:

    DEFAULT_WIDTH = 600
    DEFAULT_HEIGHT = 600
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title("BezdelnikSystem")
        self.root.resizable(False, False)

        # self.canvas = Canvas(self.root, bg='white', width=self.DEFAULT_WIDTH, height=self.DEFAULT_WIDTH)
        # self.canvas.grid(row=1, columnspan=10)
        # self.image = Image.new('RGB', (self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT), 'white')
        # self.draw = ImageDraw.Draw(self.image)
        Frame1 = Frame(self.root)
        Frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W + E + N + S)

        Label(self.root, text="Введите характеристики студента", font='Arial 20').grid(row=0, column=2, sticky=W + N)

        deadline = IntVar()
        rbut1 = Radiobutton(self.root, text="Сдаёт всё в срок", variable=deadline, value=1)
        rbut2 = Radiobutton(self.root, text="Сдаёт с небольшим опозданием", variable=deadline, value=2)
        rbut3 = Radiobutton(self.root, text="Сдаёт всё в срок", variable=deadline, value=3)

        rbut1.grid(row=2, column=1, sticky = "w")
        rbut2.grid(row=3, column=1, sticky = "w")
        rbut3.grid(row=4, column=1, sticky = "w")

        do_char = IntVar()
        do_alone = Radiobutton(self.root, text="Делает всё сам", variable=do_char, value=1)
        do_small_help = Radiobutton(self.root, text="Делает с небольшой помощью", variable=do_char, value=2)
        do_not_byself = Radiobutton(self.root, text="Большую часть работы делает не сам", variable=do_char, value=3)

        do_alone.grid(row=2, column=2, sticky = "w")
        do_small_help.grid(row=3, column=2, sticky = "w")
        do_not_byself.grid(row=4, column=2, sticky = "w")

        # Label(self.root, text="angle: ").grid(row=8, column=4)
        # self.angle_input_box = Entry(self.root)
        # self.angle_input_box.insert(0, "45")
        # self.angle_input_box.grid(row=9, column=4)

        self.additional_classes = IntVar()
        Checkbutton(self.root, text="Дополнительно изучает программирование или АСД",
                    variable=self.additional_classes).grid(row=2, column=4, sticky = "w")
        self.complex_tasks = IntVar()
        Checkbutton(self.root, text="Хорошо справляется со сложными задачами",
                    variable=self.complex_tasks).grid(row=3, column=4, sticky = "w")
        self.graph_tasks = IntVar()
        Checkbutton(self.root, text="Интересуется задачами на графы",
                    variable=self.graph_tasks).grid(row=4, column=4, sticky = "w")

        self.can_cheat = IntVar()
        Checkbutton(self.root, text="Умеет списывать",
                    variable=self.can_cheat).grid(row=5, column=4, sticky="w")
        self.know_math = IntVar()
        Checkbutton(self.root, text="Хорош в математике",
                    variable=self.know_math).grid(row=6, column=4, sticky="w")
        self.good_in_programming = IntVar()
        Checkbutton(self.root, text="Хорошо программирует",
                    variable=self.good_in_programming).grid(row=7, column=4, sticky="w")
        self.program_style = IntVar()
        Checkbutton(self.root, text="Имеет хороший стиль программирования",
                    variable=self.program_style).grid(row=8, column=4, sticky="w")
        self.procrastination = IntVar()
        Checkbutton(self.root, text="Имеет Склонность к прокрастинации",
                    variable=self.procrastination).grid(row=9, column=4, sticky="w")
        # self.rotate_x_center_button = Button(self.root, text='Rotate about center x', command=self.rotate_x_center)
        # self.rotate_x_center_button.grid(row=7, column=4)

        self.root.mainloop()


gui = WorkArea()