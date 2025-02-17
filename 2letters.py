from solid import *
from solid.utils import *
import subprocess

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
    pass

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

    a = letter_A(10)
    scad_render_to_file(a, "customA.scad")
    subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "customA.stl", "customA.scad"])

