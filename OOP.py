import pygame
import random
from blob import Blob
import numpy as np

GREEN_BLOBS = 12
BLUE_BLOBS = 10
RED_BLOBS = 8

WIDTH = 1000 
HEIGHT = 780 
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Game")
clock = pygame.time.Clock()

class BlueBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__(self, other_blob):
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0, 0, 255):
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of invalid colors.')

class RedBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)

class GreenBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)

def touching(b1,b2):
       return np.linalg.norm(np.array([b1.x, b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)

def manage_collisions(blob_list):
    blues, reds, greens = blob_list
    for blue_id, blue_blob, in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob, in other_blobs.copy().items():
                if blue_blob == other_blob:
                    pass
                else:
                    if touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            del blues[blue_id]

    return blues, reds, greens

def environment(blob_list):
    game_display.fill(BLACK)
    blues, reds, greens = manage_collisions(blob_list)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.motion()
            blob.check_bounds()

    pygame.display.update()
    return blues, reds, greens

def main():
    green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(GREEN_BLOBS)]))
    blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        blue_blobs,red_blobs,green_blobs = environment([blue_blobs,red_blobs,green_blobs])
        clock.tick(60)

if __name__ == '__main__':
    main()