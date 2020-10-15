## refactor: new abstractions

- a TRACK uses a DECK
- a TRACK is divided into SECTIONS
- each SECTION has EFFECTS
- each SECTION has a BG
- each SECTION has OPTIONS such as:
  - resync: sync to the beat when this section starts
  - knobs: 
    - dashboardKnobPre1 (default)
    - dashboardKnobBG1
    - dashboardKnobPost1
  - pulse: what to do on pulses/hits
- EFFECTS are named in a data file; 
  - use enums?
  - names should match column names
  - effects layers in Resolume should be persistent across decks


## DATA SOURCES

UDP (from svdx, or from console)
- `udp_recent_values` stores most recent values sent
- ONLY udp calls update `udp_recent_values`! (control flow)
- `udp_callbacks` (filename: `udp_callbacks.py`) handles changes to these values

TRACK INFO
- table `track_info` stores track names from svdx; use it to look up module names and deck #s

PROTOTYPE CONTROLS V2
- handle button presses and knob turns
- show SECTIONS dropdown
- show (and/or allow clicks for) BG and EFFECTS sets

UDP => RESOLUME_CONTROLLER
- track changes
- section changes
- pulses

## REQUIRED SOFTWARE
- AutoHotKey - not really necessary if you chose to compile it as .exe on host machine
- AHK script needs to be added to Windows Start scripts as appropriate
- OBS latest with obs-ndi plugin
- Resolume 7.1.0
  - To use new files:
    - Copy this Resolume\ folder into [destination]\Documents\Resolume Arena
    - Copy video clips etc. to SSD
  - To collect files:
    - Extra Effects dlls: need to check Video Preferences for locations: 
      - e:\shaders\plugins
      - e:\git\resolume-ffgl\binaries\x64
    - Collect media using Media Manager
    - Advanced mapping
      - Documents\Resolume Arena\Presets\Advanced Output
- USC: zip up on host, unzip on target, check AHK destinations

## UPDATING FILES
- Resolume
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
