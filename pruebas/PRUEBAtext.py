# import pygame as pg

# pg.init()





# class pgtextbox:#By K1521
#     def __init__(self,width=100,height=10,fontname=None):
#         self.surface=pg.Surface((width,height))
#         self.text=""
#         self.width=width
#         self.height=height
#         self.font=pg.font.Font(fontname,pgtextbox.getMaxFontSize(fontname,lineheight=height))
#         self.curserindex=0
#         self.cursersurface=pg.Surface((self.font.size("|")[0]//2,self.font.size("|")[1]))
#         self.cursersurface.fill((255,255,255))
#         #self.cursersurface=self.font.render("|",False,(255,255,255),(0,0,0))
#         self.offsety=int((height-self.font.get_linesize())/2)
#         self.offsetx=0


#     def curserpos(self):
#         return self.font.size(self.text[:self.curserindex])[0]

#     def addPgEvent(self,event):
#         if event.type==pg.KEYDOWN:
#             if event.key==pg.K_BACKSPACE:
#                 self.deleteAtCurser()
#             elif event.key==pg.K_RIGHT:
#                 self.offsetCurser(1)
#             elif event.key==pg.K_LEFT:
#                 self.offsetCurser(-1)
#             else:
#                 self.insertAtCurser(event.unicode)

#     def render(self):
#         self.surface.fill((0,0,0))

#         width=self.width-self.cursersurface.get_width()
#         text=self.font.render(self.text,False,(255,255,255),(0,0,0))


#         if self.curserindex>=0:
#             curserpos=self.curserpos()+self.offsetx

#             curserposnew=max(0,min(curserpos,width))
#             self.offsetx+=curserposnew-curserpos
#             curserpos=curserposnew
#             #if curserpos<0:
#                 #self.offsetx-=curserpos
#                 #curserpos=0
#             #if curserpos>width:
#                 #curserpos=curserpos-width
#                 #self.offsetx-=curserpos
#         else:
#             #self.offsetx=min(width-text.get_width(),0)
#             self.offsetx=0

#         self.surface.blit(text,(self.offsetx,self.offsety))
#         if self.curserindex>=0:
#             self.surface.blit(self.cursersurface,(curserpos,self.offsety))
#             #print((curserpos,self.offsety))
#         return self.surface

#     def insertAtCurser(self,t):
#         if self.curserindex<0:
#             self.curserindex=len(self.text)
#         self.text=self.text[:self.curserindex]+t+self.text[self.curserindex:]
#         self.curserindex+=len(t)

#     def deleteAtCurser(self,length=1):
#         if self.curserindex<0:
#             self.curserindex=len(self.text)

#         newcurserindex=max(0,self.curserindex-length)
#         self.text=self.text[:newcurserindex]+self.text[self.curserindex:]
#         self.curserindex=newcurserindex

#     def offsetCurser(self,i):
#         self.curserindex=max(min(self.curserindex+i,len(self.text)),0)


#     @staticmethod
#     def longestline(self,fontname,lines):
#         size=pg.font.Font(fontname,1000)
#         return max(lines,key=lambda t:size(t)[0])

#     @staticmethod
#     def getMaxFontSize(fontname,width=None,lineheight=None,line=None):
#         def font(size):
#             return pg.font.Font(fontname,size)
#         fontsize=float("inf")# inf

#         if width:
#             aproxsize=width*1000//font(1000).size(line)[0]
#             while font(aproxsize).size(line)[0]<width:
#                 aproxsize+=1
#             while font(aproxsize).size(line)[0]>width:
#                 aproxsize-=1
#             fontsize=min(aproxsize,fontsize)

#         if lineheight:
#             aproxsize=lineheight*4//3
#             while font(aproxsize).get_linesize()<lineheight:
#                 aproxsize+=1
#             while font(aproxsize).get_linesize()>lineheight:
#                 aproxsize-=1
#             fontsize=min(aproxsize,fontsize)
#         return fontsize

#     @staticmethod
#     def rendermultilinetext(text,width=None,height=10,fontname=None,antialias=False,color=(255,255,255),background=None):
#         if(len(text)-text.count("\n")==0):
#             return pg.Surface((0,0))
#         def font(size):
#             return pg.font.Font(fontname,size)

#         text=text.split("\n")
#         fontsize=1000000000# inf

#         longestline=None
#         if height:
#             longestline=pgtextbox.longestline(fontname,lines)
#         fontsize=pgtextbox.getMaxFontSize(fontname,width,lineheight,longestline)

#         font=font(fontsize)
#         width=font.size(longestline)[0]
#         lineheight=font.get_linesize()
#         heigth=len(text)*lineheight
#         textsurface=pg.Surface((width,heigth))
#         if background:
#             textsurface.fill(background)
#         for i,line in enumerate(text):
#             textsurface.blit(font.render(line,antialias,color,background),(0,i*lineheight))
#         return textsurface

# screen=pg.display.set_mode((1000,500))
# textbox=pgtextbox(200,20)
# textbox.insertAtCurser('Hallo')

# while True:
#     e = pg.event.wait(30000)
#     if e.type == pg.QUIT:
#         raise StopIteration

#     textbox.addPgEvent(e)#uses keydown events
    
#     print(textbox.text)

#     screen.fill((0,0,0))
#     screen.blit(textbox.render(),(10,0))
#     pg.display.flip()
# pg.display.quit()

# import pygame as pg


# def main():
#     screen = pg.display.set_mode((640, 480))
#     font = pg.font.Font(None, 32)
#     clock = pg.time.Clock()
#     input_box = pg.Rect(100, 100, 140, 32)
#     color_inactive = pg.Color('lightskyblue3')
#     color_active = pg.Color('dodgerblue2')
#     color = color_inactive
#     active = False
#     text = ''
#     done = False

#     while not done:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 done = True
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 # If the user clicked on the input_box rect.
#                 if input_box.collidepoint(event.pos):
#                     # Toggle the active variable.
#                     active = not active
#                 else:
#                     active = False
#                 # Change the current color of the input box.
#                 color = color_active if active else color_inactive
#             if event.type == pg.KEYDOWN:
#                 if active:
#                     if event.key == pg.K_RETURN:
#                         print(text)
#                         text = ''
#                     elif event.key == pg.K_BACKSPACE:
#                         text = text[:-1]
#                     else:
#                         text += event.unicode

#         screen.fill((30, 30, 30))
#         # Render the current text.
#         txt_surface = font.render(text, True, color)
#         # Resize the box if the text is too long.
#         width = max(200, txt_surface.get_width()+10)
#         input_box.w = width
#         # Blit the text.
#         screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
#         # Blit the input_box rect.
#         pg.draw.rect(screen, color, input_box, 2)

#         pg.display.flip()
#         clock.tick(30)


# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()


# import pygame
# pygame.init()
# window = pygame.display.set_mode((500, 200))
# clock = pygame.time.Clock()

# font = pygame.font.SysFont(None, 100)
# text = ""
# input_active = True

# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             input_active = True
#             text = ""
#         elif event.type == pygame.KEYDOWN and input_active:
#             if event.key == pygame.K_RETURN:
#                 input_active = False
#             elif event.key == pygame.K_BACKSPACE:
#                 text =  text[:-1]
#             else:
#                 text += event.unicode

#         window.fill(0)
#         text_surf = font.render(text, True, (255, 0, 0))
#         window.blit(text_surf, text_surf.get_rect(center = window.get_rect().center))
#         pygame.display.flip()

# pygame.quit()
# exit()










import pygame as pg

class TextInputBox(pg.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()
        self.borde = False

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pg.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pg.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pg.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_RETURN:
                    self.active = False
                    print('se detiene el ciclo y entrega el texto')
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.borde:
                    pass
                else:
                    self.text += event.unicode
                self.render_text()


pg.init()
window = pg.display.set_mode((500, 200))
clock = pg.time.Clock()
font = pg.font.SysFont(None, 100)

text_input_box = TextInputBox(50, 50, 400, font)
group = pg.sprite.Group(text_input_box)

run = True

while run:
    clock.tick(60)
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False
    group.update(event_list)

    window.fill(0)
    group.draw(window)
    pg.display.flip()

pg.quit()
exit()