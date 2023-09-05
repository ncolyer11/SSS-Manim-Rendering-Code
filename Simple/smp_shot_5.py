# desc: scroll through a part of the code used to generate the heatmaps

from manim import*
from colours import*

speed = 1
# speed = 1.0/3.0

class smp_shot_5(Scene):
    def construct(self):
        code = '''
import math
import xlsxwriter

bb = 0
Block = 0
T = list(range(4, 14)) + list(range(14, 27, 2))
outSheet = []
# create file (workbook)
outWorkbook = xlsxwriter.Workbook(r"HeatMapV2.xlsx")

for count1, trunkHeight in enumerate(T):
    if trunkHeight in [4, 5]:
        base = trunkHeight
        offset1 = 1
        H = list(range(base, base + offset1))
    elif trunkHeight == 6:
        H = [5, 6, 6]
    else:
        base = 5
        offset1 = math.floor(1 + trunkHeight / 3)
        H = list(range(base, base + offset1))

    for hatHeight in H:
        # probability of trunk height (Pt)
        Pt = (
            1 / 120 if trunkHeight > 13 else
            12 / 120 if trunkHeight in [8, 10, 12] else
            11 / 120
        )
        # probability of hat height (Ph)
        Ph = (
            1 if trunkHeight in [4, 5] else
            1 / math.floor(1 + trunkHeight / 3)
        )

        offset2 = trunkHeight - hatHeight
        LVS = []
        Fringe = [[1, 1], [1, 2], [2, 1], [2, 2]]
        PFringe = [2/9, 1/9, 4/9, 2/9]
        NFringe = ["A", "B", "C", "D"]

        N = 0
        while N < 4:
            m = 0
            if hatHeight == 4:
                LVS = [2, 2] + Fringe[N] + [1] + [0]*(26 - trunkHeight)
                Pf = PFringe[N]
            elif 4 < hatHeight <= 8:
                LVS = [0]*offset2 + [2]*(hatHeight - 2) + Fringe[N] + [1] + [0]*(26 - trunkHeight)
                Pf = PFringe[N]
            elif 8 < hatHeight <= 13:
                LVS = [0]*offset2 + [3]*4 + [2]*(hatHeight - 6) + Fringe[N] + [1] + [0]*(26 - trunkHeight)
                Pf = PFringe[N]
            else:
                raise TypeError("invalid parameter input")

            P = Pt * Ph * Pf

'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace", style="default")
        self.add(rendered_code)
