import common
import copy

def blur(image_matrix):
    image = copy.deepcopy(image_matrix)
    up = [-1,0]
    down = [1,0]
    left = [0,-1]
    right = [0,1] 
    top_left = [-1,-1] 
    top_right = [-1,1] 
    bottom_left = [1,-1]
    bottom_right = [1,1]
    for row in range(1,len(image)-1):#0
        for col in range(1,len(image[row])-1): #0
            pixel = image[row][col]
            pixel_bottom_left = image[row+1][col-1]
            pixel_down = image[row+1][col]
            pixel_down_right = image[row+1][col+1]
            pixel_left = image[row][col-1]
            pixel_right = image[row][col+1]
            pixel_top = image[row-1][col]
            pixel_top_left = image[row-1][col-1]
            pixel_top_right = image[row-1][col+1]
            avg_red = (pixel[0]+pixel_bottom_left[0]+pixel_down[0]+pixel_down_right[0]+pixel_left[0]+pixel_right[0]+pixel_top[0]+pixel_top_left[0]+pixel_top_right[0])//9
            avg_green = (pixel[1]+pixel_bottom_left[1]+pixel_down[1]+pixel_down_right[1]+pixel_left[1]+pixel_right[1]+pixel_top[1]+pixel_top_left[1]+pixel_top_right[1])//9
            avg_blue = (pixel[2]+pixel_bottom_left[2]+pixel_down[2]+pixel_down_right[2]+pixel_left[2]+pixel_right[2]+pixel_top[2]+pixel_top_left[2]+pixel_top_right[2])//9
            image_matrix[row][col] = [avg_red,avg_green,avg_blue]
    return image_matrix
"""
            pixel = image_matrix[row][col]
            if row == 0: #first row
                if col == 0: #first row first col
                    pixel_right = image_matrix[row + right[0]][col + right[1]]
                    pixel_down = image_matrix[row + down[0]][col + down[1]]
                    pixel_down_right = image_matrix[row + bottom_right[0]][col + bottom_right[1]]
                        #find average
                    avg_red = (pixel_down[0] + pixel_down_right[0] + pixel_right[0])//3
                    avg_green = (pixel_down[1] + pixel_down_right[1] + pixel_right[1])//3
                    avg_blue = (pixel_down[2] + pixel_down_right[2] + pixel_right[2])//3
                    image_matrix[row][col] = [avg_red,avg_green,avg_blue]
                    if col == len(image_matrix[row])-1: #firist row last col
                        pixel_left = image_matrix[row + left[0]][col + left[1]]
                        pixel_down = image_matrix[row + down[0]][col + down[1]]
                        pixel_bottom_left = image_matrix[row + bottom_left[0]][col + bottom_left[1]]
                        avg_red = (pixel_down[0] + pixel_bottom_left[0] + pixel_left[0])//3
                        avg_green = (pixel_down[1] + pixel_bottom_left[1] + pixel_left[1])//3
                        avg_blue = (pixel_down[2] + pixel_bottom_left[2] + pixel_left[2])//3
                        image_matrix[row][col] = [avg_red,avg_green,avg_blue]
            if row == len(image_matrix)-1: #last row
                if col == 0: #last row first col
                    pixel_top = image_matrix[row + top[0]][col + top[1]]
                    pixel_top_right = image_matrix[row + top_right[0]][col + top_right[1]]
                    pixel_right = image_matrix[row + right[0]][col + right[1]]
                        #find average
                    avg_red = (pixel_top[0] + pixel_top_right[0] + pixel_right[0])//3
                    avg_green = (pixel_top[1] + pixel_top_right[1] + pixel_right[1])//3
                    avg_blue = (pixel_top[2] + pixel_top_right[2] + pixel_right[2])//3
                    image_matrix[row][col] = [avg_red,avg_green,avg_blue]
                    if col == len(image_matrix[row])-1: #last row last col
                        pixel_left = image_matrix[row + left[0]][col + left[1]]
                        pixel_top = image_matrix[row + top[0]][col + top[1]]
                        pixel_top_left = image_matrix[row + top_left[0]][col + top_left[1]]
                        avg_red = (pixel_top[0] + pixel_top_left[0] + pixel_left[0])//3
                        avg_green = (pixel_top[1] + pixel_top_left[1] + pixel_left[1])//3
                        avg_blue = (pixel_top[2] + pixel_top_left[2] + pixel_left[2])//3
                        image_matrix[row][col] = [avg_red,avg_green,avg_blue]
                        
            pixel_bottom_left = image_matrix[row+1][col-1]
            pixel_down = image_matrix[row+1][col]
            pixel_down_right = image_matrix[row+1][col+1]
            pixel_left = image_matrix[row][col-1]
            pixel_right = image_matrix[row][col+1]
            pixel_top = image_matrix[row-1][col]
            pixel_top_left = image_matrix[row-1][col-1]
            pixel_top_right = image_matrix[row-1][col+1]
            avg_red = (pixel[0]+pixel_bottom_left[0]+pixel_down[0]+pixel_down_right[0]+pixel_left[0]+pixel_right[0]+pixel_top[0]+pixel_top_left[0]+pixel_top_right[0])//9
            avg_green = (pixel[1]+pixel_bottom_left[1]+pixel_down[1]+pixel_down_right[1]+pixel_left[1]+pixel_right[1]+pixel_top[1]+pixel_top_left[1]+pixel_top_right[1])//9
            avg_blue = (pixel[2]+pixel_bottom_left[2]+pixel_down[2]+pixel_down_right[2]+pixel_left[2]+pixel_right[2]+pixel_top[2]+pixel_top_left[2]+pixel_top_right[2])//9
            image_matrix[row][col] = [avg_red,avg_green,avg_blue]

             
    num_pixels = len (image_matrix)
    r_tot = 0
    for pixel in image_matrix:
        r_tot = r_tot + pixel[0]
        new_r = r_tot / num_pixels
"""

    #return image_matrix

howard_pic = common.read_file("images/logo.jpeg")

#apply the red stripe filter to the image 
blur_filter = blur(howard_pic)

# write the modified image to a new file, using common.write_file()
common.write_file("blur_logo.jpeg", blur_filter)
