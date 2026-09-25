import pyxel



class App:
    def __init__(self): 
        self.position_x = 0
        self.position_y = 0

        self.frame_count = 0

        """ self.angle
        0->右
        90ー>下
        180ー>左
        270->上
        """
        self.angle = 0
        self.game_over = False
        self.screen_size = 200
        self.speed = self.screen_size / 10
        pyxel.init(self.screen_size, self.screen_size)

        pyxel.load("./snake_game_assets.pyxres")

        pyxel.run(self.update, self.draw)

    def update(self): # 情報の更新
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.angle = 90
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.angle = 180
        if pyxel.btnp(pyxel.KEY_UP):
            self.angle = 270
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.angle = 0

        self.frame_count += 1
        if self.frame_count % 30 == 0:
            if self.angle == 0:
                self.position_x += self.speed
            if self.angle == 90:
                self.position_y += self.speed
            if self.angle == 180:
                self.position_x -= self.speed
            if self.angle == 270:
                self.position_y -= self.speed
        
        
        # ゲームオーバー判定
        if self.position_x >= self.screen_size or self.position_x < 0 or self.position_y >= self.screen_size or self.position_y < 0:
            self.game_over = True
        

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
            rotate=self.angle
        )
        if self.game_over == True:
            pyxel.text(10, 10, "GAME OVER", 12)

App()


