from media import Media

class series(Media):
    def __init__(self,id,name,direction,score,url,type,year,part):
        Media.__init__(self,id,name,direction,score,url,type,year)
        self.part=part
    def show_info(self):
        Media.show_info(self)