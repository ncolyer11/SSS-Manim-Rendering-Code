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
                [r"4 \! : \: \nicefrac{11}{120}", r"4 \! : \: \nicefrac{1}{1}"],
                [r"5 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{1}"],
                [r"6 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{3}"], # dw i used the below python program
                [r"6 \! : \: \nicefrac{11}{120}", r"6 \! : \: \nicefrac{2}{3}"], # to generate all this text :p
                [r"7 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{3}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"6 \! : \: \nicefrac{1}{3}"],
                [r"7 \! : \: \nicefrac{11}{120}", r"7 \! : \: \nicefrac{1}{3}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"5 \! : \: \nicefrac{1}{3}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"6 \! : \: \nicefrac{1}{3}"],
                [r"8 \! : \: \nicefrac{12}{120}", r"7 \! : \: \nicefrac{1}{3}"],
                [r"9 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{4}"],
                [r"9 \! : \: \nicefrac{11}{120}", r"6 \! : \: \nicefrac{1}{4}"],
                [r"9 \! : \: \nicefrac{11}{120}", r"7 \! : \: \nicefrac{1}{4}"],
                [r"9 \! : \: \nicefrac{11}{120}", r"8 \! : \: \nicefrac{1}{4}"],
                [r"10 \! : \: \nicefrac{12}{120}", r"5 \! : \: \nicefrac{1}{4}"],
                [r"10 \! : \: \nicefrac{12}{120}", r"6 \! : \: \nicefrac{1}{4}"],
                [r"10 \! : \: \nicefrac{12}{120}", r"7 \! : \: \nicefrac{1}{4}"],
                [r"10 \! : \: \nicefrac{12}{120}", r"8 \! : \: \nicefrac{1}{4}"],
                [r"11 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{4}"],
                [r"11 \! : \: \nicefrac{11}{120}", r"6 \! : \: \nicefrac{1}{4}"],
                [r"11 \! : \: \nicefrac{11}{120}", r"7 \! : \: \nicefrac{1}{4}"],
                [r"11 \! : \: \nicefrac{11}{120}", r"8 \! : \: \nicefrac{1}{4}"],
                [r"12 \! : \: \nicefrac{12}{120}", r"5 \! : \: \nicefrac{1}{5}"],
                [r"12 \! : \: \nicefrac{12}{120}", r"6 \! : \: \nicefrac{1}{5}"],
                [r"12 \! : \: \nicefrac{12}{120}", r"7 \! : \: \nicefrac{1}{5}"],
                [r"12 \! : \: \nicefrac{12}{120}", r"8 \! : \: \nicefrac{1}{5}"],
                [r"12 \! : \: \nicefrac{12}{120}", r"9 \! : \: \nicefrac{1}{5}"],
                [r"13 \! : \: \nicefrac{11}{120}", r"5 \! : \: \nicefrac{1}{5}"],
                [r"13 \! : \: \nicefrac{11}{120}", r"6 \! : \: \nicefrac{1}{5}"],
                [r"13 \! : \: \nicefrac{11}{120}", r"7 \! : \: \nicefrac{1}{5}"],
                [r"13 \! : \: \nicefrac{11}{120}", r"8 \! : \: \nicefrac{1}{5}"],
                [r"13 \! : \: \nicefrac{11}{120}", r"9 \! : \: \nicefrac{1}{5}"],
                [r"14 \! : \: \nicefrac{1}{120}", r"5 \! : \: \nicefrac{1}{5}"],
                [r"14 \! : \: \nicefrac{1}{120}", r"6 \! : \: \nicefrac{1}{5}"],
                [r"14 \! : \: \nicefrac{1}{120}", r"7 \! : \: \nicefrac{1}{5}"],
                [r"14 \! : \: \nicefrac{1}{120}", r"8 \! : \: \nicefrac{1}{5}"],
                [r"14 \! : \: \nicefrac{1}{120}", r"9 \! : \: \nicefrac{1}{5}"],
                [r"16 \! : \: \nicefrac{1}{120}", r"5 \! : \: \nicefrac{1}{6}"],
                [r"16 \! : \: \nicefrac{1}{120}", r"6 \! : \: \nicefrac{1}{6}"],
                [r"16 \! : \: \nicefrac{1}{120}", r"7 \! : \: \nicefrac{1}{6}"],
                [r"16 \! : \: \nicefrac{1}{120}", r"8 \! : \: \nicefrac{1}{6}"],
                [r"16 \! : \: \nicefrac{1}{120}", r"9 \! : \: \nicefrac{1}{6}"],
                [r"16 \! : \: \nicefrac{1}{120}", r"10 \! : \: \nicefrac{1}{6}"],
                [r"18 \! : \: \nicefrac{1}{120}", r"5 \! : \: \nicefrac{1}{7}"],
                [r"18 \! : \: \nicefrac{1}{120}", r"6 \! : \: \nicefrac{1}{7}"],
                [r"18 \! : \: \nicefrac{1}{120}", r"7 \! : \: \nicefrac{1}{7}"],
                [r"18 \! : \: \nicefrac{1}{120}", r"8 \! : \: \nicefrac{1}{7}"],
                [r"18 \! : \: \nicefrac{1}{120}", r"9 \! : \: \nicefrac{1}{7}"],
                [r"18 \! : \: \nicefrac{1}{120}", r"10 \! : \: \nicefrac{1}{7}"],
                [r"18 \! : \: \nicefrac{1}{120}", r"11 \! : \: \nicefrac{1}{7}"],
                [r"20 \! : \: \nicefrac{1}{120}", r"5 \! : \: \nicefrac{1}{7}"],
                [r"20 \! : \: \nicefrac{1}{120}", r"6 \! : \: \nicefrac{1}{7}"],
                [r"20 \! : \: \nicefrac{1}{120}", r"7 \! : \: \nicefrac{1}{7}"],
                [r"20 \! : \: \nicefrac{1}{120}", r"8 \! : \: \nicefrac{1}{7}"],
                [r"20 \! : \: \nicefrac{1}{120}", r"9 \! : \: \nicefrac{1}{7}"],
                [r"20 \! : \: \nicefrac{1}{120}", r"10 \! : \: \nicefrac{1}{7}"],
                [r"20 \! : \: \nicefrac{1}{120}", r"11 \! : \: \nicefrac{1}{7}"],
                [r"22 \! : \: \nicefrac{1}{120}", r"5 \! : \: \nicefrac{1}{8}"],
                [r"22 \! : \: \nicefrac{1}{120}", r"6 \! : \: \nicefrac{1}{8}"],
                [r"22 \! : \: \nicefrac{1}{120}", r"7 \! : \: \nicefrac{1}{8}"],
                [r"22 \! : \: \nicefrac{1}{120}", r"8 \! : \: \nicefrac{1}{8}"],
                [r"22 \! : \: \nicefrac{1}{120}", r"9 \! : \: \nicefrac{1}{8}"],
                [r"22 \! : \: \nicefrac{1}{120}", r"10 \! : \: \nicefrac{1}{8}"],
                [r"22 \! : \: \nicefrac{1}{120}", r"11 \! : \: \nicefrac{1}{8}"],
                [r"22 \! : \: \nicefrac{1}{120}", r"12 \! : \: \nicefrac{1}{8}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"5 \! : \: \nicefrac{1}{9}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"6 \! : \: \nicefrac{1}{9}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"7 \! : \: \nicefrac{1}{9}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"8 \! : \: \nicefrac{1}{9}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"9 \! : \: \nicefrac{1}{9}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"10 \! : \: \nicefrac{1}{9}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"11 \! : \: \nicefrac{1}{9}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"12 \! : \: \nicefrac{1}{9}"],
                [r"24 \! : \: \nicefrac{1}{120}", r"13 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"5 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"6 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"7 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"8 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"9 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"10 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"11 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"12 \! : \: \nicefrac{1}{9}"],
                [r"26 \! : \: \nicefrac{1}{120}", r"13 \! : \: \nicefrac{1}{9}"]],
                include_outer_lines = True,
                element_to_mobject=lambda e: MathTex(e, tex_template=myTemplate)
            ).scale(0.9).to_edge(UP, buff = 0.2)
        
        t4.get_entries((1,1)).set_color(trunk_height_colour)
        t4.get_entries((1,2)).set_color(hat_height_colour)
        
        self.play(t4.create(), run_time=speed*8)
        self.wait()

        self.play(t4.animate.to_edge(DOWN, buff = 0.2), rate_func=rate_functions.ease_in_out_cubic, run_time = speed*13.5)
        self.wait()

# code to generate the above table (executed in a separate file)
# def num_hat_heights(trunk_height):
#     if trunk_height in [4, 5]:
#         return 1
#     elif trunk_height == 6:
#         return 2
#     else:
#         return (trunk_height//3 + 1)

# with open("output.txt", "w") as file:
#     for T in list(range(4, 15)) + [16, 18, 20, 22, 24, 26]:
#         N = num_hat_heights(T)
#         for H in range(N):
#             Ph6 = 1
#             Pt = (
#                 1 if T > 13 else
#                 12 if T in [8, 10, 12] else
#                 11
#             )
#             # probability of hat height (Ph)
#             Ph = (
#                 1 if T in [4, 5] else
#                 N
#             )
#             if T == 6 and H > 1:
#                 Ph6 = 2
#             line =  "[r\"" + str(T) + " \\! : \\: \\nicefrac{" + str(Pt) + "}{120}\", r\"" + str(H + 5) + " \\! : \\: \\nicefrac{" + str(Ph6) + "}{" + str(Ph) + "}\"],"
            
#             file.write("".join(line) + "\n")
