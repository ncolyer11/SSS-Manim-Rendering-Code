from manim import *
import colours as col

BUFF = 0.15
ARROW_THICKNESS = 2.5

class CraftingProcess(Scene):
    def construct(self):
        # Initial Step: 7 Stems
        stems = Text("7 Stems", color=col.warped_stem_colour, font_size=32).shift(6 * LEFT + UP)
        self.wait(0.5)
        self.play(Write(stems))

        # Arrow and 28 Planks
        arrow1 = Arrow(stems.get_right(), stems.get_right() + RIGHT, stroke_width=ARROW_THICKNESS)
        planks = Text("28 Planks", color=col.warped_stem_colour_b, font_size=32).next_to(arrow1, RIGHT)
        self.wait(0.5)
        self.play(AnimationGroup(GrowArrow(arrow1), Write(planks), lag_ratio=0.5))

        # Arrow and 56 Sticks
        arrow2 = Arrow(planks.get_right(), planks.get_right() + RIGHT, stroke_width=ARROW_THICKNESS)
        sticks = Text("56 Sticks", color=col.crimson_stem_colour, font_size=32).next_to(arrow2, RIGHT)
        self.wait(0.5)
        self.play(AnimationGroup(GrowArrow(arrow2), Write(sticks), lag_ratio=0.5))

        # Branching arrow to "Smelts 28 Items"
        smelts_28 = Text("Smelts 28 Items", font_size=32).shift(2 * DOWN + 2 * LEFT)
        
        arrow_branch1 = Arrow(
            start=sticks.get_edge_center(DOWN),
            end=smelts_28.get_edge_center(UP),
            buff=BUFF,
            stroke_width=ARROW_THICKNESS
        )
        
        self.wait(0.5)
        self.play(AnimationGroup(GrowArrow(arrow_branch1), Write(smelts_28), lag_ratio=0.3))

        # Branching arrow to "24 Ladders"
        ladders = Text("24 Ladders", color=col.shroomlight_colour, font_size=32).shift(0.4 * DOWN + 2.5 * RIGHT)
        
        arrow_branch2 = Arrow(
            start=sticks.get_edge_center(DOWN),
            end=ladders.get_corner(UL),
            buff=BUFF,
            stroke_width=ARROW_THICKNESS
        )

        self.wait(0.5)
        self.play(AnimationGroup(GrowArrow(arrow_branch2), Write(ladders), lag_ratio=0.5))

        # Arrow from 24 Ladders to Smelts 36 Items
        smelts_36 = Text("Smelts 36 Items", font_size=32).shift(2 * DOWN + 3 * RIGHT)
        
        arrow3 = Arrow(
            start=ladders.get_center(),
            end=smelts_36.get_center(),
            buff=0.25,
            stroke_width=ARROW_THICKNESS
        )

        self.wait(0.5)
        self.play(AnimationGroup(GrowArrow(arrow3), Write(smelts_36), lag_ratio=0.5))
        
        self.wait(0.5)
        self.play(Circumscribe(smelts_36, color=col.green2, fade_out=True))

        self.wait(1)
