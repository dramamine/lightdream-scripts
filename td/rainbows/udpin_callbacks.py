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

def onRowChange(dat, rows):
  for target in rows:
    fingerId = dat[target, 0]
    spotlight = op("spotlight" + str(target))
    if not fingerId:
      spotlight.par.centerx = -1
      spotlight.par.centery = -1
    else:
      spotlight.par.centerx = float(dat[target, 1]) - 0.5
      spotlight.par.centery = float(dat[target, 2]) - 0.5

  return

def onSizeChange(dat):
  onRowChange(dat, range(0, dat.numRows))
  return
