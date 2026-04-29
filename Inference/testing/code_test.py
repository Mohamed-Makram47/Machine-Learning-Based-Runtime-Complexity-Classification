from math import sqrt

a, v = map(int, input().split())
l, d, w = map(int, input().split())

# Case 1: ignore speed limit
if v <= w or w*w >= 2*a*d:
    if v*v >= 2*a*l:
        print(sqrt(2*l/a))
    else:
        t = v/a
        s = v*v/(2*a)
        print(t + (l - s)/v)

# Case 2: speed limit matters
else:
    # before sign
    peak = sqrt((2*a*d + w*w)/2)
    
    if peak <= v:
        t1 = (peak - 0)/a
        t2 = (peak - w)/a
    else:
        t1 = v/a
        t2 = (v - w)/a
    
    # after sign
    s = (v*v - w*w)/(2*a)
    if s >= l - d:
        t3 = (sqrt(w*w + 2*a*(l - d)) - w)/a
    else:
        t3 = (v - w)/a + (l - d - s)/v

    print(t1 + t2 + t3)