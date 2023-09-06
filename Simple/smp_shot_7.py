# desc: using the equation that determines the radius of a layer (if layer < trunkHeight - randint(0,2): radius = 2, else radius = 1)

from FaR import search_shapes_in_text
from manim import*
from colours import*

speed = 1
# speed = 1.0/5

class smp_shot_7(Scene):
    def construct(self):
        self.wait(0.2)

        radius_formula = MathTex(
            r"\textbf{Layer Radius Formula:} \qquad\qquad\, \\",
            r"\text{radius} = \begin{cases} \, 2, &\text{  if rand.int}(0, 2) < \text{T}_h - \text{ layer} \\ \, 1, &\text{  else} \end{cases}"
        )

        self.play(Write(radius_formula), run_time=2*speed)
        self.wait()
        
        for group in search_shapes_in_text(radius_formula, [Tex(r"radius")], index = 1):
            self.play(*[
                radius_formula[1][group].animate.set_color(radius_colour)
            ], run_time=0.3*speed) 
        self.wait(0.5*speed)
        
        for group in search_shapes_in_text(radius_formula, [Tex(r"rand.int")], index = 1):
            self.play(*[
                radius_formula[1][group].animate.set_color(random_colour)
            ], run_time=0.3*speed) 
        self.wait(0.5*speed)
        
        for group in search_shapes_in_text(radius_formula, [MathTex(r"\text{T}_h")], index = 1):
            self.play(*[
                radius_formula[1][group].animate.set_color(trunk_height_colour)
            ], run_time=0.3*speed) 
        self.wait(0.5*speed)
        
        for group in search_shapes_in_text(radius_formula, [Tex(r"layer")], index = 1):
            self.play(*[
                radius_formula[1][group].animate.set_color(layer_colour)
            ], run_time=0.3*speed) 
        self.wait(0.5*speed)

        radius_formula_abstracted = MathTex(
            r"\textbf{Layer Radius Formula:} \qquad\qquad\;\; \\",
            r"\text{radius} = \begin{cases} \, 2, &\text{  if rand.int}(0, 2) < \text{height to top} \\ \, 1, &\text{  else} \end{cases}"
        ).shift(RIGHT * 0.01)
        
        for group in search_shapes_in_text(radius_formula_abstracted, [Tex(r"radius")], index = 1):
            radius_formula_abstracted[1][group].set_color(radius_colour)
        self.wait(0.5*speed)
        
        for group in search_shapes_in_text(radius_formula_abstracted, [Tex(r"rand.int")], index = 1):
            radius_formula_abstracted[1][group].set_color(random_colour)
        self.wait(0.5*speed)

        self.play(TransformMatchingShapes(radius_formula, radius_formula_abstracted), run_time=1*speed) 
        self.wait()