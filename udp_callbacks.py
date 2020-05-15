# me - this DAT
#
# dat - the DAT that received the data
# rowIndex - is the row number the data was placed into
# message - an ascii representation of the data
#           Unprintable characters and unicode characters will
#           not be preserved. Use the 'bytes' parameter to get
#           the raw bytes that were sent.
# bytes - a byte array of the data received
# peer - a Peer object describing the originating message
#   peer.close()    #close the connection
#   peer.owner  #the operator to whom the peer belongs
#   peer.address    #network address associated with the peer
#   peer.port       #network port associated with the peer
#
from utils import send
# import time

quickpressMap = [1, 3, 4, 6, 2, 4]

def quickUnpress(field):
  op('udp_recent_values')[field, 1] = 0

def worker(event):
  while not event.isSet():
    print("waitin...")
    event.wait(1)
    print("done waitin")
    event.set()


def onReceive(dat, rowIndex, message, bytes, peer):
  vals = message.split('|')
  action = vals[0]
  value = vals[1]

  if vals[0][:4] == 'butt' or vals[0][:4] == 'knob' or vals[0][:3] == 'bpm':
    op('udp_recent_values')[vals[0], 1] = vals[1]

  if vals[0][:3] == 'bpm':
    # print('updating bpm')
    # TODO convert from range 20-500 to 0-1
    tempo = float(vals[1])
    to_send = (tempo - 20) / 480
    send('/composition/tempocontroller/tempo', to_send)
    send('/composition/tempocontroller/resync', 1)
    send('/composition/tempocontroller/resync', 0)
  if action == 'quickpress':
    ourbutton = quickpressMap[int(value)]
    field = 'timer' + str(ourbutton)

    # WORKS!!!
    op(field).par.start.pulse()
  if action == 'zoom':
    field = 'zoom' + value
    op('udp_recent_values')[field, 1] = vals[2]

  # got a 'hit' message. used as the secret bass line
  if action == 'h':
    field = 'hit'
    op('udp_recent_values')[field, 1] = int(vals[1])
    op('pulse').par.Value0 = int(vals([1]))

  # scene gets updated. increment scene
  if action == 's':
    # print("updating scene")
    field = 'scene'
    new_value = int(vals[1])
    op('udp_recent_values')[field, 1] = new_value

    op('effects_select').par.Value0 = new_value
    # @TODO might remove BG stuff
    # op('bg_select').par.Value0 = new_value

  return
