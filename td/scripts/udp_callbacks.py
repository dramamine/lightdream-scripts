import resolume_commands

# me - this DAT
#
# dat - the DAT that received the data
# rowIndex - is the row number the data was placed into
# message - an ascii representation of the data
#           Unprintable characters and unicode characters will
#           not be preserved. Use the 'bytes' parameter to get
#           the raw bytes that were sent.
#
def onReceive(dat, rowIndex, message, bytes, peer):
  global resolume_commands
  vals = message.split('|')
  action = vals[0]
  value = vals[1]

  if vals[0][:3] == 'bpm':
    op('udp_recent_values')[action, 1] = value
    tempo = max(float(vals[1]), 100)
    # print("using tempo:", tempo)
    # convert from range 20-500 to 0-1
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

  if action == 'f':
    fingerId = vals[2]
    x = vals[3]
    y = vals[4]
    if value == '1':
      op('fifo1').appendRow([fingerId, x, y])
    elif value == '2':
      op('fifo1').replaceRow(str(fingerId), [fingerId, x, y])
    elif value == '0':
      op('fifo1').deleteRow(str(fingerId))


  if action == 'title':
    update_title(value)
    update_section(0)

  if action == 'song_playing':
    update_song_playing(value)

  return

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
    # value is our song title. look it up in the table.
    op('udp_recent_values')['track_id', 1] = row
    op('udp_recent_values')['module_name', 1] = op(
        'track_info')[row, 'module_name']
    op('udp_recent_values')['deck', 1] = op('track_info')[row, 'deck']
    op('udp_recent_values')['section', 1] = 0
    op('fifo1').clear()
    return

def update_section(value):
    op('udp_recent_values')['section', 1] = value

def update_song_playing(value):
    op('udp_recent_values')['song_playing', 1] = value
