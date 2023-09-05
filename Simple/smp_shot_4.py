# desc: 39,168 bonemeal/h to keep the farm self-sufficient, we will need to farm at least 315,694 (8.06*39,168)

from FaR import search_shapes_in_text
from manim import*
from colours import*

speed = 1
# speed = 1.0/3.0

class smp_shot_4(Scene):
    def construct(self):
        self.wait(0.2)
        # self.camera.background_color = bg_colour

        bm_for_producing_fungus_formula = Tex(r"\textbf{Bonemeal used to Produce Fungus:}",
                                             r"\\bm/h = Fungus/h $\cdot$ max(bm/Fungus$_{\text{prod}}$)")

        self.play(Write(bm_for_producing_fungus_formula), run_time=1*speed)
        
        for group in search_shapes_in_text(bm_for_producing_fungus_formula, [Tex(r"bm/h")], index=1):
            self.play(*[
                bm_for_producing_fungus_formula[1][group].animate.set_color(PURPLE_A)
            ], run_time=0.5*speed) 
        for group in search_shapes_in_text(bm_for_producing_fungus_formula, [Tex(r"Fungus/h")], index=1):
            self.play(*[
                bm_for_producing_fungus_formula[1][group].animate.set_color(green2)
            ], run_time=0.5*speed) 
        self.wait(speed)

        bm_for_producing_fungus = Tex(r"\textbf{Bonemeal used to Produce Fungus:}",
                                     r"\\7050 bm/h = 15667 Fungus/h $\cdot$ 0.45 bm/Fungus$_{\text{prod}}$")
        
        for group in search_shapes_in_text(bm_for_producing_fungus, [Tex(r"7050 bm/h")], index=1):
            bm_for_producing_fungus[1][group].set_color(PURPLE_A)
        for group in search_shapes_in_text(bm_for_producing_fungus, [Tex(r"15667 Fungus/h")], index=1):
            bm_for_producing_fungus[1][group].set_color(green2)

        self.play(TransformMatchingShapes(bm_for_producing_fungus_formula[0], bm_for_producing_fungus[0]), 
                  TransformMatchingShapes(bm_for_producing_fungus_formula[1], bm_for_producing_fungus[1]), run_time=speed)
        self.wait(speed)

        bm_for_producing_fungus_figure = Tex(r"\textbf{Bonemeal used to Produce Fungus:}",
                                            r"\\7050 bm/h")
        
        for group in search_shapes_in_text(bm_for_producing_fungus_figure, [Tex(r"7050 bm/h")], index=1):
            bm_for_producing_fungus_figure[1][group].set_color(PURPLE_A)

        self.play(TransformMatchingShapes(bm_for_producing_fungus[0], bm_for_producing_fungus_figure[0]), 
                  TransformMatchingShapes(bm_for_producing_fungus[1], bm_for_producing_fungus_figure[1]), run_time=speed)
        self.wait(speed)

        wb_for_producing_fungus = Tex(r"\textbf{Extra Wart Blocks Needed to Compost:}",
                                     r"\\wb/h = 7050 bm/h $\cdot$ 8.06 bm/wb")
        for group in search_shapes_in_text(wb_for_producing_fungus, [Tex(r"wb/h")], index=1):
            wb_for_producing_fungus[1][group].set_color(warped_wart_colour_b)
        for group in search_shapes_in_text(wb_for_producing_fungus, [Tex(r"7050 bm/h")], index=1):
            wb_for_producing_fungus[1][group].set_color(PURPLE_A)

        self.play(TransformMatchingShapes(bm_for_producing_fungus_figure[0], wb_for_producing_fungus[0]), 
                  TransformMatchingShapes(bm_for_producing_fungus_figure[1], wb_for_producing_fungus[1]), run_time=speed)
        self.wait(speed)

        wb_for_producing_fungus_figure = Tex(r"\textbf{Extra Wart Blocks Needed to Compost:}",
                                            r"\\56820 wb/h")
        for group in search_shapes_in_text(wb_for_producing_fungus_figure, [Tex(r"56820 wb/h")], index=1):
            wb_for_producing_fungus_figure[1][group].set_color(warped_wart_colour_b)

        self.play(TransformMatchingShapes(wb_for_producing_fungus[0], wb_for_producing_fungus_figure[0]), 
                  TransformMatchingShapes(wb_for_producing_fungus[1], wb_for_producing_fungus_figure[1]), run_time=speed)
        self.wait(speed)

        wb_total_formula = Tex(r"\textbf{Total Wart Blocks Needed to Compost:}",
                      r"\\wb/h$_{\text{total}}$ = wb/h$_{\text{grow}}$ + wb/h$_{\text{prod}}$")
        for group in search_shapes_in_text(wb_total_formula, [Tex(r"wb/h$_{\text{total}}$"), Tex(r"wb/h$_{\text{grow}}$"), Tex(r"wb/h$_{\text{prod}}$")], index=1):
            wb_total_formula[1][group].set_color(warped_wart_colour_b)
        self.wait(speed)

        self.play(TransformMatchingShapes(wb_for_producing_fungus_figure[0], wb_total_formula[0]), 
                  TransformMatchingShapes(wb_for_producing_fungus_figure[1], wb_total_formula[1]), run_time=speed)
        self.wait(speed)

        wb_total = Tex(r"\textbf{Total Wart Blocks Needed to Compost:}",
                              r"\\372520 wb/h = 315700 wb/h + 56820 wb/h")
        for group in search_shapes_in_text(wb_total, [Tex(r"372520 wb/h"), Tex(r"315700 wb/h"), Tex(r"56820 wb/h")], index=1):
            wb_total[1][group].set_color(warped_wart_colour_b)

        self.play(TransformMatchingShapes(wb_total_formula[0], wb_total[0]), 
                  TransformMatchingShapes(wb_total_formula[1], wb_total[1]), run_time=speed)
        self.wait(speed)

        wb_total_figure = Tex(r"\textbf{Total Wart Blocks Needed to Compost:}",
                              r"\\372520 wb/h or $\frac{372520}{15667}$ = 23.77 wb/Fungus")
        for group in search_shapes_in_text(wb_total_figure, [Tex(r"372520 wb/h"), Tex(r"23.77 wb/Fungus")], index=1):
            wb_total_figure[1][group].set_color(warped_wart_colour_b)

        self.play(TransformMatchingShapes(wb_total[0], wb_total_figure[0]), 
                  TransformMatchingShapes(wb_total[1], wb_total_figure[1]), run_time=speed)

        self.wait(speed)
        for group in search_shapes_in_text(wb_total_figure, [Tex(r"372520 wb/h"), Tex(r"23.77 wb/Fungus")], index=1):
            self.play(Indicate(wb_total_figure[1][group]), run_time=0.75*speed)
        self.wait(speed)

        self.play(Unwrite(wb_total_figure), run_time=speed)
        self.wait(speed)
