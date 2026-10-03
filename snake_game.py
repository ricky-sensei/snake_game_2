import pyxel



class App:
    def __init__(self): 
        # position_x: 画面上のマス目の数
        self.head_position_x = 3
        self.head_position_y = 2

        self.body_position_x = 2
        self.body_position_y = 2


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
        if self.game_over == False:
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
                    self.head_position_x += 1
                if self.angle == 90:
                    self.head_position_y += 1
                if self.angle == 180:
                    self.head_position_x -= 1
                if self.angle == 270:
                    self.head_position_y -= 1

        
        # ゲームオーバー判定
        if self.head_position_x > 9 or self.head_position_x < 0 or self.head_position_y > 9 or self.head_position_y < 0:
            self.game_over = True

        print(self.head_position_x)
        print(self.head_position_y)
        
        

    def draw(self): # 描画
        pyxel.cls(0)
        pyxel.blt(
            self.head_position_x * self.speed,
            self.head_position_y * self.speed,
            0,
            0,
            0,
            16,
            16,
            0,
            rotate=self.angle
        )
        pyxel.blt(
            self.body_position_x * self.speed,
            self.body_position_y * self.speed,
            0,
            16,
            0,
            16,
            16,
            0,
            rotate=self.angle
        )
        if self.game_over == True:
            pyxel.text(10, 10, "GAME OVER", 12)

App()


