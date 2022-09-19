import pytube
class Media:
    def __init__(self,id,name,direction,score,url,type,year):
        self.id=id
        self.name=name
        self.direction=direction
        self.score=score
        self.url=url
        self.type=type
        self.year=year
    def show_info(self):
        print(self.id+'\n'+self.name+'\n'+self.direction+'\n'+self.score+'\n'+self.url+'\n'+self.type+'\n'+self.year) 
    def download(self):
        link = self.url
        first_stream =pytube.YouTube(link).streams.first()
        first_stream.download(output_path = './' , filename = 'filmnew.mp4')
        print('Download is complete!')    