import pyxel

pyxel.init(200,200)
pyxel.mouse(True)


x = 0
y = 0
z = 0

a = 0
b = 0
c = 0
COUNTER = 20
IS_PLAYING = 0

hands = ["グー", "チョキ", "パー"]

def update():
    global x, y, z, hands
    global IS_PLAYING
    
    if pyxel.btn(pyxel.KEY_0):
        x = hands[0]
        a = hands[1]
        IS_PLAYING = COUNTER
    elif pyxel.btn(pyxel.KEY_1):
        y = hands[1]
        b = hands[2]
        IS_PLAYING = COUNTER
    elif pyxel.btn(pyxel.KEY_2):
        z = hands[2]
        c = hands[0]
        IS_PLAYING = COUNTER



def draw():
    global x, y, z, hands
    global IS_PLAYING
    pyxel.cls(0)
    if IS_PLAYING:
        IS_PLAYING -= 1


    if not IS_PLAYING:
        pyxel.text(35, 41, "Let's Start!! 0:GU 1:CHOKI 2:PA-", pyxel.frame_count % 16)
        x = 0
        y = 0
        z = 0
    if IS_PLAYING:
        if x == hands[0]:
            pyxel.load("zyannkenn.pyxres")
            pyxel.blt(50, 50, 0, 0, 0, 16, 16, 0)
            pyxel.load("gu-nosenntaku.pyxres")
            pyxel.blt(0, 0, 0, 0, 0, 200, 16, 0)
            pyxel.load("anatanokachi.pyxres")
            pyxel.blt(0, 80, 0, 0, 0, 200, 16, 0)
            pyxel.load("zyannkenn_cyoki.pyxres")
            pyxel.blt(80, 50, 0, 0, 0, 16, 16, 0)
            
        elif y == hands[1]:
            pyxel.load("zyannkenn_cyoki.pyxres")
            pyxel.blt(50, 50, 0, 0, 0, 16, 16, 0)
            pyxel.load("chokinosenntaku.pyxres")
            pyxel.blt(0, 0, 0, 0, 0, 200, 16, 0)
            pyxel.load("anatanokachi.pyxres")
            pyxel.blt(0, 80, 0, 0, 0, 200, 16, 0)
            pyxel.load("zyannkenn_pa-.pyxres")
            pyxel.blt(80, 50, 0, 0, 0, 16, 16, 0)
        elif z == hands[2]:
            pyxel.load("zyannkenn_pa-.pyxres")
            pyxel.blt(50, 50, 0, 0, 0, 16, 16, 0)
            pyxel.load("pa-nosenntaku.pyxres")
            pyxel.blt(0, 0, 0, 0, 0, 200, 16, 0)
            pyxel.load("anatanokachi.pyxres")
            pyxel.blt(0, 80, 0, 0, 0, 200, 16, 0)
            pyxel.load("zyannkenn.pyxres")
            pyxel.blt(80, 50, 0, 0, 0, 16, 16, 0)




pyxel.run(update, draw)
