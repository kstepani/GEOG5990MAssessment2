This repository contains a project completed as an assignment of the GEOG5990M course of MSc GIS at University of Leeds.

It is a program written in Python which takes as an input a raster dataset of heights of a hilly area and through these it calculates 
the slope gradients for all the cells using the "D8" algorithm. It also displays the heights and the gradients of the area as raster images and finally it creates
a txt output file which includes the calculated gradients.

List of files in the repository:
1.maximum_gradient: source code
2.maxgradientframework: a module including the Gradient class
3.snow.slope.txt: input file containing the heights of the area
4.gradients.txt: output file with the gradients of the area

How to run the code:
In order to run the code a raster dataset of heights is required as an input at Step 1.
It is also necessary for the parameters in Step 3 to be set. The number of columns and rows derives from the size of the raster dataset.
Then the program calculates the slope in each cell, builts a new dataset of the same size as the input,
displays the two raster images and finally creates the output txt file with the gradients.

Further development of the program:
In the maxgradientframework module, the code for calculating the slope method could be developed more. It could may be automated somehow
as it seems to be a bit complicated and time consuming to be written with all the different statements for the map edges.
Another development that could be done in the source code is setting the parameters by the console.
