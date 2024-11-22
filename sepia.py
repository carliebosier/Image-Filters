import common
def sepia(image_matrix):
    
    print(image_matrix[0][0])
    length = len(image_matrix)
    width = len(image_matrix[0])

    for row in range(length):
        for col in range(width):
            red, green, blue = image_matrix[row][col]
            output_red = int(red * 0.393) + int(green * 0.769) + int(blue * 0.189)
            output_green = int(red * 0.349) + int(green * 0.686) + int(blue * 0.168)
            output_blue = int(red * 0.272) + int(green * 0.534) + int(blue * 0.131)
            if output_red > 255:
                output_red = 255
            if output_blue > 255:
                output_blue = 255
            if output_green > 255:
                output_green = 255
            image_matrix[row][col] = (output_red, output_green, output_blue)

    return image_matrix

# read an image in the same folder using common.read_file()
howard_pic = common.read_file("logo.jpeg")

#apply the red stripe filter to the image 
sepia_filter = sepia(howard_pic)

# write the modified image to a new file, using common.write_file()
common.write_file("sepia_logo.jpeg", sepia_filter)
