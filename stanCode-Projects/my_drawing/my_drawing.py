"""
File: my_drawing
Name: 謝濡駿
----------------------
TODO: I use the same wallpaper of my phone to make the identical image of my phone's locked screen. Also, I hided some
eastern eggs about StanCode and SC101!
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GRoundRect
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage


def main():
    """
    TODO: I use the same wallpaper of my phone to make the identical image of my phone's locked screen. Also, I hided some
eastern eggs about StanCode and SC101!
    """
    window = GWindow(width=800, height=1000, title='123')
    a1 = GRoundRect(510, 850, x=None, y=None, corner=256)  # background image
    a1.filled = True
    a1.fill_color = 'BLACK'
    window.add(a1, 150, 20)
    wallpaper = GImage('J.Cole.png')  # my phone's wallpaper
    window.add(wallpaper, 150, 210)
    # seal = GImage('SC101.png')
    # window.add(seal, 150, 215)
    a2 = GRoundRect(250, 30, corner=256)  # iphone's bangs
    a2.filled = True
    a2.fill_color = 'black'
    a2.color = 'darkgrey'
    window.add(a2, 280, 20)
    a3 = GRoundRect(50, 5, corner=256)  # phone speaker
    window.add(a3, 375, 25)
    a3.filled = True
    a3.fill_color = 'BLACK'
    a3.color = 'darkgrey'
    camera = GOval(7, 7)  # front camera
    camera.filled = True
    camera.fill_color = 'BLACK'
    camera.color = 'darkgrey'
    window.add(camera, 435, 25)
    s1 = GRoundRect(5, 7, corner=1000)   # service signal intensity
    s2 = GRoundRect(5, 9, corner=1000)
    s3 = GRoundRect(5, 11, corner=1000)
    s4 = GRoundRect(5, 13, corner=1000)
    s1.filled = True
    s1.fill_color = 'WHITE'
    s2.filled = True
    s2.fill_color = 'WHITE'
    s3.filled = True
    s3.fill_color = 'WHITE'
    s4.filled = True
    s4.fill_color = 'GREY'
    window.add(s1, 542, 43)
    window.add(s2, 548, 41)
    window.add(s3, 554, 39)
    window.add(s4, 560, 37)

    s5 = GLabel('4G')  # cellular data
    s5.font = '-15'
    s5.color = 'WHITE'
    window.add(s5, 575, 52)

    battery = GRoundRect(20, 10)  # battery capacity
    battery.color = 'GREY'
    battery.filled = True
    battery.fill_color = 'WHITE'
    window.add(battery, 605, 37)
    b_head = GRoundRect(2, 4)
    b_head.color = 'GREY'
    b_head.filled = True
    b_head.fill_color = 'GREY'
    window.add(b_head, 625, 40)

    label = GLabel('StanCode')
    label.font = '-20'
    label.color = 'WHITE'
    window.add(label, 170, 52)

    locker_head_outside = GOval(22, 30)  # locker on the screen
    locker_head_outside.color = 'WHITE'
    locker_head_outside.filled = True
    locker_head_outside.fill_color = 'WHITE'
    window.add(locker_head_outside, 394, 85)
    locker_head_inside = GOval(18, 28)
    locker_head_inside.color = 'WHITE'
    locker_head_inside.filled = True
    locker_head_inside.fill_color = 'BLACK'
    window.add(locker_head_inside, 396, 86)
    locker = GRoundRect(26, 23)
    locker.color = 'WHITE'
    locker.filled = True
    locker.fill_color = 'WHITE'
    window.add(locker, 392, 100)

    clock = GLabel('10:00')  # digital clock, with the time for class on it
    clock.font = '-68'
    clock.color = 'WHITE'
    window.add(clock, 320, 200)

    date = GLabel('Tuesday, September 8')  # date for the class
    date.font = '-18'
    date.color = 'WHITE'
    window.add(date, 315, 212)

    flash_light_bg = GOval(60, 60)    # one of two shortcut icons, flashlight
    flash_light_bg.color = 'darkgray'
    flash_light_bg.filled = True
    flash_light_bg.fill_color = 'darkgray'
    window.add(flash_light_bg, 210, 750)

    f1 = GOval(13, 17)
    f1.color = 'darkgray'
    f1.filled = True
    f1.fill_color = 'WHITE'
    window.add(f1, 233, 760)

    f2 = GRect(13, 7)
    f2.color = 'darkgray'
    f2.filled = True
    f2.fill_color = 'darkgray'
    window.add(f2, 233, 760)

    f3 = GRoundRect(11, 2)
    f3.color = 'WHITE'
    f3.filled = True
    f3.fill_color = 'WHITE'
    window.add(f3, 234, 764)

    f4 = GRoundRect(5, 23)
    f4.color = 'WHITE'
    f4.filled = True
    f4.fill_color = 'WHITE'
    window.add(f4, 237, 769)

    f5 = GRoundRect(2, 5)
    f5.color = 'BLACK'
    f5.filled = True
    f5.fill_color = 'BLACK'
    window.add(f5, 239, 778)

    f6 = GOval(2, 1)
    f6.color = 'white'
    f6.filled = True
    f6.fill_color = 'white'
    window.add(f6, 239, 781)

    camera_icon_bg = GOval(60, 60)   # one of the shortcut icons, camera
    camera_icon_bg.color = 'darkgray'
    camera_icon_bg.filled = True
    camera_icon_bg.fill_color = 'darkgray'
    window.add(camera_icon_bg, 530, 750)

    c1 = GRoundRect(25, 15)
    c1.color = 'white'
    c1.filled = True
    c1.fill_color = 'white'
    window.add(c1, 547, 771)

    c2 = GRoundRect(9, 4)
    c2.color = 'white'
    c2.filled = True
    c2.fill_color = 'white'
    window.add(c2, 556, 768)

    c3 = GRoundRect(2, 1)
    c3.color = 'white'
    c3.filled = True
    c3.fill_color = 'white'
    window.add(c3, 549, 768)

    lens = GOval(13, 13)
    lens.color = 'black'
    lens.filled = True
    lens.fill_color = 'black'
    window.add(lens, 554, 772)

    lens2 = GOval(11, 11)
    lens2.color = 'white'
    lens2.filled = True
    lens2.fill_color = 'white'
    window.add(lens2, 555, 773)

    c4 = GOval(1, 1)
    c4.color = 'black'
    c4.filled = True
    c4.fill_color = 'black'
    window.add(c4, 567, 772)

    swipe_bar = GRoundRect(250, 5)   # swipe bar
    swipe_bar.color = 'ivory'
    swipe_bar.filled = True
    swipe_bar.fill_color = 'ivory'
    window.add(swipe_bar, 280, 850)

    swipe_label = GLabel('sign up for sc101!')
    swipe_label.font = '-18'
    swipe_label.color = 'ivory'
    window.add(swipe_label, 323, 848)


if __name__ == '__main__':
    main()
