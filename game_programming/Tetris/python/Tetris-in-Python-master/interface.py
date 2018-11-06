import pygame
from inspect import currentframe, getframeinfo

def start(screen, st):
    cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

    if st.start_pos == "center":
        st.start_pos = get_center_pos(screen, st.start_surface)
    screen.blit(st.start_surface, st.start_pos)

def game_over(screen, st):
    cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

    if st.game_over_pos == "center":
        st.game_over_pos = get_center_pos(screen, st.game_over_surface)

    screen.blit(st.game_over_surface, st.game_over_pos)

def get_center_pos(screen, text):
    cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
    
    screen_rect = screen.get_rect()
    text_rect = text.get_rect()
    text_rect.centerx = screen_rect.centerx
    text_rect.centery = screen_rect.centery
    return (text_rect.x, text_rect.y)
