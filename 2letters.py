from solid import *
from solid.utils import *

import math
import matplotlib.pyplot as plt
import subprocess
import os

class Hole:
    def __init__(self, x, y, radius):
        """
        Hole defined by:
        :param x: x dimension for center point of the circle as a ratio of letter height
        :param y: y dimension for center point of the circle as a ratio of letter height
        :param radius: radius of circle as a ratio of letter height
        """
        self.x = x
        self.y = y
        self.radius = radius

class Letter3D:
    def __init__(self, name, outer_shape_points, height, holes=None):
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
        self.height = height


    def generate(self):
        with open("output\\output.txt", "w") as f:
            f.write(str(self.outer_shape_points))
        shape = polygon(points=self.outer_shape_points)

        if self.holes:
            for hole in self.holes:
                circle_hole = circle(r=hole.radius*self.height)
                positioned_hole = translate([hole.x*self.height, hole.y*self.height])(circle_hole)
                shape = difference()(shape, positioned_hole)
        
        shape_3d = linear_extrude(height=self.height)(shape)
        shape_3d = translate([-self.height/2, -self.height/2, -self.height/2])(shape_3d)
        return shape_3d
    
    def render(self):
        scad_render_to_file(self.shape, f"output/{self.name}.scad", file_header='$fn=50;')
        subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", f"output\\{self.name}.stl", f"output\\{self.name}.scad"])


class TwoLetter3D:
    def __init__(self, height, letterA, letterA_face, letterB=None, letterB_face=None):
        self.height = height
        self.letterA = letterA
        self.letterB = letterB
        self.letterA_face = letterA_face
        self.letterB_face = letterB_face

    def call_letter_generation(self, letter):
        letter = letter.upper()
        function_name = f"letter_{letter}"
        func = globals().get(function_name)
        if func is None:
            raise ValueError(f"No letter generation function defined for letter '{letter}'.")
        else:
            print(func)
        return func(self.height)
    
    def rotate_object(self, face, shape):
        face = face.lower()
        if face == "z":
            return shape
        if face == "x":
            return rotate(a=90, v=[1,0,0])(shape)
        if face == "y":
            return rotate(a=90, v=[0,1,0])(shape)
        else:
            raise ValueError("Face must be one of 'x', 'y', or 'z'.")

    def render(self):
        if self.letterA:
            letterA3D = self.call_letter_generation(self.letterA)
            letterA3D = self.rotate_object(self.letterA_face, letterA3D)

        if self.letterB:
            letterB3D = self.call_letter_generation(self.letterB)
            letterB3D = self.rotate_object(self.letterB_face, letterB3D)
            combined = intersection()(letterA3D, letterB3D)
            file_name = self.letterA + self.letterB
            scad_render_to_file(combined, f"output/{file_name}.scad", file_header='$fn=50;')
            subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", f"output\\{file_name}.stl", f"output\\{file_name}.scad"])
            return
        else:
            file_name = self.letterA
            scad_render_to_file(letterA3D, f"output/{file_name}.scad", file_header='$fn=50;')
            subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", f"output\\{file_name}.stl", f"output\\{file_name}.scad"])
    
                

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
    for letter in letters:
        for other_letter in letters:
            shape = TwoLetter3D(10, letter, "z", other_letter, "y")
            shape.render()

    # Generate all letters
    # for letter in letters:
    #     shape = TwoLetter3D(10, letter, "z")
    #     shape.render()

    #Generate a letter
    # shape = TwoLetter3D(10, "B", "z")
    # shape.render()
