"""
This class represents a location inside of a grid (Maybe this class must be removed in the future)
"""

class Location(object):


    def __init__(self,row,column):
        """TODO: COMMENT METHOD
        """
        self.row = row
        self.column = column

    def __eq__(self, another):
        """TODO: COMMENT METHOD
        """
        #TODO: Is it necessary this method?
        return self.row == another.row and self.column == another.column
    
    def __str__(self):
        """TODO: COMMENT METHOD
        """
        return "r:"+repr(self.row)+",c:"+repr(self.column)

    def __repr__(self):
        """TODO: COMMENT METHOD
        """
        return self.__str__()