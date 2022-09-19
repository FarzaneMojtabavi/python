from media import Media

class clip(Media):
    def __init__(self,id,name,direction,score,url,type,year):
        Media.__init__(self,id,name,direction,score,url,type,year)
    
    def show_info(self):
        Media.show_info(self)