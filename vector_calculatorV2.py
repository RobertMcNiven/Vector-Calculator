import math

try:
    amount_of_vectors = int(input('How many vectors would you like to add?' + '\n'))
except:
    print('Please enter an integer greater than 0')
    exit()

def vector_physics():
    x_component = 0
    y_component = 0
    for numbers in range(1, amount_of_vectors+1):
        vector_direction_degrees = float(input('What is the direction of vector #' + str(numbers) + '\n'))
        magnitude_of_x = float(input('What is the magnitude of the x-component of vector #' + str(numbers) + '\n'))
        magnitude_of_y = float(input('What is the magnitude of the y-component of vector #' + str(numbers) + '\n'))

        vector_direction_radians = vector_direction_degrees*(math.pi/180)
        x_component = x_component + (magnitude_of_x * math.cos(vector_direction_radians))
        y_component = y_component + (magnitude_of_y * math.sin(vector_direction_radians))

    r_magnitude = math.sqrt(x_component**2 + y_component**2)

    print('X Comp: ' + str(x_component))
    print('y Comp: ' + str(y_component))
    print('Resultant vector magnitude: ' + str(r_magnitude))
    try:
        r_direction = y_component/x_component
        print('The arc-tan of ' + str(r_direction) + " is the resultant vectors direction")
    except:
        print('The direction of the vector is undefined due to the x-component adding up to 0')

if amount_of_vectors > 0:
    vector_physics()
else:
    print('Please enter an integer greater than 0')
