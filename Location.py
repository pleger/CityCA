"""
This class represents a location inside of a grid (Maybe this class must be removed in the future)
"""

class Location(object):


    def __init__(self,row,column):
        """ The constructor states the row and column of a location
        """
        self.row = row
        self.column = column

    def __str__(self):
        """Method used for toString
        """
        return "r:"+repr(self.row)+",c:"+repr(self.column)

    def __repr__(self):
        """Method used for toString
        """
        return self.__str__()