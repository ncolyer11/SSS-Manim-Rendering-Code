# desc: Then you can compute the chance of each fringe 
# type generating and store these values in a table

from manim import *
from colours import*

speed = 1
# speed = 1.0/4

class smp_shot_8(Scene):
    def construct(self):
        self.wait(0.2)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{nicefrac, xfrac}")

        t1 = MathTable(
                [[r"\text{\textbf{Fringe Type}}", r"\text{\textbf{Chance}}"],
                ["[1, 1]", r"\text{P(1st = 1)} \cdot \text{P(2nd = 1)}"],
                ["[1, 2]", r"\text{P(1st = 1)} \cdot \text{P(2nd = 2)}"],
                ["[2, 1]", r"\text{P(1st = 2)} \cdot \text{P(2nd = 1)}"],
                ["[2, 2]", r"\text{P(1st = 2)} \cdot \text{P(2nd = 2)}"]],
                include_outer_lines = True
            )
        self.play(t1.create(), run_time=speed*2.5)
        self.wait()
        
        t2 = MathTable(
                [[r"\text{\textbf{Fringe Type}}", r"\text{\textbf{Chance}}"],
                ["[1, 1]", r"\sfrac{1}{3} \cdot \sfrac{2}{3}"],
                ["[1, 2]", r"\sfrac{1}{3} \cdot \sfrac{1}{3}"],
                ["[2, 1]", r"\sfrac{2}{3} \cdot \sfrac{2}{3}"],
                ["[2, 2]", r"\sfrac{2}{3} \cdot \sfrac{1}{3}"]],
                include_outer_lines = True,
                element_to_mobject=lambda e: MathTex(e, tex_template=myTemplate)

            )
        self.play(ReplacementTransform(t1, t2), run_time=speed*1.5)
        self.wait()
        
        t3 = MathTable(
                [[r"\text{\textbf{Fringe Type}}", r"\text{\textbf{Chance}}"],
                ["[1, 1]", r"\nicefrac{2}{9}"],
                ["[1, 2]", r"\nicefrac{1}{9}"],
                ["[2, 1]", r"\nicefrac{4}{9}"],
                ["[2, 2]", r"\nicefrac{2}{9}"]],
                include_outer_lines = True,
                element_to_mobject=lambda e: MathTex(e, tex_template=myTemplate)
            )
        self.play(ReplacementTransform(t2, t3), run_time=speed*1.5)
        self.wait()
