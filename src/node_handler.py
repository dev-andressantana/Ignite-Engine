# Importing modules-------------------------------------------------------------
import pygame, sys, interface_nodes, physics_nodes, audio_nodes, sprite_nodes
from pygame import *
pygame.init()
sys.path.append('.')

# Node library------------------------------------------------------------------
node_types = {
'Body':physics_nodes.Body
}

# Color Pallete-----------------------------------------------------------------
black = 0,0,0

# Aliases-----------------------------------------------------------------------
error = 'something went wrong..'
window = pygame.display

# Master Node-------------------------------------------------------------------
class Node:

    def __init__(self, name):
        self.name = name
        self.children = {}

# Adding/Deleting Children------------------------------------------------------
    def add_child(self, name, node):
        node = node_types[node]
        self.children[name] = node(name)
        pass

# Root Node---------------------------------------------------------------------
class Root(Node):# Root node

    def __init__(self, name, width, height):
        super().__init__(name)
        self.size = width, height
        self.running = True
        self.canvas = window.set_mode(self.size)
        window.set_caption(self.name)

# Main Loop---------------------------------------------------------------------
    def run(self):
        while self.running:

            self.check_close_event()
            self.update()

        self.close_program()


# Closing program-----------------------------------------------------------------
    def check_close_event():
        for event in pygame.event.get():# Checking QUIT event
            if event.type == QUIT:
                self.running = False

    def close_program():
        pygame.quit()

# Updating Children-------------------------------------------------------------
    def update():
        try:
            pass
        except: pass

# Drawing Children--------------------------------------------------------------
    def draw(self, image, motion):
        self.canvas.fill(black)# Erasing Canvas

        for child in self.children.values():# Drawing Objects
            self.canvas.blit(child.image, child.motion)

        window.flip()# Displaying Canvas
