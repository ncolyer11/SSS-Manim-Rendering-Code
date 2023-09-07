# desc: which can be calculated with the equation P = 1/N
# where N = T divided by 3 rounded down (floor(T/3))

from FaR import search_shapes_in_text
from manim import*
from colours import*

speed = 1
speed = 1.0/3.0

class smp_shot_11(Scene):
    def construct(self):
        self.wait(0.2)

        hat_height_distribution_formula = Tex(
                                            r"\textbf{Hat Height Distribution Formula:\\}",
                                            r"P(H$_h$(T$_h$)) = $\frac{1}{\text{N(T$_h$)}}$, where T$_h$ $>$ 6\\",
                                            r"for N(T$_h$)} = $\lfloor \frac{\text{T}_h}{3} \rfloor$ + 1",
                                        )

        self.play(Write(hat_height_distribution_formula), run_time=4*speed)
        
        for group in search_shapes_in_text(hat_height_distribution_formula, [Tex(r"H$_h$")], index=1):
            self.play(*[
                hat_height_distribution_formula[1][group].animate.set_color(hat_height_colour)
            ], run_time=0.5*speed)

        for group in search_shapes_in_text(hat_height_distribution_formula, [Tex(r"T$_h$")], index=1):
            self.play(*[
                hat_height_distribution_formula[1][group].animate.set_color(trunk_height_colour)
            ], run_time=0.5*speed)
            break
        for group in search_shapes_in_text(hat_height_distribution_formula, [Tex(r"$_{\text{T}_h}$")], index=1):
            self.play(*[
                hat_height_distribution_formula[1][group].animate.set_color(trunk_height_colour)
            ], run_time=0.5*speed)
        skip = 0
        for i in [1,2]:
            for group in search_shapes_in_text(hat_height_distribution_formula, [Tex(r"T$_h$"), Tex(r"$_{\text{T}_h}$")], index=i):
                if skip == 0:
                    skip += 1
                    continue
                self.play(*[
                    hat_height_distribution_formula[i][group].animate.set_color(trunk_height_colour)
                ], run_time=0.5*speed)

        self.wait(3*speed)

        self.play(Unwrite(hat_height_distribution_formula), run_time=4*speed)
        self.wait(speed)
