#Sooter game code

#Creating the shooter character.
ShooterPlane = sprites.create(img("""
    ..ccc.........ffffff....
    ..f4cc.......fcc22ff....
    ..f44cc...fffccccff.....
    ..f244cccc22224442cc....
    ..f224cc2222222244b9c...
    ..cf222222222222b9999c..
    .c22c222222222911199b2c.
    f22ccccccc22229911b2222c
    fffffcc222c222222222222f
    .....f2224442222222222f.
    ....f222444fc2222222ff..
    ...c222444ffffffffff....
    ...c2222cfffc2f.........
    ...ffffffff2ccf.........
    .......ffff2cf..........
    ........fffff...........
"""), SpriteKind.player)

#Shooter stay on screen.
ShooterPlane.set_stay_in_screen(True)

#Set life to 4, game will if the shoot get hit by four bogeys.
info.set_life(8)

#Use the contorler buttons to move the shooter plane across the screen.
controller.move_sprite(ShooterPlane, 200, 200)

#When button A pressed, a Shooter will shoot a misslie towards enemy.
def on_event_pressed():
    missile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . 4 4 . . . . . . .
        . . . . . . 4 5 5 4 . . . . . .
        . . . . . . 2 5 5 2 . . . . . .
        . . . . . . . 2 2 . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), ShooterPlane, 200, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

#Every half a second an enemy bogey will pop up from the right edge of the screen.
def on_update_interval():
    bogey1 = sprites.create(img("""
        . . . . . . . . . c c 8 . . . .
        . . . . . . 8 c c c f 8 c c . .
        . . . c c 8 8 f c a f f f c c .
        . . c c c f f f c a a f f c c c
        8 c c c f f f f c c a a c 8 c c
        c c c b f f f 8 a c c a a a c c
        c a a b b 8 a b c c c c c c c c
        a f c a a b b a c c c c c f f c
        a 8 f c a a c c a c a c f f f c
        c a 8 a a c c c c a a f f f 8 a
        . a c a a c f f a a b 8 f f c a
        . . c c b a f f f a b b c c 6 c
        . . . c b b a f f 6 6 a b 6 c .
        . . . c c b b b 6 6 a c c c c .
        . . . . c c a b b c c c . . . .
        . . . . . c c c c c c . . . . .
    """), SpriteKind.enemy)

    #Setting how fast the bogey move accross the screen.
    bogey1.set_velocity(-80, 0)

    #Bogey will appear on the lft side of the screen.
    bogey1.left = scene.screen_width()
    bogey1.y = randint (0, scene.screen_height())

    #The nemey bogey will self destroy when it reach the end of the screen.
    bogey1.set_flag(SpriteFlag.AUTO_DESTROY, True)

game.on_update_interval(500, on_update_interval)

#Creating a second bogey; small and fast.
def on_update_interval2():
    bogey2 = sprites.create(img("""
        . . . b b . . .
        . . b 5 5 b . .
        . b 5 1 d 5 b .
        . b 5 1 3 5 b .
        . c d 1 3 5 c .
        . c d d 1 5 c .
        . . f d d f . .
        . . . f f . . .
    """), SpriteKind.enemy)

    #Setting how fast the bogey move accross the screen.
    bogey2.set_velocity(-150, 0)

    #Bogey will appear on the lft side of the screen.
    bogey2.left = scene.screen_width()
    bogey2.y = randint (0, scene.screen_height())

    #The emey bogey will self destroy when it reach the end of the screen.
    bogey2.set_flag(SpriteFlag.AUTO_DESTROY, True)

game.on_update_interval(2000, on_update_interval2)

#Creating the overlap event bogey and the ShooterPlane.
def on_overlap1(ShooterPlane, bogey1):
    bogey1.destroy()
    #On overlap, screen will shake, palyer will lose one life.
    ShooterPlane.start_effect(effects.ashes)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap1)

#Creating the overlap event bogey and the ShooterPlane.
def on_overlap2(ShooterPlane, bogey2):
    bogey2.destroy()
    #On overlap, screen will shake, palyer will lose one life.
    ShooterPlane.start_effect(effects.fire)
    scene.camera_shake()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap2)

#Creating the overlap event, missile and the bogey1.
def on_overlap3(missile, bogey):
    #On overlap, the bogey will destroy, player scores one point.
    bogey.destroy()
    bogey.start_effect(effects.fire)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_overlap3)

#Creating the overlap event, missile and the bogey2.
def on_overlap4(missile, bogey):
    #On overlap, the bogey2 will destroy, player scores 2 point.
    bogey.destroy()
    bogey.start_effect(effects.fire)
    info.change_score_by(2)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_overlap4)