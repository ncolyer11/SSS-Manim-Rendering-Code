# desc:   7x7x27 volume and record the chance of a shroomlight and wart block generating at each position, 
# based on what region it’s in, then we can make a list of the generation probabilities for every block for 
# just that one specific nether tree variant.

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
        return wart_map[y-1][x][z] or random.random() < 1.0/9.0
    else:
        return 0

class cmplx_shot_1(ThreeDScene):
    def construct(self):     
        self.wait(0.2) 
        self.set_camera_orientation(phi = (90-22.5) * DEGREES, theta = 45 * DEGREES, gamma = 0 * DEGREES, zoom=0.4)
        self.camera.background_color = "#1f1f1f"

        boxes = VGroup()
        LVS = [0,0,0,0,0,3,3,3,3,2,2,2,1,2,1]
        # LVS = [0,0,0,0,2,2,2,2,2,1]
        # LVS = [0,0,2,2,2,2,1]
        wart_map = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(27)]
        blocks = 0
        for layer in LVS:
            blocks += (2*layer + 1)**2
        print(f"Max Animations: {2*blocks+1}")

        h = count_non_zero_digits(LVS) # hat height
        H = len(LVS) # lvs height

        # generating the trunk first
        # trunk = Prism([1,1,H-1], fill_color="#b31d1d")
        offset = 0
        if H % 2 == 1:
            offset = 0.5

        trunk_cubes = VGroup()
        for i in range(H-1):
            trunk_cube = Cube(side_length=1, fill_opacity=1, fill_color="#b31d1d")
            trunk_cube.move_to([0.5,0.5,offset+i-H/2])
            trunk_cubes.add(trunk_cube)


        for y in range(H):
            J = H - h # layer offset value (height off the ground)
            r = LVS[y] # radius of current layer
            l = 2*r+1 # side length of current layer
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
                        shroom_chance = 0.01
                        wart_chance = 0.75
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
                            colour = "#690303"
                            wart_map[y][x][z] = 1
                            # print(f"{rand}: {x},{z},{J}: vines")
                        else:
                            opacity = 0
                            # print(f"{rand}: {x},{z},{J}: Air")
                    elif rand < shroom_chance:
                        colour = "#f56a00"
                        # print(f"{rand}: {x},{z},{J}: shroom")
                    elif rand < wart_chance:
                        colour = "#690303"
                        # print(f"{rand}: {x},{z},{J}: wart")
                        wart_map[y][x][z] = 1
                    else:
                        opacity = 0
                        # print(f"{rand}: {x},{z},{J}: air")
                    
                    cube = Cube(side_length=1, fill_opacity=opacity, fill_color=colour)
                    cube.move_to([x-(l-1)/2,z-(l-1)/2,0])
                    prism_cubes.add(cube)

            prism = VGroup(prism_cubes)
            boxes.add(prism)

        boxes.arrange(OUT, buff=0) 

        # animating in each box
        self.wait(1)
        for trunk_cube in trunk_cubes:
            self.play(DrawBorderThenFill(trunk_cube), run_time=speed*1/18)

        blocks = 0
        for prism in boxes:
            prism_cubes = prism[0]

            for cube in prism_cubes:
                cube_colour = str(cube.get_fill_color())
                anim_time = speed*0.5/25

                if cube_colour == "#690303" or cube_colour == "#f56a00":
                    self.play(DrawBorderThenFill(cube), run_time=anim_time)
                    self.wait(anim_time/2)
                    blocks += 1

            self.wait(2*anim_time)
        
        self.wait()
