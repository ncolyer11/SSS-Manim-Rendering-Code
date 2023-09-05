# desc: 2.5 bonemeal to grow (1/0.4=2.5), meaning that 39,170 (15,667*2.5)

from FaR import search_shapes_in_text
from manim import*
from colours import*


speed = 1
# speed = 1.0/2.5

class smp_shot_2(Scene):
    def construct(self):
        self.wait(0.2)
        # self.camera.background_color = bg_colour

        bm_for_growing_fungus_formula =Tex(r"\textbf{Bonemeal used to Grow Fungus:}",
                                           r"\\bm/h = Fungus/h $\cdot$ bm/Fungus")

        self.play(Write(bm_for_growing_fungus_formula), run_time=1*speed)
        
        for group in search_shapes_in_text(bm_for_growing_fungus_formula, [Tex(r"bm/h")], index=1):
            self.play(*[
                bm_for_growing_fungus_formula[1][group].animate.set_color(PURPLE_A)
            ], run_time=0.5*speed) 
        for group in search_shapes_in_text(bm_for_growing_fungus_formula, [Tex(r"Fungus/h")], index=1):
            self.play(*[
                bm_for_growing_fungus_formula[1][group].animate.set_color(green2)
            ], run_time=0.5*speed) 
        self.wait(speed)

        bm_for_growing_fungus =Tex(r"\textbf{Bonemeal used to Grow Fungus:}",
                                   r"\\39170 bm/h = 15667 Fungus/h $\cdot$ 2.5 bm/Fungus")
        for group in search_shapes_in_text(bm_for_growing_fungus, [Tex(r"39170 bm/h")], index=1):
            bm_for_growing_fungus[1][group].set_color(PURPLE_A)
        for group in search_shapes_in_text(bm_for_growing_fungus, [Tex(r"15667 Fungus/h")], index=1):
            bm_for_growing_fungus[1][group].set_color(green2)

        self.play(TransformMatchingShapes(bm_for_growing_fungus_formula[0] , bm_for_growing_fungus[0]), TransformMatchingShapes(bm_for_growing_fungus_formula[1],bm_for_growing_fungus[1]), run_time=1*speed)
        self.wait(speed)

        bm_for_growing_fungus_figure =Tex(r"\textbf{Bonemeal used to Grow Fungus:}",
                                          r"\\39170 bm/h")
        for group in search_shapes_in_text(bm_for_growing_fungus_figure, [Tex(r"39170 bm/h")], index=1):
            bm_for_growing_fungus_figure[1][group].set_color(PURPLE_A)

        self.play(TransformMatchingShapes(bm_for_growing_fungus[0], bm_for_growing_fungus_figure[0]), TransformMatchingShapes(bm_for_growing_fungus[1], bm_for_growing_fungus_figure[1]), run_time=1*speed)
        self.wait(speed)

        self.play(Unwrite(bm_for_growing_fungus_figure), run_time=1*speed)
        self.wait(0.5*speed)
