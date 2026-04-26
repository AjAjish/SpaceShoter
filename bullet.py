class Bullet:
    def __init__(self, image):
        self.image = image
        self.x = 0
        self.y = 480
        self.speed = 10
        self.state = "ready"

    def fire(self, x):
        if self.state == "ready":
            self.x = x
            self.state = "fire"

    def move(self):
        if self.state == "fire":
            self.y -= self.speed
            if self.y <= 0:
                self.reset()

    def reset(self):
        self.y = 480
        self.state = "ready"

    def draw(self, screen):
        if self.state == "fire":
            screen.blit(self.image, (self.x + 16, self.y + 10))