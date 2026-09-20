import pyxel

pyxel.init(160, 160)

class App:
    def __init__(self): 
        self.position_x = 0
        self.position_y = 0

        self.frame_count = 0

        """ self.direction
        0->右
        90ー>下
        180ー>左
        270->上
        """
        self.direction = 0

        pyxel.load("./snake_game_assets.pyxres")

        pyxel.run(self.update, self.draw)

    def update(self): # 情報の更新
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.direction = 90
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.direction = 180
        if pyxel.btnp(pyxel.KEY_UP):
            self.direction = 270
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.direction = 0
        print(self.direction)
        self.frame_count += 1
        if self.frame_count % 30 == 0:
            if self.direction == 0:
                self.position_x += 16
            if self.direction == 90:
                self.position_y += 16
            if self.direction == 180:
                self.position_x -= 16
            if self.direction == 270:
                self.position_y -= 16

    def draw(self): # 描画
        pyxel.cls(0)
        pyxel.blt(
            self.position_x,
            self.position_y,
            0,
            0,
            0,
            16,
            16,
            0,
            rotate=self.direction
        )

App()
