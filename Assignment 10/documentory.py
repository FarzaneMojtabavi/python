from media import Media

class Documantary(Media):
    def __init__(self,id,name,direction,score,url,type,year,part):
        Media.__init__(self,id,name,direction,score,url,type,year,part)

    def show_info(self):
        Media.show_info(self)