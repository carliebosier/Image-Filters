import common

inverted_colors = common.read_file("logo.jpeg")

for row in range(len(inverted_colors)):
    for col in range(len(inverted_colors[row])):
        inverted_colors[row][col] = [255 - inverted_colors[row][col][0], 255 - inverted_colors[row][col][1], 255 - inverted_colors[row][col][2]]

common.write_file("invert_colors_logo.jpeg", inverted_colors)
