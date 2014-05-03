#!/usr/bin/bash

xsetroot -cursor_name arrow &&
xbindkeys &&
font-fix &&
feh --bg-fill good-dsk/train.png &&

monsterwm | monst-parse | bar -wrk1 " term " -wrk2 " web " -wrk3 " text " -wrk4 " other " -emptybg "#101019" -wrkfg "#101019" -wrkbg "#33333b" -infobg "#33333b" -fontcol "#666666"
