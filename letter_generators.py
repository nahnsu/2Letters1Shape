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