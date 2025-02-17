// Generated by SolidPython 1.1.3 on 2025-02-16 19:45:43


linear_extrude(height = 10) {
	text(font = "Ariel", size = 10, text = "A");
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from solid import *
from solid.utils import *
import subprocess

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
    # shape = intersection_3d("A", "B", 10, "Arial")
    shapeA = letter_3d("A", 10, "Ariel")
    scad_render_to_file(shapeA, 'A.scad')

    shapeB = letter_3d("B", 10, "Ariel")
    shapeB = rotate(a=90, v=[1,0,0])(shapeB)

    final = intersection()(shapeA, shapeB)

    
    scad_render_to_file(final, "final.scad")

    # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "A.stl", "A.scad"])
    # subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "B.stl", "B.scad"])

    subprocess.run(["C:\\Program Files\\OpenSCAD\\openscad.exe", "-o", "final.stl", "final.scad"])

 
 
************************************************/
