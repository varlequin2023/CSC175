# Lab 6 by Vincent Arlequin - FA/24 CSC-175-02 - 10/11/24

# Imports image manipulation module
import image

# Purpose: Creates a window and displays a given image
# Assumptions: Parameter is an existing image object, image module is imported
# Parameters: An image object
# Post Conditions: Displays the image witin the given image object
def showImage(img):
    # Creates a window object the same size as the given image
    window = image.ImageWin(img.getWidth(), img.getHeight())
    # Draws the given image within the new window object
    img.draw(window)

# Purpose: Calculates and returns the number of pixels within a given image object
# Assumptions: Parameter is an existing image object, image module is imported
# Parameters: An image object
# Post Conditions: Returns the number of pixels within the given image object
def numOfPixels(img):
    # Multiplies the image width by the image height to get the area/number of pixels within the image object
    return img.getWidth()* img.getHeight()

# Purpose: Calculates, for a given pixel, which color is more intense
# Assumptions: Parameter is an existing image object, image module is imported
# Parameters: An image object
# Post Conditions: Returns the color that is most intense as a string, or "none"
def intensity(px):
    # If red has the greatest intensity, return "red"
    if px.getRed() > px.getGreen() and px.getRed() > px.getBlue():
        return "red"
    # If green has the greatest intensity, return "green"
    elif px.getGreen() > px.getRed() and px.getGreen() > px.getBlue():
        return "green"
    # If blue has the greatest intensity, return "blue"
    elif px.getBlue() > px.getRed() and px.getBlue() > px.getGreen():
        return "blue"
    # If no color has the greatest intensity, return "none"
    else:
        return "none"

# Purpose: For a given image, calculates the number of pixels where a given color is the most intense
# Assumptions: Parameter img is an image object, Parameter color is either "red", "green", "blue", or "none", intensity() function exists
# Parameters: An image object, A color (in string format)
# Post conditions: Returns the number of pixels where a given color is the most intense
def intensityCount(img, color):
    # Initializes counter variable
    count = 0
    # Repeats action for every column
    for col in range(img.getWidth()):
        # Repeats action for every row
        for row in range(img.getHeight()):
            # Grabs pixel at col, row
            p = img.getPixel(col, row)
            # Checks to see what the most intense color of the given pixel is
            i = intensity(p)
            # Checks to see if the given pixel's most intense color is the color requested
            if i == color:
                # If the pixel's most intense color is the color requested, adds 1 to the count
                count = count + 1
    # Returns the total number of pixels where the pixel's most intense color is the color requested
    return count

def main():
    # Creates an image object from lcastle.gif
    lcastle = image.Image("lcastle.gif")

    # Shows lcastle image within new window
    showImage(lcastle)

    # Prints the number of pixels within lcastle.gif
    print("The total number of pixels within this image is:", numOfPixels(lcastle))

    # Prints the number of pixels where red is the most intense color
    print("The total number of pixels within this image where red is the most intense color is:", intensityCount(lcastle, "red"))

    # Prints the number pixels where green is the most intense color
    print("The total number of pixels within this image where green is the most intense color is:", intensityCount(lcastle, "green"))
    
    # Prints the number pixels where blue is the most intense color
    print("The total number of pixels within this image where blue is the most intense color is:", intensityCount(lcastle, "blue"))
    
    # Prints the number pixels where no color is the most intense color
    print("The total number of pixels within this image where no color is more intense than any other is:", intensityCount(lcastle, "none"))

main()
