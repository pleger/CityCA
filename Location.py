class Location(object):
    
    def __init__(self,row,column):
        self.row = row
        self.column = column
    
    def __eq__(self, another):
        return self.row == another.row and self.column == another.column
    
    def __str__(self):
        return "r:"+repr(self.row)+",c:"+repr(self.column)