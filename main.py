#run it with python 2.7
import pygame, random, string, os
from pygame.locals import *

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY1=(222, 223, 224)
GREY2=(196, 197, 198)
GREY3=(166, 167, 168)

def setup_pygame():
    screen = pygame.display.set_mode([1060, 700])
    pygame.display.set_caption('Ular Tangga')
    clock = pygame.time.Clock()
    pygame.mixer.music.load("asset/music/lagu1.mp3")
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    battle_sound = pygame.mixer.Sound("asset/music/battle.wav")
    snake_sound = pygame.mixer.Sound("asset/music/uler.wav")
    snake_sound1 = pygame.mixer.Sound("asset/music/uler1.ogg")
    ladder_sound = pygame.mixer.Sound("asset/music/menang1.wav")
    walking_sound = pygame.mixer.Sound("asset/music/jalan.ogg")
    winning_sound = pygame.mixer.Sound("asset/music/menang.ogg")
    choose_sound = pygame.mixer.Sound("asset/music/pilih.wav")
    main_menu_background = pygame.image.load("asset/picture/tes2.png").convert()
    img_board = pygame.image.load("asset/picture/papan4.png").convert()
    img_dice1 = pygame.image.load("asset/picture/dadu1-1.png").convert()
    img_dice1.set_colorkey(WHITE)
    img_dice2 = pygame.image.load("asset/picture/DADU2.png").convert()
    img_dice2.set_colorkey(WHITE)
    img_dice3 = pygame.image.load("asset/picture/DADU3.png").convert()
    img_dice3.set_colorkey(WHITE)
    img_dice4 = pygame.image.load("asset/picture/DADU4.png").convert()
    img_dice4.set_colorkey(WHITE)
    img_dice5 = pygame.image.load("asset/picture/DADU5.png").convert()
    img_dice5.set_colorkey(WHITE)
    img_dice6 = pygame.image.load("asset/picture/DADU6.png").convert()
    img_dice6.set_colorkey(WHITE)
    img_player1 = pygame.image.load("asset/picture/PEMAIN1.png").convert()
    img_player1.set_colorkey(WHITE)
    img_player2 = pygame.image.load("asset/picture/PEMAIN2.png").convert()
    img_player2.set_colorkey(WHITE)
    img_player3 = pygame.image.load("asset/picture/PEMAIN3.png").convert()
    img_player3.set_colorkey(WHITE)
    img_player4 = pygame.image.load("asset/picture/PEMAIN4.png").convert()
    img_player4.set_colorkey(WHITE)
    font = pygame.font.Font(None, 50)
    font1 = pygame.font.Font(None, 40)
    font2 = pygame.font.Font(None, 30)
    font3 = pygame.font.Font(None, 25)
    text_a = font1.render('A.', True, WHITE)
    text_b = font1.render('B.', True, WHITE)
    text_c = font1.render('C.', True, WHITE)
    text_d = font1.render('D.', True, WHITE)
    return screen,clock,battle_sound,snake_sound,snake_sound1,ladder_sound,walking_sound,winning_sound,choose_sound,main_menu_background,img_board,img_dice1,img_dice2,img_dice3,img_dice4,img_dice5,img_dice6,img_player1,img_player2,img_player3,img_player4,font,font1,font2,font3,text_a,text_b,text_c,text_d

def reset_multiple_choice_button():
    print ('HILANGIN TOMBOL JAWABAN')
    choice_button_a,choice_button_b,choice_button_c,choice_button_d = "","","",""
    return choice_button_a,choice_button_b,choice_button_c,choice_button_d

def refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict):
    print ('CETAK ULANG PAPAN')
    screen.fill(WHITE)
    screen.blit(img_board, [0,0])
    if total_player == 2:
        screen.blit(img_player1,[player_image_pos_dict[1][0],player_image_pos_dict[1][1]])
        screen.blit(img_player2,[player_image_pos_dict[2][0],player_image_pos_dict[2][1]])
    elif total_player == 3:
        screen.blit(img_player1,[player_image_pos_dict[1][0],player_image_pos_dict[1][1]])
        screen.blit(img_player2,[player_image_pos_dict[2][0],player_image_pos_dict[2][1]])
        screen.blit(img_player3,[player_image_pos_dict[3][0],player_image_pos_dict[3][1]])
    else:
        screen.blit(img_player1,[player_image_pos_dict[1][0],player_image_pos_dict[1][1]])
        screen.blit(img_player2,[player_image_pos_dict[2][0],player_image_pos_dict[2][1]])
        screen.blit(img_player3,[player_image_pos_dict[3][0],player_image_pos_dict[3][1]])
        screen.blit(img_player4,[player_image_pos_dict[4][0],player_image_pos_dict[4][1]])
    text = font1.render('Tombol Dadu', True, BLACK)
    screen.blit(text,(812,660))
    return screen

def show_ladder_or_snake(screen,font1,font2,name_list,curr_player,temp_pos,all_ladder_pos_dict,all_snake_pos_dict,ladder_sound,snake_sound1):
    print ('CETAK TANGGA DAN ULAR')
    text = font2.render(str(name_list[curr_player-1])+' dapat', True, BLACK)
    screen.blit(text,(830,440))
    if (temp_pos in all_ladder_pos_dict):
        ladder_sound.play()
        text = font1.render('Selamat', True, BLACK)
        screen.blit(text,(830,400))
        text = font1.render('Tangga', True, BLACK)
        screen.blit(text,(830,480))
    elif (temp_pos in all_snake_pos_dict):
        snake_sound1.play()
        text = font1.render('Maaf', True, BLACK)
        screen.blit(text,(830,400))
        text = font1.render('Ular', True, BLACK)
        screen.blit(text,(830,480))
    return screen

def change_player(total_player,curr_player,temp_pos,all_player_pos_list):
    print ('GANTI PEMAIN')
    if (curr_player<total_player):
        print ('GANTI PLAYER')
        curr_player = curr_player+1
        temp_pos = all_player_pos_list[curr_player-1]
        return temp_pos,curr_player
    else:
        print ('GANTI PLAYER')
        curr_player = 1
        temp_pos = all_player_pos_list[curr_player-1]
        return temp_pos,curr_player

def main_menu(screen,main_menu_background,font,font1):
    print ('RESET AWAL')
    screen.fill(WHITE)
    screen.blit(main_menu_background, (0, 0))
    menu_border1 = pygame.draw.rect(screen, GREY2,((screen.get_width() / 2)-160,220,350,350), 0)
    menu_border1 = pygame.draw.rect(screen, GREY1,((screen.get_width() / 2)-150,230,330,330), 0)
    menu_border = pygame.draw.rect(screen, WHITE,((screen.get_width() / 2)-140,240,310,310), 0)
    text = font.render('Selamat Datang', True, BLACK)
    screen.blit(text, [(screen.get_width() / 2)-120, 250])
    text = font1.render('Silahkan Pilih', True, BLACK)
    screen.blit(text, [(screen.get_width() / 2)-80, 300])
    return screen

def button_choose_player(screen,choose_2player,choose_3player,choose_4player,font1):
    print ('TOMBOL PEMAIN')
    choose_2player = pygame.draw.rect(screen, BLACK,((screen.get_width() / 2) - 60,(screen.get_height() / 2) - 10,150,50), 0)
    choose_3player = pygame.draw.rect(screen, BLACK,((screen.get_width() / 2) - 60,(screen.get_height() / 2) + 60,150,50), 0)
    choose_4player = pygame.draw.rect(screen, BLACK,((screen.get_width() / 2) - 60,(screen.get_height() / 2) + 130,150,50), 0)
    text = font1.render('2 Pemain', True, WHITE)
    screen.blit(text, [(screen.get_width() / 2)-50, (screen.get_height() / 2)])
    text = font1.render('3 Pemain', True, WHITE)
    screen.blit(text, [(screen.get_width() / 2)-50, (screen.get_height() / 2)+70])
    text = font1.render('4 Pemain', True, WHITE)
    screen.blit(text, [(screen.get_width() / 2)-50, (screen.get_height() / 2)+140])
    return screen,choose_2player,choose_3player,choose_4player

def show_player_order(screen,font,font1,total_player,name_list,curr_player):
    print ('GILIRAN')
    text = font1.render('Giliran', True, BLACK)
    screen.blit(text,(870,50))
    if total_player == 2:
        text = font.render(str(name_list[curr_player-1]), True, BLACK)
        screen.blit(text,(860,80))
    if total_player == 3:
        text = font.render(str(name_list[curr_player-1]), True, BLACK)
        screen.blit(text,(860,80))
    if total_player == 4:
        text = font.render(str(name_list[curr_player-1]), True, BLACK)
        screen.blit(text,(860,80))
    return screen

def show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4):
    print ('POSISI')
    text = font1.render('Posisi', True, BLACK)
    screen.blit(text,(850,180))
    if total_player==2:
        text = font.render(str(name_list[0])+' : '+str(all_player_pos_list[0]), True, BLACK)
        screen.blit(text,(860,220))
        screen.blit(img_player1,(800,215))
        text = font.render(str(name_list[1])+' : '+str(all_player_pos_list[1]), True, BLACK)
        screen.blit(text,(860,260))
        screen.blit(img_player2,(800,255))
    elif total_player==3:
        text = font.render(str(name_list[0])+' : '+str(all_player_pos_list[0]), True, BLACK)
        screen.blit(text,(860,220))
        screen.blit(img_player1,(800,215))
        text = font.render(str(name_list[1])+' : '+str(all_player_pos_list[1]), True, BLACK)
        screen.blit(text,(860,260))
        screen.blit(img_player2,(800,255))
        text = font.render(str(name_list[2])+' : '+str(all_player_pos_list[2]), True, BLACK)
        screen.blit(text,(860,300))
        screen.blit(img_player3,(800,295))
    elif total_player==4:
        text = font.render(str(name_list[0])+' : '+str(all_player_pos_list[0]), True, BLACK)
        screen.blit(text,(860,220))
        screen.blit(img_player1,(800,215))
        text = font.render(str(name_list[1])+' : '+str(all_player_pos_list[1]), True, BLACK)
        screen.blit(text,(860,260))
        screen.blit(img_player2,(800,255))
        text = font.render(str(name_list[2])+' : '+str(all_player_pos_list[2]), True, BLACK)
        screen.blit(text,(860,300))
        screen.blit(img_player3,(800,295))
        text = font.render(str(name_list[3])+' : '+str(all_player_pos_list[3]), True, BLACK)
        screen.blit(text,(860,340))
        screen.blit(img_player4,(800,335))
    return screen

def show_dice(screen,dice_button,img_dice1):
    print ('TOMBOL DADU')
    dice_button = img_dice1.get_rect()
    dice_button = dice_button.move(850,550)
    screen.blit(img_dice1, [850,550])
    return screen,dice_button

def check_answer(screen,name_list,curr_player,temp_pos,bonus_dice_dict,player_answer,ladder_sound,snake_sound,font1,font2,img_board,img_dice1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict,all_ladder_pos_dict,font,all_snake_pos_dict,snake_sound1,winning_sound,exit_button,font3,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_dice,walking_sound,all_player_pos_list,dice_button):
    print ('JAWABAN')
    print ('KOTAK= '+str(temp_pos))
    print ('bonus dice dict= '+str(bonus_dice_dict))
    print ('player answer= '+str(player_answer))
    for bonus_dice_pos, answer in bonus_dice_dict.items():
        if temp_pos==bonus_dice_pos:
            if player_answer==answer:
                random_bonus,screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = get_correct_answer(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_dice,walking_sound)
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                ladder_sound.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(name_list[curr_player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(random_bonus)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                random_bonus,screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = get_false_answer(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_dice,walking_sound)
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                snake_sound.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(name_list[curr_player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(random_bonus)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
    return screen,dice_button,player_image_pos_dict,all_player_pos_list,choice_button_a,choice_button_b,choice_button_c,choice_button_d

def get_correct_answer(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_dice,walking_sound):
    print ('TAMBAH')
    random_bonus = random.randint(1,5)
    print ('Tambahan Angka: '+str(random_bonus))
    temp_pos = temp_pos + random_bonus
    print ('UPDATE POSISI GAMBAR #TAMBAH')
    is_correct_bonus = 1
    screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = update_player_image(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_bonus,walking_sound,is_correct_bonus)
    screen,dice_button,player_image_pos_dict, exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = check_position(screen,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,all_player_pos_list,winning_sound,dice_button,name_list,exit_button,font3,curr_player,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,player_image_pos_dict,battle_sound)
    pygame.display.flip()
    return random_bonus,screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d

def get_false_answer(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_dice,walking_sound):
    print ('KURANG')
    random_bonus = random.randint(1,5)
    print ('Pengurangan Angka: '+str(random_bonus))
    temp_pos = temp_pos - random_bonus
    print ('UPDATE POSISI GAMBAR #KURANG')
    is_correct_bonus = 0
    screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = update_player_image(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_bonus,walking_sound,is_correct_bonus)
    screen,dice_button,player_image_pos_dict, exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = check_position(screen,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,all_player_pos_list,winning_sound,dice_button,name_list,exit_button,font3,curr_player,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,player_image_pos_dict,battle_sound)
    pygame.display.flip()
    return random_bonus,screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d

def display_box(screen, message):
  fontobject = pygame.font.Font(None,40)
  pygame.draw.rect(screen, WHITE,
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,60), 0)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, BLACK),((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + ''.join(current_string))
  while 1:
    if len(current_string)<6:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
            screen.fill(WHITE)
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
            if len(current_string)>=5:
                screen.fill(WHITE)
                current_string = current_string[0:-1]
        display_box(screen, question + ": " + ''.join(current_string))
    else:
        screen.fill(WHITE)
        current_string = current_string[0:-1]
        
  return ''.join(current_string)

def click_choose_player(screen,choose_2player,choose_3player,choose_4player,choose_sound,total_player,name_list,mouse_pos):
    if choose_2player.collidepoint(mouse_pos):                    
        choose_sound.play()
        total_player=2
        for i in range(0,2):
            screen.fill(WHITE)
            name_list.append(ask(screen, "Nama Pemain "+ str(i+1)))
    elif choose_3player.collidepoint(mouse_pos):
        choose_sound.play()
        total_player=3
        for i in range(0,3):
            screen.fill(WHITE)
            name_list.append(ask(screen, "Nama Pemain "+ str(i+1)))
    elif choose_4player.collidepoint(mouse_pos):
        choose_sound.play()
        total_player=3
        for i in range(0,4):
            screen.fill(WHITE)
            name_list.append(ask(screen, "Nama Pemain "+ str(i+1)))
    if total_player != 0:
        choose_2player, choose_3player, choose_4player = "","",""
    return screen, choose_2player, choose_3player, choose_4player, name_list, total_player

def show_multiple_choices(screen,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,font1):
    print ('CETAK JAWABAN')
    choice_button_a = pygame.draw.rect(screen, BLACK,(395,358,350,50), 0)
    text_a = font1.render('A.', True, WHITE)
    choice_button_b = pygame.draw.rect(screen, BLACK,(395,410,350,50), 0)
    text_b = font1.render('B.', True, WHITE)
    choice_button_c = pygame.draw.rect(screen, BLACK,(395,462,350,50), 0)
    text_c = font1.render('C.', True, WHITE)
    choice_button_d = pygame.draw.rect(screen, BLACK,(395,514,350,50), 0)
    text_d = font1.render('D.', True, WHITE)
    return screen,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d

def check_is_player_finished(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,all_player_pos_list,winning_sound,dice_button,name_list,exit_button,font3,curr_player,player_image_pos_dict):
    if all_player_pos_list[curr_player-1]==63:
        print ('MENANG')
        winning_sound.play()
        dice_button = ""
        screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
        screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
        text = font1.render('Selamat', True, BLACK)
        screen.blit(text,(830,400))
        text = font1.render('Menang', True, BLACK)
        screen.blit(text,(830,480))
        exit_button = pygame.draw.rect(screen, (0,0,0),(850,510,100,30), 0)
        text = font3.render('Keluar', True, WHITE)
        screen.blit(text, [860, 520])
        text = font1.render(str(name_list[curr_player-1]), True, BLACK)
        screen.blit(text,(830,440))
    return screen, dice_button, exit_button

def check_is_player_on_bonus_box(screen,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,all_player_pos_list,curr_player,dice_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d,font1,text_a,text_b,text_c,text_d):
    for bonus_dice_pos, answer in bonus_dice_dict.items():
        if all_player_pos_list[curr_player-1]==bonus_dice_pos:
            screen.fill(WHITE)
            dice_button = ""
            random_question_number = random.randint(1,12)
            question = font1.render(bonus_question_dict[random_question_number], True, BLACK)
            if answer=='a':
                temp_quest_a = bonus_question_choices_dict[random_question_number][0]
                temp_quest_b = bonus_question_choices_dict[random_question_number][1]
                temp_quest_c = bonus_question_choices_dict[random_question_number][2]
                temp_quest_d = bonus_question_choices_dict[random_question_number][3]
            elif answer=='b':
                temp_quest_a = bonus_question_choices_dict[random_question_number][1]
                temp_quest_b = bonus_question_choices_dict[random_question_number][0]
                temp_quest_c = bonus_question_choices_dict[random_question_number][3]
                temp_quest_d = bonus_question_choices_dict[random_question_number][2]
            elif answer=='c':
                temp_quest_a = bonus_question_choices_dict[random_question_number][3]
                temp_quest_b = bonus_question_choices_dict[random_question_number][2]
                temp_quest_c = bonus_question_choices_dict[random_question_number][0]
                temp_quest_d = bonus_question_choices_dict[random_question_number][1]
            else:
                temp_quest_a = bonus_question_choices_dict[random_question_number][3]
                temp_quest_b = bonus_question_choices_dict[random_question_number][1]
                temp_quest_c = bonus_question_choices_dict[random_question_number][2]
                temp_quest_d = bonus_question_choices_dict[random_question_number][0]
            text_choice_button_a = font1.render(temp_quest_a, True, WHITE)
            text_choice_button_b = font1.render(temp_quest_b, True, WHITE)
            text_choice_button_c = font1.render(temp_quest_c, True, WHITE)
            text_choice_button_d = font1.render(temp_quest_d, True, WHITE)
            screen.blit(question, [200, 250])
            screen,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d = show_multiple_choices(screen,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,font1)
            screen.blit(text_a, [405,368])
            screen.blit(text_choice_button_a, [445,368])
            screen.blit(text_b, [405,420])
            screen.blit(text_choice_button_b, [445,420])
            screen.blit(text_c, [405,472])
            screen.blit(text_choice_button_c, [445,472])
            screen.blit(text_d, [405,524])
            screen.blit(text_choice_button_d, [445,524])
    return screen,dice_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d

def find_duplicates_with_indices(param_list):
    element_indices = {}
    duplicates_with_indices = {}

    for index, item in enumerate(param_list):
        if item!=0:
            if item in element_indices:
                # Add index to existing list of indices for this element
                if item not in duplicates_with_indices:
                    duplicates_with_indices[item] = element_indices[item]
                duplicates_with_indices[item].append(index)
            else:
                # Initialize list with the current index
                element_indices[item] = [index]
    return duplicates_with_indices

def check_if_player_battle(screen,curr_player,all_player_pos_list,battle_sound,player_image_pos_dict,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list,dice_button):
    duplicate_dict = find_duplicates_with_indices(all_player_pos_list)
    print('duplicate dict= '+str(duplicate_dict))
    print('curr player= '+str(curr_player))
    for player_pos, player_order in duplicate_dict.items():
        if (player_pos!=0):
            player_order.remove(curr_player-1)
            battle_sound.play()
            all_player_pos_list[player_order[0]] = 0
            temp_x = 0
            temp_y = 0
            if player_order[0]+1==1:
                temp_x = 0
                temp_y = 655
            elif player_order[0]+1==2:
                temp_x = 0
                temp_y = 607
            elif player_order[0]+1==3:
                temp_x = 40
                temp_y = 607
            elif player_order[0]+1==4:
                temp_x = 40
                temp_y = 655
            player_image_pos_dict[player_order[0]+1][0] = temp_x
            player_image_pos_dict[player_order[0]+1][1] = temp_y
            print ('CETAKULANGPAPAN #CEKPOSISI 1')
            screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
            screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
            screen,dice_button = show_dice(screen,dice_button,img_dice1)
            text = font1.render('Selamat', True, BLACK)
            screen.blit(text,(830,400))
            text = font1.render(str(name_list[curr_player-1])+' memulangkan '+str(name_list[player_order[0]]), True, BLACK)
            screen.blit(text,(715,450))
    print('after battle player pos= '+str(all_player_pos_list))
    print('after battle player image pos= '+str(player_image_pos_dict))
    return screen,dice_button,player_image_pos_dict

def check_position(screen,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,all_player_pos_list,winning_sound,dice_button,name_list,exit_button,font3,curr_player,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,player_image_pos_dict,battle_sound):
    print ('CEK POSISI')
    screen, dice_button, exit_button = check_is_player_finished(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,all_player_pos_list,winning_sound,dice_button,name_list,exit_button,font3,curr_player,player_image_pos_dict)
    screen,dice_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = check_is_player_on_bonus_box(screen,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,all_player_pos_list,curr_player,dice_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d,font1,text_a,text_b,text_c,text_d)                
    screen,dice_button,player_image_pos_dict = check_if_player_battle(screen,curr_player,all_player_pos_list,battle_sound,player_image_pos_dict,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list,dice_button)
    
    return screen,dice_button,player_image_pos_dict, exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d

def move_player_to_right(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button):
    walking_sound.play()
    player_image_pos_dict[curr_player][0] = player_image_pos_dict[curr_player][0] + 87
    screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
    screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
    screen,dice_button = show_dice(screen,dice_button,img_dice1)
    pygame.display.flip()
    return screen,dice_button,player_image_pos_dict

def move_player_to_left(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button):
    walking_sound.play()
    player_image_pos_dict[curr_player][0] = player_image_pos_dict[curr_player][0] - 87
    screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
    screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
    screen,dice_button = show_dice(screen,dice_button,img_dice1)
    pygame.display.flip()
    return screen,dice_button,player_image_pos_dict

def move_player_to_down(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button):
    walking_sound.play()
    player_image_pos_dict[curr_player][1] = player_image_pos_dict[curr_player][1] + 87
    screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
    screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
    screen,dice_button = show_dice(screen,dice_button,img_dice1)
    pygame.display.flip()
    return screen,dice_button,player_image_pos_dict

def move_player_to_up(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button):
    walking_sound.play()
    player_image_pos_dict[curr_player][1] = player_image_pos_dict[curr_player][1] - 87
    screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
    screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
    screen,dice_button = show_dice(screen,dice_button,img_dice1)
    pygame.display.flip()
    return screen,dice_button,player_image_pos_dict

def move_player_to_ladder(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound):
    # untuk koordinat x nanti rumusnya x (+/- berdasar (temp_pos+1 // 8 == 0) or (temp_pos+1 // 8 == 2) or (temp_pos+1 // 8 == 4) or (temp_pos+1 // 8 == 6)) ((61%8) - (27%8))*87
    # untuk koordinat y nanti rumusnya y-((61//8) - (27//8))*87 
    if (temp_pos in all_ladder_pos_dict):
        if (temp_pos==27):
            print ('TANGGA')
            for i in range(29):
                player_image_pos_dict[curr_player][0]=player_image_pos_dict[curr_player][0]-6
                player_image_pos_dict[curr_player][1]=player_image_pos_dict[curr_player][1]-12
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                screen,dice_button = show_dice(screen,dice_button,img_dice1)
                pygame.display.flip()
            screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
            screen = show_ladder_or_snake(screen,font1,font2,name_list,curr_player,temp_pos,all_ladder_pos_dict,all_snake_pos_dict,ladder_sound,snake_sound1)
            temp_pos = all_ladder_pos_dict[27]
            all_player_pos_list[curr_player-1]=temp_pos
            screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
            screen,dice_button = show_dice(screen,dice_button,img_dice1)
            pygame.display.flip()
        elif (temp_pos==37):
            print ('TANGGA')
            for i in range(29):
                player_image_pos_dict[curr_player][0]=player_image_pos_dict[curr_player][0]+6
                player_image_pos_dict[curr_player][1]=player_image_pos_dict[curr_player][1]-6
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                screen,dice_button = show_dice(screen,dice_button,img_dice1)
                pygame.display.flip()
            screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
            screen = show_ladder_or_snake(screen,font1,font2,name_list,curr_player,temp_pos,all_ladder_pos_dict,all_snake_pos_dict,ladder_sound,snake_sound1)
            temp_pos = all_ladder_pos_dict[37]
            all_player_pos_list[curr_player-1]=temp_pos
            screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
            screen,dice_button = show_dice(screen,dice_button,img_dice1)
            pygame.display.flip()
        else:
            print ('TANGGA')
            for i in range(29):
                player_image_pos_dict[curr_player][0]=player_image_pos_dict[curr_player][0]+6
                player_image_pos_dict[curr_player][1]=player_image_pos_dict[curr_player][1]-6
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                screen,dice_button = show_dice(screen,dice_button,img_dice1)
                pygame.display.flip()
            screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
            screen = show_ladder_or_snake(screen,font1,font2,name_list,curr_player,temp_pos,all_ladder_pos_dict,all_snake_pos_dict,ladder_sound,snake_sound1)
            temp_pos = all_ladder_pos_dict[44]
            all_player_pos_list[curr_player-1]=temp_pos
            screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
            screen,dice_button = show_dice(screen,dice_button,img_dice1)
            pygame.display.flip()
        screen,dice_button,player_image_pos_dict, exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = check_position(screen,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,all_player_pos_list,winning_sound,dice_button,name_list,exit_button,font3,curr_player,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,player_image_pos_dict,battle_sound)
    return screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d

def move_player_to_snake(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound):
    # untuk koordinat x nanti rumusnya x (+/- berdasar (temp_pos+1 // 8 == 0) or (temp_pos+1 // 8 == 2) or (temp_pos+1 // 8 == 4) or (temp_pos+1 // 8 == 6)) ((61%8) - (27%8))*87
    # untuk koordinat y nanti rumusnya y-((61//8) - (27//8))*87 
    print ('check snake temp pos = '+str(temp_pos))
    if (temp_pos in all_snake_pos_dict):
        if (temp_pos==60):
            print ('ULAR')
            for i in range(29):
                if player_image_pos_dict[curr_player][0]>87:
                    player_image_pos_dict[curr_player][0]=player_image_pos_dict[curr_player][0]-6
                player_image_pos_dict[curr_player][1]=player_image_pos_dict[curr_player][1]+15
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                screen,dice_button = show_dice(screen,dice_button,img_dice1)
                pygame.display.flip()
            for i in range(29):
                player_image_pos_dict[curr_player][0]=player_image_pos_dict[curr_player][0]+9
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                screen,dice_button = show_dice(screen,dice_button,img_dice1)
                pygame.display.flip()
            screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
            screen = show_ladder_or_snake(screen,font1,font2,name_list,curr_player,temp_pos,all_ladder_pos_dict,all_snake_pos_dict,ladder_sound,snake_sound1)
            temp_pos = all_snake_pos_dict[60]
            all_player_pos_list[curr_player-1]=temp_pos
            screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
            screen,dice_button = show_dice(screen,dice_button,img_dice1)
            pygame.display.flip()
        elif (temp_pos==56):
            print ('ULAR')
            for i in range(29):
                if player_image_pos_dict[curr_player][0]>174:
                    player_image_pos_dict[curr_player][0]=player_image_pos_dict[curr_player][0]-15
                player_image_pos_dict[curr_player][1]=player_image_pos_dict[curr_player][1]+12
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                screen,dice_button = show_dice(screen,dice_button,img_dice1)
                pygame.display.flip()
            for i in range(29):
                player_image_pos_dict[curr_player][0]=player_image_pos_dict[curr_player][0]+3
                player_image_pos_dict[curr_player][1]=player_image_pos_dict[curr_player][1]+3
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                screen,dice_button = show_dice(screen,dice_button,img_dice1)
                pygame.display.flip()
            screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
            screen = show_ladder_or_snake(screen,font1,font2,name_list,curr_player,temp_pos,all_ladder_pos_dict,all_snake_pos_dict,ladder_sound,snake_sound1)
            temp_pos = all_snake_pos_dict[56]
            all_player_pos_list[curr_player-1]=temp_pos
            screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
            screen,dice_button = show_dice(screen,dice_button,img_dice1)
            pygame.display.flip()
        else:
            print ('ULAR')
            for i in range(29):
                player_image_pos_dict[curr_player][0]=player_image_pos_dict[curr_player][0]+15
                player_image_pos_dict[curr_player][1]=player_image_pos_dict[curr_player][1]+9
                screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                screen,dice_button = show_dice(screen,dice_button,img_dice1)
                pygame.display.flip()
            screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
            screen = show_ladder_or_snake(screen,font1,font2,name_list,curr_player,temp_pos,all_ladder_pos_dict,all_snake_pos_dict,ladder_sound,snake_sound1)
            temp_pos = all_snake_pos_dict[29]
            all_player_pos_list[curr_player-1]=temp_pos
            screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
            screen,dice_button = show_dice(screen,dice_button,img_dice1)
            pygame.display.flip()
        screen,dice_button,player_image_pos_dict, exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = check_position(screen,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,all_player_pos_list,winning_sound,dice_button,name_list,exit_button,font3,curr_player,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,player_image_pos_dict,battle_sound)
    return screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d

def update_player_image(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_dice,walking_sound,is_correct_bonus):
    print ('UPDATE POSISI GAMBAR')
    print ('KOTAK = ' + str(temp_pos))
    print ('PLAYER = ' + str(curr_player))

    for i in range(random_dice):
        if (is_correct_bonus == 1):
            all_player_pos_list[curr_player-1] = all_player_pos_list[curr_player-1]+1
            local_temp_pos = all_player_pos_list[curr_player-1]
            print ('local_temp_pos = '+str(local_temp_pos))
            if (local_temp_pos>63):
                all_player_pos_list[curr_player-1] = 63
                all_player_pos_list[curr_player-1] = all_player_pos_list[curr_player-1]-1
                local_temp_pos = all_player_pos_list[curr_player-1]
                if local_temp_pos in [7, 15, 23, 31, 39, 47, 55]:
                    ##gerak turun
                    screen,dice_button,player_image_pos_dict = move_player_to_down(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
                elif (local_temp_pos // 8 == 0) or (local_temp_pos // 8 == 2) or (local_temp_pos // 8 == 4) or (local_temp_pos // 8 == 6):
                    ##gerak kiri
                    screen,dice_button,player_image_pos_dict = move_player_to_left(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
                else:
                    ##gerak kanan
                    screen,dice_button,player_image_pos_dict = move_player_to_right(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
                is_correct_bonus = 0
            else:
                if (local_temp_pos % 8 == 0):
                    ##gerak naik
                    screen,dice_button,player_image_pos_dict = move_player_to_up(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
                elif (local_temp_pos // 8 == 0) or (local_temp_pos // 8 == 2) or (local_temp_pos // 8 == 4) or (local_temp_pos // 8 == 6):
                    ##gerak kanan
                    screen,dice_button,player_image_pos_dict = move_player_to_right(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
                else:
                    ##gerak kiri
                    screen,dice_button,player_image_pos_dict = move_player_to_left(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
        else:
            all_player_pos_list[curr_player-1] = all_player_pos_list[curr_player-1]-1
            local_temp_pos = all_player_pos_list[curr_player-1]
            if local_temp_pos in [7, 15, 23, 31, 39, 47, 55]:
                ##gerak turun
                screen,dice_button,player_image_pos_dict = move_player_to_down(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
            elif (local_temp_pos // 8 == 0) or (local_temp_pos // 8 == 2) or (local_temp_pos // 8 == 4) or (local_temp_pos // 8 == 6):
                ##gerak kiri
                screen,dice_button,player_image_pos_dict = move_player_to_left(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
            else:
                ##gerak kanan
                screen,dice_button,player_image_pos_dict = move_player_to_right(screen,walking_sound,player_image_pos_dict,img_board,img_dice1,font,font1,curr_player,total_player,img_player1,img_player2,img_player3,img_player4,name_list,all_player_pos_list,dice_button)
        temp_pos=all_player_pos_list[curr_player-1]
        print ('IMG POS=' + str(player_image_pos_dict))
    
    screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = move_player_to_ladder(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound)
    screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = move_player_to_snake(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound)
    return screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d

def main():
    print ('MAIN')
    #initialization
    screen,clock,battle_sound,snake_sound,snake_sound1,ladder_sound,walking_sound,winning_sound,choose_sound,main_menu_background,img_board,img_dice1,img_dice2,img_dice3,img_dice4,img_dice5,img_dice6,img_player1,img_player2,img_player3,img_player4,font,font1,font2,font3,text_a,text_b,text_c,text_d = setup_pygame()
    temp_pos = 0
    all_player_pos_list = [0,0,0,0]
    all_ladder_pos_dict = {
        27:61,
        37:55,
        44:58
    }
    all_snake_pos_dict = {
        60:20,
        56:19,
        29:7
    }
    bonus_dice_dict = {
        6:'a',
        12:'c',
        18:'d',
        24:'b',
        30:'a',
        36:'d',
        42:'c',
        48:'b',
        54:'b'
    }
    bonus_question_dict = {
        1:'Asal tari Tor-Tor:',
        2:'Asal tari Piring:',
        3:'Rumah adat asal Sumatera Barat:',
        4:'Rumah adat asal Jambi:',
        5:'Asal lagu Apuse:',
        6:'Lagu asal daerah Maluku:',
        7:'Baju adat Koteka berasal dari:',
        8:'Hewan khas asal Jakarta:',
        9:'Asal daerah hewan Komodo:',
        10:'Asal daerah hewan Anoa:',
        11:'Senjata adat asal Aceh:',
        12:'Tanaman khas asal Kalimantan dan Sumatera:'
    }
    bonus_question_choices_dict = {
        1:['Sumatera Utara','Jawa Barat','Jakarta','Jawa Tengah'],
        2:['Sumatera Barat','Jakarta','Sumatera Utara','Jawa Tengah'],
        3:['Gadang','Honai','Panggung','Limas'],
        4:['Panggung','Honai','Limas','Gadang'],
        5:['Papua','Jakarta','Sumatera Utara','Jawa Tengah'],
        6:['Ayo Mama','Jali-jali','Es Lilin','Bungong Jeumpa'],
        7:['Papua','Jakarta','Sumatera Utara','Jawa Tengah'],
        8:['Elang Bondol','Anoa','Badak','Gajah'],
        9:['NTT','Jakarta','Sumatera Utara','Jawa Tengah'],
        10:['Sulawesi Tenggara','Jakarta','Sumatera Utara','Jawa Tengah'],
        11:['Rencong','Keris','Badik','Parang'],
        12:['Kantong Semar','Pepaya','Bunga Bangkai','Rafflesia']
    }
            
    finish_pos=63
    curr_player=1
    is_finish = False
    name_list = []
    player_image_pos_dict = {
        1:[0,655],
        2:[0,607],
        3:[40,607],
        4:[40,655]
    }
    choice_button_a,choice_button_b,choice_button_c,choice_button_d = reset_multiple_choice_button()
    dice_button = ""
    total_player = 0
    exit_button = ""
    is_correct_bonus = 1

    screen = main_menu(screen,main_menu_background,font,font1)
    choose_2player,choose_3player,choose_4player = "","",""
    screen,choose_2player,choose_3player,choose_4player = button_choose_player(screen,choose_2player,choose_3player,choose_4player,font1)
    while not is_finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_finish = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print (mouse_pos)
                if choose_2player != "" and choose_3player != "" and choose_4player != "":
                    print ("menu")
                    screen, choose_2player, choose_3player, choose_4player, name_list, total_player = click_choose_player(screen,choose_2player,choose_3player,choose_4player,choose_sound,total_player,name_list,mouse_pos)
                    if total_player != 0:
                        screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                        screen = show_player_order(screen,font,font1,total_player,name_list,curr_player)
                        screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                        screen,dice_button = show_dice(screen,dice_button,img_dice1)
                if dice_button == "":
                    if choice_button_a != "" and choice_button_b != "" and choice_button_c != "" and choice_button_d != "":
                        player_answer=''
                        if choice_button_a.collidepoint(mouse_pos):
                            player_answer='a'
                        elif choice_button_b.collidepoint(mouse_pos):
                            player_answer='b'
                        elif choice_button_c.collidepoint(mouse_pos):
                            player_answer='c'
                        elif choice_button_d.collidepoint(mouse_pos):
                            player_answer='d'
                        choose_sound.play()
                        print ('all player pos= '+str(all_player_pos_list))
                        screen,dice_button,player_image_pos_dict,all_player_pos_list,choice_button_a,choice_button_b,choice_button_c,choice_button_d = check_answer(screen,name_list,curr_player,temp_pos,bonus_dice_dict,player_answer,ladder_sound,snake_sound,font1,font2,img_board,img_dice1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict,all_ladder_pos_dict,font,all_snake_pos_dict,snake_sound1,winning_sound,exit_button,font3,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_dice,walking_sound,all_player_pos_list,dice_button)
                        screen,dice_button = show_dice(screen,dice_button,img_dice1)
                        screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                        choice_button_a,choice_button_b,choice_button_c,choice_button_d = reset_multiple_choice_button()
                        temp_pos,curr_player = change_player(total_player,curr_player,temp_pos,all_player_pos_list)
                        screen = show_player_order(screen,font,font1,total_player,name_list,curr_player)
                if choose_2player == "" and choose_3player == "" and choose_4player == "" and dice_button!= "":                    
                    print ('TEKAN TOMBOL DADU')
                    pygame.event.clear()
                    if dice_button.collidepoint(mouse_pos):
                        print ('POSISI KLIK= '+str(mouse_pos))
                        pygame.event.clear()
                        screen.fill(WHITE)
                        screen = refresh_board(screen,img_board,font1,total_player,img_player1,img_player2,img_player3,img_player4,player_image_pos_dict)
                        print ('PEMAIN = '+str(curr_player))
                        random_dice = (random.randint(1,6))
                        print ('ACAK = '+str(random_dice))
                        temp_pos = temp_pos + random_dice
                        screen = show_player_position(screen,font,font1,total_player,name_list, all_player_pos_list,img_player1,img_player2,img_player3,img_player4)
                        print ('UPDATE POSISI GAMBAR #MAIN')
                        screen,dice_button,player_image_pos_dict,all_player_pos_list,exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = update_player_image(screen,all_ladder_pos_dict,temp_pos,player_image_pos_dict,curr_player,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,name_list, all_player_pos_list,dice_button,font2,all_snake_pos_dict,ladder_sound,snake_sound1,winning_sound,exit_button,font3,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,battle_sound,random_dice,walking_sound,is_correct_bonus)
                        if random_dice==1:
                            screen.blit(img_dice1, [850,550])
                        elif random_dice==2:
                            screen.blit(img_dice2, [850,550])
                        elif random_dice==3:
                            screen.blit(img_dice3, [850,550])
                        elif random_dice==4:
                            screen.blit(img_dice4, [850,550])
                        elif random_dice==5:
                            screen.blit(img_dice5, [850,550])
                        elif random_dice==6:
                            screen.blit(img_dice6, [850,550])
                        screen,dice_button,player_image_pos_dict, exit_button,choice_button_a,choice_button_b,choice_button_c,choice_button_d = check_position(screen,img_board,img_dice1,font1,total_player,img_player1,img_player2,img_player3,img_player4,font,all_player_pos_list,winning_sound,dice_button,name_list,exit_button,font3,curr_player,bonus_dice_dict,bonus_question_dict,bonus_question_choices_dict,choice_button_a,choice_button_b,choice_button_c,choice_button_d,text_a,text_b,text_c,text_d,player_image_pos_dict,battle_sound)
                        if choice_button_a != "" and choice_button_b != "" and choice_button_c != "" and choice_button_d != "":
                            pass
                        else:
                            temp_pos,curr_player = change_player(total_player,curr_player,temp_pos,all_player_pos_list)
                        screen = show_player_order(screen,font,font1,total_player,name_list,curr_player)
                if exit_button != "":
                    if exit_button.collidepoint(mouse_pos):
                        is_finish=True
        pygame.display.flip()
        clock.tick(5)
    pygame.quit()
if __name__ == "__main__":
    main()