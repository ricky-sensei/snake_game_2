import pyxel

pyxel.init(160, 160)

class App:
    def __init__(self): 
        self.position_x = 20
        self.position_y = 20

        pyxel.load("./snake_game_assets.pyxres")

        pyxel.run(self.update, self.draw)

    def update(self): # 情報の更新
        # self.position_x = self.position_x + 1
        self.position_x += 1

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
        )

App()
