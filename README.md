
## REQUIRED SOFTWARE
- AutoHotKey - not really necessary if you chose to compile it as .exe on host machine
  + Win+6 through Win+9 opens all the softwares individually
- AHK script needs to be added to Windows Start scripts as appropriate
- OBS latest with obs-ndi plugin
- Resolume 7.3.3

- USC: zip up on host, unzip on target, check AHK destinations
  - should be in git\lightdream-scripts\usc


## TOUCHSCREEN
- in Control Panel, go to Tablet PC Settings to configure display options
- in Control Panel, Pen and Tablet settings also look helpful
- Update Main.cfg fullscreen settings ex.
```
ScreenWidth = 1280
ScreenHeight = 800
Fullscreen = True
FullscreenMonitorIndex = 1
```

## UPDATING FILES
- lightdream-scripts folder
  - copy and move to C:\git
- Resolume
  - To use new files:
    - Copy this Resolume\ folder into [destination]\Documents\Resolume Arena
    - Collect video clips etc. to SSD
  - To collect files:
    - Extra Effects dlls: need to check Video Preferences for locations: 
      - e:\shaders\plugins
      - e:\git\resolume-ffgl\binaries\x64
    - Collect media using Media Manager
    - Advanced mapping
      - Documents\Resolume Arena\Presets\Advanced Output

  - Move anything you need from LD Testing to LD Final
  - LD Final: Media Manager => Collect Media.. to H:\ld-campsite-v8 (external hdd named ROTTEN)
- TouchDesigner
  - Confirm the udp packet IPs and the Resolume OSC ip & port




## Effects Brainstorming 6/8
What if we shifted to a setup where we had the main (jukebox) controller but spread buttons and knobs to the 5 'brains'? Each brain would have one button and one knob. This would fit with the 5-Fer (Sectional) effects. Knob effects could be the generic-ish effects I've been thinking of; would simplify things because I could come up with generic knob effects and just rotate em.

Knobs to use:
GRID (adds negative space)
FRAGMENT (adds negative space)
ROTATE (spin 2 win)

## SONG BRAINSTORMING 6/30
Foodman
Floating Points need some of these tracks
Max Cooper
Contortionist



## EDITING TRACKS
### The track editor
E:\games\kshootmania\editor.exe

### Shortcuts reminder
Space - start stop
PNA - Pen Note Araser
H - chip notes
O - position
Ctrl+Alt+Click - position when in Note mode

## What means what
Notes:
|1234|
1: audio reactive
3: end of song
4: scene change

### "Finished" files
E:\git\unnamed-sdvx-clone\bin\songs\FANCY\Seethrough

### Music edits
C:\Dropbox\lightdream-shared\music\edits-completed

### Sending test UDP packets with Powershell
```
function Send-UdpDatagram
{
      Param ([string] $EndPoint,
      [int] $Port,
      [string] $Message)

      $IP = [System.Net.Dns]::GetHostAddresses($EndPoint)
      $Address = [System.Net.IPAddress]::Parse($IP)
      $EndPoints = New-Object System.Net.IPEndPoint($Address, $Port)
      $Socket = New-Object System.Net.Sockets.UDPClient
      $EncodedText = [Text.Encoding]::ASCII.GetBytes($Message)
      $SendMessage = $Socket.Send($EncodedText, $EncodedText.Length, $EndPoints)
      $Socket.Close()
}

Send-UdpDatagram -EndPoint "127.0.0.1"-Port 7001 -Message "bpm|100"
```
