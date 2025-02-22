from solid import *
from solid.utils import *

import math
import matplotlib.pyplot as plt
import subprocess
import os
import pdb

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
        points = []
        if self.letter == "A":
            points = [(0,0), (1/2, 1), (1, 0), (5/6, 0), (2/3, 1/3), (1/3, 1/3), (1/6, 0)]
        if self.letter == "B":
            top_arc_points = arc_points(1/4, 90, -90, center=[3/4, 3/4])
            bottom_arc_points = arc_points(1/4, 90, -90, center=[3/4, 1/4])
            other_points = [(0,0),(0,1)]
            points = top_arc_points + bottom_arc_points + other_points
        if self.letter == "C":
            outer_arc_points = arc_points(1/2, 30, 330, center=[1/2,1/2])
            inner_arc_points = arc_points(1/3, 30, 330, center=[1/2,1/2])[::-1]
            points = outer_arc_points + inner_arc_points
        if self.letter == "D":
            outer_arc_points = arc_points(1/2, 90, -90, center= [1/2, 1/2])
            points = outer_arc_points + [(0,0), (0, 1)]
        if self.letter == "E":
            points = [(0,0), (1,0), (1,1/5), (1/5,1/5), (1/5,2/5), (3/4,2/5), (3/4,3/5), (1/5,3/5), (1/5,4/5), (1,4/5), (1,1), (0,1)]
        if self.letter == "F":
            points = [(0,0), (1/5,0), (1/5,2/5), (3/4,2/5), (3/4,3/5), (1/5,3/5), (1/5,4/5), (1,4/5), (1,1), (0,1)]
        if self.letter == "H":
            points = [(0, 0), (0, 1), (1/6, 1), (1/6, 7/12), (5/6, 7/12), (5/6, 1), (1, 1), (1, 0), (5/6, 0), (5/6, 5/12), (1/6, 5/12), (1/6, 0)]
        if self.letter == "I":
            points = [(0,0), (1,0), (1,1/6), (7/12,1/6), (7/12,5/6), (1,5/6), (1,1), (0,1), (0,5/6), (5/12,5/6), (5/12,1/6), (0,1/6)]
        if self.letter == "J":
            inner_arc = arc_points(1/3, 360, 180, [1/2,1/2])
            outer_arc = arc_points(1/2, 180, 360, [1/2,1/2])
            other_points = [(1,1), (0,1), (0,5/6), (5/6,5/6)]
            points = inner_arc + outer_arc + other_points

        scaled_points = [(p[0] * self.scale, p[1] * self.scale) for p in points]
        return scaled_points
    

    def get_letter_holes(self):
        holes = []
        if self.letter == "A": 
            holes = [Hole(1/6, 1/2, 7/12)]
        if self.letter == "B":
            holes = [Hole(1/6, 1/2, 3/4), Hole(1/6, 1/2, 1/4)]
        if self.letter == "D":
            holes = [Hole(1/2, 1/2, 1/6)]

        scaled_holes = [Hole(hole.radius*self.scale, hole.x*self.scale, hole.y*self.scale) for hole in holes]
        return scaled_holes

    
    def generate(self):
        outer_shape_points = self.get_letter_points()
        shape = polygon(points=outer_shape_points)
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
            file_name = self.letterA
            scad_render_to_file(letterA3D, f"output/{file_name}.scad", file_header='$fn=50;')
            subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", f"output\\{file_name}.stl", f"output\\{file_name}.scad"])
            return
                


if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)

        # # Generate a letter
    shape = TwoLetter3D(10, "J", "C")
    shape.render()
    
    letters = [chr(x) for x in range(ord('A'), ord('H') + 1)]

    # # Generate all combos
    # for letter in letters:
    #     for other_letter in letters:
    #         shape = TwoLetter3D(10, letter, other_letter)
    #         shape.render()

    # # Generate all letters
    # for letter in letters:
    #     shape = TwoLetter3D(10, letter, "z")
