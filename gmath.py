import math
from display import *

# IMPORANT NOTE

# Ambient light is represeneted by a color value

# Point light sources are 2D arrays of doubles.
#      - The fist index (LOCATION) represents the vector to the light.
#      - The second index (COLOR) represents the color.

# Reflection constants (ka, kd, ks) are represened as arrays of
# doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4


# lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect):
    normalize(normal)
    normalize(view)
    normalize(light[0])
    return limit_color([calculate_ambient(ambient, areflect)[k] + calculate_diffuse(light, dreflect, normal)[k] +
             calculate_specular(light, sreflect, view, normal)[k] for k in range(3)])


def calculate_ambient(alight, areflect):
    return [alight[k] * areflect[k] for k in range(3)]


def calculate_diffuse(light, dreflect, normal):
    angle = dot_product(normal, light[0])
    if angle < 0:
        return (0, 0, 0)
    return [light[1][k] * dreflect[k] * angle for k in range(3)]


def calculate_specular(light, sreflect, view, normal):
    t_angle = dot_product(normal, light[0])
    if t_angle < 0:
        return (0, 0, 0)
    right_thing = [2 * t_angle * normal[k] - light[0][k] for k in range(3)]
    right_thing_2 = pow(dot_product(right_thing, view), 3)
    return [light[1][k] * sreflect[k] * right_thing_2 for k in range(3)]


def limit_color(color):
    return [max(min(255, int(k)),0) for k in color]


# vector functions
# normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt(vector[0] * vector[0] +
                          vector[1] * vector[1] +
                          vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude


# Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


# Calculate the surface normal for the triangle whose first
# point is located at index i in polygons
def calculate_normal(polygons, i):
    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i + 1][0] - polygons[i][0]
    A[1] = polygons[i + 1][1] - polygons[i][1]
    A[2] = polygons[i + 1][2] - polygons[i][2]

    B[0] = polygons[i + 2][0] - polygons[i][0]
    B[1] = polygons[i + 2][1] - polygons[i][1]
    B[2] = polygons[i + 2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
