from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
           return None
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)

            first_asteroid_movement = self.velocity.rotate(random_angle)
            second_asteroid_movement = self.velocity.rotate(-random_angle)

            first_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            second_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            smaller_asteroid1 = Asteroid(self.position.x,self.position.y, first_asteroid_radius)
            smaller_asteroid2 = Asteroid(self.position.x,self.position.y, second_asteroid_radius)

            smaller_asteroid1.velocity = (first_asteroid_movement * 1.2)
            smaller_asteroid2.velocity = (second_asteroid_movement * 1.2)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
