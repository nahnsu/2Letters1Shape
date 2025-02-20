from solid import *
from solid.utils import *

import math
import matplotlib.pyplot as plt
import subprocess
import os
import pdb

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
    def __init__(self, name, outer_shape_points, holes=None):
        """
        3D Letter defined by:
        :param name: name of letter
        :param outer_shape_points: points defining the outer shape of the letter
        :param heigh: size of cube that letter fits inside
        :param holes: list of Holes
        """
        self.name = name
        self.outer_shape_points = outer_shape_points
        self.holes = holes if holes is not None else []
        self.shape = self.generate()

    def generate(self):
        shape = polygon(points=self.outer_shape_points)

        if self.holes:
            for hole in self.holes:
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

    
    def get_letter_points(self, letter):
        points = []
        if letter == "A":
            points = [(0,0), (1/2, 1), (1, 0), (5/6, 0), (2/3, 1/3), (1/3, 1/3), (1/6, 0)]
        if letter == "B":
            top_arc_points = arc_points(1/4, 90, -90, center=[3/4, 3/4])
            bottom_arc_points = arc_points(1/4, 90, -90, center=[3/4, 1/4])
            other_points = [(0,0),(0,1)]
            points = top_arc_points + bottom_arc_points + other_points
        
        scaled_points = [(p[0] * self.height, p[1] * self.height) for p in points]
        return scaled_points
        

    def get_letter_holes(self, letter):
        holes = []
        if letter == "A": 
            holes = [Hole(1/6, 1/2, 7/12)]
        if letter == "B":
            holes = [Hole(1/6, 1/2, 3/4), Hole(1/6, 1/2, 1/4)]
        scaled_holes = [Hole(hole.radius*self.height, hole.x*self.height, hole.y*self.height) for hole in holes]
        return scaled_holes
    

    def generate_3d_letter(self, letter):
        letter = letter.upper()
        outer_shape_points = self.get_letter_points(letter)
        holes = self.get_letter_holes(letter)
        shape = Letter2D(letter, outer_shape_points, holes).generate()
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
                

def arc_points(radius, start_angle, end_angle, center=[0,0], num_points=50):
    angles = [start_angle + i * (end_angle - start_angle) / (num_points - 1)
              for i in range(num_points)]
    points = [
        (center[0] + radius * math.cos(math.radians(angle)),
         center[1] + radius * math.sin(math.radians(angle)))
        for angle in angles
    ]
    return points

def letter_A(h):
    shape_points = [(0,0), (h/2, h), (h, 0), (5/6*h, 0), (2/3*h, 1/3*h), (1/3*h, 1/3*h), (h/6, 0)]
    holes = [Hole(1/2, 7/12, 1/6)]
    A = Letter3D("A", shape_points, h, holes)
    return A.generate()

def letter_B(h):
    top_arc_points = arc_points(h/4, 90, -90, center=[3/4*h, 3/4*h])
    bottom_arc_points = arc_points(h/4, 90, -90, center=[3/4*h, h/4])
    other_points = [(0,0),(0,h)]

    shape_points = top_arc_points + bottom_arc_points + other_points
    holes = [Hole(1/2, 3/4, 1/6), Hole(1/2, 1/4, 1/6)]
    B = Letter3D("B", shape_points, h, holes)
    return B.generate()

def letter_C(h):
    outer_arc_points = arc_points(h/2, 30, 330, center=[h/2,h/2])
    inner_arc_points = arc_points(h/4, 30, 330, center=[h/2,h/2])[::-1]
    shape_points = outer_arc_points + inner_arc_points
    # print(shape_points)
    C = Letter3D("C", shape_points, h)
    return C.generate()


def letter_D(h):
    outer_arc_points = arc_points(h/2, 90, -90, center= [h/2, h/2])
    shape_points = outer_arc_points + [(0,0), (0, h)]
    holes = [Hole(1/2, 1/2, 1/6)]
    D = Letter3D("D", shape_points, h, holes)
    return D.generate()

def letter_E(h):
    points = [(0,0), (h,0), (h,h/5), (h/5,h/5), (h/5,2/5*h), (3/4*h,2/5*h), (3/4*h,3/5*h), (h/5,3/5*h), (h/5,4/5*h), (h,4/5*h), (h,h), (0,h)]
    E = Letter3D("E", points, h)
    return E.generate()

def letter_F(h):
    points = [(0,0), (h/5,0), (h/5,2/5*h), (3/4*h,2/5*h), (3/4*h,3/5*h), (h/5,3/5*h), (h/5,4/5*h), (h,4/5*h), (h,h), (0,h)]
    F = Letter3D("F", points, h)
    return F.generate()

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    
    letters = [chr(x) for x in range(ord('A'), ord('F') + 1)]

    # Generate all combos
    # for letter in letters:
    #     for other_letter in letters:
    #         shape = TwoLetter3D(10, letter, other_letter)
    #         shape.render()

    # Generate all letters
    # for letter in letters:
    #     shape = TwoLetter3D(10, letter, "z")
    #     shape.render()

    #Generate a letter
    shape = TwoLetter3D(10, "A", "B")
    shape.render()
