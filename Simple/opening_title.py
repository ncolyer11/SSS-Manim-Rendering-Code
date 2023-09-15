# desc: opening title for the sss

from manim import*
from colours import*

class title(Scene):
    def construct(self):
        self.wait(0.2)
        txt = Tex(
            r"Self(sustaining)\\Stem \& Shroomlight\textsuperscript{Farm}"
        )

        txt.set_color_by_gradient("#166be0", "#ed2828", "#ed6f0e")
        txt.font_size = 100

        self.play(DrawBorderThenFill(txt), run_time = 6.2)
        self.wait(0.5)