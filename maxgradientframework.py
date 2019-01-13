"""This is a module containig the Gradient class. This class includes the required variables and methods for calculating 
the maximum gradient in each cell of a raster dataset"""

class Gradient():
    
    def __init__(self, heights):
        """
        Initialise the required variables
        heights -- a raster dataset containing the heights of a hilly area
        slope1-8 -- the eight different slopes that are going to be calulated for each cell
        """

        self.heights = heights
        self.slope1=0
        self.slope2=0
        self.slope3=0
        self.slope4=0
        self.slope5=0
        self.slope6=0
        self.slope7=0
        self.slope8=0
        
    def calculate_slope(self, i, j):
        """
        Calculates the slope between each cell and its eight neighbours using their heights and distance. Different statements
        are taken into account for the cells located at the edges of the map
        """
        
        if i==0:
            if j==0:#this is the cell at the top left corner of the map
                self.slope1=(self.heights[i][j]-self.heights[i][j+1])/1
                self.slope2=(self.heights[i][j]-self.heights[i+1][j+1])/(2**0.5)
                self.slope3=(self.heights[i][j]-self.heights[i+1][j])/1
            elif j==299: #this is the cell at the top right corner of the map
                self.slope1=(self.heights[i][j]-self.heights[i][j-1])/1
                self.slope2=(self.heights[i][j]-self.heights[i+1][j-1])/(2**0.5)
                self.slope3=(self.heights[i][j]-self.heights[i+1][j])/1
            else: # this is for the cells at the top line of the map apart from the corners
                self.slope1=(self.heights[i][j]-self.heights[i][j-1])/1
                self.slope2=(self.heights[i][j]-self.heights[i+1][j-1])/(2**0.5)
                self.slope3=(self.heights[i][j]-self.heights[i+1][j])/1
                self.slope4=(self.heights[i][j]-self.heights[i+1][j+1])/(2**0.5)
                self.slope5=(self.heights[i][j]-self.heights[i][j+1])/1
                
        elif i==299:
            if j==0:#this is the cell at the bottom left corner of the map
                self.slope1=(self.heights[i][j]-self.heights[i][j+1])/1
                self.slope2=(self.heights[i][j]-self.heights[i-1][j+1])/(2**0.5)
                self.slope3=(self.heights[i][j]-self.heights[i-1][j])/1
            elif j==299: #this is the cell at the bottom right corner of the map
                self.slope1=(self.heights[i][j]-self.heights[i][j-1])/1
                self.slope2=(self.heights[i][j]-self.heights[i-1][j-1])/(2**0.5)
                self.slope3=(self.heights[i][j]-self.heights[i-1][j])/1
            else: # this is for the cells at the bottom line of the map apart from the corners
                self.slope1=(self.heights[i][j]-self.heights[i][j-1])/1
                self.slope2=(self.heights[i][j]-self.heights[i-1][j-1])/(2**0.5)
                self.slope3=(self.heights[i][j]-self.heights[i-1][j])/1
                self.slope4=(self.heights[i][j]-self.heights[i-1][j+1])/(2**0.5)
                self.slope5=(self.heights[i][j]-self.heights[i][j+1])/1
                
        elif j==0:#this is for the cells of the first column apart from the corners
            self.slope1=(self.heights[i][j]-self.heights[i-1][j])/1
            self.slope2=(self.heights[i][j]-self.heights[i-1][j+1])/(2**0.5)
            self.slope3=(self.heights[i][j]-self.heights[i][j+1])/1
            self.slope4=(self.heights[i][j]-self.heights[i+1][j+1])/(2**0.5)
            self.slope5=(self.heights[i][j]-self.heights[i+1][j])/1
            
        elif j==299:# this is for the cells of the last column apart from the corners
            self.slope1=(self.heights[i][j]-self.heights[i-1][j])/1
            self.slope2=(self.heights[i][j]-self.heights[i-1][j-1])/(2**0.5)
            self.slope3=(self.heights[i][j]-self.heights[i][j-1])/1
            self.slope4=(self.heights[i][j]-self.heights[i+1][j-1])/(2**0.5)
            self.slope5=(self.heights[i][j]-self.heights[i+1][j])/1   
            
        else:#this is for all the cells apart from the map edges
            self.slope1=(self.heights[i][j]-self.heights[i-1][j])/1
            self.slope2=(self.heights[i][j]-self.heights[i-1][j-1])/(2**0.5)
            self.slope3=(self.heights[i][j]-self.heights[i][j-1])/1
            self.slope4=(self.heights[i][j]-self.heights[i+1][j-1])/(2**0.5)
            self.slope5=(self.heights[i][j]-self.heights[i+1][j])/1 
            self.slope6=(self.heights[i][j]-self.heights[i+1][j+1])/(2**0.5)
            self.slope7=(self.heights[i][j]-self.heights[i][j+1])/1    
            self.slope8=(self.heights[i][j]-self.heights[i-1][j+1])/(2**0.5)
            
    def find_maximum_slope(self):
        """
        Makes a list of all the calulated eight slopes for each cell and then finds and returns the maximum value of them
        """
        slopes=[self.slope1, self.slope2, self.slope3, self.slope4, self.slope5, self.slope6, self.slope7, self.slope8]
        return max(slopes)
            