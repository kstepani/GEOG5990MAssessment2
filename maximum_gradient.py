# -*- coding: utf-8 -*-
"""
This is a program reading a raster dataset of the heights of a hilly area. It then calculates the maximum slope in all the 
raster cells using the "D8" algorithm and displays the heights as well as the maximum gradients as images. It finally creates an
output txt file containing the calculated gradients of the area.
"""


"""
Import necessary libraries and files
"""
import matplotlib.pyplot
import maxgradientframework

"""
Pull in the heights from a txt file
"""
print("Step 1:Pull in the heights from a txt file")
#read the txt file and create a 2D List containing the heights
with open("snow.slope.txt") as f:
    heights = []
    for line in f:
        parsed_line = str.split(line," ")
        heights_line = []
        for word in parsed_line:
            heights_line.append(int(word))
        heights.append(heights_line)
        
"""
Print the heights list just for testing
"""
print("Step 2:Print the heights list")
print(heights)

"""
Initialise all necessary parameters
"""
print("Step 3: Initialise parameters")
num_of_columns=300 # this is the number of columns of the input raster file of heights
num_of_rows=300 # this is the number of rows of the input raster file of heights
maxgradients=[] # create an empty list for the calculated maximum slopes to be stored
gradient=maxgradientframework.Gradient(heights)


"""
Calculate the slope between each cell and its eight neighbours, take the maximum value of them and put it into 
the maxgradients dataset
"""
print("Step 4:Calculate the slope between each cell and its eight neighbours, take the maximum value of them and put it into the maxgradients dataset")
for i in range(num_of_rows):
    maxgradients_rowlist=[]
    for j in range(num_of_columns):
        
        gradient.calculate_slope(i,j)
        maxgradients_rowlist.append(gradient.find_maximum_slope())
    
    maxgradients.append(maxgradients_rowlist)


"""
Print the maxgradients list for testing
"""    
print("Step 5:Print the maxgradients list")
print(maxgradients)



"""
Display the heights and the gradients as an image
"""
print("Step 6:Display heights as an image")
#plot the heights as a raster image              
matplotlib.pyplot.imshow(heights)
matplotlib.pyplot.show()
print("Step 7:Display gradients as an image")
#plot the gradients as a raster image
matplotlib.pyplot.imshow(maxgradients)
matplotlib.pyplot.show()



"""
Save the calculated gradients to a txt file
"""
print("Step 8:Save the calculated gradients to a txt file ")
with open("gradients.txt", "w") as f:
    for line in maxgradients:
        for value in line:
            f.write(str(value) + " ")
        f.write("\n")