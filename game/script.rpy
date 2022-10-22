# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define p = Character('Крошка Картошка', color="#c8ffc8")
define pp = Character('ПРИНЦЕССА Картошка', color="#c8ffc8")

transform left_center:
    xalign 0.3 yalign 0.2

    linear 0.5 xalign 0.3 yalign 0.3
    linear 0.5 xalign 0.3 yalign 0.2
    repeat
screen hamster_cage:
    add "bg field" anchor(0.5,0.3)
    add "target" at Transform(function=target1.transform)
    add "potato happy" anchor (0.5,0.5) at Transform(function=player.transform)
   

    key "focus_left" action SetField(player,"xoffset",-0.05)
    key "focus_right" action SetField(player,"xoffset",+0.05)
    key "focus_up" action SetField(player,"yoffset",-0.05)
    key "focus_down" action SetField(player,"yoffset",+0.05)
    key "dismiss" action Return("hamster")
init -2 python:
    class Coordinate:
        def __init__(self,x,y,xmin,ymin,xmax,ymax):
            (self.x, self.y, self.xmin, self.ymin, self.xmax, self.ymax) = (x, y, xmin, ymin, xmax, ymax)
            self.xoffset,self.yoffset=0,0
            return       
        def transform(self,d,show_time,animate_time):
            d.pos=(self.x,self.y) 
    class Target(Coordinate):
        
        def is_close(self,player):
            x = self.x - player.x
            y = self.y - player.y
            dist = (x*x + y*y)
            if dist < 0.1:
                self.activate()
                self.x = -42.0
        def transform(self,d,show_time,animate_time):
            self.is_close(self.player)
            super().transform(d,show_time,animate_time)
        def set_player(self,player):
            self.player = player
        def activate(self):
            self.player.add_point()            
    class Player(Coordinate):
        def add_point(self):
            pass
        def transform(self,d,show_time,animate_time):
            self.x+=self.xoffset
            self.y+=self.yoffset
            self.xoffset,self.yoffset=0,0
            if self.x<self.xmin:
                self.x=self.xmin
            if self.y<self.ymin:
                self.y=self.ymin
            if self.x>self.xmax:
                self.x=self.xmax
            if self.y>self.ymax:
                self.y=self.ymax
            super().transform(d,show_time,animate_time)
            return 0
    player = Player(0.5,0.5,0.05,0.05,0.95,0.95)
    target1 = Target(0.9,0.9,0.05,0.05,0.95,0.95)
    target1.set_player(player)

label start:

    scene bg room

    show potato happy at left_center

    p "AAAAAAAAAAAAAAAAAAAAAAA."
    'внутренний голос?''чо происходит'
    p "POTATO"
    'внутренний?'"что? картошка?"
    call screen hamster_cage
    p "OR NOT POTATO"
    'что такое внутри?'"при чем тут картошка?"
    menu:
        "choose"
        "potato":
            p "POTATO"
            'а что снаружи?'"это что за выбор такой"
            show potato princess at truecenter,left
            "А ЭТО ЧТО ТАКОЕ""А ЭТО ЧТО ТАКОЕ"
            pp "POTATO!!!!!!!!!!!!!!"

        "not potato":
            show potato sad at left
            p "OR NOT POTATO"
    return
