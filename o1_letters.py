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
E = [(0,0), (1,0), (1,1/5), (1/5,1/5), (1/5,2/5), (3/4,2/5),
     (3/4,3/5), (1/5,3/5), (1/5,4/5), (1,4/5), (1,1), (0,1)]

# F
F = [(0,0), (1/5,0), (1/5,2/5), (3/4,2/5), (3/4,3/5),
     (1/5,3/5), (1/5,4/5), (1,4/5), (1,1), (0,1)]

# G
outer_arc_points_G = arc_points(1/2, 30, 360, [1/2,1/2])
# We'll add a small “inset” line to represent the cross stroke 
# and then an inner arc. The math below is a simplified approach
# so that the "open" side includes a short line plus the arc.
other_points_G = [(0.5,0.5), (0.7,0.5)]
inner_arc_points_G = arc_points(1/3, 330, 30, [0.5,0.5])  # reversed
G = outer_arc_points_G + other_points_G + inner_arc_points_G

# H
H = [(0, 0), (0, 1), (1/6, 1), (1/6, 7/12),
     (5/6, 7/12), (5/6, 1), (1, 1), (1, 0),
     (5/6, 0), (5/6, 5/12), (1/6, 5/12), (1/6, 0)]

# I
I = [(0,0), (1,0), (1,1/6), (7/12,1/6), (7/12,5/6),
     (1,5/6), (1,1), (0,1), (0,5/6), (5/12,5/6),
     (5/12,1/6), (0,1/6)]

# J
inner_arc_J = arc_points(1/3, 360, 180, [1/2,1/2])
outer_arc_J = arc_points(1/2, 180, 360, [1/2,1/2])
other_points_J = [(1,1), (0,1), (0,5/6), (5/6,5/6)]
J = inner_arc_J + outer_arc_J + other_points_J

# ------------------------------------------------------
# K through Z
# ------------------------------------------------------

# K
# Approx: left vertical bar + top diagonal + bottom diagonal
K = [
    # Left bar:
    (0,0), (0,1), (1/6,1), (1/6,0.6),
    # Upper diagonal "chunk":
    (5/6,1), (1,1), (1,0.9), (0.5,0.5),
    # Lower diagonal "chunk":
    (1,0.1), (1,0), (5/6,0), (1/6,0.4), (1/6,0)
]

# L
L = [
    (0,0), (1,0), (1,1/6),
    (1/6,1/6), (1/6,1), (0,1)
]

# M
# Two thick verticals plus diagonal peaks in the middle
M = [
    (0,0), (0,1), (1/6,1), (1/6,0.5),
    (1/2,0.2), (5/6,0.5), (5/6,1), (1,1),
    (1,0), (5/6,0), (5/6,0.4), (1/2,0.1),
    (1/6,0.4), (1/6,0)
]

# N
# Left bar + diagonal + right bar
N = [
    (0,0), (0,1), (1/6,1),
    (5/6,0), (1,0), (1,1),
    (5/6,1), (1/6,0)
]

# O
outer_arc_points_O = arc_points(1/2, 0, 360, [1/2,1/2])
inner_arc_points_O = arc_points(1/3, 360, 0, [1/2,1/2])
O = outer_arc_points_O + inner_arc_points_O

# P
# Similar to B but only a top bubble
p_arc = arc_points(1/4, 90, -90, center=[3/4, 3/4])
p_line = [(0,0), (0,1)]
P = p_arc + p_line

# Q
# Like O but with a small slash
outer_arc_points_Q = arc_points(1/2, 0, 360, [1/2,1/2])
inner_arc_points_Q = arc_points(1/3, 360, 0, [1/2,1/2])
slash_points_Q = [(0.65,0.3), (0.8,0.15), (1,0.3)]  # small slash
Q = outer_arc_points_Q + slash_points_Q + inner_arc_points_Q

# # R
# # Like P but add a diagonal leg
# top_arc_R = arc_points(1/4, 90, -90, center=[3/4, 3/4])
# other_points_R = [(0,0), (0,1), (0.5,0.4), (1,0)]
# R = top_arc_R + other_points_R

# # S
# # Approx: top arc + bottom arc, outer then inner reversed
# # We'll do two arcs for top (outer, inner) and two arcs for bottom (outer, inner).
# # This is quite rough but demonstrates the idea.
# top_outer_S   = arc_points(0.5,  30, 180,  [0.5, 0.75])
# top_inner_S   = arc_points(0.3333, 180,  30, [0.5, 0.75])
# bot_outer_S   = arc_points(0.5,  180, 330, [0.5, 0.25])
# bot_inner_S   = arc_points(0.3333, 330, 180,[0.5, 0.25])
# S = top_outer_S + top_inner_S + bot_outer_S + bot_inner_S

# # T
# # Top bar + thick vertical
# T = [
#     (0,1), (1,1), (1,5/6), (5/6,5/6),
#     (5/6,0), (1/6,0), (1/6,5/6), (0,5/6)
# ]

# # U
# # Two vertical bars connected by a bottom arc
# left_side_U  = [(0,1), (1/6,1), (1/6,1/6)]
# arc_bottom_U = arc_points(1/3, 180, 0, [0.5,1/6])
# right_side_U = [(5/6,1/6), (5/6,1), (1,1)]
# U = left_side_U + arc_bottom_U + right_side_U

# # V
# V = [
#     (0,1), (1/6,1), (1/2,0), (5/6,1), (1,1)
# ]

# # W
# # Like M mirrored in the middle, for a double peak
# W = [
#     (0,1), (1/6,1), (1/4,0.4), (0.5,0.6),
#     (3/4,0.4), (5/6,1), (1,1), (0.85,1),
#     (0.75,0.45), (0.5,0.65), (0.25,0.45), (0.15,1)
# ]

# # X
# # Two thick diagonals forming X
# X = [
#     (0,0), (0,0.1), (0.4,0.5), (0,0.9), (0,1),
#     (0.1,1), (0.5,0.6), (0.9,1), (1,1), (1,0.9),
#     (0.6,0.5), (1,0.1), (1,0), (0.9,0), (0.5,0.4),
#     (0.1,0), (0,0)
# ]

# # Y
# # Top arms + a vertical bar
# Y = [
#     (0,1), (0.3,1), (0.5,0.6), (0.7,1), (1,1),
#     (0.6,0.5), (0.6,0), (0.4,0), (0.4,0.5)
# ]

# # Z
# Z = [
#     (0,1), (1,1), (1,0.9), (0.2,0.1),
#     (0,0.1), (0,0), (1,0), (1,0.1),
#     (0.8,0.3), (0.8,0.3), (0.2,0.9), (0,0.9)
# ]
import math

def arc_points(radius, start_angle, end_angle, center=[0,0], num_points=50):
    """
    Returns a list of (x, y) points approximating
    an arc of 'radius' from 'start_angle' to 'end_angle'
    (in degrees), centered at 'center'.
    """
    angles = [
        start_angle + i*(end_angle - start_angle)/(num_points - 1)
        for i in range(num_points)
    ]
    pts = [
        (
            center[0] + radius*math.cos(math.radians(a)),
            center[1] + radius*math.sin(math.radians(a))
        )
        for a in angles
    ]
    return pts

# -------------------------------------------------------------------
# Existing A–Q definitions go here (your code).
# e.g.
#
# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q
# -------------------------------------------------------------------

# R: Similar to P, but adding a diagonal “leg”
# P had a top arc for the “bubble” plus a vertical spine.
# We’ll reuse that arc and then add a line for the diagonal.
def letter_R():
    r_arc = arc_points(1/4, 90, -90, center=[3/4, 3/4])  # top bubble arc
    # We’ll splice in a diagonal from (1/6, 1/2) out to (1,0),
    # then continue the spine down to (1/6, 0) and back to (0,0)->(0,1).
    other_points_R = [
        (1/6, 1/2),  # where bubble meets spine
        (1, 0),      # diagonal leg to bottom-right
        (1/6, 0),
        (0, 0),
        (0, 1)
    ]
    return r_arc + other_points_R

R = letter_R()

# S: Approximate “S” shape with a top curve & bottom curve
# We can approximate with two arcs in the top half and two arcs in the bottom half.
def letter_S():
    # Top outer arc (roughly from ~20° to ~160°),
    # centered slightly above the midpoint so it bulges near top
    top_outer = arc_points(0.5, 20, 160, center=[0.5, 0.65])
    top_inner = arc_points(1/3, 160, 20, center=[0.5, 0.65])  # reversed

    # Bottom outer arc (roughly from ~200° to ~340°),
    # centered below the midpoint
    bot_outer = arc_points(0.5, 200, 340, center=[0.5, 0.35])
    bot_inner = arc_points(1/3, 340, 200, center=[0.5, 0.35])  # reversed

    return top_outer + top_inner + bot_outer + bot_inner

S = letter_S()

# T: Horizontal bar on top, vertical bar in center
def letter_T():
    # Wide top bar from y=1 down to y=5/6,
    # then a vertical bar approx from x=5/12..7/12
    return [
        (0,   1), (1,   1), (1,   5/6), (7/12, 5/6),
        (7/12, 0), (5/12, 0), (5/12, 5/6), (0,   5/6)
    ]

T = letter_T()

# U: Two vertical strokes joined by an arc at bottom
def letter_U():
    # Left vertical from (0,1) to (1/6,1)->(1/6,1/6)
    left_side  = [(0,1), (1/6,1), (1/6,1/6)]

    # Arc along bottom from x=1/6 to x=5/6
    # So center around [0.5, 1/6], radius=0.333 -> thickness 1/6
    bottom_arc_outer = arc_points(1/2, 180, 0, center=[0.5, 1/6])
    bottom_arc_inner = arc_points(1/3, 0, 180, center=[0.5, 1/6])  # reversed

    # Right vertical from (5/6,1/6) up to (5/6,1)->(1,1)
    right_side = [(5/6,1/6), (5/6,1), (1,1)]

    return left_side + bottom_arc_outer + bottom_arc_inner + right_side

U = letter_U()

# V: Simple “V” shape. For thickness, we do a polygon that
# extends slightly left/right at top & near bottom center.
def letter_V():
    # Top left -> top right -> near bottom
    # Add slight offsets for thickness if needed
    return [
        (0,1), (1/6,1),   # left top
        (1/2,0),          # bottom
        (5/6,1), (1,1)    # right top
    ]

V = letter_V()

# W: Like “double V”
def letter_W():
    # We can create a shape with two “V” peaks
    # This is a rough outline:
    return [
        (0,1), (1/6,1),       # left top
        (1/4,0.4), (1/2,0.7), # mid peaks
        (3/4,0.4), (5/6,1),
        (1,1)
    ]

W = letter_W()

# X: Two thick diagonals crossing. 
def letter_X():
    # A simple approach: outline that zig-zags
    return [
        (0,0), (0,0.1), (0.4,0.5), (0,0.9), (0,1),
        (0.1,1), (0.5,0.6), (0.9,1), (1,1), (1,0.9),
        (0.6,0.5), (1,0.1), (1,0), (0.9,0), (0.5,0.4),
        (0.1,0), (0,0)
    ]

X = letter_X()

# Y: top arms + vertical down
def letter_Y():
    # Rough shape: (0,1)->(0.4,0.6)->(0.4,0)->(0.6,0)->(0.6,0.6)->(1,1)
    # etc.  Adjust as desired for thickness.
    return [
        (0,1), (0.3,1), (0.5,0.6),
        (0.7,1), (1,1), (0.6,0.5),
        (0.6,0), (0.4,0), (0.4,0.5)
    ]

Y = letter_Y()

# Z: Top bar, diagonal, bottom bar
def letter_Z():
    # Top from (0,1)->(1,1), diagonal to bottom left, bottom bar
    return [
        (0,1), (1,1), (1,0.9), (0.3,0.1),
        (0,0.1), (0,0), (1,0), (1,0.1),
        (0.7,0.9), (0.7,0.9), (0,0.9)
    ]

Z = letter_Z()

# --------------------------
# Example usage / debugging:
if __name__ == "__main__":
    # Print the first few points of each letter for sanity check
    for ch, pts in zip(
        ["R","S","T","U","V","W","X","Y","Z"],
        [R,S,T,U,V,W,X,Y,Z]
    ):
        print(f"{ch} => {pts[:5]} ... total {len(pts)} points")

