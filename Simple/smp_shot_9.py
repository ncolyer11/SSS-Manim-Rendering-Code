# desc: so now we need to find all the valid trunk and hat height sets

from manim import *
from colours import*

speed = 1
# speed = 1.0/5

class smp_shot_9(Scene):
    def construct(self):
        self.wait(0.2)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{nicefrac, xfrac}")        

        t4 = MathTable(
                [[r"\text{\textbf{T}}_{\mathbf{h}} \, \mathbf{: \: (\%)}", r"\text{\textbf{H}}_{\mathbf{h}} \, \mathbf{: \: (\%)}"],
                [r"4 \! : \: \nicefrac{11}{120}", r"1 \! : \: \nicefrac{1}{4}"],
                [r"4 \! : \: \nicefrac{11}{120}", r"2 \! : \: \nicefrac{1}{4}"],
                [r"4 \! : \: \nicefrac{11}{120}", r"3 \! : \: \nicefrac{1}{4}"],
                [r"4 \! : \: \nicefrac{11}{120}", r"4 \! : \: \nicefrac{1}{4}"],
                [r"5 \! : \: \nicefrac{11}{120}", r"1 \! : \: \nicefrac{1}{5}"],
                [r"5 \! : \: \nicefrac{11}{120}", r"2 \! : \: \nicefrac{1}{5}"],
                [r"5 \! : \: \nicefrac{11}{120}", r"3 \! : \: \nicefrac{1}{5}"],
                [r"5 \! : \: \nicefrac{11}{120}", r"4 \! : \: \nicefrac{1}{5}"],
                [r"5 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{5}"],
                [r"6 \! : \: \nicefrac{11}{120}", r"1 \! : \: \nicefrac{1}{6}"],
                [r"6 \! : \: \nicefrac{11}{120}", r"2 \! : \: \nicefrac{1}{6}"],
                [r"6 \! : \: \nicefrac{11}{120}", r"3 \! : \: \nicefrac{1}{6}"],
                [r"6 \! : \: \nicefrac{11}{120}", r"4 \! : \: \nicefrac{1}{6}"],
                [r"6 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{6}"],
                [r"6 \! : \: \nicefrac{11}{120}", r"6 \! : \: \nicefrac{1}{6}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"1 \! : \: \nicefrac{1}{7}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"2 \! : \: \nicefrac{1}{7}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"3 \! : \: \nicefrac{1}{7}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"4 \! : \: \nicefrac{1}{7}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{7}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"6 \! : \: \nicefrac{1}{7}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"7 \! : \: \nicefrac{1}{7}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"1 \! : \: \nicefrac{1}{8}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"2 \! : \: \nicefrac{1}{8}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"3 \! : \: \nicefrac{1}{8}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"4 \! : \: \nicefrac{1}{8}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"5 \! : \: \nicefrac{1}{8}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"6 \! : \: \nicefrac{1}{8}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"7 \! : \: \nicefrac{1}{8}"],  # wasn't going to make this table at run-
                [r"8 \! : \: \nicefrac{12}{120}", r"8 \! : \: \nicefrac{1}{8}"]], # time with for loops so you get this now
                include_outer_lines = True,
                element_to_mobject=lambda e: MathTex(e, tex_template=myTemplate)
            ).scale(0.9).to_edge(UP, buff = 0.2)
        
        t4.get_entries((1,1)).set_color(trunk_height_colour)
        t4.get_entries((1,2)).set_color(hat_height_colour)
        
        self.play(t4.create(), run_time=speed*4)
        self.wait()

        self.play(t4.animate.to_edge(DOWN, buff = -0.2), rate_func=rate_functions.ease_in_cubic, run_time = speed*7)
        self.wait()




