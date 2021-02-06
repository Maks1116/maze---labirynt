@namespace
class SpriteKind:
    Landmine = SpriteKind.create()
def setLevel(lvl: number):
    if lvl == 0:
        tiles.set_tilemap(tilemap("""
            level1
        """))
    elif lvl == 1:
        tiles.set_tilemap(tilemap("""
            level2
        """))
    elif lvl == 2:
        tiles.set_tilemap(tilemap("""
            level0
        """))
def create_wroga():
    global wrog
    wrog = sprites.create(img("""
            ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f11111111f.......
                    ......fd11111111df......
                    ......fd11111111df......
                    ......fddd1111dddf......
                    ......fbdbfddfbdbf......
                    ......fcdcf11fcdcf......
                    .......fb111111bf.......
                    ......fffcdb1bdffff.....
                    ....fc111cbfbfc111cf....
                    ....f1b1b1ffff1b1b1f....
                    ....fbfbffffffbfbfbf....
                    .........ffffff.........
                    ...........fff..........
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.enemy)
    animation.run_image_animation(wrog,
        [img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111ffff.....
                        ......fffcdb1bc111cf....
                        ....fc111cbfbf1b1b1f....
                        ....f1b1b1ffffbfbfbf....
                        ....fbfbfffffff.........
                        .........fffff..........
                        ..........fff...........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .....ffff111111bf.......
                        ....fc111cdb1bdfff......
                        ....f1b1bcbfbfc111cf....
                        ....fbfbfbffff1b1b1f....
                        .........fffffffbfbf....
                        ..........fffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """)],
        100,
        True)
    tiles.place_on_random_tile(wrog, sprites.castle.tile_path5)
    wrog.set_velocity(50, 50)
    wrog.set_stay_in_screen(False)
    wrog.set_bounce_on_wall(True)

def on_up_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f f 2 f e f . . 
                        . . f f f 2 f e e 2 2 f f f . . 
                        . . f e 2 f f e e 2 f e e f . . 
                        . f f e f f e e e f e e e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . . e f f f f f f f f 4 e . . 
                        . . . 4 f 2 2 2 2 2 e d d 4 . . 
                        . . . e f f f f f f e e 4 . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e f 2 f f f 2 f 2 e f . . 
                        . . f f f 2 2 e e f 2 f f f . . 
                        . . f e e f 2 e e f f 2 e f . . 
                        . f f e e e f e e e f f e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f e . . . 
                        . . 4 d d e 2 2 2 2 2 f 4 . . . 
                        . . . 4 e e f f f f f f e . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite, otherSprite):
    global musicPlayable
    musicPlayable = False
    sprite.destroy()
    otherSprite.destroy()
    music.pew_pew.play()
    create_wroga()
    musicPlayable = True
sprites.on_overlap(SpriteKind.enemy, SpriteKind.Landmine, on_on_overlap)

def on_b_pressed():
    global pocisk
    if pocisk > 0:
        pocisk = 0
        effects.clear_particles(mySprite)
        create_missile()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global ile_min
    if ile_min >= 0:
        ile_min += -1
        create_rock()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    pass
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 2 2 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """),
            img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e d d 4 . . . . 
                        . . . f 2 2 2 2 e d d e . . . . 
                        . . f f 5 5 4 4 f e e f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    pass
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    pass
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_countdown_end():
    controller.move_sprite(mySprite, 100, 100)
info.on_countdown_end(on_countdown_end)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e e e d d d f . . . 
                        . . . . . f 4 d d e 4 e f . . . 
                        . . . . . f e d d e 2 2 f . . . 
                        . . . . f f f e e f 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . 4 d d e 4 4 4 e f . . . 
                        . . . . e d d e 2 2 2 2 f . . . 
                        . . . . f e e f 4 4 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.start_effect(effects.fire, 1000)
    music.power_down.play()
    info.change_life_by(-1)
    scene.camera_shake(4, 500)
    sprite.destroy()
    pause(2000)
    create_wroga()
    effects.clear_particles(otherSprite)
    tiles.place_on_random_tile(mySprite, sprites.castle.tile_path4)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_up_released():
    pass
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . . f e 4 d d d d 4 e f e . . 
                        . . f e f 2 2 2 2 e d d 4 e . . 
                        . . e 4 f 2 2 2 2 e d d e . . . 
                        . . . . f 4 4 5 5 f e e . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 2 2 2 2 2 2 e f f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 2 2 2 2 f e f . . 
                        . . . e d d e 2 2 2 2 f 4 e . . 
                        . . . . e e f 5 5 4 4 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def create_missile():
    global missile
    missile = sprites.create(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . d 2 2 2 2 d . 
                    . 2 4 5 5 4 2 . 
                    . 2 5 f f 5 2 . 
                    . 2 5 f f 5 2 . 
                    . 2 4 5 5 4 2 . 
                    . d 2 2 2 2 d .
        """),
        SpriteKind.projectile)
    missile.lifespan = 20000
    missile.set_position(mySprite.x, mySprite.y)
    missile.set_velocity(randint(40, 100), randint(40, 100))
    missile.set_bounce_on_wall(True)

def on_on_overlap3(sprite, otherSprite):
    global ile_min, pocisk
    music.ba_ding.play()
    if otherSprite.z == 1:
        controller.move_sprite(mySprite, 200, 200)
        info.start_countdown(10)
    elif otherSprite.z == 2:
        ile_min += 1
    elif otherSprite.z == 3:
        pocisk = 1
        sprite.start_effect(effects.rings)
    otherSprite.destroy()
    create_ciastko()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

def create_ciastko():
    global ciastko
    if Math.percent_chance(20):
        ciastko = sprites.create(img("""
                . . 2 2 b b b b b . . . . . . . 
                            . 2 b 4 4 4 4 4 4 b . . . . . . 
                            2 2 4 4 4 4 d d 4 4 b . . . . . 
                            2 b 4 4 4 4 4 4 d 4 b . . . . . 
                            2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                            2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                            2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                            2 2 b 4 4 4 4 4 4 4 b e . . . . 
                            . 2 b b b 4 4 4 b b b e . . . . 
                            . . e b b b b b b b e e . . . . 
                            . . . e e b 4 4 b e e e b . . . 
                            . . . . . e e e e e e b d b b . 
                            . . . . . . . . . . . b 1 1 1 b 
                            . . . . . . . . . . . c 1 d d b 
                            . . . . . . . . . . . c 1 b c . 
                            . . . . . . . . . . . . c c . .
            """),
            SpriteKind.food)
        ciastko.z = 1
    elif Math.percent_chance(60):
        ciastko = sprites.create(img("""
                . . . . c c c b b b b b . . . . 
                            . . c c b 4 4 4 4 4 4 b b b . . 
                            . c c 4 4 4 4 4 5 4 4 4 4 b c . 
                            . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
                            e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
                            e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
                            e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
                            . e b 4 4 4 4 4 5 4 4 4 4 b e . 
                            8 7 e e b 4 4 4 4 4 4 b e e 6 8 
                            8 7 2 e e e e e e e e e e 2 7 8 
                            e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
                            e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
                            e b e 8 8 c c 8 8 c c c 8 e b e 
                            e e b e c c e e e e e c e b e e 
                            . e e b b 4 4 4 4 4 4 4 4 e e . 
                            . . . c c c c c e e e e e . . .
            """),
            SpriteKind.food)
        ciastko.z = 2
    else:
        ciastko = sprites.create(img("""
                . . . . . . . e c 7 . . . . . . 
                            . . . . e e e c 7 7 e e . . . . 
                            . . c e e e e c 7 e 2 2 e e . . 
                            . c e e e e e c 6 e e 2 2 2 e . 
                            . c e e e 2 e c c 2 4 5 4 2 e . 
                            c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
                            . e e e 2 2 2 2 2 2 2 2 2 4 e . 
                            . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
                            . . 2 e e 2 2 2 2 2 4 4 2 e . . 
                            . . . 2 2 e e 4 4 4 2 e e . . . 
                            . . . . . 2 2 e e e e . . . . .
            """),
            SpriteKind.food)
        ciastko.z = 3
    tiles.place_on_random_tile(ciastko, sprites.castle.tile_path5)
def musik():
    while True:
        if musicPlayable:
            music.play_melody("E B C5 A B G A F ", 120)
        if musicPlayable:
            music.play_melody("B A G A G F A C5 ", 120)
        if musicPlayable:
            music.play_melody("G B A G C5 B A B ", 120)

def on_overlap_tile(sprite, location):
    global level, ile_min, pocisk
    music.power_up.play()
    level += 1
    setLevel(level)
    for value in sprites.all_of_kind(SpriteKind.Landmine):
        value.destroy()
    for value2 in sprites.all_of_kind(SpriteKind.projectile):
        value2.destroy()
    for value3 in sprites.all_of_kind(SpriteKind.food):
        value3.destroy()
    for value4 in sprites.all_of_kind(SpriteKind.enemy):
        value4.destroy()
    tiles.place_on_random_tile(mySprite, sprites.castle.tile_path4)
    info.set_life(3)
    ile_min = 5
    pocisk = 0
    create_ciastko()
    create_wroga()
    controller.move_sprite(mySprite, 100, 100)
    scene.camera_follow_sprite(mySprite)
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.tile_path6,
    on_overlap_tile)

# gfdhfhgdhdhf

def on_on_overlap4(sprite, otherSprite):
    music.pew_pew.play()
    otherSprite.destroy()
    sprite.destroy()
    
    def on_set_timeout():
        music.magic_wand.play()
        create_wroga()
    set_timeout(on_set_timeout, 10000)
    
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap4)

def create_rock():
    global mina
    mina = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . c c c . . . . . . 
                    . . . . . . a b a a . . . . . . 
                    . . . . . c b a f c a c . . . . 
                    . . . . c b b b f f a c c . . . 
                    . . . . b b f a b b a a c . . . 
                    . . . . c b f f b a f c a . . . 
                    . . . . . c a a c b b a . . . . 
                    . . . . . . c c c c . . . . . . 
                    . . . . . . . c . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Landmine)
    animation.run_image_animation(mina,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . c c c . . . . . . 
                        . . . . . . a b a a . . . . . . 
                        . . . . . c b a f c a c . . . . 
                        . . . . c b b b f f a c c . . . 
                        . . . . b b f a b b a a c . . . 
                        . . . . c b f f b a f c a . . . 
                        . . . . . c a a c b b a . . . . 
                        . . . . . . c c c c . . . . . . 
                        . . . . . . . c . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c . . . . . . 
                        . . . . . c a a a a . . . . . . 
                        . . . . . a a f f b a . . . . . 
                        . . . . c a b f f c b . . . . . 
                        . . . . c b b b a f c b . . . . 
                        . . . . c b a c a b b b . . . . 
                        . . . . . b b f f a a c . . . . 
                        . . . . . . a a b b c . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . c c . . . . . . . 
                        . . . . c a a a a . . . . . . . 
                        . . . . a a f f b a . . . . . . 
                        . . . c a b f f c b . . . . . . 
                        . . . c b b b a f c b . . . . . 
                        . . . c b a c a b b b . . . . . 
                        . . . . b b f f a a c . . . . . 
                        . . . . . a a b b c . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . c . . . . . . . . 
                        . . . . c a a a c . . . . . . . 
                        . . . c c f a b b c . . . . . . 
                        . . . b f f b f a a . . . . . . 
                        . . . b b a b f f a . . . . . . 
                        . . . c b f b b a c . . . . . . 
                        . . . . b a f c c . . . . . . . 
                        . . . . . b b c . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
    mina.set_position(mySprite.x, mySprite.y)
    mina.z = game.runtime()
mina: Sprite = None
ciastko: Sprite = None
missile: Sprite = None
musicPlayable = False
wrog: Sprite = None
pocisk = 0
ile_min = 0
mySprite: Sprite = None
level = 0
level = 0
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
new_levels = [img("""
        f f f f f f f f f f 
            f f f f f f f f f f 
            f f f f f f f f f f 
            f 4 f f f f f f 7 f 
            f f f f f f f f f f 
            f f f f f f f f f f 
            f f f f f f f f f f 
            f f f f f f f f f f
    """),
    img("""
        9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 
            9 4 9 9 9 9 9 9 7 9 
            9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9
    """),
    img("""
        3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 
            3 4 3 3 3 3 3 3 7 3 
            3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3
    """)]
setLevel(level)
tiles.place_on_random_tile(mySprite, sprites.castle.tile_path4)
scene.camera_follow_sprite(mySprite)
create_ciastko()
create_wroga()
info.set_life(3)
ile_min = 5
pocisk = 0

def on_on_update():
    for value5 in sprites.all_of_kind(SpriteKind.Landmine):
        if game.runtime() - value5.z > 10000:
            value5.destroy()
game.on_update(on_on_update)
