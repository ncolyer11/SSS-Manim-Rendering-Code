# desc: 39,168 bonemeal/h to keep the farm self-sufficient, we will need to farm at least 315,694 (8.06*39,168)

from FaR import search_shapes_in_text
from manim import*
from colours import*

speed = 1
# speed = 1.0/2.5

class smp_shot_3(Scene):
    def construct(self):
        self.wait(0.2)
        # self.camera.background_color = bg_colour

        wb_for_growing_fungus_formula =Tex(r"\textbf{Wart Blocks Needed to Compost:}",
                                           r"\\wb/h = bm/h $\cdot$ wb/bm")

        self.play(Write(wb_for_growing_fungus_formula), run_time=1*speed)
        
        for group in search_shapes_in_text(wb_for_growing_fungus_formula, [Tex(r"bm/h")], index=1):
            self.play(*[
                wb_for_growing_fungus_formula[1][group].animate.set_color(PURPLE_A)
            ], run_time=0.5*speed) 
        for group in search_shapes_in_text(wb_for_growing_fungus_formula, [Tex(r"wb/h")], index=1):
            self.play(*[
                wb_for_growing_fungus_formula[1][group].animate.set_color(warped_wart_colour_b)
            ], run_time=0.5*speed) 
        self.wait(speed)

        wb_for_growing_fungus =Tex(r"\textbf{Wart Blocks Needed to Compost:}",
                                   r"\\315700 wb/h = 39170 bm/h $\cdot$ 8.06 wb/bm")
        for group in search_shapes_in_text(wb_for_growing_fungus, [Tex(r"39170 bm/h")], index=1):
            wb_for_growing_fungus[1][group].set_color(PURPLE_A)
        for group in search_shapes_in_text(wb_for_growing_fungus, [Tex(r"315700 wb/h")], index=1):
            wb_for_growing_fungus[1][group].set_color(warped_wart_colour_b)

        self.play(TransformMatchingShapes(wb_for_growing_fungus_formula[0] , wb_for_growing_fungus[0]), TransformMatchingShapes(wb_for_growing_fungus_formula[1],wb_for_growing_fungus[1]), run_time=1*speed)
        self.wait(speed)

        wb_for_growing_fungus_figure =Tex(r"\textbf{Wart Blocks Needed to Compost:}",
                                          r"\\315700 wb/h")
        for group in search_shapes_in_text(wb_for_growing_fungus_figure, [Tex(r"315700 wb/h")], index=1):
            wb_for_growing_fungus_figure[1][group].set_color(warped_wart_colour_b)

        self.play(TransformMatchingShapes(wb_for_growing_fungus[0], wb_for_growing_fungus_figure[0]), TransformMatchingShapes(wb_for_growing_fungus[1], wb_for_growing_fungus_figure[1]), run_time=1*speed)
        self.wait(speed)

        self.play(Unwrite(wb_for_growing_fungus_figure), run_time=1*speed)
        self.wait(0.5*speed)
