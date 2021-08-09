import pygame
import random
import math

# Do the Installation
pygame.init()

# Set the Screen Size
height = 300
width = 550

screen = pygame.display.set_mode([height,width])

# Change the Title
pygame.display.set_caption("Car Game")

# Change the Logo
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Set the Player
def player(x,y):
    img_player = pygame.image.load("car.png")
    screen.blit(img_player, (x,y))
    
x_player = 120
y_player = 485
x_player_point = 0

# Set the Enemy
def enemy(x,y):
    img_enemy = pygame.image.load("enemy.png")
    screen.blit(img_enemy,(x,y))

x_enemy = random.randint(10,100)
y_enemy = random.randint(25,30)
y_enemy_point = 6

# Make the Collision Detection
def collision(x_player,y_player,x_enemy,y_enemy):
    distance = math.sqrt(math.pow(x_player-x_enemy,2)) + (math.pow(y_player-y_enemy,2))
    if distance < 10:
        return True
    else:
        return False

# Set the Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 16)

def show_score(x,y):
    score_number = font.render("score:" + str(score), True, (255,255,255))
    screen.blit(score_number,(x,y))

x_score = 10
y_score = 10
    
# Frame Border
clock = pygame.time.Clock()

# Running the Game
running = True
while running:
    # Change the Screen Color
    screen.fill((0,0,0))
    # Input the Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                x_player_point -= 4
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                x_player_point += 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                x_player_point = 0
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                x_player_point = 0
    
    # Set the Player Movement
    x_player += x_player_point
    if x_player >= 250:
        x_player = 240
    if x_player <= 10:
        x_player = 35

    #Set the Enemy Movement
    y_enemy += y_enemy_point
    if y_enemy >= 540:
        x_enemy = random.randint(50,200)
        y_enemy = random.randint(5,10)
        score += 1
    
    # Show the Collision
    tabrakan = collision(x_player,y_player,x_enemy,y_enemy)
    if tabrakan:
        break
    
    #Time
    clock.tick(60)

    # Show the Player
    player(x_player, y_player)

    # Show the Enemy
    enemy(x_enemy, y_enemy)

    # Show the Score
    show_score(x_score,y_score)

    pygame.display.update()

pygame.quit()

print("Your score :", score)
