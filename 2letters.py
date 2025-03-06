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
import letter_holes as letter_holes

def arc_points(radius, start_angle, end_angle, center=[0,0], num_points=50):
    angles = [start_angle + i * (end_angle - start_angle) / (num_points - 1)
              for i in range(num_points)]
    points = [
        (center[0] + radius * math.cos(math.radians(angle)),
         center[1] + radius * math.sin(math.radians(angle)))
        for angle in angles
    ]
    return points

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
        try:
            holes = getattr(letter_holes, self.letter)
        except:
            holes = []

        scaled_holes = [letter_holes.Hole(hole.radius*self.scale, hole.x*self.scale, hole.y*self.scale) for hole in holes]
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

    # Generate a letter
    # letter = input()
    # shape = TwoLetter3D(10, letter)
    # shape.render()
    
    # letters = [chr(x) for x in range(ord('A'), ord('J') + 1)]

    # # Generate all combos
    # for letter in letters:
    #     for other_letter in letters:
    #         shape = TwoLetter3D(10, letter, other_letter)
    #         shape.render()

    # Generate an input combo
    letter1 = input("Enter the first letter:")
    letter2 = input("Enter the second letter:")
    shape = TwoLetter3D(10, letter1, letter2)
    shape.render()