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

theta = math.degrees(math.atan(math.sqrt(5)/2))
q_arc = arc_points(1/2, -theta, 270, center=[1/2,1/2])
other_points = [(1,0), (1,1/6)]
Q = q_arc + other_points

r_arc = arc_points(1/4, 90, -90, center=[3/4, 3/4])
other_points = [(1/2, 1/2), (1,0), (1-math.sqrt(2)/6,0), (1/2-math.sqrt(2)/6,1/2), (1/6,1/2), (1/6,0), (0,0), (0,1)]
R = r_arc + other_points

arc_1 = arc_points(7/24, 0, 90, center=[17/24,17/24])
arc_2 = arc_points(7/24, 90, 270, center=[7/24,17/24])
arc_3 = arc_points(1/8, 90, -90, center=[17/24,7/24])
arc_4 = arc_points(1/8, 270, 180, center=[7/24,7/24])
arc_5 = arc_points(7/24, 180, 270, center=[7/24,7/24])
arc_6 = arc_points(7/24, -90, 90, center=[17/24,7/24])
arc_7 = arc_points(1/8, 270, 90, center=[7/24,17/24])
arc_8 = arc_points(1/8, 90, 0, center=[17/24,17/24])
S = arc_1 + arc_2 + arc_3 + arc_4 + arc_5 + arc_6 + arc_7 + arc_8

T = [(0,1), (1,1), (1,5/6), (7/12,5/6), (7/12,0), (5/12,0), (5/12,5/6), (0,5/6)]

# U
outer_arc_U = arc_points(1/2, 180, 360, center=[1/2, 1/2])
other_points_U = [(1,1), (5/6,1), (5/6,1/2)]
inner_arc_U = arc_points(1/3, 360, 180, center=[1/2, 1/2])
other_other_points = [(1/6,1), (0,1)]
U = outer_arc_U + other_points_U + inner_arc_U + other_other_points

V = [(0,1), (1/6,1), (1/2,1/6), (5/6,1), (1,1), (3/5,0), (2/5,0)]

W = [(0,1), (1/6,1), (1/3,1/6), (2/5,1/2), (3/5,1/2), (2/3,1/6), (5/6,1), (1,1), (4/5,0), (17/30,0), (1/2,1/3), (13/30,0), (1/5,0)]

X = [(0,0), (math.sqrt(2)/6,0), (1/2,(6-math.sqrt(2))/12), (1-math.sqrt(2)/6,0), (1,0), ((6+math.sqrt(2))/12,1/2), (1,1), (1-math.sqrt(2)/6,1), (1/2,(6+math.sqrt(2))/12), (math.sqrt(2)/6,1), (0,1), ((6-math.sqrt(2))/12,1/2)]

Y = [((6+math.sqrt(2))/12,1/2), (1,1), (1-math.sqrt(2)/6,1), (1/2,(6+math.sqrt(2))/12), (math.sqrt(2)/6,1), (0,1), ((6-math.sqrt(2))/12,1/2), (5/12,11/24), (5/12,0), (7/12,0), (7/12,11/24)]

Z = [(0, 0),(1, 0),(1, 1/6),((17/6 + 17*math.sqrt(2)*(6+math.sqrt(2))/34) / (3*(6+math.sqrt(2))), 1/6),(1,1),(0,1),(0,5/6),(85/(18*(6+math.sqrt(2))), 5/6)]