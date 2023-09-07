# desc: plugged into the equation for N, it yields 3 hat heights: 5,6,7

from FaR import search_shapes_in_text
from manim import*
from colours import*

speed = 1
# speed = 1.0/3.0

class smp_shot_12(Scene):
    def construct(self):
        self.wait(0.2)

        hat_height_quantity_formula = Tex(r"N(T$_h$)} = $\lfloor \frac{\text{T}_h}{3} \rfloor$ + 1")
        self.play(Write(hat_height_quantity_formula), run_time=1.5*speed)
        self.wait()

        for group in search_shapes_in_text(hat_height_quantity_formula, [Tex(r"T$_h$"), Tex(r"$_{\text{T}_h}$")]):
            self.play(*[
                hat_height_quantity_formula[0][group].animate.set_color(trunk_height_colour)
            ], run_time=0.5*speed)
        self.wait()

        hat_height_quantity_formula_subbed = Tex(r"N(6)} = $\lfloor \frac{6}{3} \rfloor$ + 1")
        for group in search_shapes_in_text(hat_height_quantity_formula_subbed, [Tex(r"6")]):
                hat_height_quantity_formula_subbed[0][group].set_color(trunk_height_colour)
        hat_height_quantity_formula_subbed[0][6].set_color(trunk_height_colour)

        self.play(ReplacementTransform(hat_height_quantity_formula, hat_height_quantity_formula_subbed), run_time=speed*1)
        self.wait()

        hat_height_quantity_formula_subbed_simplified = Tex(r"N(6)} = 3")
        for group in search_shapes_in_text(hat_height_quantity_formula_subbed_simplified, [Tex(r"6")]):
                hat_height_quantity_formula_subbed_simplified[0][group].set_color(trunk_height_colour)
        hat_height_note = Tex(r"(i.e. 3 hat heights starting from 5)").scale(0.5).next_to(hat_height_quantity_formula_subbed_simplified, DOWN, buff=0.075)

        self.play(
            ReplacementTransform(hat_height_quantity_formula_subbed, hat_height_quantity_formula_subbed_simplified),
            Write(hat_height_note),
        run_time=speed*1)
        self.wait()

        hat_heights_example_6 = Tex(r"$\implies\!$H$_6$ = \{5, 6, 7\}").next_to(hat_height_note, DOWN, buff=0.125)
        hat_heights_example_6[0][2].set_color(hat_height_colour)
        hat_heights_example_6[0][3].set_color(hat_height_colour)
        self.play(Write(hat_heights_example_6), run_time=speed*1)
        self.wait()

        hat_heights_example_6_correct = Tex(r"$\implies\!$H$_6$ = \{5, 6, 6\}").next_to(hat_height_note, DOWN, buff=0.125)
        hat_heights_example_6_correct[0][2].set_color(hat_height_colour)
        hat_heights_example_6_correct[0][3].set_color(hat_height_colour)
        hat_heights_example_6_note = Tex(r"as min(7, 6) = 6").scale(0.5).next_to(hat_heights_example_6_correct, RIGHT, buff=0.15)
        hat_heights_example_6_note[0][6].set_color(random_colour)
        hat_heights_example_6_note[0][8].set_color(trunk_height_colour)
        hat_heights_example_6_note[0][11].set_color(hat_height_colour)
        self.play(
            ReplacementTransform(hat_heights_example_6, hat_heights_example_6_correct),
            Write(hat_heights_example_6_note),
        run_time=speed*1)
        self.wait()

        self.play(
            Unwrite(hat_height_quantity_formula_subbed_simplified), 
            Unwrite(hat_heights_example_6), 
            Unwrite(hat_height_note), 
            Unwrite(hat_heights_example_6_correct), 
            Unwrite(hat_heights_example_6_note), 
        run_time=speed*1)
        self.wait()
