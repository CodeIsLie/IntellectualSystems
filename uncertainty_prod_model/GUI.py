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

        Label(self.root, text="Введите характеристики студента", font='Arial 20').grid(row=0, column=2, columnspan=3, sticky=W + N)

        self.deadline = IntVar(value=1)
        self.in_deadline = Radiobutton(self.root, text="Сдаёт всё в срок", variable=self.deadline, value=1)
        self.small_delay = Radiobutton(self.root, text="Сдаёт с небольшим опозданием", variable=self.deadline, value=2)
        self.big_delay = Radiobutton(self.root, text="Сдаёт c большим опозданием", variable=self.deadline, value=3)

        self.in_deadline.grid(row=2, column=1, sticky = "w")
        self.small_delay.grid(row=3, column=1, sticky = "w")
        self.big_delay.grid(row=4, column=1, sticky = "w")

        self.skill = IntVar(value=1)
        self.good_skill = Radiobutton(self.root, text="Хорошо разбирается", variable=self.skill, value=1)
        self.mid_skill = Radiobutton(self.root, text="Средне разбирается", variable=self.skill, value=2)
        self.poor_skill = Radiobutton(self.root, text="Плохо разбирается", variable=self.skill, value=3)

        self.good_skill.grid(row=2, column=2, sticky = "w")
        self.mid_skill.grid(row=3, column=2, sticky = "w")
        self.poor_skill.grid(row=4, column=2, sticky = "w")

        self.additional_classes = IntVar()
        Checkbutton(self.root, text="Дополнительно занимается",
                    variable=self.additional_classes).grid(row=2, column=3, sticky = "w")
        self.graph_tasks = IntVar()
        Checkbutton(self.root, text="Интересуется графами",
                    variable=self.graph_tasks).grid(row=4, column=3, sticky = "w")

        self.can_cheat = IntVar()
        Checkbutton(self.root, text="Умеет списывать",
                    variable=self.can_cheat).grid(row=2, column=4, sticky="w")
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
            GraphNode("Хорошо разбирается", 1 if self.skill.get() == 1 else 0),
            GraphNode("Средне разбирается", 1 if self.skill.get() == 2 else 0),
            GraphNode("Плохо разбирается", 1 if self.skill.get() == 3 else 0),
            GraphNode("Сдаёт в срок", 1 if self.deadline.get() == 1 else 0),
            GraphNode("Сдаёт с маленьким опозданием", 1 if self.deadline.get() == 2 else 0),
            GraphNode("Сдаёт с большим опозданием", 1 if self.deadline.get() == 3 else 0),
            GraphNode("Дополнительно занимается", 1 if self.additional_classes.get() == 1 else 0),
            GraphNode("Интересуют графы", 1 if self.graph_tasks.get() == 1 else 0),
            GraphNode("Прокрастинация", 1 if self.procrastination.get() == 1 else 0),
            GraphNode("Умеет списывать", 1 if self.can_cheat.get() == 1 else 0)
        ]
        return start_facts

    def calc_factors(self):
        self.run()
        for x, y in self.prod_system.facts.items():
            print("{} - {}".format(x, y))
        print('*' * 20)

    def run(self):
        facts = self.get_facts()
        self.prod_system = ProductionSystem.get_instance(facts)
        prod_system = self.prod_system
        prod_system.mainloop()
        result = prod_system.get_result()

        passProbability = (1 + result[0].CF) / 2
        Label(self.root, text="Вероятность сдачи зачёта - {0:.2f}".format(passProbability))\
            .grid(row=8, column=4, columnspan=2)
        Label(self.root, text="Вероятность не сдачи зачёта - {0:.2f}".format(1 - passProbability))\
            .grid(row=9, column=4, columnspan=2)


gui = WorkArea()