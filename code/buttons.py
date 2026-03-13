#pygame.init()
# screen = pygame.display.set_mode((WIDTH,HEIGTH))
# pygame.display.set_caption("Button")
#font= pygame.font.Font(UI_FONT, 40)

class Button():
    def __init__ (self, image, pos, text_input, font, base_color, hovering_color,):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is not None:
            self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
        
        
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
        
        
    def check_input(self, position):
        #   x pos                                                      y pos
        #if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        if self.rect.collidepoint(position):
            return True
        return False
            
            
            
    def change_color(self, position):
        #if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            
# button_surface = font.render("Start Your Adventure",False,'Blue')
# button_surface = pygame.transform.scale(button_surface,(640,300))
# 
# button = Button(button_surface, 640, 300, "Start Your Adventure" )
# 
# while True: 
    # for event in pygame.event.get():
        # if event.type == pygame.QUIT:
            # pygame.quit()
            # sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # button.check_input(pygame.mouse.get_pos())
            # 
    # 
    # button.update()
    # button.change_color(pygame.mouse.get_pos())
    # 
    # pygame.display.update()