from engine.services.Service import Service


class CollisionService(Service):

    def init(self):
        self.collisions = []

    def i_am_colliding(self, collision):
        for i in self.collisions:
            if i.collide(collision):
                return True
        return False

    def register_collision(self, collision):
        self.collisions.append(collision)