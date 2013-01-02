"""
This class represents a location inside of a grid (Maybe this class must be removed in the future)
"""

class Location(object):
    
    def __init__(self,row,column):
        self.row = row
        self.column = column

    #FIX: Is it necessary this method?
    def __eq__(self, another):
        return self.row == another.row and self.column == another.column
    
    def __str__(self):
        return "r:"+repr(self.row)+",c:"+repr(self.column)

    def __repr__(self):
        return self.__str__()