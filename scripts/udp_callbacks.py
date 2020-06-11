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
import resolume_commands

def update_title(title):
    # check the 1st column for the offical track name, then
    # grab the track_id, i.e. row index
    print("update title called", title)
    row = op('track_info')[title, 'track_id']
    print("trackid:", op('track_info')[title, 'track_id'])
    print("mod name:", op('track_info')[title, 'module_name'])
    if row is None:
      print("ERR: track name not found in track_info table.", title)
      return
    # row = row + 1
    print("using row:", row)
    # value is our song title. look it up in the table.
    op('udp_recent_values')['track_id', 1] = row
    op('udp_recent_values')['module_name', 1] = op(
        'track_info')[row, 'module_name']
    op('udp_recent_values')['deck', 1] = op('track_info')[row, 'deck']
    op('udp_recent_values')['section', 1] = 0
    return

def update_section(value):
    op('udp_recent_values')['section', 1] = value

def onReceive(dat, rowIndex, message, bytes, peer):
  vals = message.split('|')
  action = vals[0]
  value = vals[1]

  if vals[0][:3] == 'bpm':
    op('udp_recent_values')[action, 1] = value
    # print('updating bpm')
    # TODO convert from range 20-500 to 0-1
    tempo = float(vals[1])
    to_send = (tempo - 20) / 480
    resolume_commands.update_tempo(to_send)
    resolume_commands.resync()

  # got a 'hit'/pulse message. used as the secret bass line
  if action == 'h':
    field = 'hit'
    op('udp_recent_values')[field, 1] = int(value)

  # section gets updated. increment section
  if action == 's':
    update_section(int(value))

  if action == 'title':
    print("yep got title", value)
    update_title(value)
    update_section(0)

  return
