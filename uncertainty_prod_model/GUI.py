from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk, ImageDraw
from production import *


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
        # Frame1 = Frame(self.root)
        # Frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W + E + N + S)

        Label(self.root, text="Введите характеристики студента", font='Arial 20').grid(row=0, column=2, columnspan=3, sticky=W + N)

        self.deadline = IntVar()
        rbut1 = Radiobutton(self.root, text="Сдаёт всё в срок", variable=self.deadline, value=1)
        rbut2 = Radiobutton(self.root, text="Сдаёт с небольшим опозданием", variable=self.deadline, value=2)
        rbut3 = Radiobutton(self.root, text="Сдаёт c большим опозданием", variable=self.deadline, value=3)

        rbut1.grid(row=2, column=1, sticky = "w")
        rbut2.grid(row=3, column=1, sticky = "w")
        rbut3.grid(row=4, column=1, sticky = "w")

        do_char = IntVar()
        do_alone = Radiobutton(self.root, text="Хорошо разбирается", variable=do_char, value=1)
        do_small_help = Radiobutton(self.root, text="Средне разбирается", variable=do_char, value=2)
        do_not_byself = Radiobutton(self.root, text="Плохо разбирается", variable=do_char, value=3)

        do_alone.grid(row=2, column=2, sticky = "w")
        do_small_help.grid(row=3, column=2, sticky = "w")
        do_not_byself.grid(row=4, column=2, sticky = "w")

        self.additional_classes = IntVar()
        Checkbutton(self.root, text="Дополнительно занимается",
                    variable=self.additional_classes).grid(row=2, column=3, sticky = "w")
        self.complex_tasks = IntVar()
        Checkbutton(self.root, text="Обычно всё сдаёт быстро",
                    variable=self.complex_tasks).grid(row=3, column=3, sticky = "w")
        self.graph_tasks = IntVar()
        Checkbutton(self.root, text="Интересуется задачами на графы",
                    variable=self.graph_tasks).grid(row=4, column=3, sticky = "w")

        self.can_cheat = IntVar()
        Checkbutton(self.root, text="Умеет списывать",
                    variable=self.can_cheat).grid(row=2, column=4, sticky="w")
        # self.know_math = IntVar()
        # Checkbutton(self.root, text="Хорош в математике",
        #             variable=self.know_math).grid(row=6, column=4, sticky="w")
        self.good_in_programming = IntVar()
        Checkbutton(self.root, text="Хорошо программирует",
                    variable=self.good_in_programming).grid(row=3, column=4, sticky="w")
        self.procrastination = IntVar()
        Checkbutton(self.root, text="Имеет Склонность к прокрастинации",
                    variable=self.procrastination).grid(row=4, column=4, sticky="w")
        # self.rotate_x_center_button = Button(self.root, text='Rotate about center x', command=self.rotate_x_center)
        self.calc_button = Button(self.root, text = "Посчитать вероятность сдачи курса", command=self.calc_factors)
        self.calc_button.grid(row=5, column=2, columnspan=3, sticky="w")
        # self.rotate_x_center_button.grid(row=7, column=4)

        self.root.mainloop()

    # TODO: get facts from GUI
    def get_facts(self):
        start_facts = [
            GraphNode("Сдал лабы", 1 if self.deadline.get() == 1 else 0),
            GraphNode("Не сдал лабы", 1 if self.deadline.get() == 2 else 0),
            GraphNode("Сдал опросы", 1)
        ]
        return start_facts

    def calc_factors(self):

        self.run()

    def run(self):
        facts = self.get_facts()
        prod_system = ProductionSystem.get_instance(facts)
        prod_system.mainloop()
        result = prod_system.get_result()

        passProbability = result[0].CF
        Label(self.root, text="Вероятность сдачи зачёта - {0:.2f}".format(passProbability))\
            .grid(row=8, column=4, columnspan=2)
        Label(self.root, text="Вероятность не сдачи зачёта - {0:.2f}".format(1 - passProbability))\
            .grid(row=9, column=4, columnspan=2)


gui = WorkArea()