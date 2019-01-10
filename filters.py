""" SYSC 1005 A Fall 2017.

Filters for a photo-editing application.
"""

from Cimpl import * # Imports Cimpl functions

# grayscale, solarize, black_and_white and black_and_white_and_gray
# were presented in class.

def grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)    
    """
    for pixel in image:
        x, y, (r, g, b) = pixel

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
    
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def solarize(image):
    """ (Cimpl.Image) -> None
    
    Solarize image.
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image)
    >>> show(image)     
    """
    for pixel in image:
        x, y, (red, green, blue) = pixel

        # Invert the values of all RGB components that are less than 128,
        # leaving components with higher values unchanged.

        if red < 128:
            red = 255 - red

        if green < 128:
            green = 255 - green

        if blue < 128:
            blue = 255 - blue
            
        col = create_color(red, green, blue)
        set_color(image, x, y, col)


def black_and_white(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white (two-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white(image)
    >>> show(image)     
    """
    # Creates the color black
    black = create_color(0, 0, 0)
    # Creates the color white
    white = create_color(255, 255, 255)
    
    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on 
    # whether its brightness is in the lower or upper half of this range.       

    for pixel in image:
        x, y, (red, green, blue) = pixel

        brightness = (red + green + blue) // 3      
        
        if brightness < 128:
            set_color(image, x, y, black)
        else:      # brightness is between 128 and 255, inclusive              
            set_color(image, x, y, white)


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white-and-gray (three-tone) image.

    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)     
    """
    # Creates the color black
    black = create_color(0, 0, 0)
    # Creates the color gray
    gray = create_color(128, 128, 128)
    # Creates the color white
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for pixel in image:
        x, y, (red, green, blue) = pixel
        
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(image, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(image, x, y, white)
            
            
def weighted_grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> weighted_grayscale(image)
    >>> show(image)    
    """
    for pixel in image:
        x, y, (r, g, b) = pixel

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r * 0.299 + g * 0.587 + b * 0.114)
        
        # takes all red, blue, green components and multiplies by its repective 
        # ratio and sets the value created as the new brightness value for each
        # components
       
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)
        

        
def negative(image):
    """ (Cimpl.Image) -> None
    
    Convert image into a negative version of the original image
    
    >>> image = load_image(choose_file()) 
    >>> negative(image)
    >>> show(image)    
    """
    for pixel in image:
        x, y, (red, green, blue) = pixel
        
        red = 255 - red
        green = 255 - green
        blue = 255 - blue
        
        col = create_color(red, green, blue)
        set_color(image, x, y, col)
        
def solarize(image, threshold):
    """ (Cimpl.Image) -> None
    
    Solarize image.
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image)
    >>> show(image)     
    """
    for pixel in image:
        x, y, (red, green, blue) = pixel

        # Invert the values of all RGB components that are less than 128,
        # leaving components with higher values unchanged.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(image, x, y, col)
        
def extreme_contrast(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white (two-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white(image)
    >>> show(image)     
    """
    
    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on 
    # whether its brightness is in the lower or upper half of this range.       

    for pixel in image:
        x, y, (red, green, blue) = pixel   
        
        if red < 128:
            red = 0
        else:     # brightness is between 128 and 255, inclusive
            red = 255
            
        if green < 128:
            green = 0
        else:       # brightness is between 128 and 255, inclusive
            green = 255
            
        if blue < 128:
            blue = 0
        else:       # brightness is between 128 and 255, inclusive
            blue = 255
            
        col = create_color(red, green, blue)
        set_color(image, x, y, col)
        
def sepia_tint(image):
    """(Cimple.Image)  -> None
    
    Convert image to sepia tones.
    
    >>>image = load_image(choose_file())
    >>>sepia_tint(image)
    >>>show(image)
    """
    # Grayscales the image that is loaded because all pixel values will be 
    # of the same shade of color
    grayscale(image)
    
    # Pixels will then be modified by a ratio depending on the pictures rgb 
    # values
    for pixel in image:
        x, y, (red, green, blue) = pixel
        
        if red < 64:
            red = red * 1.1
           
        elif red < 192:
            red = red * 1.15
        else:
            red = red * 1.08
            
        if blue < 64:
            blue = blue * 0.9
        elif blue < 192:
            blue = blue * 0.85
        else:
            blue = blue * 0.93
            
        
        col = create_color(red, green, blue)
        set_color(image, x, y, col)
            
            
def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)  
    """

    # Creates a copy of the original image
    target = copy(image)
    
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_r, top_g, top_b = get_color(image, x, y - 1)
            left_r, left_g, left_b = get_color(image, x - 1, y)
            bottom_r, bottom_g, bottom_b = get_color(image, x, y + 1)
            right_r, right_g, right_b = get_color(image, x + 1, y)
            center_r, center_g, center_b = get_color(image, x, y)

            # Average the red components of the five pixels
            new_r = (top_r + left_r + bottom_r +
                       right_r + center_r ) // 5

            # Average the green components of the five pixels
            new_g = (top_g + left_g + bottom_g +
                                   right_g + center_g ) // 5

            # Average the blue components of the five pixels
            new_b = (top_b + left_b + bottom_b +
                                   right_b + center_b ) // 5

            new_color = create_color(new_r, new_g, new_b)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target


def detect_edges(image, threshold):
    """(climp.image, float) -> None
    
    Modify image using edge detection.
    An edge is detected when a pxiel's brightness differs
    from that od its neighbour by an amount that is great 
    then the specified threshold.
    
    >>>image = load_image(choose_file())
    >>>edges = detect_edges(image, 10.0)
    >>>show(edges)
    """
    
    # Creates a copy of the original image
    target = copy(image)
    
    
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    
    # Checks the neighbouring pixels
    for y in range (1, get_height(image) - 1):
        for x in range (1, get_width(image) - 1):
            
            # Unpacks the color tuple to obtain the values of the rgb values 
            # of the top and centre of the image 
            top_r, top_g, top_b = get_color(image, x, y -1)
            centre_r, centre_g, centre_b = get_color(image, x, y)
             
            top_brightness = (top_r + top_g + top_b) // 3
            centre_brightness = (centre_r + centre_g + centre_b) // 3
             
            contrast = abs(top_brightness - centre_brightness)
             
             # Checks if the contrast value is less than the threshold specified
            if contrast < threshold:
                set_color(target, x, y, white)
            else:
                set_color(target, x, y, black)
                 
    return target


def detect_edges_better(image, threshold):
    """(climp.image, float) -> None
    
    Modify image using edge detection.
    An edge is detected when a pxiel's brightness differs
    from that od its neighbour by an amount that is great 
    then the specified threshold.
    
    >>>image = load_image(choose_file())
    >>>Edges = detect_edges(image, 10.0)
    >>>show(Edges)
    """
    # Creates a copy of the image
    target = copy(image)
    
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    
    for y in range (1, get_height(image) - 1):
        for x in range (1, get_width(image) - 1):
            
             # Unpacks the color tuple to obtain the values of the rgb values 
            # of the top, centre and right of the image
            top_r, top_g, top_b = get_color(image, x, y -1)
            centre_r, centre_g, centre_b = get_color(image, x, y)
            right_r, right_g, right_b = get_color(image, x + 1, y)
             
            top_brightness = (top_r + top_g + top_b) // 3
            centre_brightness = (centre_r + centre_g + centre_b) // 3
            right_brightness = (right_r + right_g + right_b) // 3
             
            contrast_top_centre = abs(top_brightness - centre_brightness)
            contrast_right_centre = abs(right_brightness - centre_brightness)
             
             # Checks if the contrast of the top or the contrast of the centre 
             # right are less than threshold
            if contrast_top_centre < threshold or \
               contrast_right_centre < threshold:
                
                set_color(target, x, y, white)
            else:
                set_color(target, x, y, black)
                 
    return target


def blur_changed(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur_changed(original)
    show(original)
    show(blurred)    
    """

    # Modifies a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    # Creates a copy of the original image
    target = copy(image)
    
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            red_sum = 0
            green_sum = 0
            blue_sum = 0
            
            # Checks neighbouring pixels and applies the blur filter
            for y1 in range (y-1,y+2):
                for x1 in range (x-1,x+2):
                    r, g, b = get_color(image, x1, y1)
                
                    r_sum += r
                    g_sum += g
                    b_sum += b
                    
                    new_r = r_sum // 9
                    new_g = g_sum // 9
                    new_b = b_sum // 9 
            
                    new_color = create_color(new_r, new_g, new_b)
                    set_color(target, x, y, new_color)
    
    # Returns the image that has been modified 
    return target

