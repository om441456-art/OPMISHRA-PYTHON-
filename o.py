import math

def print_star_circle(radius=5):
    for y in range(-radius, radius + 1):
        row = ""
        for x in range(-2 * radius, 2 * radius + 1):
            # adjust x scale for approximate circle shape
            dist = math.sqrt((x / 2) ** 2 + y ** 2)
            row += "*" if abs(dist - radius) < 0.7 else " "
        print(row)

if __name__ == "__main__":
    print_star_circle(5)