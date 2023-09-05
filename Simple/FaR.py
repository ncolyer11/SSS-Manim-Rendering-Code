# A livesaving 'find and replace' function written by Abul4fia with some bug testing
# done by ncolyer

from manim import*
# example:
"""
for group in search_shapes_in_text(compliment_formula, [MathTex(r"\text{Growth Chance}")], index=3):
    self.play(*[
        compliment_formula[3][group].animate.set_color(warped_stem_colour)
    ], run_time=1*speed) 
"""

def search_shape_in_text(text, shape, index=0):
    def get_mobject_key(mobject: Mobject) -> int:
        mobject.save_state()
        mobject.center()
        mobject.height=1
        result = hash(np.array2string(mobject.points, precision=4, separator=', ', suppress_small=True))
        mobject.restore()
        return result
    results = []
    l = len(shape.submobjects[0])
    shape_aux = VMobject()
    shape_aux.points = np.concatenate([p.points for p in shape.submobjects[0]])
    for i in range(len(text.submobjects[index])):
        subtext = VMobject()
        subtext.points = np.concatenate([p.points for p in text.submobjects[index][i:i+l]])
        # shape.move_to(subtext.get_center())
        if get_mobject_key(subtext) == get_mobject_key(shape_aux):
            results.append(slice(i, i+l))
    return results

def search_shapes_in_text(text, shapes, index=0):
    results = []
    for shape in shapes:
        results += search_shape_in_text(text, shape, index)
    return results
