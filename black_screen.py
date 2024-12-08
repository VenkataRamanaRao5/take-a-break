import math
import pygame
import ctypes

class black_screen:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.hwnd = pygame.display.get_wm_info()["window"]
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.centerx, self.centery = self.screen.get_rect().center
        self.font = pygame.font.Font(None, 100)
        ctypes.windll.user32.ShowWindow(self.hwnd, 0)

    def show_black_screen(self, interval, seconds_to_mmss):
        ctypes.windll.user32.SetWindowPos(self.hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)
        ctypes.windll.user32.ShowWindow(self.hwnd, 5)
        i = interval
        while i > 0:
            for event in pygame.event.get():
                pass
            self.screen.fill((0, 0, 0))
            i -= 1.0/30
            self.clock.tick(30)
            pygame.draw.arc(self.screen, (255, 255, 255), (self.centerx - 150, self.centery - 150, 300, 300), math.pi / 2, i / interval * math.pi * 2 + math.pi / 2, 10)
            text = self.font.render(seconds_to_mmss(math.ceil(i)), True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.centerx, self.centery))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
        ctypes.windll.user32.ShowWindow(self.hwnd, 0)