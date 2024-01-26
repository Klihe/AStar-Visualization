import math

start_point = (0, 0)
end_point = (-4, -4)

def distance_point(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) * 10
    return distance

# Calculate and print the distance
distance = distance_point(start_point, end_point)
print(f"The distance between {start_point} and {end_point} is: {distance}")
