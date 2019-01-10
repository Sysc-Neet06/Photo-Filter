# SYSC 1005 A Fall 2017 Lab 7


import sys  
from Cimpl import * # Imports cimpl functions
from filters import  * # Imports functions from filters

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img


    
if __name__ == "__main__":
    
    loaded = False
    done = False
    
    while True:
        print("L)oad\nN)egative, G)rayscale, X)treme contrast, S)epia tint, E)Detect edge\nQ)uit:")
        ask = input(": ")
        
       
        if ask in ["L", "Q", "N", "G", "X", "S", "E"]:
                
            if ask == "L":
                # If L is inputted, it loads the image the user selects from files               
                image = get_image()
                loaded = True
            
            if ask == "N":
                # If N is selected with an image loaded it performs the 
                # Negative filter to the image that was loaded                
                if loaded == True:
                    negative(image)
                    show(image)
                else:
                    # else it will on print this statement if a image is not 
                    # loaded                    
                    print("No image loaded")
                
            if ask == "G":
                # If G is inputted with an image loaded it performs the 
                # weighted grayscale filter to the image that was loaded                
                if loaded == True:
                    weighted_grayscale(image)
                    show(image)
                else:
                    # else it will on print this statement if a image is not 
                    # loaded                    
                    print("No image loaded")
                
            if ask == "X":
                # If X is inputted with an image loaded it performs the 
                # extreme contrast filter to the image that was loaded                
                if loaded == True:
                    extreme_contrast(image)
                    show(image)
                else:
                    # else it will on print this statement if a image is not 
                    # loaded                    
                    print("No image loaded")
                
            if ask == "S":
                # If S is inputted with an image loaded it performs the 
                # sepia tint filter to the image that was loaded
                if loaded == True:
                    sepia_tint(image)
                    show(image)
                else:
                    # else it will on print this statement if a image is not 
                    # loaded
                    print("No image loaded")            
                
            if ask == "E":
                # If E is inputted with an image loaded it performs the 
                # detect edges function with a threshold value the user inputs
                if loaded == True:
                    threshold = int(input("threshold? "))
                    edges = detect_edges_better(image, threshold)                    
                    print(threshold)                    
                    show(edges)
                else:
                    # else it will on print this statement if a image is not 
                    # loaded                    
                    print("No image loaded")                

            if ask == "Q":
               # Done = True
                print("The program has finished")
                break
        else:
            # If a command that is not in the command list is entered it prints 
            # the following statement
            print("No such command")