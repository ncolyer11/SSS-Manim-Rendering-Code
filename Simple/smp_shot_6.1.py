# desc: table for simple shot 6

from manim import *
from colours import*

speed = 1
# speed = 1.0/4

class smp_shot_6_1(Scene):
    def construct(self):
        t1 = MathTable(
                [[r"\text{\textbf{Height(s)}}", r"\text{\textbf{Chance}}"],
                [r"\text{4, 5, 6, 7}", r"\frac{11}{120}"],
                [8 , r"\frac{11}{120} + \frac{1}{120}"],
                [9 , r"\frac{11}{120}"],
                [10, r"\frac{11}{120} + \frac{1}{120}"],
                [11, r"\frac{11}{120}"],
                [12, r"\frac{11}{120} + \frac{1}{120}"],
                [13, r"\frac{11}{120}"],
                [r"\text{14, 16, ..., 26}", r"\frac{1}{120}"]],
                include_outer_lines = True,
            )
        for i in [3,5,7,9]:
            t1.add_highlighted_cell((i,2), color=trunk_table_highlight_colour)
        t1.scale(0.48).shift(RIGHT * 5)

        self.play(t1.create(), run_time=speed*2.5)
        self.wait()

        t2 = MathTable(
                [[r"\text{\textbf{Height(s)}}", r"\text{\textbf{Chance}}"],
                [r"\text{4, 5, 6, 7}", r"\frac{11}{120}"],
                [8 , r"\frac{12}{120}"],
                [9 , r"\frac{11}{120}"],
                [10, r"\frac{12}{120}"],
                [11, r"\frac{11}{120}"],
                [12, r"\frac{12}{120}"],
                [13, r"\frac{11}{120}"],
                [r"\text{14, 16, ..., 26}", r"\frac{1}{120}"]],
                include_outer_lines = True,
            )
        for i in [3,5,7,9]:
            t2.add_highlighted_cell((i,2), color=trunk_table_highlight_colour)
        t2.scale(0.48).shift(RIGHT * 5)
        
        self.play(ReplacementTransform(t1, t2), run_time=speed*1)
        self.wait()

        self.play(Flash(t2.get_entries((1,11)), run_time=1*speed,))  # Highlight cell (row 11, column 1)
        self.wait(speed*0.2)
        self.play(Wiggle(t2.get_entries((1,12)), run_time=1.25*speed,))  # Wiggle cell (row 11, column 2)
        self.wait()
