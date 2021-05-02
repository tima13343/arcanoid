import pygame 

pygame.init()

back = (1, 217, 253)
mw = pygame.display.set_mode((500,500))
game = True
clock = pygame.time.Clock()

class Area():

    def __init__(self,x=0,y=0,width=0,height=0,color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self,new_color):
        self.fill = new_color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

    def collidepoint(self,rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self,filename,x=10,y=10,width=10,height=10,color=10):
        Area.__init__(self,x = x,y = y,width = width,height = height,color = None)
        self.image = pygame.image.load(filename)
    
    def draw(self):
        mw.blit(self.image,(self.rect.x, self.rect.y))

#cпрайть|
ball = Picture('ball', 160,200,50,50)
platform = Picture('', 200,300,100,30)
bricks = []
count = 9
for j in range(4):
    y = 5 + (55*j)
    x = 5 + (27.5*j)
    for i in range(count):
        br = Picture('', x,y,50,50)
        bricks.apppend(br)
        x += 55
    count -= 1

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    mw.fill(back)
    pygame.display.update()
    clock.tick(40)

    for br in bricks():
        br.draw()

    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)