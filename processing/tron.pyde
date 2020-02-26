# processing.org - Python
# not done

w = 5
rows = 0
cols = 0

def setup():
    global w, rows, cols
    frameRate(30)
    size(640,480)
    cols = width / w
    rows = height / w

def draw():
    background(0)
    player.move()
    ai.move()
    ai.random_move()
    
    ai.render()
    player.render()
    
class Player():
    def __init__(self, tag):
        global w
        self.tag = tag
        self.w = w
        self.body = []
        self.pos = []
        self.dir_x = 0
        self.dir_y = 0
        if(self.tag == "player"):        
            self.body.append(PVector(640/2, 480/2))
        elif(self.tag == "AI"):
            self.body.append(PVector(0, 0))
     
    def random_move(self):    
        if(self.tag == "AI"):
            get_random = floor(random(0,4))
            if(get_random == 0):
                self.dir_y = -1
                self.dir_x = 0
            elif(get_random == 1):
                self.dir_y = 0
                self.dir_x = -1
            elif(get_random == 2):
                self.dir_y = 1
                self.dir_x = 0
            elif(get_random == 3):
                self.dir_y = 0
                self.dir_x = 1    
        
    def move(self):        
        if(len(self.pos) == 0):
               self.pos.append(PVector(self.body[0].x,self.body[0].y))
        elif(len(self.pos) > 0):
            if(self.body[0] not in self.pos):
                self.body.append(PVector(self.body[0].x,self.body[0].y))
                self.pos.append(PVector(self.body[0].x,self.body[0].y))              
        
        while(len(self.pos) > 2):
            self.pos.pop(0)
    
        self.body[0].x += (self.dir_x * self.w)
        self.body[0].y += (self.dir_y * self.w)        
        
    def render(self):
        if(self.tag == "player"):        
            fill(255,0,0)
        elif(self.tag == "AI"):
            fill(0,0,255)
        noStroke()
        for i in range(len(self.body)):                
                rect(self.body[i].x, self.body[i].y, self.w, self.w)

player = Player("player")
ai = Player("AI")

# w = 87
# a = 65
# s = 83
# d = 68

def keyPressed():
    if(keyCode == 87):
        player.dir_y = -1
        player.dir_x = 0
    elif(keyCode == 83):
        player.dir_y = 1
        player.dir_x = 0
    if(keyCode == 65):
        player.dir_x = -1
        player.dir_y = 0
    elif(keyCode == 68):
        player.dir_x = 1
        player.dir_y = 0
