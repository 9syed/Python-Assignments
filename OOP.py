import pygame
import random
from blob import Blob

GREEN_BLOBS = 10
BLUE_BLOBS = 4

WIDTH = 800
HEIGHT = 700
WHITE = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
Green = (0, 255, 0)

display_game = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("A Game") 
clock = pygame.time.Clock()

class GreenBlob(Blob):
       
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        self.color = Green

    def fast_motion(self):
        self.x += random.randrange(-10, 10)
        self.y += random.randrange(-10, 10)


def environment(blob_list): 
    display_game.fill(WHITE) 

    for blob_dict in blob_list: 
        for blob_id in blob_dict: 
            blob = blob_dict[blob_id]
            pygame.draw.circle(display_game, blob.color, [blob.x, blob.y], blob.size) 
            blob.fast_motion()
            blob.check_bounds()

    pygame.display.update()


def main():
    green_blobs = dict(enumerate([GreenBlob(Green,WIDTH,HEIGHT) for I in range(GREEN_BLOBS)])) 
    blue_blobs = dict(enumerate([GreenBlob(BLUE,WIDTH,HEIGHT) for I in range(BLUE_BLOBS)]))  
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

        environment([green_blobs,blue_blobs])
        clock.tick(60)
        #print(blue_blob.x, blue_blob.y)

if __name__ == '__main__':
    main()