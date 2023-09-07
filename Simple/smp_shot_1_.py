# desc:  87% chance of it growing after 4 attempts from 4 dispensers as calculated by this formula

from FaR import search_shapes_in_text
from manim import*
from colours import*

speed = 1
# speed = 1.0/2.5

class smp_shot_1(Scene):
    def construct(self):
        self.wait(0.2)
        # self.camera.background_color = bg_colour

        fourty_percent = MathTex(r"40\%").scale(4)
        zero_point_four = MathTex(r"0.4").scale(4)
        self.play(Write(fourty_percent, run_time = 0.85*speed))
        
        self.wait()
        self.play(CounterclockwiseTransform(fourty_percent, zero_point_four), run_time=1*speed)

        compliment_formula = MathTex(r"&\text{\textbf{Compliment Formula:}} \\ &1-(1-",
                                         r"0.4",
                                         r")^{\text{Dispensers}}=\text{Total Growth Chance}")
        self.wait()
        self.remove(fourty_percent)
        self.play(TransformMatchingTex(zero_point_four,compliment_formula), run_time=1*speed)

        for group in search_shapes_in_text(compliment_formula, [MathTex(r"\text{Total Growth Chance}")], index=2):
            self.play(*[
                compliment_formula[2][group].animate.set_color(warped_stem_colour)
            ], run_time=1*speed) 

        fungus_growth_equation = MathTex(r"\text{\textbf{Fungus Growth }}&\text{\textbf{Chance per Cycle:}} \\ 1-0.6^4&=87.04\%")

        for group in search_shapes_in_text(fungus_growth_equation, [MathTex(r"87.04\%")]):
            fungus_growth_equation[0][group].set_color(warped_stem_colour)
        self.wait()
        self.play(TransformMatchingShapes(compliment_formula, fungus_growth_equation), run_time=1*speed) 

        self.wait()
        for group in search_shapes_in_text(fungus_growth_equation, [MathTex(r"87.04\%")]):
            self.play(ApplyWave(fungus_growth_equation[0][group]), run_time=1*speed)

# transition to dispenser bonemeals/h
        cycles_an_hour_formula = MathTex(r"\text{\textbf{Finding Fung}}&\text{\textbf{us Grown/h:}} \\ \text{Dispenser Cycles/h } = &\text{ Cycles/s} \cdot \text{Seconds/h}")

        self.wait()
        self.play(TransformMatchingShapes(fungus_growth_equation, cycles_an_hour_formula), run_time=1*speed) 

        for group in search_shapes_in_text(cycles_an_hour_formula, [MathTex(r"\text{Dispenser Cycles/h}")]):
            self.play(*[
                cycles_an_hour_formula[0][group].animate.set_color(YELLOW_D)
            ], run_time=1*speed) 

        cycles_an_hour = MathTex(r"\text{\textbf{Finding Fungus}}\text{\textbf{ Gr}}&\text{\textbf{own/h:}} \\ \;18000/ \text{h}=\; \frac{\text{20gt}}{\text{4gt}} \cdot 3&600\text{/h}")
        for group in search_shapes_in_text(cycles_an_hour, [MathTex(r"18000/ \text{h}")]):
            cycles_an_hour[0][group].set_color(YELLOW_D)

        self.wait()
        self.play(TransformMatchingShapes(cycles_an_hour_formula, cycles_an_hour), run_time=1*speed) 

        fungi_an_hour = MathTex(r"\text{\textbf{Finding }}\text{\textbf{Fung}}&\text{\textbf{us Grown/h:}} \\ 15667 \text{ Fungi/h }=&\;18000/ \text{h} \cdot 0.8704")
        for group in search_shapes_in_text(fungi_an_hour, [MathTex(r"0.8704")]):
            fungi_an_hour[0][group].set_color(warped_stem_colour)
        self.wait()
        for group in search_shapes_in_text(fungi_an_hour, [MathTex(r"18000/ \text{h}")]):
            fungi_an_hour[0][group].set_color(YELLOW_D)

        self.wait()
        self.play(TransformMatchingShapes(cycles_an_hour, fungi_an_hour), run_time=1*speed)

        fungi_an_hour_result = MathTex(r"\text{\textbf{Finding }}\text{\textbf{Fu}}&\text{\textbf{ngus Grown/h:}} \\ 15667 &\text{ Fungi/h}")
        for group in search_shapes_in_text(fungi_an_hour_result, [MathTex(r"15667 \text{ Fungi/h}")]):
            fungi_an_hour_result[0][group].set_color(green2)
            
        self.wait()
        self.play(TransformMatchingShapes(fungi_an_hour, fungi_an_hour_result), run_time=1*speed)

# or more generally
        general_fungus_per_hour_formula = MathTex(r"\text{\textbf{General Fungu}}&\text{\textbf{s/h Formula:}} \\ \text{Fungi/h } = \text{ Cycles/h}&\cdot(1-0.6^{\text{Dispensers}})")
        for group in search_shapes_in_text(general_fungus_per_hour_formula, [MathTex(r"\text{Fungi/h }")]):
            general_fungus_per_hour_formula[0][group].set_color(green2)
        for group in search_shapes_in_text(general_fungus_per_hour_formula, [MathTex(r"(1-0.6^{\text{Dispensers}})")]):
            general_fungus_per_hour_formula[0][group].set_color(warped_stem_colour)
        for group in search_shapes_in_text(general_fungus_per_hour_formula, [MathTex(r"\text{ Cycles/h}")]):
            general_fungus_per_hour_formula[0][group].set_color(YELLOW_D)

        self.wait()
        self.play(TransformMatchingShapes(fungi_an_hour_result, general_fungus_per_hour_formula), run_time=1*speed)

        self.wait()
