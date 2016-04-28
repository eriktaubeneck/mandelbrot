def compute_z_and_count(x, y, max_iter):
    count = 0
    z = 0.0
    c = complex(x, y)
    while count < max_iter:
        z = z ** 2 + c
        if abs(z) > 2.0:
            break
        count += 1
    return z, count
