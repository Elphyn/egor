def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    while True:
        points.append((x0, y0))

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x0 += sx

        if e2 < dx:
            err += dx
            y0 += sy

    return points


def main():
    x0, y0 = map(int, input("Enter starting point (x0, y0): ").split())
    x1, y1 = map(int, input("Enter ending point (x1, y1): ").split())

    points = bresenham_line(x0, y0, x1, y1)

    print("Line points:")
    for point in points:
        print(point)


if __name__ == "__main__":
    main()
