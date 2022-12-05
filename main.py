
# @tigercoder5067
# 1 year ago
#This is source code for everyone
import pygame
import glob

size = width,height = 500,600

fps = 20
white = (255,255,255)

class MySprite(pygame.sprite.Sprite):
    def __init__(self, action):
        super(MySprite, self).__init__()
        im = glob.glob(f'{action}*.png')
        lenim = len(im[0])
        self.images =[pygame.image.load(img) for img in glob.glob(f'{action}*.png')
                      if len(img) == lenim]
        self.images2 = [pygame.image.load(img) for img in glob.glob(f'{action}*.png')
                      if len(img) > lenim] 
        self.images.extend(self.images2)
        self.index = 0
        self.rect = pygame.Rect(5,5,150,198)
    def update(self):
        if self.index >= len(self.images):
            self.index =0
        self.image = self.images[self.index]
        self.index += 1


def action(action):
    my_sprite = MySprite(action)
    my_group = pygame.sprite.Group(my_sprite)
    return my_group

def main():
    pygame.init()
    screen =pygame.display.set_mode(size)
    pygame.display.set_caption('how to animate sprite')
    my_sprite = MySprite("idle ")
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    my_group = action("dead ")
                if event.key == pygame.K_i or event.key == pygame.K_LEFT:
                    my_group = action("Idle ")
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    my_group = action("jump ")

                if event.key == pygame.K_r or event.key == pygame.K_RIGHT :
                    my_group = action("run ")
                if event.key == pygame.K_q:
                    my_group = action("walk ")


        my_group.update()
        screen.fill(white)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

if __name__ == '__main__':
     main()