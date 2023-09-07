# desc: increments through every block in its volume and evaluates the shroomlight 
# and wart block generation chance given the region that block is situated in and 
# multiplies it by the chance of the bounding box generating

from FaR import search_shapes_in_text
from manim import*
from colours import*

speed = 1
# speed = 1.0/3.0

class smp_shot_14(Scene):
    def construct(self):
        self.wait(0.2)

        block_gen_chance_formula = Tex(
                                    r"\textbf{Single Block Type Generation Chance:}\\",
                                    r"P(($x,y,z$) = type) =\\"
                                ).shift(UP * 0.75)
        block_gen_chance_sum = MathTex(
                                r"\sum_{k=1}^{332} \text{Region(LVS$_k$, $x$, $y$, $z$, type)$^*$} \cdot \text{P(}",
                                r"\text{LVS}_k",
                                r")"
                            ).next_to(block_gen_chance_formula, DOWN, buff = 0.075)
        
        block_formula = VGroup(block_gen_chance_formula, block_gen_chance_sum)
        self.play(Write(block_formula), run_time=4*speed)
        
        # top formula
        for group in search_shapes_in_text(block_gen_chance_formula, [Tex(r"$x,y,z$")], index=1):
            self.play(*[
                block_gen_chance_formula[1][group].animate.set_color(x_y_z_coord_colour)
            ], run_time=0.5*speed)
        
        for group in search_shapes_in_text(block_gen_chance_formula, [Tex(r"type")], index=1):
            self.play(*[
                block_gen_chance_formula[1][group].animate.set_color(shroomlight_colour)
            ], run_time=0.5*speed)

        # bottom sum
        for group in search_shapes_in_text(block_gen_chance_sum, [Tex(r"LVS$_k$")]):
            self.play(*[
                block_gen_chance_sum[0][group].animate.set_color(lvs_colour)
            ], run_time=0.5*speed)
        
        for group in search_shapes_in_text(block_gen_chance_sum, [Tex(r"$x$, $y$, $z$")]):
            self.play(*[
                block_gen_chance_sum[0][group].animate.set_color(x_y_z_coord_colour)
            ], run_time=0.5*speed)
        
        for group in search_shapes_in_text(block_gen_chance_sum, [Tex(r"type")]):
            self.play(*[
                block_gen_chance_sum[0][group].animate.set_color(shroomlight_colour)
            ], run_time=0.5*speed)
        self.play(block_gen_chance_sum[1].animate.set_color(lvs_colour), run_time=0.5*speed)

        region_func_note = Tex(r"*where the function Region() returns the probability \\ of block `type' being found at offset `(x,y,z)' \\ from the grown fungi for `LVS$_k$'").scale(0.5).next_to(block_gen_chance_sum, DOWN, buff = 0.1)

        self.wait()

        self.play(Write(region_func_note), run_time=speed*1)
        block_formula.add(region_func_note)
        self.wait()

        # example showing the most likely place to find shroomlights
        block_gen_chance_formula_eg = Tex(
                                    r"\textbf{Most Common Shroomlight Example:}\\",
                                    r"P((1,8,1) = shroom) =\\"
                                ).shift(UP * 0.75)
        block_gen_chance_sum_eg = MathTex(
                        r"\sum_{k=1}^{332} \text{Region(LVS$_k$, 1, 8, 1, shroom)} \cdot \text{P(}",
                        r"\text{LVS}_k",
                        r") = ",
                        r"2.925\%"
                        ).next_to(block_gen_chance_formula_eg, DOWN, buff = 0.075)

        block_formula_eg = VGroup(block_gen_chance_formula_eg, block_gen_chance_sum_eg)

        # top formula
        for group in search_shapes_in_text(block_gen_chance_formula_eg, [Tex(r"1,8,1")], index=1):
            block_gen_chance_formula_eg[1][group].set_color(x_y_z_coord_colour)
        
        for group in search_shapes_in_text(block_gen_chance_formula_eg, [Tex(r"shroom")], index=1):
                block_gen_chance_formula_eg[1][group].set_color(shroomlight_colour)

        # bottom sum
        for group in search_shapes_in_text(block_gen_chance_sum_eg, [Tex(r"LVS$_k$")]):
            block_gen_chance_sum_eg[0][group].set_color(lvs_colour)
        
        for group in search_shapes_in_text(block_gen_chance_sum_eg, [Tex(r"1, 8, 1")]):
            block_gen_chance_sum_eg[0][group].set_color(x_y_z_coord_colour)
        
        for group in search_shapes_in_text(block_gen_chance_sum_eg, [Tex(r"shroom")]):
            block_gen_chance_sum_eg[0][group].set_color(shroomlight_colour)

        block_gen_chance_sum_eg[1].set_color(lvs_colour)

        self.play(TransformMatchingShapes(block_formula, block_formula_eg), run_time=speed*2)
        self.wait()

        self.play(Indicate(block_gen_chance_sum_eg[3]))
        self.wait()

        self.play(Unwrite(block_formula_eg), run_time=1.5*speed)
        self.wait()
