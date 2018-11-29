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
kotak=0
kotak1=0
kotak2=0
kotak3=0
kotak4=0
tangga1=27
tangga2=37
tangga3=44
ttangga1=61
ttangga2=55
ttangga3=58
ular1=60
ular2=56
ular3=29
tular1=20
tular2=19
tular3=7
kr1=6
kr2=12
kr3=18
kr4=24
kr5=30
kr6=36
kr7=42
kr8=48
kr9=54
finish=63
player=1
jkr1='a'
jkr2='c'
jkr3='d'
jkr4='b'
jkr5='a'
jkr6='d'
jkr7='c'
jkr8='b'
jkr9='b'
selesai = False
nama = []
pos_x1 = 0
pos_y1 = 655
pos_x2 = 0
pos_y2 = 607
pos_x3 = 40
pos_y3 = 607
pos_x4 = 40
pos_y4 = 655
screen = pygame.display.set_mode([1060, 700])
pygame.display.set_caption('Ular Tangga')
clock = pygame.time.Clock()
pygame.mixer.music.load("musik/lagu1.mp3")
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()
suara_battle = pygame.mixer.Sound("musik/battle.wav")
suara_uler = pygame.mixer.Sound("musik/uler.wav")
suara_uler1 = pygame.mixer.Sound("musik/uler1.ogg")
suara_tangga = pygame.mixer.Sound("musik/menang1.wav")
suara_jalan = pygame.mixer.Sound("musik/jalan.ogg")
suara_menang = pygame.mixer.Sound("musik/menang.ogg")
suara_pilih = pygame.mixer.Sound("musik/pilih.wav")
peta = pygame.image.load("gambar/tes2.png").convert()
tes_background = pygame.image.load("gambar/background.png").convert()
background = pygame.transform.scale(tes_background,(1060,700))
papan = pygame.image.load("gambar/papan4.png").convert()
dadu1 = pygame.image.load("gambar/dadu1-1.png").convert()
dadu1.set_colorkey(WHITE)
dadu2 = pygame.image.load("gambar/DADU2.png").convert()
dadu2.set_colorkey(WHITE)
dadu3 = pygame.image.load("gambar/DADU3.png").convert()
dadu3.set_colorkey(WHITE)
dadu4 = pygame.image.load("gambar/DADU4.png").convert()
dadu4.set_colorkey(WHITE)
dadu5 = pygame.image.load("gambar/DADU5.png").convert()
dadu5.set_colorkey(WHITE)
dadu6 = pygame.image.load("gambar/DADU6.png").convert()
dadu6.set_colorkey(WHITE)
player1 = pygame.image.load("gambar/PEMAIN1.png").convert()
player1.set_colorkey(WHITE)
player2 = pygame.image.load("gambar/PEMAIN2.png").convert()
player2.set_colorkey(WHITE)
player3 = pygame.image.load("gambar/PEMAIN3.png").convert()
player3.set_colorkey(WHITE)
player4 = pygame.image.load("gambar/PEMAIN4.png").convert()
player4.set_colorkey(WHITE)
font = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 30)
font3 = pygame.font.Font(None, 25)
jawaba = None
jawabb = None
jawabc = None
jawabd = None
texta = font1.render('A.', True, WHITE)
textb = font1.render('B.', True, WHITE)
textc = font1.render('C.', True, WHITE)
textd = font1.render('D.', True, WHITE)
tomboldadu= None
jumlah = 0
tahan = 0
tombolkeluar = None
def cetakulangpapan():
    print 'CETAK ULANG PAPAN'
    screen.fill(WHITE)
    screen.blit(papan, [0,0])
    if jumlah==2:
        screen.blit(player1,[pos_x1,pos_y1])
        screen.blit(player2,[pos_x2,pos_y2])
    elif jumlah==3:
        screen.blit(player1,[pos_x1,pos_y1])
        screen.blit(player2,[pos_x2,pos_y2])
        screen.blit(player3,[pos_x3,pos_y3])
    else:
        screen.blit(player1,[pos_x1,pos_y1])
        screen.blit(player2,[pos_x2,pos_y2])
        screen.blit(player3,[pos_x3,pos_y3])
        screen.blit(player4,[pos_x4,pos_y4])
    screen.blit(dadu1, [850,550])
    text = font1.render('Tombol Dadu', True, BLACK)
    screen.blit(text,(812,660))
def cetaktanggadanular():
    print 'CETAK TANGGA DAN ULAR'
    global tomboldadu
    text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
    screen.blit(text,(830,440))
    if (kotak==tangga1) or (kotak==tangga2) or (kotak==tangga3):
        suara_tangga.play()
        text = font1.render('Selamat', True, BLACK)
        screen.blit(text,(830,400))
        text = font1.render('Tangga', True, BLACK)
        screen.blit(text,(830,480))
    else:
        suara_uler1.play()
        text = font1.render('Maaf', True, BLACK)
        screen.blit(text,(830,400))
        text = font1.render('Ular', True, BLACK)
        screen.blit(text,(830,480))
class Gantipemain:
    def ganti(self):
        print 'GANTI PEMAIN'
        global player,kotak,kotak1,kotak2,kotak3,kotak4,jumlah,nama
        if (jumlah==2):
            if (player==1):
                print 'GANTI PLAYER 2'
                kotak=kotak2
                player=player+1
            else:
                print 'GANTI PLAYER 1'
                kotak=kotak1
                player=1
        elif (jumlah==3):
            if (player==1):
                kotak=kotak2
                player=player+1
            elif(player==2):
                kotak=kotak3
                player=player+1
            else:
                kotak=kotak1
                player=1
        else:
            if (player==1):
                kotak=kotak2
                player=player+1
            elif(player==2):
                kotak=kotak3
                player=player+1
            elif(player==3):
                kotak=kotak4
                player=player+1
            else:
                kotak=kotak1
                player=1
def updateposisigambar(a,b):
    global kotak,kotak1,kotak2,kotak3,kotak4,player,pos_x1,pos_y1,pos_x2,pos_y2,pos_x3,pos_y3,pos_x4,pos_y4
    acak = a
    tanda = b
    langkah = acak
    print 'UPDATE POSISI GAMBAR'
    print 'KOTAK = ',kotak
    print 'PLAYER = ',player
    if player==1:
        kotak1=kotak
        if kotak1>63:
            kotak1=63-(kotak1-63)
        if kotak<=7:
            for i in range(acak):
                if pos_y1==655:
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x1 = pos_x1+87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x1-87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                if pos_y1==568:
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x1 = pos_x1+87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x1+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                if pos_x1==609 and pos_y1==568:
                    for j in range(1):
                        if tanda == 0:
                            pos_y1=pos_y1-87
                            print 'tanda ',tanda
                        else:
                            pos_y1=pos_y1+87
                            print 'tanda ',tanda
                        langkah = langkah-1
                        print 'posisi player 1: ',(pos_x1,pos_y1)
                        print 'posisi player 1: ', kotak1
                        print 'sisa langkah player 1: ',langkah
                        cetakulangpapan()
                        posisi()
                        tomboldadu = dadu1.get_rect()
                        tomboldadu = tomboldadu.move(850,550)
                        pygame.display.flip()
                if langkah==0:
                    break   
        if kotak>7 and kotak <=15:
            for i in range(acak):
                if pos_x1<609 and pos_y1==655:
                    suara_jalan.play()
                    if tanda == 0 :
                        pos_x1 = pos_x1+87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x1-87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x1==609 and pos_y1==655:
                        for j in range(1):
                            if tanda == 0:
                                pos_y1=pos_y1-87
                                print 'tanda ',tanda
                            else:
                                pos_y1=pos_y1+87
                                print 'tanda ',tanda
                            langkah = langkah-1
                            print 'posisi player 1: ',(pos_x1,pos_y1)
                            print 'posisi player 1: ', kotak1
                            print 'sisa langkah player 1: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        if langkah == 0:
                            break
            if pos_y1==481:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x1 = pos_x1 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x1 - 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x1==0 and pos_y1 ==481:
                        break
            if pos_x1 == 0 and pos_y1 == 481:
                for j in range(1):
                    if tanda == 0:
                        pos_y1=pos_y1-87
                        print 'tanda ',tanda
                    else:
                        pos_y1=pos_y1+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y1==568:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x1 = pos_x1 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x1 + 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        if kotak>15 and kotak<=23:
            for i in range(acak):
                if pos_x1>0 and pos_y1==568:
                    suara_jalan.play()
                    if tanda ==0:
                        pos_x1 = pos_x1-87
                    else:
                        pos_x1=pos_x1+87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x1==0 and pos_y1==568:
                        for j in range(1):
                            if tanda == 0:
                                pos_y1=pos_y1-87
                            else:
                                pos_y1=pos_y1+87
                            langkah = langkah-1
                            print 'posisi player 1: ',(pos_x1,pos_y1)
                            print 'posisi player 1: ', kotak1
                            print 'sisa langkah player 1: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_x1 == 609 and pos_y1 == 394:
                for j in range(1):
                    if tanda == 0:
                        pos_y1=pos_y1-87
                        print 'tanda ',tanda
                    else:
                        pos_y1=pos_y1+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y1 == 481:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1+87
                    else:
                        pos_x1=pos_x1-87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        if kotak>23 and kotak<=31:
            for i in range(acak):
                if pos_x1<609 and pos_y1==481:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1+87
                    else:
                        pos_x1=pos_x1-87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x1==609 and pos_y1==481:
                        for j in range(1):
                            if tanda==0:
                                pos_y1=pos_y1-87
                            else:
                                pos_y1=pos_y1+87
                            langkah = langkah-1
                            print 'posisi player 1: ',(pos_x1,pos_y1)
                            print 'posisi player 1: ', kotak1
                            print 'sisa langkah player 1: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y1 == 307:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x1 = pos_x1 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x1 - 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x1==0 and pos_y1 ==307:
                        break
            if pos_x1 == 0 and pos_y1 == 307:
                for j in range(1):
                    if tanda == 0:
                        pos_y1=pos_y1-87
                        print 'tanda ',tanda
                    else:
                        pos_y1=pos_y1+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y1==394:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1 - 87
                    else:
                        pos_x1=pos_x1+87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        if kotak>31 and kotak<=39:
            for i in range(acak):
                if pos_x1>0 and pos_y1==394:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1-87
                    else:
                        pos_x1=pos_x1+87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x1==0 and pos_y1==394:
                        for j in range(1):
                            if tanda==0:
                                pos_y1=pos_y1-87
                            else:
                                pos_y1=pos_y1+87
                            langkah = langkah-1
                            print 'posisi player 1: ',(pos_x1,pos_y1)
                            print 'posisi player 1: ', kotak1
                            print 'sisa langkah player 1: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y1 == 220:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x1 = pos_x1 + 87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x1 + 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x1==609 and pos_y1 ==220:
                        break
            if pos_x1 == 609 and pos_y1 == 220:
                for j in range(1):
                    if tanda == 0:
                        pos_y1=pos_y1-87
                        print 'tanda ',tanda
                    else:
                        pos_y1=pos_y1+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y1 == 307:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1+87
                    else:
                        pos_x1 = pos_x1-87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        if kotak>39 and kotak<=47:
            for i in range(acak):
                if pos_x1<609 and pos_y1==307:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1+87
                    else:
                        pos_x1=pos_x1-87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x1==609 and pos_y1==307:
                        for j in range(1):
                            if tanda==0:
                                pos_y1=pos_y1-87
                            else:
                                pos_y1=pos_y1+87
                            langkah=langkah-1
                            print 'posisi player 1: ',(pos_x1,pos_y1)
                            print 'posisi player 1: ', kotak1
                            print 'sisa langkah player 1: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_x1 == 0 and pos_y1 == 133:
                for j in range(1):
                    if tanda == 0:
                        pos_y1=pos_y1-87
                        print 'tanda ',tanda
                    else:
                        pos_y1=pos_y1+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y1==220:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1 - 87
                    else:
                        pos_x1=pos_x1+87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        if kotak>47 and kotak<=55:
            for i in range(acak):
                if pos_x1>0 and pos_y1==220:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1-87
                    else:
                        pos_x1=pos_x1+87
                    langkah = langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x1==0 and pos_y1==220:
                        for j in range(1):
                            if tanda==0:
                                pos_y1=pos_y1-87
                            else:
                                pos_y1=pos_y1+87
                            langkah = langkah-1
                            print 'posisi player 1: ',(pos_x1,pos_y1)
                            print 'posisi player 1: ', kotak1
                            print 'sisa langkah player 1: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y1 == 133:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1+87
                    else:
                        pos_x1=pos_x1-87
                    langkah=langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        if kotak>55 and kotak<=63:
            for i in range(acak):
                if pos_x1<609 and pos_y1==133:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1+87
                    else:
                        pos_x1=pos_x1-87
                    langkah=langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x1==609 and pos_y1==133:
                        for j in range(1):
                            if tanda==0:
                                pos_y1=pos_y1-87
                            else:
                                pos_y1=pos_y1+87
                            langkah=langkah-1
                            print 'posisi player 1: ',(pos_x1,pos_y1)
                            print 'posisi player 1: ', kotak1
                            print 'sisa langkah player 1: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y1==46:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1 - 87
                    else:
                        pos_x1=pos_x1+87
                    langkah=langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        if kotak>63:
            for k in range(acak):
                if pos_x1>0:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1 = pos_x1 - 87
                    else:
                        pos_x1=pos_x1+87
                    langkah=langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    break
            if pos_x1<=0:
                for i in range (langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x1=pos_x1+87
                    else:
                        pos_x1=pos_x1-87
                    langkah=langkah-1
                    print 'posisi player 1: ',(pos_x1,pos_y1)
                    print 'posisi player 1: ', kotak1
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            kotak = 63 - (kotak-63)
    if player==2:
        kotak2=kotak
        if kotak2>63:
            kotak2=63-(kotak2-63)
        if kotak<=7:
            for i in range(acak):
                suara_jalan.play()
                if pos_y2==607:
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                if pos_y2==520:
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2+87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                if pos_x2==609 and pos_y2==520:
                    for j in range(1):
                        if tanda == 0:
                            pos_y2=pos_y2-87
                            print 'tanda ',tanda
                        else:
                            pos_y2=pos_y2+87
                            print 'tanda ',tanda
                        langkah = langkah-1
                        print 'posisi player 1: ',(pos_x1,pos_y1)
                        print 'posisi player 1: ', kotak1
                        print 'sisa langkah player 1: ',langkah
                        cetakulangpapan()
                        posisi()
                        tomboldadu = dadu1.get_rect()
                        tomboldadu = tomboldadu.move(850,550)
                        pygame.display.flip()
                if langkah==0:
                    break
        elif kotak>7 and kotak <=15:
            for i in range(acak):
                if pos_x2<609 and pos_y2==607:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x2==609 and pos_y2==607:
                        for j in range(1):
                            if tanda==0:
                                pos_y2=pos_y2-87
                            else:
                                pos_y2=pos_y2+87
                            langkah = langkah-1
                            print 'posisi player 2: ',(pos_x2,pos_y2)
                            print 'posisi player 2: ', kotak2
                            print 'sisa langkah player 2: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y2==433:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x2 = pos_x2 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x2 - 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x2==0 and pos_y2 ==433:
                        break
            if pos_x2 == 0 and pos_y2 == 433:
                for j in range(1):
                    if tanda == 0:
                        pos_y2=pos_y2-87
                        print 'tanda ',tanda
                    else:
                        pos_y2=pos_y2+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y2==520:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2 - 87
                    else:
                        pos_x2 = pos_x2+87
                    langkah = langkah - 1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>15 and kotak<=23:
            for i in range(acak):
                if pos_x2>0 and pos_y2==520:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2 - 87
                    else:
                        pos_x2 = pos_x2+87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x2==0 and pos_y2==520:
                        for j in range(1):
                            if tanda==0:
                                pos_y2=pos_y2-87
                            else:
                                pos_y2=pos_y2+87
                            langkah = langkah-1
                            print 'posisi player 2: ',(pos_x2,pos_y2)
                            print 'posisi player 2: ', kotak2
                            print 'sisa langkah player 2: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_x2 == 609 and pos_y2 == 346:
                for j in range(1):
                    if tanda == 0:
                        pos_y2=pos_y2-87
                        print 'tanda ',tanda
                    else:
                        pos_y2=pos_y2+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y2 == 433:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>23 and kotak<=31:
            for i in range(acak):
                if pos_x2<609 and pos_y2==433:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x2==609 and pos_y2==433:
                        for j in range(1):
                            if tanda==0:
                                pos_y2=pos_y2-87
                            else:
                                pos_y2=pos_y2+87
                            langkah = langkah-1
                            print 'posisi player 2: ',(pos_x2,pos_y2)
                            print 'posisi player 2: ', kotak2
                            print 'sisa langkah player 2: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y2==259:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x2 = pos_x2 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x2 - 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x2==0 and pos_y2 ==259:
                        break
            if pos_x2 == 0 and pos_y2 == 259:
                for j in range(1):
                    if tanda == 0:
                        pos_y2=pos_y2-87
                        print 'tanda ',tanda
                    else:
                        pos_y2=pos_y2+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y2==346:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2 - 87
                    else:
                        pos_x2 = pos_x2+87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>31 and kotak<=39:
            for i in range(acak):
                if pos_x2>0 and pos_y2==346:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2 - 87
                    else:
                        pos_x2 = pos_x2+87
                    langkah = langkah -1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x2==0 and pos_y2==346:
                        for j in range(1):
                            if tanda==0:
                                pos_y2=pos_y2-87
                            else:
                                pos_y2=pos_y2+87
                            langkah = langkah-1
                            print 'posisi player 2: ',(pos_x2,pos_y2)
                            print 'posisi player 2: ', kotak2
                            print 'sisa langkah player 2: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y2==172:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x2 = pos_x2 + 87
                        print 'tanda ',tanda
                    else:
                        pos_x1 = pos_x2 + 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x2==609 and pos_y2 ==172:
                        break
            if pos_x2 == 609 and pos_y2 == 172:
                for j in range(1):
                    if tanda == 0:
                        pos_y2=pos_y2-87
                        print 'tanda ',tanda
                    else:
                        pos_y2=pos_y2+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y2 == 259:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>39 and kotak<=47:
            for i in range(acak):
                if pos_x2<609 and pos_y2==259:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x2==609 and pos_y2==259:
                        for j in range(1):
                            if tanda==0:
                                pos_y2=pos_y2-87
                            else:
                                pos_y2=pos_y2+87
                            langkah=langkah-1
                            print 'posisi player 2: ',(pos_x2,pos_y2)
                            print 'posisi player 2: ', kotak2
                            print 'sisa langkah player 2: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_x2 == 0 and pos_y2 == 85:
                for j in range(1):
                    if tanda == 0:
                        pos_y2=pos_y2-87
                        print 'tanda ',tanda
                    else:
                        pos_y2=pos_y2+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y2==172:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2 - 87
                    else:
                        pos_x2 = pos_x2+87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>47 and kotak<=55:
            for i in range(acak):
                if pos_x2>0 and pos_y2==172:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2 - 87
                    else:
                        pos_x2 = pos_x2+87
                    langkah = langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x2==0 and pos_y2==172:
                        for j in range(1):
                            if tanda==0:
                                pos_y2=pos_y2-87
                            else:
                                pos_y2=pos_y2+87
                            langkah = langkah-1
                            print 'posisi player 2: ',(pos_x2,pos_y2)
                            print 'posisi player 2: ', kotak2
                            print 'sisa langkah player 2: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y2 == 85:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah=langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>55 and kotak<=63:
            for i in range(acak):
                if pos_x2<609 and pos_y2==85:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah=langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x2==609 and pos_y2==85:
                        for j in range(1):
                            if tanda==0:
                                pos_y2=pos_y2-87
                            else:
                                pos_y2=pos_y2+87
                            langkah=langkah-1
                            print 'posisi player 2: ',(pos_x2,pos_y2)
                            print 'posisi player 2: ', kotak2
                            print 'sisa langkah player 2: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y2==-2:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2 - 87
                    else:
                        pos_x2 = pos_x2+87
                    langkah=langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>63:
            for k in range(acak):
                if pos_x2>0:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2 - 87
                    else:
                        pos_x2=pos_x2+87
                    langkah=langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    break
            if pos_x2<=0:
                for i in range (langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x2 = pos_x2+87
                    else:
                        pos_x2=pos_x2-87
                    langkah=langkah-1
                    print 'posisi player 2: ',(pos_x2,pos_y2)
                    print 'posisi player 2: ', kotak2
                    print 'sisa langkah player 2: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            kotak = 63 - (kotak-63)
    if player==3:
        kotak3=kotak
        if kotak<=7:
            for i in range(acak):
                if pos_y3 == 607:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                if pos_y3==520:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3+87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                if pos_x3==649 and pos_y3==520:
                    for j in range(1):
                        if tanda == 0:
                            pos_y3=pos_y3-87
                            print 'tanda ',tanda
                        else:
                            pos_y3=pos_y3+87
                            print 'tanda ',tanda
                        langkah = langkah-1
                        print 'posisi player 3: ',(pos_x3,pos_y3)
                        print 'posisi player 3: ', kotak3
                        print 'sisa langkah player 3: ',langkah
                        cetakulangpapan()
                        posisi()
                        tomboldadu = dadu1.get_rect()
                        tomboldadu = tomboldadu.move(850,550)
                        pygame.display.flip()
                if langkah==0:
                    break
        elif kotak>7 and kotak <=15:
            for i in range(acak):
                if pos_x3<649 and pos_y3==607:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x3==649 and pos_y3==607:
                        for j in range(1):
                            if tanda == 0:
                                pos_y3=pos_y3-87
                            else:
                                pos_y3=pos_y3+87
                            langkah = langkah-1
                            print 'posisi player 3: ',(pos_x3,pos_y3)
                            print 'posisi player 3: ', kotak3
                            print 'sisa langkah player 3: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y3==433:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x3 = pos_x3 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x3 = pos_x3 - 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x3==40 and pos_y3 ==433:
                        break
            if pos_x3 == 40 and pos_y3 == 433:
                for j in range(1):
                    if tanda == 0:
                        pos_y3=pos_y3-87
                        print 'tanda ',tanda
                    else:
                        pos_y3=pos_y3+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y3==520:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3 - 87
                    else:
                        pos_x3=pos_x3+87
                    langkah = langkah - 1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>15 and kotak<=23:
            for i in range(acak):
                if pos_x3>40 and pos_y3==520:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3 - 87
                    else:
                        pos_x3=pos_x3+87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x3==40 and pos_y3==520:
                        for j in range(1):
                            if tanda == 0:
                                pos_y3=pos_y3-87
                            else:
                                pos_y3=pos_y3+87
                            langkah = langkah-1
                            print 'posisi player 3: ',(pos_x3,pos_y3)
                            print 'posisi player 3: ', kotak3
                            print 'sisa langkah player 3: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_x3 == 649 and pos_y3 == 346:
                for j in range(1):
                    if tanda == 0:
                        pos_y3=pos_y3-87
                        print 'tanda ',tanda
                    else:
                        pos_y3=pos_y3+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y3 == 433:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>23 and kotak<=31:
            for i in range(acak):
                if pos_x3<649 and pos_y3==433:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x3==649 and pos_y3==433:
                        for j in range(1):
                            if tanda == 0:
                                pos_y3=pos_y3-87
                            else:
                                pos_y3=pos_y3+87
                            langkah = langkah-1
                            print 'posisi player 3: ',(pos_x3,pos_y3)
                            print 'posisi player 3: ', kotak3
                            print 'sisa langkah player 3: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y3==259:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x3 = pos_x3 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x3 = pos_x3 - 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x3==40 and pos_y3 ==259:
                        break
            if pos_x3 == 40 and pos_y3 == 259:
                for j in range(1):
                    if tanda == 0:
                        pos_y3=pos_y3-87
                        print 'tanda ',tanda
                    else:
                        pos_y3=pos_y3+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y3==346:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3 - 87
                    else:
                        pos_x3=pos_x3+87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>31 and kotak<=39:
            for i in range(acak):
                if pos_x3>40 and pos_y3==346:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3 - 87
                    else:
                        pos_x3=pos_x3+87
                    langkah = langkah -1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x3==40 and pos_y3==346:
                        for j in range(1):
                            if tanda == 0:
                                pos_y3=pos_y3-87
                            else:
                                pos_y3=pos_y3+87
                            langkah = langkah-1
                            print 'posisi player 3: ',(pos_x3,pos_y3)
                            print 'posisi player 3: ', kotak3
                            print 'sisa langkah player 3: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y3==172:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x3 = pos_x3 + 87
                        print 'tanda ',tanda
                    else:
                        pos_x3 = pos_x3 + 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x3==649 and pos_y3 ==172:
                        break
            if pos_x3 == 649 and pos_y3 == 172:
                for j in range(1):
                    if tanda == 0:
                        pos_y3=pos_y3-87
                        print 'tanda ',tanda
                    else:
                        pos_y3=pos_y3+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y3 == 259:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>39 and kotak<=47:
            for i in range(acak):
                if pos_x3<649 and pos_y3==259:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x3==649 and pos_y3==259:
                        for j in range(1):
                            if tanda == 0:
                                pos_y3=pos_y3-87
                            else:
                                pos_y3=pos_y3+87
                            langkah=langkah-1
                            print 'posisi player 3: ',(pos_x3,pos_y3)
                            print 'posisi player 3: ', kotak3
                            print 'sisa langkah player 3: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_x3 == 40 and pos_y3 == 85:
                for j in range(1):
                    if tanda == 0:
                        pos_y3=pos_y3-87
                        print 'tanda ',tanda
                    else:
                        pos_y3=pos_y3+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y3==172:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3 - 87
                    else:
                        pos_x3=pos_x3+87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>47 and kotak<=55:
            for i in range(acak):
                if pos_x3>40 and pos_y3==172:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3 - 87
                    else:
                        pos_x3=pos_x3+87
                    langkah = langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x3==40 and pos_y3==172:
                        for j in range(1):
                            if tanda == 0:
                                pos_y3=pos_y3-87
                            else:
                                pos_y3=pos_y3+87
                            langkah = langkah-1
                            print 'posisi player 3: ',(pos_x3,pos_y3)
                            print 'posisi player 3: ', kotak3
                            print 'sisa langkah player 3: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y3 == 85:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah=langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>55 and kotak<=63:
            for i in range(acak):
                if pos_x3<649 and pos_y3==85:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah=langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x3==649 and pos_y3==85:
                        for j in range(1):
                            if tanda == 0:
                                pos_y3=pos_y3-87
                            else:
                                pos_y3=pos_y3+87
                            langkah=langkah-1
                            print 'posisi player 3: ',(pos_x3,pos_y3)
                            print 'posisi player 3: ', kotak3
                            print 'sisa langkah player 3: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y3==-2:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3 - 87
                    else:
                        pos_x3=pos_x3+87
                    langkah=langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>63:
            for k in range(acak):
                if pos_x3>40:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3 - 87
                    else:
                        pos_x3=pos_x3+87
                    langkah=langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    break
            if pos_x3<=40:
                for i in range (langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x3 = pos_x3+87
                    else:
                        pos_x3 = pos_x3-87
                    langkah=langkah-1
                    print 'posisi player 3: ',(pos_x3,pos_y3)
                    print 'posisi player 3: ', kotak3
                    print 'sisa langkah player 3: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            kotak = 63 - (kotak-63)
        if kotak3>63:
            kotak3=63-(kotak3-63)
    if player==4:
        kotak4=kotak
        if kotak<=7:
            for i in range(acak):
                if pos_y4==655:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                if pos_y4==568:
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x4 = pos_x4+87
                        print 'tanda ',tanda
                    else:
                        pos_x4 = pos_x4+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                if pos_x4==649 and pos_y4==568:
                    for j in range(1):
                        if tanda == 0:
                            pos_y4=pos_y4-87
                            print 'tanda ',tanda
                        else:
                            pos_y4=pos_y4+87
                            print 'tanda ',tanda
                        langkah = langkah-1
                        print 'posisi player 4: ',(pos_x4,pos_y4)
                        print 'posisi player 4: ', kotak4
                        print 'sisa langkah player 4: ',langkah
                        cetakulangpapan()
                        posisi()
                        tomboldadu = dadu1.get_rect()
                        tomboldadu = tomboldadu.move(850,550)
                        pygame.display.flip()
                if langkah==0:
                    break
        elif kotak>7 and kotak <=15:
            for i in range(acak):
                if pos_x4<649 and pos_y4==655:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x4==649 and pos_y4==655:
                        for j in range(1):
                            if tanda==0:
                                pos_y4=pos_y4-87
                            else:
                                pos_y4=pos_y4+87
                            langkah = langkah-1
                            print 'posisi player 4: ',(pos_x4,pos_y4)
                            print 'posisi player 4: ', kotak4
                            print 'sisa langkah player 4: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y4==481:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x4 = pos_x4 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x4 = pos_x4 - 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x4==40 and pos_y4 ==481:
                        break
            if pos_x4 == 40 and pos_y4 == 481:
                for j in range(1):
                    if tanda == 0:
                        pos_y4=pos_y4-87
                        print 'tanda ',tanda
                    else:
                        pos_y4=pos_y4+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y4==568:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4 - 87
                    else:
                        pos_x4=pos_x4+87
                    langkah = langkah - 1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>15 and kotak<=23:
            for i in range(acak):
                if pos_x4>40 and pos_y4==568:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4 - 87
                    else:
                        pos_x4=pos_x4+87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x4==40 and pos_y4==568:
                        for j in range(1):
                            if tanda==0:
                                pos_y4=pos_y4-87
                            else:
                                pos_y4=pos_y4+87
                            langkah = langkah-1
                            print 'posisi player 4: ',(pos_x4,pos_y4)
                            print 'posisi player 4: ', kotak4
                            print 'sisa langkah player 4: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_x4 == 649 and pos_y4 == 394:
                for j in range(1):
                    if tanda == 0:
                        pos_y4=pos_y4-87
                        print 'tanda ',tanda
                    else:
                        pos_y4=pos_y4+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y4 == 481:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>23 and kotak<=31:
            for i in range(acak):
                if pos_x4<649 and pos_y4==481:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x4==649 and pos_y4==481:
                        for j in range(1):
                            if tanda==0:
                                pos_y4=pos_y4-87
                            else:
                                pos_y4=pos_y4+87
                            langkah = langkah-1
                            print 'posisi player 4: ',(pos_x4,pos_y4)
                            print 'posisi player 4: ', kotak4
                            print 'sisa langkah player 4: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y4 == 307:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x4 = pos_x4 - 87
                        print 'tanda ',tanda
                    else:
                        pos_x4 = pos_x4 - 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x4==40 and pos_y4 ==307:
                        break
            if pos_x4 == 40 and pos_y4 == 307:
                for j in range(1):
                    if tanda == 0:
                        pos_y4=pos_y4-87
                        print 'tanda ',tanda
                    else:
                        pos_y4=pos_y4+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y4==394:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4 - 87
                    else:
                        pos_x4=pos_x4+87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>31 and kotak<=39:
            for i in range(acak):
                if pos_x4>40 and pos_y4==394:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4 - 87
                    else:
                        pos_x4=pos_x4+87
                    langkah = langkah -1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x4==40 and pos_y4==394:
                        for j in range(1):
                            if tanda==0:
                                pos_y4=pos_y4-87
                            else:
                                pos_y4=pos_y4+87
                            langkah = langkah-1
                            print 'posisi player 4: ',(pos_x4,pos_y4)
                            print 'posisi player 4: ', kotak4
                            print 'sisa langkah player 4: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y4 == 220:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda == 0:
                        pos_x4 = pos_x4 + 87
                        print 'tanda ',tanda
                    else:
                        pos_x4 = pos_x4 + 87
                        print 'tanda ',tanda
                    langkah = langkah - 1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                    elif pos_x4==649 and pos_y4 ==220:
                        break
            if pos_x4 == 649 and pos_y4 == 220:
                for j in range(1):
                    if tanda == 0:
                        pos_y4=pos_y4-87
                        print 'tanda ',tanda
                    else:
                        pos_y4=pos_y4+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y4 == 307:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>39 and kotak<=47:
            for i in range(acak):
                if pos_x4<649 and pos_y4==307:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x4==649 and pos_y4==307:
                        for j in range(1):
                            if tanda==0:
                                pos_y4=pos_y4-87
                            else:
                                pos_y4=pos_y4+87
                            langkah=langkah-1
                            print 'posisi player 4: ',(pos_x4,pos_y4)
                            print 'posisi player 4: ', kotak4
                            print 'sisa langkah player 4: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_x4 == 40 and pos_y4 == 133:
                for j in range(1):
                    if tanda == 0:
                        pos_y4=pos_y4-87
                        print 'tanda ',tanda
                    else:
                        pos_y4=pos_y4+87
                        print 'tanda ',tanda
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 1: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            if pos_y4==220:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4 - 87
                    else:
                        pos_x4=pos_x4+87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>47 and kotak<=55:
            for i in range(acak):
                if pos_x4>40 and pos_y4==220:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4 - 87
                    else:
                        pos_x4=pos_x4+87
                    langkah = langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x4==40 and pos_y4==220:
                        for j in range(1):
                            if tanda==0:
                                pos_y4=pos_y4-87
                            else:
                                pos_y4=pos_y4+87
                            langkah = langkah-1
                            print 'posisi player 4: ',(pos_x4,pos_y4)
                            print 'posisi player 4: ', kotak4
                            print 'sisa langkah player 4: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y4 == 133:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah=langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>55 and kotak<=63:
            for i in range(acak):
                if pos_x4<649 and pos_y4==133:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah=langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    suara_jalan.play()
                    if pos_x4==649 and pos_y4==133:
                        for j in range(1):
                            if tanda==0:
                                pos_y4=pos_y4-87
                            else:
                                pos_y4=pos_y4+87
                            langkah=langkah-1
                            print 'posisi player 4: ',(pos_x4,pos_y4)
                            print 'posisi player 4: ', kotak4
                            print 'sisa langkah player 4: ',langkah
                            cetakulangpapan()
                            posisi()
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            pygame.display.flip()
                        break
                        if langkah == 0:
                            break
            if pos_y4==46:
                for k in range(langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4 - 87
                    else:
                        pos_x4=pos_x4+87
                    langkah=langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
        elif kotak>63:
            for k in range(acak):
                if pos_x4>40:
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4 - 87
                    else:
                        pos_x4=pos_x4+87
                    langkah=langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
                else:
                    break
            if pos_x4<=40:
                for i in range (langkah):
                    suara_jalan.play()
                    if tanda==0:
                        pos_x4 = pos_x4+87
                    else:
                        pos_x4=pos_x4-87
                    langkah=langkah-1
                    print 'posisi player 4: ',(pos_x4,pos_y4)
                    print 'posisi player 4: ', kotak4
                    print 'sisa langkah player 4: ',langkah
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    pygame.display.flip()
                    if langkah == 0:
                        break
            kotak = 63 - (kotak-63)
        if kotak4>63:
            kotak4=63-(kotak4-63)
    if (kotak==tangga1):
        print 'TANGGA'
        if player==1:
            pos_x1=380
            pos_y1=360
            for i in range(36):
                pos_x1=pos_x1-5
                pos_y1=pos_y1-8
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x1=174
            pos_y1=46
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga1
            kotak1=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif player==2:
            pos_x2=380
            pos_y2=360
            for i in range(36):
                pos_x2=pos_x2-5
                pos_y2=pos_y2-8
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x2=174
            pos_y2=-2            
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga1
            kotak2=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif player==3:
            pos_x3=380
            pos_y3=360
            for i in range(36):
                pos_x3=pos_x3-5
                pos_y3=pos_y3-8
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x3=214
            pos_y3=-2            
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga1
            kotak3=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        else:
            pos_x4=380
            pos_y4=360
            for i in range(36):
                pos_x4=pos_x4-5
                pos_y4=pos_y4-8
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x4=214
            pos_y4=46            
            cetakulangpapan()
            cetaktanggadanular()
            kotak = ttangga1
            kotak4=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        Cekposisi().cekposisi()
    if (kotak==tangga2):
        print 'TANGGA'
        if player==1:
            pos_x1=500
            pos_y1=270
            for i in range(20):
                pos_x1=pos_x1+5
                pos_y1=pos_y1-8
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x1=609
            pos_y1=133            
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga2
            kotak1=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif player==2:
            pos_x2=500
            pos_y2=270
            for i in range(20):
                pos_x2=pos_x2+5
                pos_y2=pos_y2-8
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x2=609
            pos_y2=85            
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga2
            kotak2=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif player==3:
            pos_x3=500
            pos_y3=270
            for i in range(20):
                pos_x3=pos_x3+5
                pos_y3=pos_y3-8
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x3=649
            pos_y3=85            
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga2
            kotak3=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        else:
            pos_x4=500
            pos_y4=270
            for i in range(20):
                pos_x4=pos_x4+5
                pos_y4=pos_y4-8
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x4=649
            pos_y4=133            
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga2
            kotak4=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        Cekposisi().cekposisi()
    if (kotak==tangga3):
        print 'TANGGA'
        if player==1:
            pos_x1=326
            pos_y1=186
            for i in range(53):
                pos_x1=pos_x1+1
                pos_y1=pos_y1-3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x1=435
            pos_y1=46
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga3
            kotak1=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif player==2:
            pos_x2=326
            pos_y2=186
            for i in range(53):
                pos_x2=pos_x2+1
                pos_y2=pos_y2-3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x2=435
            pos_y2=-2
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga3
            kotak2=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif player==3:
            pos_x3=326
            pos_y3=186
            for i in range(53):
                pos_x3=pos_x3+1
                pos_y3=pos_y3-3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x3=475
            pos_y3=-2
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga3
            kotak3=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        else:
            pos_x4=326
            pos_y4=186
            for i in range(53):
                pos_x4=pos_x4+1
                pos_y4=pos_y4-3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x4=475
            pos_y4=46            
            cetakulangpapan()
            cetaktanggadanular()
            kotak=ttangga3
            kotak4=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        Cekposisi().cekposisi()
    if (kotak==ular1):
        print 'ULAR'
        if (player==1):
            pos_x1=316
            pos_y1=60
            for i in range(12):
                pos_y1=pos_y1-5
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(12):
                pos_x1=pos_x1-4
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(10):
                pos_x1=pos_x1-20
                pos_y1=pos_y1+20
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(6):
                pos_y1=pos_y1+30
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(10):
                pos_x1=pos_x1+20
                pos_y1=pos_y1+15
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x1=348
            pos_y1=481
            print 'posisi player 1: ',(pos_x1,pos_y1)
            print 'posisi player 1: ', kotak1
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular1
            kotak1=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()            
        elif (player==2):
            pos_x2=316
            pos_y2=60
            for i in range(12):
                pos_y2=pos_y2-5
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(12):
                pos_x2=pos_x2-4
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(10):
                pos_x2=pos_x2-20
                pos_y2=pos_y2+20
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(6):
                pos_y2=pos_y2+30
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(10):
                pos_x2=pos_x2+20
                pos_y2=pos_y2+15
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x2=348
            pos_y2=433            
            print 'posisi player 2: ',(pos_x2,pos_y2)
            print 'posisi player 2: ', kotak2
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular1
            kotak2=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif(player==3):
            pos_x3=316
            pos_y3=60
            for i in range(12):
                pos_y3=pos_y3-5
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(12):
                pos_x3=pos_x3-4
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(10):
                pos_x3=pos_x3-20
                pos_y3=pos_y3+20
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(6):
                pos_y3=pos_y3+30
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(10):
                pos_x3=pos_x3+20
                pos_y3=pos_y3+15
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x3=388
            pos_y3=433            
            print 'posisi player 3: ',(pos_x3,pos_y3)
            print 'posisi player 3: ', kotak3
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular1
            kotak3=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        else:
            pos_x4=316
            pos_y4=60
            for i in range(12):
                pos_y4=pos_y4-5
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(12):
                pos_x4=pos_x4-4
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(10):
                pos_x4=pos_x4-20
                pos_y4=pos_y4+20
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(6):
                pos_y4=pos_y4+30
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(10):
                pos_x4=pos_x4+20
                pos_y4=pos_y4+15
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x4=388
            pos_y4=481            
            print 'posisi player 4: ',(pos_x4,pos_y4)
            print 'posisi player 4: ', kotak4
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular1
            kotak4=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        Cekposisi().cekposisi()
    if (kotak==ular2):
        print 'ULAR'
        if (player==1):
            pos_x1=612
            pos_y1=10
            for i in range(12):
                pos_x1=pos_x1-20
                pos_y1=pos_y1+20
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(12):
                pos_x1=pos_x1-18
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(5):
                pos_y1=pos_y1+30
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x1=261
            pos_y1=481            
            print 'posisi player 1: ',(pos_x1,pos_y1)
            print 'posisi player 1: ', kotak1
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular2
            kotak1=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif (player==2):
            pos_x2=612
            pos_y2=10
            for i in range(12):
                pos_x2=pos_x2-20
                pos_y2=pos_y2+20
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(12):
                pos_x2=pos_x2-18
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(5):
                pos_y2=pos_y2+30
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x2=261
            pos_y2=433            
            print 'posisi player 2: ',(pos_x2,pos_y2)
            print 'posisi player 2: ', kotak2
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular2
            kotak2=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif(player==3):
            pos_x3=612
            pos_y3=10
            for i in range(12):
                pos_x3=pos_x3-20
                pos_y3=pos_y3+20
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(12):
                pos_x3=pos_x3-18
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(5):
                pos_y3=pos_y3+30
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x3=301
            pos_y3=433            
            print 'posisi player 3: ',(pos_x3,pos_y3)
            print 'posisi player 3: ', kotak3
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular2
            kotak3=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        else:
            pos_x4=612
            pos_y4=10
            for i in range(12):
                pos_x4=pos_x4-20
                pos_y4=pos_y4+20
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(12):
                pos_x4=pos_x4-18
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            for i in range(5):
                pos_y4=pos_y4+30
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x4=301
            pos_y4=481            
            print 'posisi player 4: ',(pos_x4,pos_y4)
            print 'posisi player 4: ', kotak4
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular2
            kotak4=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        Cekposisi().cekposisi()
    if (kotak==ular3):
        print 'ULAR'
        if (player==1):
            pos_x1=234
            pos_y1=328
            for i in range(12):
                pos_x1=pos_x1+30
                pos_y1=pos_y1+20
                print 'posisi player 1: ',(pos_x1,pos_y1)
                print 'posisi player 1: ', kotak1
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x1=609
            pos_y1=655            
            print 'posisi player 1: ',(pos_x1,pos_y1)
            print 'posisi player 1: ', kotak1
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular3
            kotak1=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif (player==2):
            pos_x2=234
            pos_y2=328
            for i in range(12):
                pos_x2=pos_x2+30
                pos_y2=pos_y2+20
                print 'posisi player 2: ',(pos_x2,pos_y2)
                print 'posisi player 2: ', kotak2
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x2=609
            pos_y2=607            
            print 'posisi player 2: ',(pos_x2,pos_y2)
            print 'posisi player 2: ', kotak2
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular3
            kotak2=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        elif(player==3):
            pos_x3=234
            pos_y3=328
            for i in range(12):
                pos_x3=pos_x3+30
                pos_y3=pos_y3+20
                print 'posisi player 3: ',(pos_x3,pos_y3)
                print 'posisi player 3: ', kotak3
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x3=649
            pos_y3=607            
            print 'posisi player 3: ',(pos_x3,pos_y3)
            print 'posisi player 3: ', kotak3
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular3
            kotak3=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        else:
            pos_x4=234
            pos_y4=328
            for i in range(12):
                pos_x4=pos_x4+30
                pos_y4=pos_y4+20
                print 'posisi player 4: ',(pos_x4,pos_y4)
                print 'posisi player 4: ', kotak4
                cetakulangpapan()
                posisi()
                tomboldadu = dadu1.get_rect()
                tomboldadu = tomboldadu.move(850,550)
                pygame.display.flip()
            pos_x4=649
            pos_y4=655            
            print 'posisi player 4: ',(pos_x4,pos_y4)
            print 'posisi player 4: ', kotak4
            cetakulangpapan()
            cetaktanggadanular()
            kotak=tular3
            kotak4=kotak
            posisi()
            tomboldadu = dadu1.get_rect()
            tomboldadu = tomboldadu.move(850,550)
            pygame.display.flip()
        Cekposisi().cekposisi()
def tambah():
    global kotak
    print 'TAMBAH'
    tambah.angka = random.randint(1,5)
    print 'Tambahan Angka: ',tambah.angka
    kotak=kotak+tambah.angka
    print 'UPDATE POSISI GAMBAR #TAMBAH'
    updateposisigambar(tambah.angka,0)
    Cekposisi().cekposisi()
    pygame.display.flip()
def kurang():
    global kotak
    print 'KURANG'
    kurang.angka = random.randint(1,5)
    print 'Pengurangan Angka: ',kurang.angka
    kotak=kotak-kurang.angka
    print 'UPDATE POSISI GAMBAR #KURANG'
    updateposisigambar(kurang.angka,1)
    Cekposisi().cekposisi()
    pygame.display.flip()
class Cekposisi:
    def jawaban(self,jawaban):
        global kotak,kotak1,kotak2,kotak3,kotak4,jumlah,pos_x1,pos_x2,pos_x3,pos_x4,pos_y1,pos_y2,pos_y3,pos_y4
        print 'JAWABAN'
        print 'KOTAK= ',kotak
        '''if jumlah==2:
            Gantipemain().ganti()
        elif jumlah==3:
            Gantipemain().ganti()
            Gantipemain().ganti()
        elif jumlah==4:
            Gantipemain().ganti()
            Gantipemain().ganti()
            Gantipemain().ganti()'''
        if kotak==kr1:
            if jawaban==jkr1:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                print 'CETAK ULANG PAPAN #JAWABAN'
                cetakulangpapan()
                suara_uler.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
                print 'SELESAI JAWABAN'
        if kotak==kr2:
            if jawaban==jkr2:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                cetakulangpapan()
                suara_uler.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
        if kotak==kr3:
            if jawaban==jkr3:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                cetakulangpapan()
                suara_uler.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
        if kotak==kr4:
            if jawaban==jkr4:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                cetakulangpapan()
                suara_uler.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
        if kotak==kr5:
            if jawaban==jkr5:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                cetakulangpapan()
                suara_uler.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
        if kotak==kr6:
            if jawaban==jkr6:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                cetakulangpapan()
                suara_uler.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
        if kotak==kr7:
            if jawaban==jkr7:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                cetakulangpapan()
                suara_uler.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
        if kotak==kr8:
            if jawaban==jkr8:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                cetakulangpapan()
                suara_uler.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
        if kotak==kr9:
            if jawaban==jkr9:
                tambah()
                cetakulangpapan()
                suara_tangga.play()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' dapat', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Bonus: '+str(tambah.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
            else:
                kurang()
                cetakulangpapan()
                suara_ular.play()
                text = font1.render('Maaf', True, BLACK)
                screen.blit(text,(830,400))
                text = font2.render(str(nama[player-1])+' harus', True, BLACK)
                screen.blit(text,(830,440))
                text = font2.render('Mundur: '+str(kurang.angka)+' kotak', True, BLACK)
                screen.blit(text,(830,480))
    def cekposisi(self):
        global tombolkeluar,tomboldadu,kotak,kotak1,kotak2,kotak3,kotak4,tangga1,tangga2,tangga3, ttangga1,ttangga2,ttangga3,ular1,ular2,ular3,tular1,tular2,tular3,kr1,kr2,kr3,kr4,kr5,kr6,kr7,kr8,kr9,jkr1,jkr2,jkr3,jkr4,jkr5,jkr6,jkr7,jkr8,jkr9,player,finish,selesai,nama,pos_x1,pos_x2,pos_x3,pos_x4,pos_y1,pos_y2,pos_y3,pos_y4
        'gantiorang = Gantipemain()'
        print 'CEK POSISI'
        if ((pos_x1==0 and pos_y1==46) or (pos_x2==0 and pos_y2==-2) or (pos_x3==40 and pos_y3==-2) or (pos_x4==40 and pos_y4==46)) and kotak==63:
            print 'MENANG'
            if jumlah==2:
                suara_menang.play()
                tomboldadu=None
                cetakulangpapan()
                posisi()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font1.render('Menang', True, BLACK)
                screen.blit(text,(830,480))
                tombolkeluar = pygame.draw.rect(screen, (0,0,0),(850,510,100,30), 0)
                text = font3.render('Keluar', True, WHITE)
                screen.blit(text, [860, 520])
                if ((player)==1):                    
                    text = font1.render(str(nama[0]), True, BLACK)
                    screen.blit(text,(830,440))                        
                else:                        
                    text = font1.render(str(nama[1]), True, BLACK)
                    screen.blit(text,(830,440))                
            elif jumlah==3:
                suara_menang.play()
                tomboldadu=None
                cetakulangpapan()
                posisi()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font1.render('Menang', True, BLACK)
                screen.blit(text,(830,480))
                tombolkeluar = pygame.draw.rect(screen, (0,0,0),(850,510,100,30), 0)
                text = font3.render('Keluar', True, WHITE)
                screen.blit(text, [860, 520])
                if ((player)==1):                        
                    text = font1.render(str(nama[0]), True, BLACK)
                    screen.blit(text,(830,440))                        
                elif ((player)==2):                        
                    text = font1.render(str(nama[1]), True, BLACK)
                    screen.blit(text,(830,440))                        
                else:                        
                    text = font1.render(str(nama[2]), True, BLACK)
                    screen.blit(text,(830,440))
            elif jumlah==4:
                suara_menang.play()
                tomboldadu=None
                cetakulangpapan()
                posisi()
                text = font1.render('Selamat', True, BLACK)
                screen.blit(text,(830,400))
                text = font1.render('Menang', True, BLACK)
                screen.blit(text,(830,480))
                tombolkeluar = pygame.draw.rect(screen, (0,0,0),(850,510,100,30), 0)
                text = font3.render('Keluar', True, WHITE)
                screen.blit(text, [860, 520])
                if ((player)==1):                        
                    text = font1.render(str(nama[0]), True, BLACK)
                    screen.blit(text,(830,440))                        
                elif ((player)==2):                        
                    text = font1.render(str(nama[1]), True, BLACK)
                    screen.blit(text,(830,440))                        
                elif((player)==3):                        
                    text = font1.render(str(nama[2]), True, BLACK)
                    screen.blit(text,(830,440))                        
                else:                        
                    text = font1.render(str(nama[3]), True, BLACK)
                    screen.blit(text,(830,440))                        
                        
        if kotak==kr1:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihb = font1.render('Jawa Barat', True, WHITE)
                pilihc = font1.render('Jakarta', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                piliha = font1.render('Sumatera Barat', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                piliha = font1.render('Gadang', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Panggung', True, WHITE)
                pilihd = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                piliha = font1.render('Panggung', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Limas', True, WHITE)
                pilihd = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                piliha = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                piliha = font1.render('Ayo Mama', True, WHITE)
                pilihb = font1.render('Jali-jali', True, WHITE)
                pilihc = font1.render('Es Lilin', True, WHITE)
                pilihd = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                piliha = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                piliha = font1.render('Elang Bondol', True, WHITE)
                pilihb = font1.render('Anoa', True, WHITE)
                pilihc = font1.render('Badak', True, WHITE)
                pilihd = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                piliha = font1.render('NTT', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                piliha = font1.render('Sulawesi Tenggara', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                piliha = font1.render('Rencong', True, WHITE)
                pilihb = font1.render('Keris', True, WHITE)
                pilihc = font1.render('Badik', True, WHITE)
                pilihd = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                piliha = font1.render('Kantong Semar', True, WHITE)
                pilihb = font1.render('Pepaya', True, WHITE)
                pilihc = font1.render('Bunga Bangkai', True, WHITE)
                pilihd = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if kotak==kr2:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihb = font1.render('Jawa Barat', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                pilihc = font1.render('Sumatera Barat', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                pilihc = font1.render('Gadang', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                piliha = font1.render('Panggung', True, WHITE)
                pilihd = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                pilihc = font1.render('Panggung', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                piliha = font1.render('Limas', True, WHITE)
                pilihd = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                pilihc = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                pilihc = font1.render('Ayo Mama', True, WHITE)
                pilihb = font1.render('Jali-jali', True, WHITE)
                piliha = font1.render('Es Lilin', True, WHITE)
                pilihd = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                pilihc = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                pilihc = font1.render('Elang Bondol', True, WHITE)
                pilihb = font1.render('Anoa', True, WHITE)
                piliha = font1.render('Badak', True, WHITE)
                pilihd = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                pilihc = font1.render('NTT', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                pilihc = font1.render('Sulawesi Tenggara', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                pilihc = font1.render('Rencong', True, WHITE)
                pilihb = font1.render('Keris', True, WHITE)
                piliha = font1.render('Badik', True, WHITE)
                pilihd = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                pilihc = font1.render('Kantong Semar', True, WHITE)
                pilihb = font1.render('Pepaya', True, WHITE)
                piliha = font1.render('Bunga Bangkai', True, WHITE)
                pilihd = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if kotak==kr3:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                pilihd = font1.render('Sumatera Utara', True, WHITE)
                pilihb = font1.render('Jawa Barat', True, WHITE)
                pilihc = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                pilihd = font1.render('Sumatera Barat', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                pilihd = font1.render('Gadang', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Panggung', True, WHITE)
                piliha = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                pilihd = font1.render('Panggung', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Limas', True, WHITE)
                piliha = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                pilihd = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                pilihd = font1.render('Ayo Mama', True, WHITE)
                pilihb = font1.render('Jali-jali', True, WHITE)
                pilihc = font1.render('Es Lilin', True, WHITE)
                piliha = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                pilihd = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                pilihd = font1.render('Elang Bondol', True, WHITE)
                pilihb = font1.render('Anoa', True, WHITE)
                pilihc = font1.render('Badak', True, WHITE)
                piliha = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                pilihd = font1.render('NTT', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                pilihd = font1.render('Sulawesi Tenggara', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                pilihd = font1.render('Rencong', True, WHITE)
                pilihb = font1.render('Keris', True, WHITE)
                pilihc = font1.render('Badik', True, WHITE)
                piliha = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                pilihd = font1.render('Kantong Semar', True, WHITE)
                pilihb = font1.render('Pepaya', True, WHITE)
                pilihc = font1.render('Bunga Bangkai', True, WHITE)
                piliha = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if kotak==kr4:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                pilihb = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Barat', True, WHITE)
                pilihc = font1.render('Jakarta', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                pilihb = font1.render('Sumatera Barat', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                pilihb = font1.render('Gadang', True, WHITE)
                piliha = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Panggung', True, WHITE)
                pilihd = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                pilihb = font1.render('Panggung', True, WHITE)
                piliha = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Limas', True, WHITE)
                pilihd = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                pilihb = font1.render('Papua', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                pilihb = font1.render('Ayo Mama', True, WHITE)
                piliha = font1.render('Jali-jali', True, WHITE)
                pilihc = font1.render('Es Lilin', True, WHITE)
                pilihd = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                pilihb = font1.render('Papua', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                pilihb = font1.render('Elang Bondol', True, WHITE)
                piliha = font1.render('Anoa', True, WHITE)
                pilihc = font1.render('Badak', True, WHITE)
                pilihd = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                pilihb = font1.render('NTT', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                pilihb = font1.render('Sulawesi Tenggara', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                pilihb = font1.render('Rencong', True, WHITE)
                piliha = font1.render('Keris', True, WHITE)
                pilihc = font1.render('Badik', True, WHITE)
                pilihd = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                pilihb = font1.render('Kantong Semar', True, WHITE)
                piliha = font1.render('Pepaya', True, WHITE)
                pilihc = font1.render('Bunga Bangkai', True, WHITE)
                pilihd = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if kotak==kr5:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihb = font1.render('Jawa Barat', True, WHITE)
                pilihc = font1.render('Jakarta', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                piliha = font1.render('Sumatera Barat', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                piliha = font1.render('Gadang', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Panggung', True, WHITE)
                pilihd = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                piliha = font1.render('Panggung', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Limas', True, WHITE)
                pilihd = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                piliha = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                piliha = font1.render('Ayo Mama', True, WHITE)
                pilihb = font1.render('Jali-jali', True, WHITE)
                pilihc = font1.render('Es Lilin', True, WHITE)
                pilihd = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                piliha = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                piliha = font1.render('Elang Bondol', True, WHITE)
                pilihb = font1.render('Anoa', True, WHITE)
                pilihc = font1.render('Badak', True, WHITE)
                pilihd = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                piliha = font1.render('NTT', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                piliha = font1.render('Sulawesi Tenggara', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                piliha = font1.render('Rencong', True, WHITE)
                pilihb = font1.render('Keris', True, WHITE)
                pilihc = font1.render('Badik', True, WHITE)
                pilihd = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                piliha = font1.render('Kantong Semar', True, WHITE)
                pilihb = font1.render('Pepaya', True, WHITE)
                pilihc = font1.render('Bunga Bangkai', True, WHITE)
                pilihd = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if kotak==kr6:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                pilihd = font1.render('Sumatera Utara', True, WHITE)
                pilihb = font1.render('Jawa Barat', True, WHITE)
                pilihc = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                pilihd = font1.render('Sumatera Barat', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                pilihd = font1.render('Gadang', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Panggung', True, WHITE)
                piliha = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                pilihd = font1.render('Panggung', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Limas', True, WHITE)
                piliha = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                pilihd = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                pilihd = font1.render('Ayo Mama', True, WHITE)
                pilihb = font1.render('Jali-jali', True, WHITE)
                pilihc = font1.render('Es Lilin', True, WHITE)
                piliha = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                pilihd = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                pilihd = font1.render('Elang Bondol', True, WHITE)
                pilihb = font1.render('Anoa', True, WHITE)
                pilihc = font1.render('Badak', True, WHITE)
                piliha = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                pilihd = font1.render('NTT', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                pilihd = font1.render('Sulawesi Tenggara', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                pilihd = font1.render('Rencong', True, WHITE)
                pilihb = font1.render('Keris', True, WHITE)
                pilihc = font1.render('Badik', True, WHITE)
                piliha = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                pilihd = font1.render('Kantong Semar', True, WHITE)
                pilihb = font1.render('Pepaya', True, WHITE)
                pilihc = font1.render('Bunga Bangkai', True, WHITE)
                piliha = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if kotak==kr7:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihb = font1.render('Jawa Barat', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                pilihc = font1.render('Sumatera Barat', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                pilihc = font1.render('Gadang', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                piliha = font1.render('Panggung', True, WHITE)
                pilihd = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                pilihc = font1.render('Panggung', True, WHITE)
                pilihb = font1.render('Honai', True, WHITE)
                piliha = font1.render('Limas', True, WHITE)
                pilihd = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                pilihc = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                pilihc = font1.render('Ayo Mama', True, WHITE)
                pilihb = font1.render('Jali-jali', True, WHITE)
                piliha = font1.render('Es Lilin', True, WHITE)
                pilihd = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                pilihc = font1.render('Papua', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                pilihc = font1.render('Elang Bondol', True, WHITE)
                pilihb = font1.render('Anoa', True, WHITE)
                piliha = font1.render('Badak', True, WHITE)
                pilihd = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                pilihc = font1.render('NTT', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                pilihc = font1.render('Sulawesi Tenggara', True, WHITE)
                pilihb = font1.render('Jakarta', True, WHITE)
                piliha = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                pilihc = font1.render('Rencong', True, WHITE)
                pilihb = font1.render('Keris', True, WHITE)
                piliha = font1.render('Badik', True, WHITE)
                pilihd = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                pilihc = font1.render('Kantong Semar', True, WHITE)
                pilihb = font1.render('Pepaya', True, WHITE)
                piliha = font1.render('Bunga Bangkai', True, WHITE)
                pilihd = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if kotak==kr8:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                pilihb = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Barat', True, WHITE)
                pilihc = font1.render('Jakarta', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                pilihb = font1.render('Sumatera Barat', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                pilihb = font1.render('Gadang', True, WHITE)
                piliha = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Panggung', True, WHITE)
                pilihd = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                pilihb = font1.render('Panggung', True, WHITE)
                piliha = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Limas', True, WHITE)
                pilihd = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                pilihb = font1.render('Papua', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                pilihb = font1.render('Ayo Mama', True, WHITE)
                piliha = font1.render('Jali-jali', True, WHITE)
                pilihc = font1.render('Es Lilin', True, WHITE)
                pilihd = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                pilihb = font1.render('Papua', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                pilihb = font1.render('Elang Bondol', True, WHITE)
                piliha = font1.render('Anoa', True, WHITE)
                pilihc = font1.render('Badak', True, WHITE)
                pilihd = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                pilihb = font1.render('NTT', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                pilihb = font1.render('Sulawesi Tenggara', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                pilihb = font1.render('Rencong', True, WHITE)
                piliha = font1.render('Keris', True, WHITE)
                pilihc = font1.render('Badik', True, WHITE)
                pilihd = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                pilihb = font1.render('Kantong Semar', True, WHITE)
                piliha = font1.render('Pepaya', True, WHITE)
                pilihc = font1.render('Bunga Bangkai', True, WHITE)
                pilihd = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if kotak==kr9:
            screen.fill(WHITE)
            tomboldadu = None
            acaksoal = random.randint(1,12)
            if acaksoal == 1:
                soal = font1.render('Asal tari Tor-Tor:', True, BLACK)
                pilihb = font1.render('Sumatera Utara', True, WHITE)
                piliha = font1.render('Jawa Barat', True, WHITE)
                pilihc = font1.render('Jakarta', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 2:
                soal = font1.render('Asal tari Piring:', True, BLACK)
                pilihb = font1.render('Sumatera Barat', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 3:
                soal = font1.render('Rumah adat asal Sumatera Barat:', True, BLACK)
                pilihb = font1.render('Gadang', True, WHITE)
                piliha = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Panggung', True, WHITE)
                pilihd = font1.render('Limas', True, WHITE)
            elif acaksoal == 4:
                soal = font1.render('Rumah adat asal Jambi:', True, BLACK)
                pilihb = font1.render('Panggung', True, WHITE)
                piliha = font1.render('Honai', True, WHITE)
                pilihc = font1.render('Limas', True, WHITE)
                pilihd = font1.render('Gadang', True, WHITE)
            elif acaksoal == 5:
                soal = font1.render('Asal lagu Apuse:', True, BLACK)
                pilihb = font1.render('Papua', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 6:
                soal = font1.render('Lagu asal daerah Maluku:', True, BLACK)
                pilihb = font1.render('Ayo Mama', True, WHITE)
                piliha = font1.render('Jali-jali', True, WHITE)
                pilihc = font1.render('Es Lilin', True, WHITE)
                pilihd = font1.render('Bungong Jeumpa', True, WHITE)
            elif acaksoal == 7:
                soal = font1.render('Baju adat Koteka berasal dari:', True, BLACK)
                pilihb = font1.render('Papua', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 8:
                soal = font1.render('Hewan khas asal Jakarta:', True, BLACK)
                pilihb = font1.render('Elang Bondol', True, WHITE)
                piliha = font1.render('Anoa', True, WHITE)
                pilihc = font1.render('Badak', True, WHITE)
                pilihd = font1.render('Gajah', True, WHITE)
            elif acaksoal == 9:
                soal = font1.render('Asal daerah hewan Komodo:', True, BLACK)
                pilihb = font1.render('NTT', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 10:
                soal = font1.render('Asal daerah hewan Anoa:', True, BLACK)
                pilihb = font1.render('Sulawesi Tenggara', True, WHITE)
                piliha = font1.render('Jakarta', True, WHITE)
                pilihc = font1.render('Sumatera Utara', True, WHITE)
                pilihd = font1.render('Jawa Tengah', True, WHITE)
            elif acaksoal == 11:
                soal = font1.render('Senjata adat asal Aceh:', True, BLACK)
                pilihb = font1.render('Rencong', True, WHITE)
                piliha = font1.render('Keris', True, WHITE)
                pilihc = font1.render('Badik', True, WHITE)
                pilihd = font1.render('Parang', True, WHITE)
            elif acaksoal == 12:
                soal = font1.render('Tanaman khas asal Kalimantan dan Sumatera:', True, BLACK)
                pilihb = font1.render('Kantong Semar', True, WHITE)
                piliha = font1.render('Pepaya', True, WHITE)
                pilihc = font1.render('Bunga Bangkai', True, WHITE)
                pilihd = font1.render('Rafflesia', True, WHITE)
            screen.blit(soal, [200, 250])
            cetakjawaban()
            screen.blit(texta, [405,368])
            screen.blit(piliha, [445,368])
            screen.blit(textb, [405,420])
            screen.blit(pilihb, [445,420])
            screen.blit(textc, [405,472])
            screen.blit(pilihc, [445,472])
            screen.blit(textd, [405,524])
            screen.blit(pilihd, [445,524])
        if (kotak!=0):
            if(player==1):
                if (kotak==kotak2):
                    suara_battle.play()
                    kotak2=0
                    pos_x2 = 0
                    pos_y2 = 607
                    print 'CETAKULANGPAPAN #CEKPOSISI 1'
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[0])+' memulangkan '+str(nama[player]), True, BLACK)
                    screen.blit(text,(715,450))
                if (kotak==kotak3):
                    suara_battle.play()
                    kotak3=0
                    pos_x3 = 40
                    pos_y3 = 607
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)                    
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[0])+' memulangkan '+str(nama[player+1]), True, BLACK)
                    screen.blit(text,(705,450))                    
                    pygame.display.flip()
                if (kotak==kotak4):
                    suara_battle.play()
                    kotak4=0
                    pos_x4 = 40
                    pos_y4 = 655
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[0])+' memulangkan '+str(nama[player+2]), True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
            if (player==2):
                if (kotak==kotak1):
                    suara_battle.play()
                    kotak1=0
                    pos_x1 = 0
                    pos_y1 = 655
                    print 'CETAKULANGPAPAN #CEKPOSISI 2'
                    cetakulangpapan()
                    posisi()
                    print 'TOMBOLDADU'
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[1])+' memulangkan '+str(nama[player-2]), True, BLACK)
                    screen.blit(text,(705,450))
                    print 'SELESAI CEKPOSISI'
                    pygame.display.flip()
                if (kotak==kotak3):
                    suara_battle.play()
                    kotak3=0
                    pos_x3 = 40
                    pos_y3 = 607
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[1])+' memulangkan '+str(nama[player]), True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
                if (kotak==kotak4):
                    suara_battle.play()
                    kotak4=0
                    pos_x4 = 40
                    pos_y4 = 655
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[1])+' memulangkan '+str(nama[player+1]), True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
            if (player==3):
                if (kotak==kotak1):
                    suara_battle.play()
                    kotak1=0
                    pos_x1 = 0
                    pos_y1 = 655
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[2])+' memulangkan '+str(nama[player-3]), True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
                if (kotak==kotak2):
                    suara_battle.play()
                    kotak2=0
                    pos_x2 = 0
                    pos_y2 = 607
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[2])+' memulangkan '+str(nama[player-2]), True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
                if (kotak==kotak4):
                    suara_battle.play()
                    kotak4=0
                    pos_x4 = 40
                    pos_y4 = 655
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[2])+' memulangkan '+str(nama[player]), True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
            if (player==4):
                if (kotak==kotak1):
                    suara_battle.play()
                    kotak1=0
                    pos_x1 = 0
                    pos_y1 = 655
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[3])+' memulangkan '+str(nama[player-4]), True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
                if (kotak==kotak2):
                    suara_battle.play()
                    kotak2=0
                    pos_x2 = 0
                    pos_y2 = 607
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[3])+' memulangkan '+str(nama[player-3]),True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
                if (kotak==kotak3):
                    suara_battle.play()
                    kotak3=0
                    pos_x3 = 40
                    pos_y3 = 607
                    cetakulangpapan()
                    posisi()
                    tomboldadu = dadu1.get_rect()
                    tomboldadu = tomboldadu.move(850,550)
                    text = font1.render('Selamat', True, BLACK)
                    screen.blit(text,(830,400))
                    text = font1.render(str(nama[3])+' memulangkan '+str(nama[player-2]), True, BLACK)
                    screen.blit(text,(705,450))
                    pygame.display.flip()
def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass
def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,40)
  pygame.draw.rect(screen, WHITE,
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,60), 0)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, BLACK),((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()
def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
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
        display_box(screen, question + ": " + string.join(current_string,""))
    else:
        screen.fill(WHITE)
        current_string = current_string[0:-1]
        
  return string.join(current_string,"") 
def resetawal():
    print 'RESET AWAL'
    screen.fill(WHITE)
    screen.blit(peta, (0, 0))
    bingkaimenu1 = pygame.draw.rect(screen, GREY2,((screen.get_width() / 2)-160,220,350,350), 0)
    bingkaimenu1 = pygame.draw.rect(screen, GREY1,((screen.get_width() / 2)-150,230,330,330), 0)
    bingkaimenu = pygame.draw.rect(screen, WHITE,((screen.get_width() / 2)-140,240,310,310), 0)
    text = font.render('Selamat Datang', True, BLACK)
    screen.blit(text, [(screen.get_width() / 2)-120, 250])
    text = font1.render('Silahkan Pilih', True, BLACK)
    screen.blit(text, [(screen.get_width() / 2)-80, 300])
def tombolpemain():
    global duapemain,tigapemain,empatpemain
    print 'TOMBOL PEMAIN'
    tombolpemain.duapemain = pygame.draw.rect(screen, BLACK,((screen.get_width() / 2) - 60,(screen.get_height() / 2) - 10,150,50), 0)
    tombolpemain.tigapemain = pygame.draw.rect(screen, BLACK,((screen.get_width() / 2) - 60,(screen.get_height() / 2) + 60,150,50), 0)
    tombolpemain.empatpemain = pygame.draw.rect(screen, BLACK,((screen.get_width() / 2) - 60,(screen.get_height() / 2) + 130,150,50), 0)
    text = font1.render('2 Pemain', True, WHITE)
    screen.blit(text, [(screen.get_width() / 2)-50, (screen.get_height() / 2)])
    text = font1.render('3 Pemain', True, WHITE)
    screen.blit(text, [(screen.get_width() / 2)-50, (screen.get_height() / 2)+70])
    text = font1.render('4 Pemain', True, WHITE)
    screen.blit(text, [(screen.get_width() / 2)-50, (screen.get_height() / 2)+140])
def tomboldadu():
    global tomboldadu
    print 'TOMBOL DADU'
    tomboldadu = dadu1.get_rect()
    tomboldadu = tomboldadu.move(850,550)    
def giliran():
    print 'GILIRAN'
    text = font1.render('Giliran', True, BLACK)
    screen.blit(text,(870,50))
    if jumlah==2:
        text = font.render(str(nama[player-1]), True, BLACK)
        screen.blit(text,(860,80))
    if jumlah==3:
        text = font.render(str(nama[player-1]), True, BLACK)
        screen.blit(text,(860,80))
    if jumlah==4:
        text = font.render(str(nama[player-1]), True, BLACK)
        screen.blit(text,(860,80))
def hilangintomboljawaban():
    print 'HILANGIN TOMBOL JAWABAN'
    global jawaba,jawabb,jawabc,jawabd
    jawaba=None
    jawabb=None
    jawabc=None
    jawabd=None
def posisi():
    print 'POSISI'
    text = font1.render('Posisi', True, BLACK)
    screen.blit(text,(850,180))
    if jumlah==2:
        text = font.render(str(nama[0])+' : '+str(kotak1), True, BLACK)
        screen.blit(text,(860,220))
        screen.blit(player1,(800,215))
        text = font.render(str(nama[1])+' : '+str(kotak2), True, BLACK)
        screen.blit(text,(860,260))
        screen.blit(player2,(800,255))
    if jumlah==3:
        text = font.render(str(nama[0])+' : '+str(kotak1), True, BLACK)
        screen.blit(text,(860,220))
        screen.blit(player1,(800,215))
        text = font.render(str(nama[1])+' : '+str(kotak2), True, BLACK)
        screen.blit(text,(860,260))
        screen.blit(player2,(800,255))
        text = font.render(str(nama[2])+' : '+str(kotak3), True, BLACK)
        screen.blit(text,(860,300))
        screen.blit(player3,(800,295))
    if jumlah==4:
        text = font.render(str(nama[0])+' : '+str(kotak1), True, BLACK)
        screen.blit(text,(860,220))
        screen.blit(player1,(800,215))
        text = font.render(str(nama[1])+' : '+str(kotak2), True, BLACK)
        screen.blit(text,(860,260))
        screen.blit(player2,(800,255))
        text = font.render(str(nama[2])+' : '+str(kotak3), True, BLACK)
        screen.blit(text,(860,300))
        screen.blit(player3,(800,295))
        text = font.render(str(nama[3])+' : '+str(kotak4), True, BLACK)
        screen.blit(text,(860,340))
        screen.blit(player4,(800,335))
def cetakjawaban():
    global jawaba,jawabb,jawabc,jawabd,texta,textb,textc,textd
    print 'CETAK JAWABAN'
    jawaba = pygame.draw.rect(screen, BLACK,(395,358,350,50), 0)
    texta = font1.render('A.', True, WHITE)
    jawabb = pygame.draw.rect(screen, BLACK,(395,410,350,50), 0)
    textb = font1.render('B.', True, WHITE)
    jawabc = pygame.draw.rect(screen, BLACK,(395,462,350,50), 0)
    textc = font1.render('C.', True, WHITE)
    jawabd = pygame.draw.rect(screen, BLACK,(395,514,350,50), 0)
    textd = font1.render('D.', True, WHITE)   
def main():
    global tombolkeluar,jumlah,kotak,kotak1,kotak2,kotak3,kotak4,tangga1,tangga2,tangga3,ttangga1,ttangga2,ttangga3,ular1,ular2,ular3,tular1,tular2,tular3,kr1,kr2,kr3,kr4,kr5,kr6,kr7,kr8,kr9,jkr1,jkr2,jkr3,jkr4,jkr5,jkr6,jkr7,jkr8,jkr9,player,finish,selesai,nama,jumlah,pos_x1, pos_y1,pos_x2, pos_y2,pos_x3, pos_y3,pos_x4, pos_y4, papan,dadu1,dadu2,dadu3,dadu4,dadu5,dadu6,player1,player2,player3,player4,duapemain,tigapemain,empatpemain,tomboldadu,texta,textb,textc,textd
    print 'MAIN'
    resetawal()
    tombolpemain()
    while not selesai:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                selesai = True
            if event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('lagu1.mp3')
                pygame.mixer.music.play()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print mouse_pos
                if (tombolpemain.duapemain != None) and (tombolpemain.tigapemain != None) and (tombolpemain.empatpemain != None):
                    if tombolpemain.duapemain.collidepoint(mouse_pos):                    
                        suara_pilih.play()
                        jumlah=2
                        for i in range(0,2):
                            screen.fill(WHITE)
                            nama.append(ask(screen, "Nama Pemain "+ str(i+1)))                        
                        tombolpemain.duapemain = None
                        tombolpemain.tigapemain = None
                        tombolpemain.empatpemain = None
                        cetakulangpapan()
                        giliran()
                        posisi()
                        tomboldadu()

                    elif tombolpemain.tigapemain.collidepoint(mouse_pos):
                        suara_pilih.play()
                        jumlah=3
                        for i in range(0,3):
                            screen.fill(WHITE)
                            nama.append(ask(screen, "Nama Pemain "+ str(i+1)))
                        tombolpemain.duapemain = None
                        tombolpemain.tigapemain = None
                        tombolpemain.empatpemain = None
                        cetakulangpapan()
                        giliran()
                        posisi()
                        tomboldadu()
                        
                    elif tombolpemain.empatpemain.collidepoint(mouse_pos):
                        suara_pilih.play()
                        jumlah=4
                        for i in range(0,4):
                            screen.fill(WHITE)
                            nama.append(ask(screen, "Nama Pemain "+ str(i+1)))
                        tombolpemain.duapemain = None
                        tombolpemain.tigapemain = None
                        tombolpemain.empatpemain = None
                        cetakulangpapan()
                        giliran()
                        posisi()
                        tomboldadu()
                if tomboldadu==None:
                    if jawaba!= None and jawabb!= None and jawabc!=None and jawabd!= None:
                        if jawaba.collidepoint(mouse_pos):
                            suara_pilih.play()
                            Cekposisi().jawaban('a')
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            posisi()
                            hilangintomboljawaban()
                            Gantipemain().ganti()
                        elif jawabb.collidepoint(mouse_pos):
                            suara_pilih.play()
                            Cekposisi().jawaban('b')
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            posisi()
                            hilangintomboljawaban()
                            Gantipemain().ganti()
                        elif jawabc.collidepoint(mouse_pos):
                            suara_pilih.play()
                            Cekposisi().jawaban('c')
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            posisi()
                            hilangintomboljawaban()
                            Gantipemain().ganti()
                        elif jawabd.collidepoint(mouse_pos):
                            suara_pilih.play()
                            print 'PILIH JAWABAN D'
                            Cekposisi().jawaban('d')
                            tomboldadu = dadu1.get_rect()
                            tomboldadu = tomboldadu.move(850,550)
                            posisi()
                            hilangintomboljawaban()
                            print 'SELESAI MILIH'
                            Gantipemain().ganti()
                        giliran()
                if (tombolpemain.duapemain == None and tombolpemain.tigapemain == None and tombolpemain.empatpemain == None and tomboldadu!= None):                    
                    print 'TEKAN TOMBOL DADU'
                    pygame.event.clear()
                    if tomboldadu.collidepoint(mouse_pos):
                        print 'POSISI KLIK= ',mouse_pos
                        pygame.event.clear()
                        screen.fill(WHITE)
                        cetakulangpapan()
                        print 'PEMAIN = ',player
                        acak = (random.randint(1,6))
                        print 'ACAK = ',acak
                        kotak = kotak + acak
                        posisi()
                        print 'UPDATE POSISI GAMBAR #MAIN'
                        updateposisigambar(acak,0)
                        if acak==1:
                            screen.blit(dadu1, [850,550])
                        elif acak==2:
                            screen.blit(dadu2, [850,550])
                        elif acak==3:
                            screen.blit(dadu3, [850,550])
                        elif acak==4:
                            screen.blit(dadu4, [850,550])
                        elif acak==5:
                            screen.blit(dadu5, [850,550])
                        elif acak==6:
                            screen.blit(dadu6, [850,550])
                        cek = Cekposisi()
                        cek2=cek.cekposisi()
                        if jawaba!= None and jawabb!= None and jawabc!=None and jawabd!= None:
                            pass
                        else:
                            Gantipemain().ganti()
                        giliran()
                if tombolkeluar != None:
                    if tombolkeluar.collidepoint(mouse_pos):
                        selesai=True
        pygame.display.flip()
        clock.tick(5)
    pygame.quit()
if __name__ == "__main__":
    main()