// Generated by SolidPython 1.1.3 on 2025-02-25 01:33:37
$fn=50;


intersection() {
	translate(v = [-5.0000000000, -5.0000000000, -5.0000000000]) {
		linear_extrude(height = 10) {
			difference() {
				polygon(points = [[0, 0], [5.0000000000, 10], [10, 0], [8.3333333333, 0], [6.6666666667, 3.3333333333], [3.3333333333, 3.3333333333], [1.6666666667, 0]]);
				translate(v = [5.0000000000, 5.8333333333]) {
					circle(r = 1.6666666667);
				}
			}
		}
	}
	rotate(a = 90, v = [0, 1, 0]) {
		translate(v = [-5.0000000000, -5.0000000000, -5.0000000000]) {
			linear_extrude(height = 10) {
				polygon(points = [[8.3333333333, 5.0000000000], [8.3264846425, 4.7864326001], [8.3059667127, 4.5737427944], [8.2718638566, 4.3628045710], [8.2243162101, 4.1544847203], [8.1635191567, 3.9496392733], [8.0897225245, 3.7491099837], [8.0032295597, 3.5537208696], [7.9043956804, 3.3642748267], [7.7936270163, 3.1815503293], [7.6713787396, 3.0062982317], [7.5381531946, 2.8392386823], [7.3944978337, 2.6810581647], [7.2410029675, 2.5324066764], [7.0782993395, 2.3938950584], [6.9070555337, 2.2660924847], [6.7279752277, 2.1495241233], [6.5417943008, 2.0446689788], [6.3492778104, 1.9519579233], [6.1512168481, 1.8717719265], [5.9484252888, 1.8044404899], [5.7417364465, 1.7502402927], [5.5319996501, 1.7093940553], [5.3200767530, 1.6820696235], [5.1068385919, 1.6683792793], [4.8931614081, 1.6683792793], [4.6799232470, 1.6820696235], [4.4680003499, 1.7093940553], [4.2582635535, 1.7502402927], [4.0515747112, 1.8044404899], [3.8487831519, 1.8717719265], [3.6507221896, 1.9519579233], [3.4582056992, 2.0446689788], [3.2720247723, 2.1495241233], [3.0929444663, 2.2660924847], [2.9217006605, 2.3938950584], [2.7589970325, 2.5324066764], [2.6055021663, 2.6810581647], [2.4618468054, 2.8392386823], [2.3286212604, 3.0062982317], [2.2063729837, 3.1815503293], [2.0956043196, 3.3642748267], [1.9967704403, 3.5537208696], [1.9102774755, 3.7491099837], [1.8364808433, 3.9496392733], [1.7756837899, 4.1544847203], [1.7281361434, 4.3628045710], [1.6940332873, 4.5737427944], [1.6735153575, 4.7864326001], [1.6666666667, 5.0000000000], [0.0000000000, 5.0000000000], [0.0102730362, 4.6796489001], [0.0410499309, 4.3606141916], [0.0922042150, 4.0442068565], [0.1635256848, 3.7317270805], [0.2547212649, 3.4244589099], [0.3654162133, 3.1236649756], [0.4951556605, 2.8305813044], [0.6434064794, 2.5464122400], [0.8095594755, 2.2723254939], [0.9929318907, 2.0094473475], [1.1927702082, 1.7588580235], [1.4082532495, 1.5215872470], [1.6384955487, 1.2986100146], [1.8825509907, 1.0908425877], [2.1394166994, 0.8991387270], [2.4080371584, 0.7242861850], [2.6873085488, 0.5670034681], [2.9760832844, 0.4279368849], [3.2731747279, 0.3076578898], [3.5773620668, 0.2066607348], [3.8873953302, 0.1253604391], [4.2020005248, 0.0640910829], [4.5198848705, 0.0231044353], [4.8397421121, 0.0025689190], [5.1602578879, 0.0025689190], [5.4801151295, 0.0231044353], [5.7979994752, 0.0640910829], [6.1126046698, 0.1253604391], [6.4226379332, 0.2066607348], [6.7268252721, 0.3076578898], [7.0239167156, 0.4279368849], [7.3126914512, 0.5670034681], [7.5919628416, 0.7242861850], [7.8605833006, 0.8991387270], [8.1174490093, 1.0908425877], [8.3615044513, 1.2986100146], [8.5917467505, 1.5215872470], [8.8072297918, 1.7588580235], [9.0070681093, 2.0094473475], [9.1904405245, 2.2723254939], [9.3565935206, 2.5464122400], [9.5048443395, 2.8305813044], [9.6345837867, 3.1236649756], [9.7452787351, 3.4244589099], [9.8364743152, 3.7317270805], [9.9077957850, 4.0442068565], [9.9589500691, 4.3606141916], [9.9897269638, 4.6796489001], [10.0000000000, 5.0000000000], [10, 10], [0, 10], [0, 8.3333333333], [8.3333333333, 8.3333333333]]);
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from solid import *
from solid.utils import *

import math
import matplotlib.pyplot as plt
import subprocess
import os
import grok_letters as grok
import grok_think as grok_think
import letters as let
import o1_letters as o1

def arc_points(radius, start_angle, end_angle, center=[0,0], num_points=50):
    angles = [start_angle + i * (end_angle - start_angle) / (num_points - 1)
              for i in range(num_points)]
    points = [
        (center[0] + radius * math.cos(math.radians(angle)),
         center[1] + radius * math.sin(math.radians(angle)))
        for angle in angles
    ]
    return points

class Hole:
    def __init__(self, radius, x, y):
        """
        Hole defined by:
        :param x: x dimension for center point of the circle as a ratio of letter height
        :param y: y dimension for center point of the circle as a ratio of letter height
        :param radius: radius of circle as a ratio of letter height
        """
        self.x = x
        self.y = y
        self.radius = radius

class Letter2D:
    def __init__(self, letter, scale):
        self.letter = letter
        self.scale = scale
        self.shape = self.generate()
    
    def get_letter_points(self):
        points = getattr(let, self.letter)
        # points = getattr(o1, self.letter)
        # points = getattr(grok, self.letter)
        scaled_points = [(point[0] * self.scale, point[1] * self.scale) for point in points]
        return scaled_points

    def get_letter_holes(self):
        holes = []
        if self.letter == "A": 
            holes = [Hole(1/6, 1/2, 7/12)]
        if self.letter == "B":
            holes = [Hole(1/6, 1/2, 3/4), Hole(1/6, 1/2, 1/4)]
        if self.letter == "D":
            holes = [Hole(1/3, 1/2, 1/2)]

        scaled_holes = [Hole(hole.radius*self.scale, hole.x*self.scale, hole.y*self.scale) for hole in holes]
        return scaled_holes

    
    def generate(self):
        shape = polygon(points=self.get_letter_points())
        holes = self.get_letter_holes()

        if holes:
            for hole in holes:
                circle_hole = circle(r=hole.radius)
                positioned_hole = translate([hole.x, hole.y])(circle_hole)
                shape = difference()(shape, positioned_hole)
        return shape
    

    def render(self):
        scad_render_to_file(self.shape, f"output/{self.name}.scad", file_header='$fn=50;')
        subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", f"output\\{self.name}.stl", f"output\\{self.name}.scad"])


class TwoLetter3D:
    def __init__(self, height, letterA, letterB=None):
        self.height = height
        self.letterA = letterA
        self.letterB = letterB
    

    def generate_3d_letter(self, letter):
        letter = letter.upper()
        # TODO: add catch here for is letter is not a letter
        shape = Letter2D(letter, self.height).generate()
        shape_3d = linear_extrude(height=self.height)(shape)
        centered_shape_3d = translate([-self.height/2, -self.height/2, -self.height/2])(shape_3d)
        return centered_shape_3d


    def render(self):
        letterA3D = self.generate_3d_letter(self.letterA)

        if self.letterB:
            letterB3D = self.generate_3d_letter(self.letterB)
            letterB3D = rotate(a=90, v=[0,1,0])(letterB3D)

            combined = intersection()(letterA3D, letterB3D)
            file_name = self.letterA + self.letterB
            scad_render_to_file(combined, f"output/{file_name}.scad", file_header='$fn=50;')
            subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", f"output\\{file_name}.stl", f"output\\{file_name}.scad"])
            return
        else:
            # file_name = "o1_" + self.letterA
            # file_name = "grok_think_" + self.letterA
            file_name = self.letterA
            # file_name = "grok_" + self.letterA
            scad_render_to_file(letterA3D, f"output/{file_name}.scad", file_header='$fn=50;')
            subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", f"output\\{file_name}.stl", f"output\\{file_name}.scad"])
            # subprocess.run(["openscad", "-o", f"output\\{file_name}.png", f"output\\{file_name}.scad", "--imgsize=800,600", "--autocenter"])
            subprocess.run(["openscad", "-o", f"output\\{file_name}.png", f"output\\{file_name}.scad", "--imgsize=800,600", "--camera=0,0,30,0,0,0", "--viewall", "--autocenter", "--projection=o"])
            os.remove(f"output/{file_name}.scad")
            return
                


if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)

    # # Generate a letter
    # letter = input()
    # shape = TwoLetter3D(10, letter)
    # shape.render()
    
    letters = [chr(x) for x in range(ord('A'), ord('j') + 1)]

    # Generate all combos
    for letter in letters:
        for other_letter in letters:
            shape = TwoLetter3D(10, letter, other_letter)
            shape.render()

    # # Generate all letters
    # for letter in letters:
    #     shape = TwoLetter3D(10, letter)
    #     shape.render()
 
 
************************************************/
