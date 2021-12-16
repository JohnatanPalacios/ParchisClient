import pygame as pg


class Pawn(pg.sprite.Sprite):
    def __init__(self, **kwargs):
        super().__init__()
        self.current_sprite = 0
        self.image = pg.image.load(kwargs['address']).convert_alpha()
        self.id = kwargs['id']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = kwargs['pos']

    def setPos(self, pos):
        self.rect.x = pos['x']
        self.rect.y = pos['y']
    
    def is_clicked(self):
        return pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos())


class PawnManager:
    def __init__(self, board, redPawns, greenPawns, yellowPawns, bluePawns):
        self.board = board
        self.redPawns = redPawns
        self.greenPawns = greenPawns
        self.yellowPawns = yellowPawns
        self.bluePawns = bluePawns

    def update(self, status):
        for j in status:
            color = j["color"]
            pawnsStatus = j["pawnsStatus"]
            if color == 0:
                for yp in self.yellowPawns:
                    for ps in pawnsStatus:
                        ps["id"] = yp["id"]
                        pos = self.board[str(ps["position"])]
                        yp.setPos(pos)
            if color == 1:
                for gp in self.greenPawns:
                    for ps in pawnsStatus:
                        ps["id"] = gp["id"]
                        pos = self.board[str(ps["position"])]
                        gp.setPos(pos)
            if color == 2:
                for rp in self.redPawns:
                    for ps in pawnsStatus:
                        ps["id"] = rp["id"]
                        pos = self.board[str(ps["position"])]
                        rp.setPos(pos)
            if color == 3:
                for bp in self.bluePawns:
                    for ps in pawnsStatus:
                        ps["id"] = bp["id"]
                        pos = self.board[str(ps["position"])]
                        bp.setPos(pos)
    
    def __movePawns(self):
        for event in pg.event.get():
            # if event.type == pg.QUIT:
            #     run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                # obtener ficha
                # evaluar posición de nuevo lugar
                    # mover al nuevo lugar
                # {
                #     "operation":2,
                #     "pawn_1":1,
                #     "pawn_2":2
                # }
    
    def free_pawns(self, board, color):
        # 0:'Amarillo'
        # 1:'Verde'
        # 2:'Rojo'
        # 3:'Azul',
        if color == 0:
            pos = board['5']
            for f in self.bluePawns:
                f.setPos(pos)
        elif color == 1:
            pos = board['22']
            for f in self.bluePawns:
                f.setPos(pos)
        elif color == 2:
            pos = board['39']
            for f in self.bluePawns:
                f.setPos(pos)
        elif color == 3:
            pos = board['56']
            for f in self.bluePawns:
                f.setPos(pos)