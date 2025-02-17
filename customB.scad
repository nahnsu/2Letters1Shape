// Generated by SolidPython 1.1.3 on 2025-02-16 23:01:38


linear_extrude(height = 10) {
	polygon(points = [[0, 0], [6.6666666667, 0], [6.6666666667, -0.0000000000], [7.8067338111, 0.2010245974], [8.8092920323, 0.7798518563], [9.5534180126, 1.6666666667], [9.9493591767, 2.7545060744], [9.9493591767, 3.9121605922], [9.5534180126, 5.0000000000], [8.8092920323, 5.8868148104], [7.8067338111, 6.4656420693], [6.6666666667, 6.6666666667], [5.0000000000, 5.0000000000], [5.5700335722, 5.1005122987], [6.0713126828, 5.3899259281], [6.4433756730, 5.8333333333], [6.6413462550, 6.3772530372], [6.6413462550, 6.9560802961], [6.4433756730, 7.5000000000], [6.0713126828, 7.9434074052], [5.5700335722, 8.2328210346], [5.0000000000, 8.3333333333], [0, 10]]);
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
import math
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
    return solid_with_hole

def letter_B(h):
    large_arc = arc_points(h/3, -90, 90, num_points = 10, center=[2/3*h, 1/3*h])
    # large_arc_transposed = translate([2/3*h, 1/3*h])(large_arc)

    small_arc = arc_points(h/6, -90, 90, num_points= 10, center=[h/2, 2/3*h])
    # small_arc_transposed = translate([h/2, 2/3*h])(small_arc)

    outer_points = [(0,0), (2/3*h, 0)]
    outer_points.extend(large_arc)
    outer_points.extend(small_arc)
    outer_points.extend([(0,h)])

    outer_shape = polygon(outer_points)
    outer_solid = linear_extrude(height=h)(outer_shape)
    return outer_solid


def letter_3d(letter, size, font):
    letter_2d = text(text=letter, size=size, font=font)

    letter_3d = linear_extrude(height=size)(letter_2d)

    return letter_3d

def intersection_3d(letter1, letter2, size, font):
    letter1_3d = letter_3d(letter1, size, font)
    letter2_3d = letter_3d(letter2, size, font)

    letter2_3d = rotate(a=90, v=[1,0,0])(letter2_3d)

    intersect = intersection()(letter1_3d, letter2_3d)

    return intersect



if __name__ == "__main__":
    # shapeA = letter_3d("A", 10, "Ariel")
    # scad_render_to_file(shapeA, 'A.scad')
    # shapeB = letter_3d("B", 10, "Ariel")
    # shapeB = rotate(a=90, v=[1,0,0])(shapeB)
    # final = intersection()(shapeA, shapeB)
    # scad_render_to_file(final, "final.scad")
    # # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "A.stl", "A.scad"])
    # # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "B.stl", "B.scad"])
    # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "final.stl", "final.scad"])

    # a = letter_A(10)
    # scad_render_to_file(a, "customA.scad")
    # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "customA.stl", "customA.scad"])

    b = letter_B(10)
    scad_render_to_file(b, "customB.scad")
    subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "customB.stl", "customB.scad"])

 
 
************************************************/
