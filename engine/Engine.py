import pyxel


class Engine:
    def __init__(self, nom, gamepath="./", splash_screen=None, splash_screen_size=(32, 32), screen_size=(160, 120), game_class=None):
        self.nom = nom
        self.started = False
        self.gamepath = gamepath
        self.splash_screen_size = splash_screen_size
        self.screen_size = screen_size
        self.services = {}
        self.states = {}
        if not game_class is None:
            self.game = game_class(self)
        else:
            self.game = None

        pyxel.init(screen_size[0], screen_size[1], title=nom)

        if not splash_screen is None:
            pyxel.images[0].load(0, 0, gamepath + splash_screen)

        pyxel.run(self.update, self.draw)

    def reg_service(self, name, service):
        instance = service(self)
        self.services[name] = instance
        instance.init()

    def set_state(self, name, state):
        self.states[name] = state
        return state

    def get_state(self, name):
        return self.states[name]

    def get_service(self, name):
        return self.services[name]

    def load(self, file):
        return pyxel.load(self.gamepath + file)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if not self.started:
            self.init_game()


        for service in self.services.values():
            service.update()

    def draw(self):
        if not self.started:
            pyxel.cls(1)
            w, h = self.splash_screen_size
            x = (pyxel.width - w) // 2
            y = (pyxel.height - h) // 2

            pyxel.blt(x, y, 0, 0, 0, w, h)
        else:
            pyxel.cls(0)
            for service in self.services.values():
                service.draw()

    def init_game(self):
        if not self.game is None:
            self.game.init()
            print("Game started")
        else:
            print("Game started (WARN: No Game Core)")
        self.started = True
        return