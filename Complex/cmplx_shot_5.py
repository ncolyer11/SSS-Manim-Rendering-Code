# desc: Essentially, each shape of nether tree can be referred to as a layer value set; 
# a set of integers ranging from 0 to 3 that describes the radius of the hat at each layer

from manim import*

# animation speed
speed = 1

class cmplx_shot_5(ThreeDScene):
    def construct(self):
        self.wait(0.2) 
        self.set_camera_orientation(phi = 90 * DEGREES, theta = 0 * DEGREES, zoom = 1)
        self.camera.background_color = "#1f1f1f"
        
        lvs_array = [
            [2,2,1,2,1],
            [0,0,2,2,2,2,1,1],
            [0,0,0,2,2,2,2,2,2,1,2,1],
            [0,0,0,0,3,3,3,3,2,2,2,2,1,1],
            [0,0,0,0,0,0,0,3,3,3,3,2,2,2,2,1,2,1],
        ]

        lvs_array_mod = [ # [max len, 0 (buffer), len, amount, len, amount, ...]
            [5,0, 2,2, 1,1, 2,1, 1,1],
            [5,0, 0,2, 2,4, 1,2],
            [5,0, 0,3 ,2,6 ,1,1 ,2,1 ,1,1],
            [7,0, 0,4 ,3,4 ,2,4 ,1,2],
            [7,0, 0,8 ,3,4 ,2,4, 1,1, 2,1 ,1,1],
        ]

        nether_trees = VGroup()
        nether_tree_index = 0
        for lvs in lvs_array_mod:
            nether_tree = VGroup()
            layer_index = 0
            max_layer_size = 0
            i = 0
            while i < len(lvs):
                if i == 0:
                    max_layer_size = lvs[i]
                    i += 2
                    continue

                length = 2 * lvs[i] + 1
                # print(f"length: {length}")
                # print(f"height: {lvs[i+1]}")
                if length == 1:
                    prism_layer = Prism(dimensions=[length, length, lvs[i+1]], fill_color = "#344a94", fill_opacity = 1)
                else:
                    # prism_layer = Prism(dimensions=[length, length, lvs[i+1]], fill_color = "#1068b0", fill_opacity = 1)
                    prism_layer = Prism(dimensions=[length, length, lvs[i+1]], fill_color = WHITE, fill_opacity = 1)
                prism_layer.move_to([0,0,-10 + layer_index + lvs[i+1]/2])
                layer_index += lvs[i+1]
                nether_tree.add(prism_layer)
                i += 2

            nether_tree.shift(LEFT * 11, DOWN * (16 - nether_tree_index))
            nether_trees.add(nether_tree)
            # print(max_layer_size)
            nether_tree_index += max_layer_size + 2

        nether_trees.shift(LEFT * 30)
        
        text_boxes = VGroup()
        index = 0
        for nether_tree in nether_trees:
            text = Text(f"{(lvs_array[index])}")  
            text.rotate(90 * DEGREES, axis=OUT)  
            text.rotate(90 * DEGREES, axis=UP)
            text.next_to(nether_tree, OUT, buff = 0.75)
            text_boxes.add(text)
            index += 1
        
        self.play(Create(nether_trees), run_time = 0.75 * speed)
        self.wait(1)
        self.play(Write(text_boxes), run_time = 1.5 * speed)
        self.wait(0.2)
