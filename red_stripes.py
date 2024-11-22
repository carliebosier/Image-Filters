import common

red_stripes = common.read_file("logo.jpeg")

stripe_height = 50
in_stripe = True  

for row in range(len(red_stripes)):
    if in_stripe:
        for col in range(len(red_stripes[0])):
            red_stripes[row][col] = (255, red_stripes[row][col][1], red_stripes[row][col][2])
    if (row + 1) % stripe_height == 0:
        in_stripe = not in_stripe  


# write the modified image to a new file, using common.write_file()
common.write_file("red_stripes.jpeg", red_stripes)


