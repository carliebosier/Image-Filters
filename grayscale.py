import common
grayscale_image = common.read_file("logo.jpeg")

print(grayscale_image[0][0])
length = len(grayscale_image)
width = len(grayscale_image[0])

for row in range(length):
    for col in range(width):
        r, g, b = (grayscale_image[row][col])
        grays = int((r + g + b)/3)
        grayscale_image[row][col] = (grays, grays, grays)

common.write_file("grayscale_logo.jpeg", grayscale_image)
