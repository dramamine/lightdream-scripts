# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
#
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.
import sld_resolume_commands as resolume_commands


def onValueChange(par, prev):
	print("value change:", par.eval(), par, prev)
	# use par.eval() to get current value
	# print("value change:", par.eval())
	if par.eval() == False:
		return
	# resolume_commands.heartbeat()
	# resolume_commands.first_layer_only_instant_fadeout_others()
	# resolume_commands.add_mask()

	return

# Called at end of frame with complete list of individual parameter changes.
# The changes are a list of named tuples, where each tuple is (Par, previous value)


def onValuesChanged(changes):
	for c in changes:
		# use par.eval() to get current value
		par = c.par
		prev = c.prev
		print("onValuesChanged called.", par, prev)
	return


def onPulse(par):
	print("onPulse called.")
	return


def onExpressionChange(par, val, prev):
	return


def onExportChange(par, val, prev):
	return


def onEnableChange(par, val, prev):
	return


def onModeChange(par, val, prev):
	return
