import pygame

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                print("Button Pressed")
                if j.get_button(6):
                    print("Turning ON Left Motor with L2")
                elif j.get_button(7):
                    print("Turning ON Right Motor with R2")
            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
