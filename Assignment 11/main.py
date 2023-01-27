import random
import arcade

SCREEN_WIDTH=500
SCREEN_HEIGHT=500

class snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width=16
        self.height=16
        self.color_1=arcade.color.YELLOW
        self.color_2=arcade.color.RED
        self.change_x=0
        self.change_y=0
        self.score=0
        self.center_x=SCREEN_WIDTH//2
        self.center_y=SCREEN_HEIGHT//2
        self.speed=2
        self.body=[]
    def move(self):
        #add old position to body list
        self.body.append([self.center_x,self.center_y])
        if len(self.body)>self.score:
            self.body.pop(0)
        # update new posion snake
        if self.change_x>0:
            self.center_x+=self.speed
        elif self.change_x<0:
            self.center_x-=self.speed    
        if self.change_y>0:
            self.center_y+=self.speed
        elif self.change_y<0:
            self.center_y-=self.speed       
        # self.center_x+=self.center_x*self.speed
        # self.center_y+=self.center_y*self.speed
    def eat(self,status):
        if status=='sum':
            self.score+=1
        if status=='sub':
            self.score-=1

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x,self.center_y,
            self.width,self.height,
            self.color_1
        )
        for i in range(len(self.body)):
            if i%2==0:
                arcade.draw_rectangle_filled(
                self.body[i][0],
                self.body[i][1],
                self.width,self.height,
                self.color_2)
            else:
                arcade.draw_rectangle_filled(
                self.body[i][0],
                self.body[i][1],
                self.width,self.height,
                self.color_1
                )    
        arcade.draw_text("score: "+str(self.score),10.0,480.0,
                         arcade.color.WHITE,12,12,'left')        



class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width=16
        self.height=16
        # self.color_1=arcade.color.RED
        self.appleimg = arcade.Sprite('apple.png', scale=0.5)
        self.r=8
        self.appleimg.center_x=random.randint(10,SCREEN_WIDTH-10)
        self.appleimg.center_y=random.randint(10,SCREEN_HEIGHT-10)
        # self.center_x=random.randint(0,SCREEN_WIDTH)
        # self.center_y=random.randint(0,SCREEN_HEIGHT)
    def draw(self):
        self.appleimg.draw()
        # arcade.draw_circle_filled(
        #     self.center_x,
        #     self.center_y,
        #     self.r,
        #     self.color_1
        # )    
class Dead(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width=16
        self.height=16
        self.deadimg = arcade.Sprite('dead.png', scale=0.5)
        self.r=8
        self.deadimg.center_x=random.randint(10,SCREEN_WIDTH-10)
        self.deadimg.center_y=random.randint(10,SCREEN_HEIGHT-10)
    def draw(self):
        self.deadimg.draw()    

class game(arcade.Window):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title="snake game")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.snake=snake()
        self.apple=Apple()
        self.dead=Dead()


    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.dead.draw()
        if self.snake.score<0 or self.snake.center_x<=0 or self.snake.center_x>=SCREEN_WIDTH or self.snake.center_y<=0 or self.snake.center_y>=SCREEN_HEIGHT:
            arcade.draw_text("Game over",SCREEN_WIDTH/2,SCREEN_HEIGHT/2,arcade.color.RED,20)
            arcade.exit()
    def on_update(self,delta_time:float):
        self.snake.move()    
        
        if arcade.check_for_collision(self.snake,self.apple.appleimg):
            self.snake.eat('sum')
            self.apple=Apple()
            print(self.snake.score)
        elif arcade.check_for_collision(self.snake,self.dead.deadimg):
            self.snake.eat('sub')
            self.dead=Dead()
            print(self.snake.score)

    def on_key_release(self, key: int, modifiers: int):
        if key==arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0
        elif key==arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
        elif key==arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1
        elif key==arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y=-1
my_game=game()
arcade.run()