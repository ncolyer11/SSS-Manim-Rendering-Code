# desc: ...there are only 17 different trunk heights, T. We
# can plug each of these values into the hat height equation

from FaR import search_shapes_in_text
from manim import *
from colours import*
import random

speed = 1
# speed = 1.0/5

class smp_shot_9(Scene):
    def construct(self):
        self.wait(0.2)
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
                include_outer_lines = True
            ).scale(0.48).to_edge(LEFT, buff = 0.2)
        
        self.play(t2.create(), run_time=speed*1)
        self.wait()

        hat_height_equation = Tex(
                                r"H$_h$ = min(rand.int$ \Bigl( \Bigl\lfloor \frac{\text{T}_h}{3} \Bigl\rfloor \Bigl) $ + 5, T$_h$)"
                            ).next_to(t2, buff = 0.5)
                                
        self.play(Write(hat_height_equation), run_time=speed*2)
        self.wait()

        for group in search_shapes_in_text(hat_height_equation, [Tex(r"H$_h$")]):
            self.play(*[
                hat_height_equation[0][group].animate.set_color(hat_height_colour)
            ], run_time=0.3*speed)
        self.wait(0.5*speed)

        for group in search_shapes_in_text(hat_height_equation, [Tex(r"rand.int")]):
            self.play(*[
                hat_height_equation[0][group].animate.set_color(random_colour)
            ], run_time=0.3*speed) 
        self.wait(0.5*speed)

        for group in search_shapes_in_text(hat_height_equation, [Tex(r"$_{\text{T}_h}$"), Tex(r"T$_h$")]):
            self.play(*[
                hat_height_equation[0][group].animate.set_color(trunk_height_colour)
            ], run_time=0.3*speed) 
        self.wait(speed*1)

        T = 4
        hat_height_equation2 = Tex("shut it compiler")
        j = 0
        for i in range(6):
            self.remove(hat_height_equation2)
            rand = random.randint(0, T//3)
            H = f"{min(rand + 5, T)}"
            # H = f"{min(5, T)}"
            hat_height_equation2 = Tex(
                                    r"H$_h$",
                                    r" = min(",
                                    str(rand),
                                    r" + 5, ",
                                    str(T),
                                    r") = ",
                                    H
                                ).next_to(t2, buff = 0.5)
            
            hat_height_equation2[0].set_color(hat_height_colour)
            hat_height_equation2[2].set_color(random_colour)
            hat_height_equation2[4].set_color(trunk_height_colour)
            hat_height_equation2[6].set_color(hat_height_colour)

            rect = SurroundingRectangle(t2.get_rows()[j + 1])
            if i == 0:
                self.play(TransformMatchingShapes(hat_height_equation, hat_height_equation2), Create(rect), run_time=speed*1)
            elif i < 3:
                self.play(ReplacementTransform(hat_height_equation2, hat_height_equation2), ReplacementTransform(rect2, rect), run_time=speed*1)
            else:
                self.play(ReplacementTransform(hat_height_equation2, hat_height_equation2), ReplacementTransform(rect2, rect), run_time=speed*1)
                j += 1

            rect2 = rect
            T += 1 
            self.wait(speed)

        self.play(Uncreate(t2), Unwrite(hat_height_equation2), Uncreate(rect), Uncreate(rect2), run_time=speed*1.5)
        self.wait(speed)
