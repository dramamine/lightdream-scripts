# DEPRECATED
#
import resolume_commands

def onReceive(dat, rowIndex, message, bytes, peer):
  vals = message.split('|')
  action = vals[0]
  value = int(vals[1])

  # print(action, value)

  # got a 'hit'/pulse message. used as the secret bass line
  if action == 'rc':
    rlayer = 10
    rclip = 1
    resolume_commands.send(
      "/composition/layers/{}/clips/{}/video/opacity".format(rlayer, rclip), float(value)
    )

  return
