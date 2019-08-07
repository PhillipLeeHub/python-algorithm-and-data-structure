#      x     y    x     y
#r1 = [[0,    0], [5,    5]]
r1 = [[-5,    -5], [-2,    -2]]
r2 = [[7,    1], [1,    8]]
r3 = [[-1.2, 4], [3.7, 1.1]]

def rect_intersection_area(r1, r2, r3):
    area = 0 
    
    r1_p1, r1_p2 = r1 
    r2_p1, r2_p2 = r2 
    r3_p1, r3_p2 = r3 
    right_x_p = 0
    left_x_p = 0
    top_y_p = 0 
    bottom_y_p = 0
    
    # check for x    
    # max of left
    left_x_p = max(min(r2_p1[0], r2_p2[0]), min(r1_p1[0], r1_p2[0]), min(r3_p1[0], r3_p2[0]))

    # min of right
    right_x_p = min(max(r2_p1[0], r2_p2[0]), max(r1_p1[0], r1_p2[0]), min(r3_p1[0], r3_p2[0]))

    
    # max of left
    top_y_p = max(min(r2_p1[1], r2_p2[1]), min(r1_p1[1], r1_p2[1]), min(r3_p1[1], r3_p2[1]))

    # min of right
    bottom_y_p = min(max(r2_p1[1], r2_p2[1]), max(r1_p1[1], r1_p2[1]), min(r3_p1[1], r3_p2[1]))

    print('left_x_p:', left_x_p)
    print('right_x_p:', right_x_p)
    print('top_y_p:', top_y_p)
    print('bottom_y_p:', bottom_y_p)
    y_length = max(top_y_p, bottom_y_p) - min(top_y_p, bottom_y_p)
    x_length = max(left_x_p, right_x_p) - min(left_x_p, right_x_p)
    
    if right_x_p < left_x_p:
        # no overlap
        return 0
    if bottom_y_p < top_y_p:
        # no overlap
        return 0
    
    area = y_length * x_length    
    return area

#def is_within()

print(rect_intersection_area(r1, r2, r3))
