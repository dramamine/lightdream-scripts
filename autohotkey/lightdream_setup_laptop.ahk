; load resolume, turn on Advanced Output
#7::
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
Sleep 8000
WinActivate, Resolume Arena
WinWaitActive, Resolume Arena
Send, +^a
Sleep 1000
WinMinimize, Advanced Output
Return

; load touchdesigner
; @TODO: TD standalone EXE? this should show the "physical" controls and
; generally be nicer
#8::
Run %A_ProgramFiles%\Derivative\TouchDesigner\bin\TouchDesigner099.exe "C:\git\lightdream-scripts\td\LightdreamOSC.toe"
WinWait TouchDesigner, , 120
if ErrorLevel
{
    MsgBox, Timed out waiting for TouchDesigner to open.
    return
}
WinMinimize TouchDesigner
Return

; load USC
#9::
Run C:\git\lightdream-scripts\usc\bin\usc-game.exe
WinWait USC-Game, , 60
if ErrorLevel
{
    MsgBox, Timed out waiting for USC to open.
    return
}
WinActivate, USC-Game
WinWaitActive, USC-Game
Send, 1
Return

; load OBS
#0::
; Run %A_ProgramFiles%\obs-studio\bin\64bit\obs64.exe %A_ProgramFiles%\obs-studio\bin\64bit
obs_window_name := "OBS 25"
Run C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio\OBS Studio (64bit).lnk
WinWait %obs_window_name%, , 120
if ErrorLevel
{
    MsgBox, Timed out waiting for OBS to open.
    return
}
Sleep 2000
WinActivate, %obs_window_name%
WinWaitActive, %obs_window_name%
WinGetPos, X, Y, Width, Height, %obs_window_name%
; MouseMove, X+Width/2, Y+Height/2
MouseClick, Right, Width/2, Height/2
Send {Down}{Down}{Down}{Down}{Right}{Down}
Sleep 1000
Send {Enter}
Sleep 1000
WinMinimize %obs_window_name%
Return
