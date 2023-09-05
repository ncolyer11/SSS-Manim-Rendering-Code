# stack of 1-block-high square prisms acting as a sort of bounding box that the game 
# will increment through 1 block at a time to and try to generate a shroomlight or wart block at

from manim import*
import random

# animation speed
speed = 1

def count_non_zero_digits(arr):
    count = 0
    for digit in arr:
        if digit != 0:
            count += 1
    return count

def isVines(x, z, y, wart_map):
    if y != 0:
        return wart_map[y-1][x][z] or random.random() < 1.0/8
    else:
        return random.random() < 1.0/8

class cmplx_shot_6(ThreeDScene):
    def construct(self):     
        self.wait(0.2) 
        self.set_camera_orientation(phi = 90 * DEGREES, theta = 0 * DEGREES, zoom = 1)
        self.camera.background_color = "#1f1f1f"

        boxes = VGroup()
        hat_and_trunk  = VGroup()
        LVS = [0,0,0,2,2,2,2,2,2,1,2,1]
        lvs_mod = [0,3 ,2,6 ,1,1 ,2,1 ,1,1] # [len, amount, len, amount, ...]

        nether_tree_box = VGroup()
        layer_index = 0
        i1 = 0
        while i1 < len(lvs_mod):
            length = 2 * lvs_mod[i1] + 1
            if length == 1:
                prism_layer = Prism(dimensions=[length, length, lvs_mod[i1+1]], fill_color = "#344a94", fill_opacity = 1)
            else:
                prism_layer = Prism(dimensions=[length, length, lvs_mod[i1+1]], fill_color = WHITE, fill_opacity = 1)
            prism_layer.move_to([0,0,-10 + layer_index + lvs_mod[i1+1]/2])
            layer_index += lvs_mod[i1+1]
            nether_tree_box.add(prism_layer)
            i1 += 2

        nether_tree_box.shift(LEFT * 41, DOWN * 2)
        self.play(Create(nether_tree_box), run_time = 0.1)
        self.wait(1)

        nether_tree = VGroup()
        layer_index = 0
        i1 = 0
        while i1 < len(lvs_mod):
            length = 2 * lvs_mod[i1] + 1
            if length == 1:
                prism_layer = Prism(dimensions=[length, length, len(LVS) - 1], fill_color = "#344a94", fill_opacity = 1)
                prism_layer.move_to([0,0,-10 + layer_index + (len(LVS) - 1)/2])
            else:
                prism_layer = Prism(dimensions=[length, length, lvs_mod[i1+1]], stroke_width = 2.5, stroke_color = WHITE, fill_opacity = 0)
                prism_layer.move_to([0,0,-10 + layer_index + lvs_mod[i1+1]/2])
            layer_index += lvs_mod[i1+1]
            nether_tree.add(prism_layer)
            i1 += 2

        nether_tree.shift(LEFT * 41, DOWN * 2)
        self.play(ReplacementTransform(nether_tree_box, nether_tree), run_time = 1)
        self.wait(1)

        wart_map = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(27)]
        blocks = 0
        for layer in LVS:
            blocks += (2*layer + 1)**2
        print(f"Max Animations: {2*blocks+1}")

        h = count_non_zero_digits(LVS) # hat height
        H = len(LVS)                   # lvs height

        # generating the trunk first
        offset = 0
        if H % 2 == 1:
            offset = 0.5

        trunk_cubes = VGroup()
        for i in range(H-1):
            trunk_cube = Cube(side_length=1, fill_opacity=1, fill_color="#344a94")
            trunk_cube.move_to([0,0,offset+i-H/2])
            trunk_cubes.add(trunk_cube)


        for y in range(H):
            J = H - h  # layer offset value (height off the ground)
            r = LVS[y] # radius of current layer
            l = 2*r+1  # side length of current layer
            prism_cubes = VGroup()
            for x in range(-r,r+1):
                for z in range(-r,r+1):
                    Z = abs(z)
                    X = abs(x)
                    bl1 = X == 0
                    bl2 = Z == 0
                    bl3 = X == r
                    bl4 = Z == r
                    bl5 = y == H-1

                    if bl1 and bl2 and not bl5:
                        shroom_chance = 0.0
                        wart_chance = 0.0
                    elif bl3 and bl4:
                        shroom_chance = 0.02
                        wart_chance = 0.8
                    elif bl3 or bl4 or (bl1 and bl2 and bl5):
                        shroom_chance = 0.001
                        wart_chance = 0.98
                    else:
                        shroom_chance = 0.13
                        wart_chance = 0.2
                    
                    rand = random.random()
                    opacity = 1
                    colour = BLACK

                    if y < J + 3:
                        if (bl3 or bl4) and isVines(x,z,y,wart_map) == 1:
                            colour = "#1068b0"
                            wart_map[y][x][z] = 1
                        else:
                            opacity = 0
                    elif rand < shroom_chance:
                        colour = "#f56a00"
                    elif rand < wart_chance:
                        colour = "#1068b0"
                        wart_map[y][x][z] = 1
                    else:
                        opacity = 0
                    
                    cube = Cube(side_length=1, fill_opacity=opacity, fill_color=colour)
                    cube.move_to([x-(l-1)/2,z-(l-1)/2,0])
                    prism_cubes.add(cube)

            prism = VGroup(prism_cubes)
            boxes.add(prism)

        boxes.arrange(OUT, buff=0) 
        boxes.shift(IN * 0.5)
        hat_and_trunk.add(boxes, trunk_cubes)
        hat_and_trunk.shift(LEFT * 41, DOWN * 2, IN * 3.5)
        hat_and_trunk.move_to([0,0,0])
        hat_and_trunk.scale(0.5)
        hat_and_trunk.rotate(-30 * DEGREES, axis = Z_AXIS)

        self.begin_ambient_camera_rotation(rate=-0.2, about = "phi")
        self.play(
            nether_tree.animate.scale(0.5).rotate(-30 * DEGREES, axis = Z_AXIS).move_to([0,0,0]),
            run_time = 1*speed
        )
        self.stop_ambient_camera_rotation(about = "phi")
        self.begin_ambient_camera_rotation(rate = 0.67, about = "theta")

        # runs replacement by placing over the prior blank ntf
        blocks = 0
        for prism in boxes:
            prism_cubes = prism[0]

            for cube in prism_cubes:
                cube_colour = str(cube.get_fill_color())
                anim_time = speed*0.5/25

                if cube_colour == "#1068b0" or cube_colour == "#f56a00":
                    self.play(DrawBorderThenFill(cube), run_time=anim_time)
                    self.wait(anim_time/2)
                    blocks += 1
            self.wait(2*anim_time)

        self.wait(3.5)
        self.stop_ambient_camera_rotation(about = "theta")
        self.wait()
