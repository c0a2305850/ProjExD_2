import os
import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
DELTA = {  # 移動量辞書
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}# 練習1
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_bound(obj_rct):
    """
    こうかとんRect,または,爆弾Rectの画面外判定用の関数
    引数：こうかとんRect,または,爆弾Rect
    戻り値：横方向判定結果, 縦方向判定結果（True：画面内/False：画面外）
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate
# 練習3
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bm_img = pg.Surface((20, 20))
    bm_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bm_img, (255, 0, 0), (10, 10), 10)
    bm_rct = bm_img.get_rect()
    bm_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = +5, -5
    # 練習2
    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bm_rct): # こうかとんと爆弾がぶつかったら
            print("Gameover")
            return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in DELTA.items():
            if key_lst[k]:
            # if key_lst[k] == Trueは×
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        #if key_lst[pg.K_UP]:
        #    sum_mv[1] -= 5
        #if key_lst[pg.K_DOWN]:
        #    sum_mv[1] += 5
        #if key_lst[pg.K_LEFT]:
        #    sum_mv[0] -= 5
        #if key_lst[pg.K_RIGHT]:
        #    sum_mv[0] += 5
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)
        bm_rct.move_ip(vx, vy)
        screen.blit(bm_img, bm_rct)
        yoko, tate = check_bound(bm_rct)
        if not yoko:
            vx *= -1 # 横にはみだし
        if not tate:
            vy *= -1 # 縦にはみだし
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
