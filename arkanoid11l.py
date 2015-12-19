from curses import initscr,curs_set,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP;from random import randrange;initscr();curs_set(0);win = newwin(30,50,0,0);win.keypad(1);win.nodelay(1);win.border('|','|','-','-','+','+','+','+');ball=[10,10];x = 20;dx = dy = 1;score = 0;key = KEY_RIGHT;win.timeout(100);
for n in range(5): win.hline(n+1,randrange(1,24,1),ord('a'),randrange(1,24,1))
while key != 27:
    win.addstr(0,2,' Score: '+str(score)+' '); key = win.getch(); win.hline(28,x,ord(' '),6);x = (x - 1 if x - 1 > 0 else x) if key==KEY_LEFT else (x + 1 if x + 1 < 44 else x) if key==KEY_RIGHT else x;win.hline(28,x,ord('X'),6)
    if (ball[0] < 2 or ball[0] > 47 ): dx=dx*-1
    if (ball[1] < 2 or ball[1] >= 29 ) or chr(win.inch(ball[1]+dy,ball[0]+dx)) in ['X','a']:
        if chr(win.inch(ball[1]+dy,ball[0]+dx))=='a':  win.addch(ball[1]+dy,ball[0]+dx,' ');  score=score+1 
        dy=dy*-1
    ball[0] = ball[0] + dx;ball[1] = ball[1] + dy;win.addch(ball[1]-dy,ball[0]-dx,' ');win.addch(ball[1],ball[0],'0');
    if (ball[1]==29): break;
endwin();print('\n  arkanoid11l.py (by K!),\n  Thanks for playing, your score: '+str(score)+'\n')