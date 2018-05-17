import ui


	
	
lastTurn = "O"
tiles = ["TL","TM","TR","ML","MM","MR","BL","BM","BR"]
newTiles = ["TL","TM","TR","ML","MM","MR","BL","BM","BR"]


	

def restart(sender):
	'type sender: ui.Button'
	global newTiles
	global lastTurn
	t = ["TL","TM","TR","ML","MM","MR","BL","BM","BR"]
	tiles = t
	newTiles = t
	lastTurn = "O"
	v = sender.superview
	v['label1'].text = "Its X’s Turn"
	for item in t:
		v[item].enabled = True
		v[item + "L"].text = ""
		lastTurn = "O"
def end(send):
	t = ["TL","TM","TR","ML","MM","MR","BL","BM","BR"]
	v = send.superview
	for item in t:
		v[item].enabled = False

def checkWin(t):
	if t[0] == t[4] and t[4] == t[8]:
		return t[0]
	elif t[2] == t[4] and t[4] == t[6]:
		return t[2]
		
	for i in range(0,3):
		if t[i] == t[i+3] and t[i+3] == t[i+6]:
			return t[i]
	for i in range(0,9,3):
		if t[i] == t[i+1] and t[i+1] == t[i+2]:
			return t[i]

	
		 
def win(player, send):
	v = send.superview
	v['label1'].text = player + "'s Wins!"	
	end(send) 


def button_tapped(sender):
	'@type sender: ui.Button'
	global lastTurn

	
	v = sender.superview
	
	
	if lastTurn == "X":
		v['label1'].text = "Its X’s Turn"
	else:
		v['label1'].text = "Its O's Turn'"

	for item in tiles:
		if sender.name == item:
			tiles.remove(sender.name)
					
	if lastTurn == "X":
		v[sender.name + "L"].text = "O"
		v[sender.name].enabled = False
		lastTurn = "O"
		isUse = True
	else:
		v[sender.name + "L"].text = "X"
		v[sender.name].enabled = False
		lastTurn = "X"
		isUse = True

	for num in range(0, len(newTiles)):
		if newTiles[num] == sender.name:
			newTiles[num] = v[sender.name + "L"].text
	if checkWin(newTiles) == "X" or checkWin(newTiles) == "O":
			win(checkWin(newTiles), sender)
	else:
		c = 0
		for item in ["TLL","TML","TRL","MLL","MML","MRL","BLL","BML","BRL"]:
			if len(v[item].text) > 0:
				c += 1 
			if c == 9:
				v['label1'].text = "It's a Tie"
				end(sender)
			
	
	
	
	 
	 
v = ui.load_view('UntitledE')

if ui.get_screen_size()[1] >= 768:
	# iPad
	v.present('sheet')
else:
	# iPhone
	v.present()
	
	
while True:
	#slider_action(v['slider1'])
	#button_action(v['button1'])
	pass
