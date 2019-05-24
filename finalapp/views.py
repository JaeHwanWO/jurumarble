from django.shortcuts import render
from finalapp.models import Data
import random

def login(request):
    global data
    data = Data()
    return render(request, 'login.html')

def playerSelect_2p(request):
    data.players = 2
    data.save()
    return render(request, 'board_2p.html')

def playerSelect_3p(request):
    data.players = 3
    data.save()
    return render(request, 'board_3p.html')

def playerSelect_4p(request):
    data.players = 4
    data.save()
    return render(request, 'board_4p.html')

def diceCheck(request): #assume function name is views
    data.diceNum = int(request.GET['dicenum'])
   
    if data.players == 2:
        if data.turn == 1:
            data.pos1_2pmode += data.diceNum
        else:
            data.pos2_2pmode += data.diceNum
    elif data.players==3:
        if data.turn==1: 
            data.pos1_3pmode += data.diceNum
        elif data.turn==2 :
            data.pos2_3pmode += data.diceNum
        else:
            data.pos3_3pmode += data.diceNum
    else:
        if data.turn==1 :
            data.pos1_4pmode += data.diceNum
        elif data.turn==2 :
            data.pos2_4pmode += data.diceNum
        elif data.turn==3 :
            data.pos3_4pmode += data.diceNum
        else:
            data.pos4_4pmode += data.diceNum

    
    if data.players == 2:
        data.turn += 1
        if data.turn == 3:
            data.turn = 1
    elif data.players == 3:
        data.turn += 1
        if data.turn == 4:
            data.turn =1 
    else:
        data.turn += 1
        if data.turn == 5:
            data.turn =1


    data.save()

    if data.players == 2:
        return render(request, 'board_2p.html', {'pos1_2pmode':data.pos1_2pmode, 'pos2_2pmode':data.pos2_2pmode, 'whosturn':data.turn})
    elif data.players == 3:
        return render(request, 'board_3p.html', {'pos1_3pmode':data.pos1_3pmode, 'pos2_3pmode':data.pos2_3pmode, 'pos3_3pmode':data.pos3_3pmode, 'whosturn':data.turn})
    else:
        return render(request, 'board_4p.html', {'pos1_4pmode':data.pos1_4pmode, 'pos2_4pmode':data.pos2_4pmode, 'pos3_4pmode':data.pos3_4pmode, 'pos4_4pmode':data.pos4_4pmode, 'whosturn':data.turn})

def game_final01(request):
    return render(request, 'game_final01.html')

def game_final03(request):
    return render(request, 'game_final03.html')
def game_final04(request):
    return render(request, 'game_final04.html')
def game_final05(request):
    return render(request, 'game_final05.html')
def game_final06(request):
    return render(request, 'game_final06.html')
def game_final08(request):
    return render(request, 'game_final08.html')
def game_final09(request):
    return render(request, 'game_final09.html')
def game_final10(request):
    return render(request, 'game_final10.html')
def game_final11(request):
    return render(request, 'game_final11.html')
def game_final12(request):
    return render(request, 'game_final12.html')
def game_final13(request):
    return render(request, 'game_final13.html')
def game_final14(request):
    return render(request, 'game_final14.html')   

def game_final15(request):
    return render(request, 'game_final15.html') 
def game_final16(request):
    return render(request, 'game_final16.html') 

def game_final18(request):
    return render(request, 'game_final18.html') 



def game_final19(request):
    return render(request, 'game_final19.html')

def game_final20(request):
    return render(request, 'game_final20.html')
def game_final21(request):
    return render(request, 'game_final21.html')
def game_final23(request):
    return render(request, 'game_final23.html')
def game_final24A(request):
    return render(request, 'game_final24_a.html')
def game_final24B(request):
    return render(request, 'game_final24_b.html')
def game_final25(request):
    return render(request, 'game_final25.html')
def game_final26(request):
    return render(request, 'game_final26.html')
def game_final27(request):
    return render(request, 'game_final27.html')
def game_final28(request):
    return render(request, 'game_final28.html')
def game_final29(request):
    return render(request, 'game_final29.html')

def game_final31(request):
    randomNum = random.randrange(1,4)

    if randomNum == 1 :
        return render(request, 'game_final31_b.html')
    elif randomNum == 2 :
        return render(request, 'game_final31_c.html')
    else :
        return render(request, 'game_final31_d.html')


def game_final32(request):
    return render(request, 'game_final32.html')

def game_final34(request):
    if data.players==2 and data.turn==1:
        data.pos1_2pmode = 37
    elif data.players==2 and data.turn==2:
        data.pos2_2pmode = 37
        
    elif data.players==3 and data.turn==1:
        data.pos1_3pmode = 37
    elif data.players==3 and data.turn==2:
        data.pos2_3pmode = 37
    elif data.players==3 and data.turn==3:
        data.pos3_3pmode = 37
        
    elif data.players==4 and data.turn==1:
        data.pos1_4pmode = 37
    elif data.players==4 and data.turn==2:
        data.pos2_4pmode = 37
    elif data.players==4 and data.turn==3:
        data.pos3_4pmode = 37
    elif data.players==4 and data.turn==4:
        data.pos4_4pmode = 37

    data.save()

    return render(request, 'game_final34.html')

def game_final35(request):
    return render(request, 'game_final35.html')
def game_final37(request):
    return render(request, 'game_final37.html')

def game_final38(request):
    return render(request, 'game_final38.html')
def game_final39(request):
    return render(request, 'game_final39.html')

def goldenKey(request):
    randomNum2 = random.randrange(1,4)

    if randomNum2 == 1:
        return render(request, 'goldkey_a.html')
    elif randomNum2 == 2:
        return render(request, 'goldkey_b.html')   
    else:
        return render(request, 'goldkey_c.html') 
