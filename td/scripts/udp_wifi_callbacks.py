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

def onReceive(dat, rowIndex, message, bytes, peer):
  vals = message.split('|')
  action = vals[0]
  value = int(vals[1])

  print(action, value)

  rlayer = 10
  rclip = 1
  # got a 'hit'/pulse message. used as the secret bass line
  if action == 'rc':
    resolume_commands.send(
      "/composition/layers/{}/clips/{}/video/opacity".format(rlayer, rclip), float(value)
    )

  # section gets updated. increment section
  if action == 'rb':
    angle = (1.25 - float(value / 127)) % 1
    resolume_commands.send(
      "/composition/layers/{}/clips/{}/video/effects/radialmask/effect/angle".format(rlayer, rclip), angle
    )
  if action == 'ra':
    rnge = float(value / 127)
    resolume_commands.send(
      "/composition/layers/{}/clips/{}/video/effects/radialmask/effect/range".format(rlayer, rclip), rnge
    )

  return
