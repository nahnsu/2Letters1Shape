# points.py
import math

def arc_points(radius, start_angle, end_angle, center=[0,0], num_points=50):
    angles = [start_angle + i * (end_angle - start_angle) / (num_points - 1)
              for i in range(num_points)]
    points = [
        (center[0] + radius * math.cos(math.radians(angle)),
         center[1] + radius * math.sin(math.radians(angle)))
        for angle in angles
    ]
    return points

# A
A = [(0,0), (1/2, 1), (1, 0), (5/6, 0), (2/3, 1/3), (1/3, 1/3), (1/6, 0)]

# B
top_arc_points_B = arc_points(1/4, 90, -90, center=[3/4, 3/4])
bottom_arc_points_B = arc_points(1/4, 90, -90, center=[3/4, 1/4])
other_points_B = [(0,0), (0,1)]
B = top_arc_points_B + bottom_arc_points_B + other_points_B

# C
outer_arc_points_C = arc_points(1/2, 30, 330, center=[1/2,1/2])
inner_arc_points_C = arc_points(1/3, 30, 330, center=[1/2,1/2])[::-1]
C = outer_arc_points_C + inner_arc_points_C

# D
outer_arc_points_D = arc_points(1/2, 90, -90, center=[1/2, 1/2])
D = outer_arc_points_D + [(0,0), (0, 1)]

# E
E = [(0,0), (1,0), (1,1/5), (1/5,1/5), (1/5,2/5), (3/4,2/5), (3/4,3/5), (1/5,3/5), (1/5,4/5), (1,4/5), (1,1), (0,1)]

# F
F = [(0,0), (1/5,0), (1/5,2/5), (3/4,2/5), (3/4,3/5), (1/5,3/5), (1/5,4/5), (1,4/5), (1,1), (0,1)]

# G
outer_arc_points_G = arc_points(1/2, 30, 360, [1/2,1/2])
other_points_G = [(1/2,1/2), (1/2,1/3)]
x = math.sqrt(1/3**2 - 1/6**2)
theta = math.degrees(math.atan(1/6 * 1/x))
inner_arc_points_G = arc_points(1/3, -theta, -330, [1/2,1/2])
G = outer_arc_points_G + other_points_G + inner_arc_points_G

# H
H = [(0, 0), (0, 1), (1/6, 1), (1/6, 7/12), (5/6, 7/12), (5/6, 1), (1, 1), (1, 0), (5/6, 0), (5/6, 5/12), (1/6, 5/12), (1/6, 0)]

# I
I = [(0,0), (1,0), (1,1/6), (7/12,1/6), (7/12,5/6), (1,5/6), (1,1), (0,1), (0,5/6), (5/12,5/6), (5/12,1/6), (0,1/6)]

# J
inner_arc_J = arc_points(1/3, 360, 180, [1/2,1/2])
outer_arc_J = arc_points(1/2, 180, 360, [1/2,1/2])
other_points_J = [(1,1), (0,1), (0,5/6), (5/6,5/6)]
J = inner_arc_J + outer_arc_J + other_points_J

K = [(0,0), (1/6,0), (1/6, math.sqrt(2)/6), (1/2-math.sqrt(2)/12,1/2-math.sqrt(2)/12), (1-math.sqrt(2)/6,0), (1,0), (1/2,1/2), (1,1), (1-math.sqrt(2)/6,1), (1/6,math.sqrt(2)/3), (1/6,1), (0,1)]

# GROK
L = [(0,0), (0,1), (1/6,1), (1/6,1/6), (1,1/6), (1,0)]

M = [(1/6,0), (0,0), (0,1), (1/6,1), (1/2,1/6), (5/6,1), (1,1), (1,0), (5/6,0), (5/6,1-math.sqrt(2)/3), (1/2+math.sqrt(2)/12, 0), (1/2,0), (1/2-math.sqrt(2)/12, 0), (1/6,1-math.sqrt(2)/3)
     ]

N = [(0,0), (0,1), (1/6,1), (5/6,math.sqrt(2)/6), (5/6,1), (1,1), (1,0), (5/6,0), (1/6,1-math.sqrt(2)/6), (1/6,0)]

outer_arc_points_O = arc_points(1/2, 0, 360, [1/2,1/2])
inner_arc_points_O = arc_points(1/3, 360, 0, [1/2,1/2])
O = outer_arc_points_O + inner_arc_points_O

# P
p_arc = arc_points(1/4, 90, -90, center=[3/4, 3/4])
other_points = [(1/6,1/2), (1/6,0), (0,0), (0,1)]
P = p_arc + other_points