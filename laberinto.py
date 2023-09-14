import pygame, sys
pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)
imagenx = pygame.image.load("1.jpg").convert()
mifuente = pygame.font.Font(None,30)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

clock = pygame.time.Clock()

coord_x = 320
coord_y = 40

x_speed = 0
y_speed = 0

tx = 320
ty = 40






l1 = ("#...##########################")
l2 = ("#........#....................#")
l3 =("###.###..#####.###.###.###.#.##")
l4 =("#.#...#.......#.#...#.#.#.#...#")
l5 =("#.#.###.#####.#.#.###.#.#.#.#.#")


mitexto1 = mifuente.render(l1,0,(green))
mitexto2 = mifuente.render(l2,0,(red))
mitexto3 = mifuente.render(l3,0,(red))
mitexto4 = mifuente.render(l4,0,(red))
mitexto5 = mifuente.render(l5,0,(green))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            
            
            
            if event.key == pygame.K_LEFT:
                x_speed = -3    
            if event.key == pygame.K_RIGHT:    
                x_speed = 3
            
            if event.key == pygame.K_UP:
                y_speed = -3    
            if event.key == pygame.K_DOWN:    
                y_speed =  3   
                
                
                
                
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_LEFT:
                x_speed = 0    
            if event.key == pygame.K_RIGHT:    
                x_speed = 0   
                
                
            if event.key == pygame.K_UP:
                y_speed = 0    
            if event.key == pygame.K_DOWN:    
                y_speed = 0
                
                
                
 # para no salir del mapa x              
              
    if (coord_x < 300 or coord_x < -10):   
        x_speed *= -1
     
    if (coord_x > 600 or coord_x < -10):   
        x_speed *= -1
         
 # para no salir del mapa y         
        
    if (coord_y < 40 or coord_y < 0):     
        y_speed *= -1    
     
    if (coord_y > 180 or coord_y < 0):     
        y_speed *= -1       
        
        
        
        
        
    screen.blit(imagenx,[0,0])
    coord_x += x_speed
    coord_y += y_speed
    
    
    screen.blit(mitexto1,(300,50))        
    screen.blit(mitexto2,(300,75))
    screen.blit(mitexto3,(300,105))
    screen.blit(mitexto4,(300,130))
    screen.blit(mitexto5,(300,160))
    
    
    pygame.draw.rect(screen, blue, (coord_x,coord_y, 5, 5))
    
   

    

    pygame.display.flip()
    clock.tick(60)
            

            






