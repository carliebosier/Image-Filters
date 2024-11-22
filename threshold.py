import common 

def threshold(image_matrix, red_min, red_max, green_min, green_max, blue_min, blue_max):

    length = len(image_matrix)
    width = len(image_matrix[0])

    for row in range(length):
        for col in range(width):
            red, green, blue = image_matrix[row][col]
            if red < red_min or red >= red_max:
                red = 0
            if green < green_min or green >= green_max:
                green = 0
            if blue < blue_min or blue >= blue_max:
                blue = 0
            image_matrix[row][col] = [red, green, blue]

    return image_matrix

red_min = 0
red_max = 120
green_min = 0
green_max = 200
blue_min = 0
blue_max = 200

# Read an image using common.read_file()
howard_pic = common.read_file("logo.jpeg")

# Apply the threshold filter to the image
threshold_filter = threshold(howard_pic, red_min, red_max, green_min, green_max, blue_min, blue_max)

# Write the modified image to a new file using common.write_file()
common.write_file("threshold_logo.jpeg", threshold_filter)
