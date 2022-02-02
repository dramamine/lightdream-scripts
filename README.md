
## REQUIRED SOFTWARE
- AutoHotKey - not really necessary if you chose to compile it as .exe on host machine
  + Win+7 through Win+9 opens all the softwares individually
- AHK script needs to be added to Windows Start scripts as appropriate
- Resolume 7.3.3

- USC: zip up on host, unzip on target, check AHK destinations
  - should be in git\lightdream-scripts\usc
  - https://github.com/dramamine/unnamed-sdvx-clone/tree/lightdream-0.4


## TOUCHSCREEN
- in Control Panel, go to Tablet PC Settings to configure display options
- in Control Panel, Pen and Tablet settings also look helpful
- Update Main.cfg fullscreen settings ex.
```
ScreenWidth = 1920
ScreenHeight = 1080
Fullscreen = True
FullscreenMonitorIndex = 1
ShowFPS = False
```

## UPDATING FILES
### 1. COLLECTION
a. Resolume
  - To collect files: (load up lightdream-scripts/resolume subfolders and git commit them)
    - Extra Effects dlls: need to check Video Preferences for locations: 
      - e:\shaders\plugins
      - e:\git\resolume-ffgl\binaries\x64
    - Advanced mapping
      - Documents\Resolume Arena\Presets\Advanced Output
    - Collect media using Media Manager

  - LD Testing to LD Final: remove unused decks, columns, rows
  - LD Final: Media Manager => Collect Media.. to H:\lightdream-vxx (external hdd named ROTTEN)
b. USC
  - Add git\usc4\bin files to an archive and move to lightdream-scripts\usc
c. lightdream-scripts folder
  - copy and move to external drive


### 2. PROPAGATION
- Resolume
  * Copy this Resolume\ folder into [destination]\Documents\Resolume Arena
  * Move collected video clips etc. to folder on SSD ex. C:\lightdream-vxx
  * In Resolume, Relocate Files
  * Open new file in Resolume (so that it's the last loaded)
  * Confirm the Advanced Output looks good
  * Confirm audio input is "IN 1-2 (BEHRINGER...)"
  * Confirm Layer 3 - TDSyphonSpoutOut is active on start
  * Confirm Layer 5 - Kaleidoscope is active on start
    - if not, edit layer - play first clip on load
    - and set clip to Persistent
- TouchDesigner
  * Confirm the udp packet IPs and the Resolume OSC ip & port
- USC
  * Unpack archive
  * Remove any songs inappropriate for the venue
  * Confirm config settings: should be fullscreen 1920x1080 on second monitor

Double-check:
- Autohotkey script runs on startup for the domegod user because there's a shortcut to the script here:
  C:\Users\domegod\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
- Touchscreen behavior should be correct
- Audio Device (speaker icon in taskbar) is OUT 1-2 (BEHRINGER UMC...)
- Bios (F2 at startup) -> Power Management -> AC Behavior -> Wake on AC (should be on)
- Control Panel/Hardware and Sound -> Tablet PC Settings -> Other -> Pen & Touch
  * Disable all touch actions and visual feedback


## DEBUGGING / WHAT COULD GO WRONG?




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
