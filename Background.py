import pygame
from random import randint
from System import *

def make_background():
    #tiled sand background
    sand_tile_location = 'kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile029.png'
    sand_tile = pygame.image.load(sand_tile_location)

    #big tree
    big_tree_location = 'kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile134.png'
    big_tree_tile = pygame.image.load(big_tree_location)

    #small rock
    small_rock_location = 'kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile135.png'
    small_rock_tile = pygame.image.load(small_rock_location)

    #turret bae
    turret_base_location = 'kenney_tower-defense-top-down/PNG/Retina/towerDefense_tile181.png'
    turret_base_tile = pygame.image.load(turret_base_location)

    #Maybe add these later
    """
    #small tree
    small_tree_location = 'kenney_tower-defense-top-down/PNG/Default size/towerDefense_tile132.png'
    small_tree_tile = pygame.image.load(small_tree_location)
    #big rock
    big_rock_location = 'kenney_tower-defense-top-down/PNG/Default size/towerDefense_tile136.png'
    big_rock_tile = pygame.image.load(big_rock_location)
    """

    # get the tile width, height
    tile_width = sand_tile.get_width()
    tile_height = sand_tile.get_height()

    # make a new surface, background, with the same w,h as screen
    background = pygame.Surface((WIDTH,HEIGHT))

    # loop over the background and place tiles on it
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(sand_tile, (x,y))

    #randomly place a rock
    num_rocks = 1
    for i in range(num_rocks):
        x = randint(200,WIDTH-100)
        y = randint(100,HEIGHT-200)
        # blit that seaweed
        background.blit(small_rock_tile,(x,y))

    #randomly place some trees
    num_trees = 2
    for i in range(num_trees):
        x = randint(100,WIDTH)
        y = randint(0,HEIGHT)
        # blit that seaweed
        background.blit(big_tree_tile,(x,y))

    #place turret base
    background.blit(turret_base_tile,(100,HEIGHT//2))


    # return the background surface
    return background