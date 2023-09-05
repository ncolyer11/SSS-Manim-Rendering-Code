# desc: 7x7x27 box, into individual blocks and then assign a pair of values to each block

from manim import*
import heatmap_data as Hdata
import colorsys

# animation speed
speed = 1
heatmap = 2 # 0: stems, 1: shroomlights, 2: wart blocks (vrm0)

warped_wart_colour = "#084678" # 207°, 93%, 47%
nether_wart_colour = "#690303" # 0°, 97%, 41%
shroomlight_colour = "#f56a00" # 26°, 100%, 96%

def rgb_to_hex(rgb):
    r, g, b = rgb
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    hex_string = "#{0:02x}{1:02x}{2:02x}".format(r, g, b)
    return hex_string

class cmplx_shot_3(ThreeDScene):
    def construct(self):   
        self.wait(0.2)   
        self.set_camera_orientation(phi = (90-17.5) * DEGREES, theta = 45 * DEGREES, gamma = 0 * DEGREES, zoom=0.265)
        self.camera.background_color = "#1f1f1f"

        boxes = VGroup()

        # heatmaps_array[heatmap][row][col]
        heatmaps_array = Hdata.heatmap_array
        for x in range(7):
            slices = VGroup()
            for y in range(27):
                for z in range(7):
                # 3D data is stored in 'slices' on a 2D spreadsheet, hence some math is needed to convert between them
                    col = z + (7 * x)
                    row = 26 - y
                    generation_chance = float(format(heatmaps_array[heatmap][row][col]/0.31,'f')) # max_shroom: 0.02925, max_wart: 0.31
                    if generation_chance > 0: # so it doesn't animate invisible cube elements
                        block_colour = rgb_to_hex(colorsys.hsv_to_rgb(207.0/360.0,1.0,generation_chance))
                        cube = Cube(side_length=1, fill_color=block_colour, fill_opacity=1.0)
                        cube.move_to([x,z,y])
                        slices.add(cube)

            prism = VGroup(slices)
            boxes.add(prism)

        boxes.move_to([0,0,-1.8])
        for slices in boxes:
            for cubes in slices:    
                self.play(ShowSubmobjectsOneByOne(cubes), run_time=5)  
        
        self.wait()
