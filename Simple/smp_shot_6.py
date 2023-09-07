# desc: we need to multiply the chance of the trunk height by the chance of the layer value set

from FaR import search_shapes_in_text
from manim import*
from colours import*

speed = 1
# speed = 1.0/4

class smp_shot_6(Scene):
    def construct(self):
        self.wait(0.2)

        bounding_box_formula = Tex(
                            r"\textbf{Bounding Box Chance:}\\",
                            r"P(Bounding Box) = P(Trunk Height) $\cdot$ P({LVS})"
                        )
        
        self.play(Write(bounding_box_formula), run_time=2*speed)

        self.wait()

        for group in search_shapes_in_text(bounding_box_formula, [Tex(r"Bounding Box")], index=1):
            self.play(*[
                bounding_box_formula[1][group].animate.set_color(bounding_box_colour)
            ], run_time=0.3*speed) 
        self.wait(0.5*speed)

        for group in search_shapes_in_text(bounding_box_formula, [Tex(r"Trunk Height")], index=1):
            self.play(*[
                bounding_box_formula[1][group].animate.set_color(trunk_height_colour)
            ], run_time=0.3*speed) 
        self.wait(0.5*speed)

        for group in search_shapes_in_text(bounding_box_formula, [Tex(r"LVS")], index=1):
            self.play(*[
                bounding_box_formula[1][group].animate.set_color(lvs_colour)
            ], run_time=0.3*speed) 

        self.wait()

        trunk_height_formula = Tex(
                            r"\textbf{Trunk Height Formula:}\\",
                            r"T$_h$ = random.int(4, 13)"
                        ).shift(UP * 0.54)
        
        for group in search_shapes_in_text(trunk_height_formula, [Tex(r"T$_h$")], index=1):
                trunk_height_formula[1][group].set_color(trunk_height_colour)
        self.wait(0.5*speed)

        for group in search_shapes_in_text(trunk_height_formula, [Tex(r"random.int")], index=1):
                trunk_height_formula[1][group].set_color(random_colour)
        self.wait(0.5*speed)

        self.play(TransformMatchingShapes(bounding_box_formula, trunk_height_formula), run_time=1*speed) 
        self.wait()

        trunk_height_double_formula = Tex(
                            r"\textbf{Trunk Height Formula:}\\",
                            r"T$_h$ = rand.int(4, 13)\\",
                            r"\textbf{if} rand(0, 1) $< \frac{1}{12}$:\\",
                            r"T$_h$ = 2 $\cdot$ T$_h$"
                        )
        
        for i in [1,2,3]:
            for group in search_shapes_in_text(trunk_height_double_formula, [Tex(r"T$_h$")], index=i):
                    trunk_height_double_formula[i][group].set_color(trunk_height_colour)

        for i in [1,2,3]:
            for group in search_shapes_in_text(trunk_height_double_formula, [Tex(r"rand.int"), Tex(r"rand")], index=i):
                    trunk_height_double_formula[i][group].set_color(random_colour)
        self.wait(0.5*speed)

        self.play(TransformMatchingShapes(trunk_height_formula, trunk_height_double_formula), run_time=1*speed) 
        self.wait()

