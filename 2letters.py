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
    def __init__(self, name, outer_shape_points, height, holes=[]):
        """
        3D Letter defined by:
        :param name: name of letter
        :param outer_shape_points: points defining the outer shape of the letter
        :param heigh: size of cube that letter fits inside
        :param holes: list of Holes
        """
        self.name = name
        self.outer_shape_points = outer_shape_points
        self.holes = holes
        self.height = height

    def render(self):
        shape = polygon(points=self.outer_shape_points)

        if self.holes:
            for hole in self.holes:
                circle_hole = circle(r=hole.radius*self.height)
                positioned_hole = translate([hole.x*self.height, hole.y*self.height])(circle_hole)
                shape = difference()(shape, positioned_hole)
        
        shape_3d = linear_extrude(height=self.height)(shape)
        shape_3d = translate([-self.height/2, -self.height/2, -self.height/2])(shape_3d)
        
        scad_render_to_file(shape_3d, f"output/{self.name}.scad", file_header='$fn=50;')
        subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", f"output\\{self.name}.stl", f"output\\{self.name}.scad"])
                

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
    return A.render()


def letter_B(h):
    top_arc_points = arc_points(h/4, 90, -90, center=[3/4*h, 3/4*h])
    bottom_arc_points = arc_points(h/4, 90, -90, center=[3/4*h, h/4])
    other_points = [(0,0),(0,h)]

    shape_points = top_arc_points + bottom_arc_points + other_points
    holes = [Hole(1/2, 3/4, 1/6), Hole(1/2, 1/4, 1/6)]
    B = Letter3D("B", shape_points, h, holes)
    return B.render()

def letter_C(h):
    outer_arc_points = arc_points(h/2, 30, 330)
    inner_arc_points = arc_points(h/4, 30, 330)[::-1]
    shape_points = outer_arc_points + inner_arc_points
    C = Letter3D("C", shape_points, h)
    return C.render()


def letter_D(h):
    outer_arc_points = arc_points(h/2, 90, -90, center= [h/2, h/2])
    shape_points = outer_arc_points + [(0,0), (0, h)]
    holes = [Hole(1/2, 1/2, 1/6)]
    D = Letter3D("D", shape_points, h, holes)
    return D.render()

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)

    # Just the letter B
    letter_D(10)
    # scad_render_to_file(b, "customB.scad", file_header='$fn=50;')
    # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "customB.stl", "customB.scad"])

    # Intersection of A and A
    # a1 = translate([0,0,0])(letter_A(10))
    # a2 = translate([0,0,0])(rotate(a=90, v=[0,1,0])(letter_B(10)))
    # combined = intersection()(a1, a2)
    # scad_render_to_file(combined, "AB.scad")
    # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "AB.stl", "AB.scad"])
