#turns the image into like a blueish hue, like a twilight filter 
import common

def custom(image_matrix, red_min, red_max, green_min, green_max, blue_min, blue_max):
    length = len(image_matrix)
    width = len(image_matrix[0])
    for row in range(length):
        for col in range(width):
            red, green, blue = image_matrix[row][col]
            if red_min < red <= red_max and green_min < green <= green_max and blue_min < blue <= blue_max:
                pass
            else:
                image_matrix[row][col] = [0, 0, 0]

            red = min(max(0, red), 120)
            green = min(max(0, green), 200)
            blue = min(max(0, blue), 200)
            image_matrix[row][col] = [red, green, blue]

    return image_matrix

red_min = 50
red_max = 150
green_min = 100
green_max = 200
blue_min = 0
blue_max = 100

# Read an image using common.read_file()
howard_pic = common.read_file("twilighty.jpeg")

# Apply the threshold filter to the image
custom_filter = custom(howard_pic, red_min, red_max, green_min, green_max, blue_min, blue_max)

# Write the modified image to a new file using common.write_file()
common.write_file("twilighty.jpeg", custom_filter)
