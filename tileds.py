#initiating proccess
def init():
    global initiated
    global localTiles
    global tileSize
    import pygame
    initiated = True
    localTiles = []

class parameters:
    tileSize = 16

class tiles:
    def create(window,tile,position):
        global localTiles
        localTiles.append([tile[1],position])
        window.blit(tile[0],(position[0] * parameters.tileSize, position[1] * parameters.tileSize))
    def getpos(position, offset = (0,0)):
        type = None
        position = (round((position[0] - offset[0] - 32) / parameters.tileSize), round((position[1] - offset[1] - 32) / parameters.tileSize))
        for tile in localTiles:
            if tile[1] == position:
                type = tile[0]
                break
        return type
        
        