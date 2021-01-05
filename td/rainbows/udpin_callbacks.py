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

def flipAt(y,z,flip):
  network_target = "quadrant" + str(y+1) + "/add" + str(z+1)
  op(network_target).bypass = not flip
  return

def toggleAll(flip):
  for y in range(0, 5):
    for z in range(0, 9):
      flipAt(y, z, flip)
  return

def onReceive(dat, rowIndex, message, bytes, peer):
  print(message)
  x = message.split(',')
  target = int(x[0])
  flip = bool(int(x[1]))
  if target == 99:
    toggleAll(flip)
    return

  y = math.floor(target/9)
  z = target % 9
  flipAt(y, z, flip)
  
  return
