import math
import matplotlib.pyplot as plt
from solid import *
from solid.utils import *
import subprocess

def arc_points(radius, start_angle, end_angle, num_points=50, center=[0,0]):
    angles = [start_angle + i * (end_angle - start_angle) / (num_points - 1)
              for i in range(num_points)]
    points = [
        [center[0] + radius * math.cos(math.radians(angle)),
         center[1] + radius * math.sin(math.radians(angle))]
        for angle in angles
    ]
    return points

def letter_A(h):
    shape_points = [(0,0), (h/2, h), (h, 0), (5/6*h, 0), (2/3*h, 1/3*h), (1/3*h, 1/3*h), (h/6, 0)]
    shape = polygon(shape_points)
    solid_A = linear_extrude(height=h)(shape)
    
    # hole_points = [(h/2, 2/3*h), (5/12*h, h/2), (7/12*h, h/2)]
    # hole = polygon(hole_points)
    # solid_hole = linear_extrude(height=h)(hole)
    hole = circle(r=h/6)
    positioned_hole = translate([h/2, 7/12*h])(hole)
    solid_hole = linear_extrude(height=h)(positioned_hole)
    
    solid_with_hole = difference()(solid_A, solid_hole)
    centered = translate([-h/2, -h/2, -h/2])(solid_with_hole)
    return centered

def letter_B(h):
    large_arc = arc_points(h/3, -90, 90, num_points = 10, center=[2/3*h, 1/3*h])
    large_arc_shape = polygon(large_arc)
    large_arc_transposed = translate([2/3*h, 1/3*h])(large_arc_shape)

    small_arc = arc_points(h/6, -90, 90, num_points= 10, center=[h/2, 2/3*h])
    small_arc_shape = polygon(small_arc)
    small_arc_transposed = translate([h/2, 2/3*h])(small_arc_shape)

    outer_points = [(0,0), (2/3*h, 0), (2/3*h, 2/3*h), (h/2, 2/3*h), (h/2, h), (0,h)]
    outer_shape = polygon(outer_points)

    total_shape = union()(large_arc_transposed, small_arc_transposed, outer_shape)
    outer_solid = linear_extrude(height=h)(total_shape)
    return outer_solid



if __name__ == "__main__":

    # Just the letter A
    # a = letter_A(10)
    # scad_render_to_file(a, "customA.scad")
    # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "customA.stl", "customA.scad"])

    # Just the letter B
    b = letter_B(10)
    scad_render_to_file(b, "customB.scad")
    subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "customB.stl", "customB.scad"])

    # Intersection of A and A
    # a1 = translate([0,0,0])(letter_A(10))
    # a2 = translate([0,0,0])(rotate(a=90, v=[0,1,0])(letter_A(10)))
    # combined = intersection()(a1, a2)
    # scad_render_to_file(combined, "AA.scad")
    # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "AA.stl", "AA.scad"])
