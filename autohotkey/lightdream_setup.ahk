; open all the programs
; GoSub #7
; GoSub #8
; GoSub #9

; load touchdesigner
#7::
Run G:\TouchDesigner\bin\TouchDesigner.exe "E:\git\lightdream-scripts\td\LightdreamTouchscreen.toe"
SetTitleMatchMode 2
WinWait LightdreamTouchscreen, , 120
if ErrorLevel
{
    MsgBox, Timed out waiting for TouchDesigner to open.
    return
}
WinActivate, LightdreamTouchscreen
WinWaitActive, LightdreamTouchscreen
; Sleep 1000
; Send, {F1}
Return

; load resolume, turn on Advanced Output
#8::
Run, %A_ProgramFiles%\Resolume Arena 6\Arena.exe
WinWait Resolume Arena, , 120
if ErrorLevel
{
    MsgBox, Timed out waiting for Resolume to open.
    return
}

WinWait Resolume Arena - L, , 120
if ErrorLevel
{
    MsgBox, Timed out waiting for Resolume with our comp loaded.
    return
}
Sleep 2500
WinActivate, Resolume Arena
WinWaitActive, Resolume Arena
; Send, +^a
; Sleep 2500
; WinMinimize, Advanced Output
Return

; load USC
#9::
Run E:\git\usc4\bin\usc-game.exe -notitle
WinWait USC-Game, , 60
if ErrorLevel
{
    MsgBox, Timed out waiting for USC to open.
    return
}
WinActivate, USC-Game
WinWaitActive, USC-Game
Return
