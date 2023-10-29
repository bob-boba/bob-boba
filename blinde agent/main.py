# -*- coding: utf-8 -*-
#importing library
import pygame as pg
import sys
import time
import random 
#//////////////////////////////--------global variable----------////////////////////////////////////////
backgraund_color = (0,150,0)
BLOCK_SIZE = 15
nbr_agent=15
nbr_food= 40
val_food = 5
#//////////////////////////////--------global images----------////////////////////////////////////////

backraound1 = pg.image.load('images/backraound1.jpeg')
food= pg.image.load('images/food1.png')
walls= pg.image.load('images/wall1s.png')
#//////////////////////////////--------class for the base----------////////////////////////////////////////

class Base:
   def __init__(self):
       self.isEnable = False
       self.x = 0
       self.y = 0    

#//////////////////////////////--------class for the ants----------////////////////////////////////////////


class agent:
    def __init__(self,base_x,base_y,main_screen,map_for_agent,food_table):
        
        self.x,self.base_x = base_x, base_x
        self.y ,self.base_y = base_y,base_y
       
        self.screen = main_screen
        self.trace= 0.9#the left over
       
        self.derection = random.choice(('N','E','w','s')) 
        self.map_for_agent = map_for_agent
        self.status = 'free' # for beeing free to move randomly
        self.path_to_base= []
        self.food_table=food_table
        self.image_free = pg.image.load('images/agent_frees.png')
        self.image_back= pg.image.load('images/agent_backs.png')
        self.image_free_res = pg.image.load('images/agent_frees.png')
        self.image_back_res= pg.image.load('images/agent_backs.png')
        self.image = self.image_free 
#//////////////////////////////--------fun  for drawing ----------////////////////////////////////////////

    def draw(self):
        
        self.screen.blit(self.image, (( self.y)*BLOCK_SIZE,( self.x) *BLOCK_SIZE))

#//////////////////////////////--------fun for returning to the base----------////////////////////////////////////////
    
    def return_to_base(self,path):
        
       
        self.image= self.image_back
        for move in path:
            if move =='S':
                    self.x=  self.x + 1 
                    self.map_for_agent[self.x][self.y]=self.trace 
                    self.draw()# draw after every move
            elif move =='N':
               
                    self.x=  self.x - 1 
                    self.map_for_agent[self.x][self.y]=self.trace 
                    self.draw()# draw after every move
            elif move =='W':
                    self.y=  self.y -1 
                    self.map_for_agent[self.x][self.y]=self.trace 
                    self.draw()# draw after every move
            else:
                    self.y=  self.y + 1
                    self.map_for_agent[self.x][self.y]=self.trace 
                    self.draw()# draw after every move
#//////////////////////////////--------fun for finding the base----------////////////////////////////////////////
        
    def find_the_base (self,x,y):
        path_to_the_base = []#start with empty path 
        
        while (x,y) != (self.base_x,self.base_y) :
               
            
                if x > self.base_x:# going up
                    if self.map_for_agent[x-1][y]==1:# if it a wall
                        if self.map_for_agent[x][y-1]!=1:# go left
                            path_to_the_base.append('W')
                            
                            y-=1
                        elif self.map_for_agent[x][y+1]!=1:#go right
                            path_to_the_base.append('E')
                            
                            y+=1
                    else:        
                        path_to_the_base.append('N')
                        x-=1
                   
                if x < self.base_x :#going down
                    if self.map_for_agent[x+1][y]==1:# if it a wall
                        if self.map_for_agent[x][y-1]!=1:#go left
                            path_to_the_base.append('W')
                            
                            y-=1
                        elif self.map_for_agent[x][y+1]!=1:#go right
                            path_to_the_base.append('E')
                            
                            y+=1
                    else:
                        
                        path_to_the_base.append('S')
                        x+=1
                     
                if y > self.base_y:#going left
                    if self.map_for_agent[x][y-1]==1:# if it a wall
                        if self.map_for_agent[x-1][y]!=1:#go up
                         path_to_the_base.append('N')
                         
                         x-=1
                        elif self.map_for_agent[x+1][y]!=1:#go down
                            path_to_the_base.append('S')
                            
                            x+=1
                    else:
                        path_to_the_base.append('W')
                        y-=1
                     
                if y < self.base_y :#going right
                    if self.map_for_agent[x][y+1]==1:#if it a wall
                        if self.map_for_agent[x-1][y]!=1:#go up
                         path_to_the_base.append('N')
                         
                         x-=1
                        elif self.map_for_agent[x+1][y]!=1:#go down
                            path_to_the_base.append('S')
                            
                            x+=1
                    else:
                        path_to_the_base.append('E')
                        y+=1
                    
                
        return path_to_the_base
  
#//////////////////////////////--------fun for random move or follow the base----------////////////////////////////////////////
            
    def random_move_or_follow_path(self):
            
            if( (self.map_for_agent[self.x][self.y] < 1 )and (self.map_for_agent[self.x][self.y] > 0) ):# if the spotte have a trace
                
                # start follow the trace
                
                if( (self.map_for_agent[self.x+1][self.y] < 1 )and (self.map_for_agent[self.x+1][self.y] > 0) ):
            
                    if self.map_for_agent[self.x+1][self.y] < self.map_for_agent[self.x][self.y]:
                        self.x+=1
                   
                 
                if( (self.map_for_agent[self.x][self.y+1] < 1 )and (self.map_for_agent[self.x][self.y+1] > 0) ) :
                    if self.map_for_agent[self.x][self.y+1] <  self.map_for_agent[self.x][self.y]:
                        self.y+=1
                if( (self.map_for_agent[self.x-1][self.y] < 1 )and (self.map_for_agent[self.x-1][self.y] > 0) ) :
                    if self.map_for_agent[self.x-1][self.y] < self.map_for_agent[self.x][self.y]:
                        self.x-=1
                    
                    
               
                
               
                
               
                if( (self.map_for_agent[self.x][self.y-1] < 1 )and (self.map_for_agent[self.x][self.y-1] > 0) ) :
                    if self.map_for_agent[self.x][self.y-1] <  self.map_for_agent[self.x][self.y]:
                        self.y-=1
                    
                    
                
                #if the ant find a candy when they following the trace    
                if  self.map_for_agent[self.x+1][self.y] == -1 :
                            self.x+=1                          
                            self.food_table[(self.x,self.y)]-=1
                            if self.food_table[(self.x,self.y)]==0:
                                self.map_for_agent[self.x][self.y] = 0
                            self.status = 'back'
                               # self.follow_trace(self.x, self.y)
                elif  self.map_for_agent[self.x-1][self.y] == -1 :
                            self.x-=1                          
                            self.food_table[(self.x,self.y)]-=1
                            if self.food_table[(self.x,self.y)]==0:
                                self.map_for_agent[self.x][self.y] = 0
                            self.status = 'back'
                elif  self.map_for_agent[self.x][self.y+1] == -1 :
                            self.y+=1                          
                            self.food_table[(self.x,self.y)]-=1
                            if self.food_table[(self.x,self.y)]==0:
                                self.map_for_agent[self.x][self.y] = 0
                            self.status = 'back'
                elif  self.map_for_agent[self.x][self.y-1] == -1 :
                            self.y-=1                          
                            self.food_table[(self.x,self.y)]-=1
                            if self.food_table[(self.x,self.y)]==0:
                                self.map_for_agent[self.x][self.y] = 0
                            self.status = 'back'
                    
            else:# the random move
                self.derection = random.choice(('N','E','W','S'))
                if self.derection == 'N':#going up 
                    if self.map_for_agent[self.x][self.y-1]!=1:# if not a wall
                        self.y=  self.y - 1 
                        
                        
                        
                        
                        if  self.map_for_agent[self.x][self.y] == -1 : # if it a candy
                            self.food_table[(self.x,self.y)]-=1 # remove a candy from the pack
                            if self.food_table[(self.x,self.y)]==0:
                                self.map_for_agent[self.x][self.y] = 0
                            self.status = 'back' # change from free to back to the base 
                            return (self.x,self.y)# exit th random function
                            
                           
                            
                elif self.derection =='W': # going left
                    if self.map_for_agent[self.x][self.y+1]!=1:# if not a wall
                        self.y=  self.y + 1 
                        
                        if  self.map_for_agent[self.x][self.y] == -1 :# if it a candy
                            self.food_table[(self.x,self.y)]-=1 # remove a candy from the pack
                            if self.food_table[(self.x,self.y)]==0:
                                self.map_for_agent[self.x][self.y] = 0
                            self.status = 'back'# change from free to back to the base 
                            return (self.x,self.y)# exit th random function
                            
                elif self.derection == 'E':#going right
                    if self.map_for_agent[self.x+1][self.y]!=1:# if not a wall
                        self.x=  self.x + 1 
                        
                        if  self.map_for_agent[self.x][self.y] == -1 :# if it a candy
                            self.food_table[(self.x,self.y)]-=1# remove a candy from the pack
                            if self.food_table[(self.x,self.y)]==0:
                                self.map_for_agent[self.x][self.y] = 0
                            self.status = 'back'# change from free to back to the base 
                            return (self.x,self.y)# exit th random function
                            
                else:#going down
                    if self.map_for_agent[self.x-1][self.y]!=1:# if not a wall
                        self.x=  self.x - 1 
                       
                        if  self.map_for_agent[self.x][self.y] == -1 :# if it a candy
                            self.food_table[(self.x,self.y)]-=1# remove a candy from the pack
                            if self.food_table[(self.x,self.y)]==0:
                                self.map_for_agent[self.x][self.y] = 0
                            self.status = 'back'# change from free to back to the base 
                            return (self.x,self.y)# exit th random function
                            
            
                return 0


#//////////////////////////////---------------------------------------------////////////////////////////////////////
#//////////////////////////////---------------------main function----------////////////////////////////////////////

class start:    
    def __init__(self):
        pg.init()#intialising the paygame window
        self.RES = self.WIDTH, self.HEIGHT = 1200, 600
       
        self.FPS = 60
       
        # the map 1 is a wall
        #         0 is free space
        #         1 is a candy
        #         5 is the base
        self.map_for_agent = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],                              
                              [1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                              [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],                              
                              [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                              [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                              [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                              [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],                              
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],                              
                              [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1],                              
                              [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],                              
                              [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                              [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                              [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
                              [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],                              
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],                              
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],                              
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1],
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],                              
                              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
       
       
        self.screen = pg.display.set_mode(self.RES)
        self.food_table ={}
        
        self.clock = pg.time.Clock()
        
        self.base = Base()
        # creat  (nbr_agent) ant
        self.table_agent = [agent(self.base.x,self.base.y,self.screen,self.map_for_agent,self.food_table) for k in range(nbr_agent)]

#//////////////////////////////--------random candy----------////////////////////////////////////////

    def random_food(self):
        i =0
        while i <  nbr_food :
            done = False
            while (done == False) : 
               
                x=  random.randint(1, 39)
                y = random.randint(1, 79)
                if self.map_for_agent[x][y]== 0:
                    self.food_table[(x,y)] = val_food
                    self.map_for_agent[x][y]=-1
                   
                    done = True
            i+=1
            
#//////////////////////////////--------drawing the walls----------////////////////////////////////////////
            
    def draw_walls (self) :
        
        
        map_tace = []
        for i in range(40):
            for j in range(80):
                if(self.map_for_agent[i][j] == 1):
                    self.screen.blit(walls, (j*BLOCK_SIZE,i*BLOCK_SIZE))
                if( (self.map_for_agent[i][j] < 1) and  (self.map_for_agent[i][j] > 0 ) ):
                    if self.map_for_agent[i][j] != -1:
                        map_tace.append((i,j))
                        pg.draw.rect(self.screen,(200*self.map_for_agent[i][j],200*self.map_for_agent[i][j],0), pg.Rect(( j)*BLOCK_SIZE,( i) *BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
       
        
        #rediuce the trace after evry move of ant       
        for case in map_tace:
            i,j = case
            if self.map_for_agent[i][j] != -1:
                self.map_for_agent[i][j]-=0.02
        
       
        
            
        #//////////////////////////////--------drawing the base after enable it----------////////////////////////////////////////
    
        if self.base.isEnable :
            pg.draw.rect(self.screen, (0,0,255), pg.Rect((self.base.y-1)*BLOCK_SIZE,(self.base.x-1) *BLOCK_SIZE, 3*BLOCK_SIZE, 3*BLOCK_SIZE))
            pg.draw.rect(self.screen, (0,0,150), pg.Rect((self.base.y)*BLOCK_SIZE,(self.base.x) *BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            
            #/////////////--------drawing the candy----------/////////////

            for key in self.food_table :
                  if self.food_table[key]>0 :
                    self.screen.blit(food, ((key[1]) *BLOCK_SIZE,(key[0]) *BLOCK_SIZE))
                
   
       
   
        
#//////////////////////////////--------__________________________----------////////////////////////////////////////
                
    def run(self):
        
        
        
        
        while True:
            
            self.screen.blit(backraound1, (0,0))# put the backraoud image
                            
           
            for event in pg.event.get():
                 if event.type == pg.QUIT:
                     
                     pg.quit()
                     sys.exit()
                 if event.type == pg.MOUSEBUTTONDOWN:#enabling the base and relees the ants
                    if self.base.isEnable == False:
                        
                         self.base.y , self.base.x =  pg.mouse.get_pos()
                         self.base.x = round(self.base.x / BLOCK_SIZE)
                         self.base.y = round(self.base.y / BLOCK_SIZE)
                         
                         
                         if self.map_for_agent[self.base.x][self.base.y]== 1:
                             pass
                         else:
                             self.map_for_agent[self.base.x][self.base.y]= 5 
                             self.base.isEnable=True
                             self.random_food()
                             for agent in self.table_agent :
                                 agent.y= self.base.y
                                 agent.x= self.base.x
                                 agent.base_y = self.base.y
                                 agent.base_x = self.base.x
                         
                         
                         
                         
                
            
                
            pg.font.init()
           
            self.draw_walls()
            time.sleep(0.2)# FREESe THE PYGAME WINDOW FOR SLOWIN DOWN THE ANTS
            
            for agent in self.table_agent :
                if agent.status == 'free':
                    
                    action = agent.random_move_or_follow_path()
                    agent.draw()
                
                else: #agent.status == 'back':
                     
                         path = agent.find_the_base(agent.x,agent.y)
                         
                         agent.trace= 0.9
                         agent.return_to_base(path[0])
                         
                         
                         
                         if len(path) == 1:
                            
                             agent.status = 'free'
                             
                             agent.image= agent.image_free
                     
                    
                     
               
                       
                    
                    
                
            
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = start()
    app.run()

