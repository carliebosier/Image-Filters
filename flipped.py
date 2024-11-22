import common

def flip(image_matrix):
    flipped_image = image_matrix[::-1]

    return flipped_image

howard_pic = common.read_file("logo.jpeg")

flipped_howard_pic = flip(howard_pic)

common.write_file("flipped_logo.jpeg", flipped_howard_pic)
