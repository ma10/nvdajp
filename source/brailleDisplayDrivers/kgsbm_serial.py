# coding: UTF-8
#brailleDisplayDrivers/kgsbm_serial.py
#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2015 Takuya Nishimoto

from logHandler import log
import inputCore
from kgs import BrailleDisplayDriver, InputGesture

kgsBmSerialGestureMapData = {
	"globalCommands.GlobalCommands": {
		"showGui": ("br(kgsbm_serial):ins",),
		"kb:escape": ("br(kgsbm_serial):esc",),
		"kb:windows": ("br(kgsbm_serial):read",),
		"kb:shift": ("br(kgsbm_serial):select",),
		"kb:control": ("br(kgsbm_serial):ctrl",),
		"kb:alt": ("br(kgsbm_serial):alt",),
		"kb:alt+tab": ("br(kgsbm_serial):alt+inf",),
		"kb:enter": ("br(kgsbm_serial):enter","br(kgsbm_serial):ok","br(kgsbm_serial):set",),
		"kb:space": ("br(kgsbm_serial):space",),
		"kb:delete": ("br(kgsbm_serial):del",),
		"kb:backspace": ("br(kgsbm_serial):bs",),
		"kb:tab": ("br(kgsbm_serial):inf",),
		"kb:shift+tab": ("br(kgsbm_serial):select+inf",),
		"kb:upArrow": ("br(kgsbm_serial):upArrow",),
		"kb:downArrow": ("br(kgsbm_serial):downArrow",),
		"kb:leftArrow": ("br(kgsbm_serial):leftArrow",),
		"kb:rightArrow": ("br(kgsbm_serial):rightArrow",),
		"kb:shift+upArrow": ("br(kgsbm_serial):select+upArrow",),
		"kb:shift+downArrow": ("br(kgsbm_serial):select+downArrow",),
		"kb:shift+leftArrow": ("br(kgsbm_serial):select+leftArrow",),
		"kb:shift+rightArrow": ("br(kgsbm_serial):select+rightArrow",),
		"review_previousLine": ("br(kgsbm_serial):bw",),
		"review_nextLine": ("br(kgsbm_serial):fw",),
		"review_previousWord": ("br(kgsbm_serial):ls",),
		"review_nextWord": ("br(kgsbm_serial):rs",),
		"braille_routeTo": ("br(kgsbm_serial):route",),
		"braille_scrollBack": ("br(kgsbm_serial):func1","br(kgsbm_serial):func3+leftArrow",),
		"braille_scrollForward": ("br(kgsbm_serial):func4","br(kgsbm_serial):func3+rightArrow",),
		"braille_previousLine": ("br(kgsbm_serial):func3+upArrow",),
		"braille_nextLine": ("br(kgsbm_serial):func3+downArrow",),
		"kb:a": ("br(kgsbm_serial):dot1",),
		"kb:b": ("br(kgsbm_serial):dot1+dot2",),
		"kb:c": ("br(kgsbm_serial):dot1+dot4",),
		"kb:d": ("br(kgsbm_serial):dot1+dot4+dot5",),
		"kb:e": ("br(kgsbm_serial):dot1+dot5",),
		"kb:f": ("br(kgsbm_serial):dot1+dot2+dot4",),
		"kb:g": ("br(kgsbm_serial):dot1+dot2+dot4+dot5",),
		"kb:h": ("br(kgsbm_serial):dot1+dot2+dot5",),
		"kb:i": ("br(kgsbm_serial):dot2+dot4",),
		"kb:j": ("br(kgsbm_serial):dot2+dot4+dot5",),
		"kb:k": ("br(kgsbm_serial):dot1+dot3",),
		"kb:l": ("br(kgsbm_serial):dot1+dot2+dot3",),
		"kb:m": ("br(kgsbm_serial):dot1+dot3+dot4",),
		"kb:n": ("br(kgsbm_serial):dot1+dot3+dot4+dot5",),
		"kb:o": ("br(kgsbm_serial):dot1+dot3+dot5",),
		"kb:p": ("br(kgsbm_serial):dot1+dot2+dot3+dot4",),
		"kb:q": ("br(kgsbm_serial):dot1+dot2+dot3+dot4+dot5",),
		"kb:r": ("br(kgsbm_serial):dot1+dot2+dot3+dot5",),
		"kb:s": ("br(kgsbm_serial):dot2+dot3+dot4",),
		"kb:t": ("br(kgsbm_serial):dot2+dot3+dot4+dot5",),
		"kb:u": ("br(kgsbm_serial):dot1+dot3+dot6",),
		"kb:v": ("br(kgsbm_serial):dot1+dot2+dot3+dot6",),
		"kb:w": ("br(kgsbm_serial):dot2+dot4+dot5+dot6",),
		"kb:x": ("br(kgsbm_serial):dot1+dot3+dot4+dot6",),
		"kb:y": ("br(kgsbm_serial):dot1+dot3+dot4+dot5+dot6",),
		"kb:z": ("br(kgsbm_serial):dot1+dot3+dot5+dot6",),
		"kb:control+a": ("br(kgsbm_serial):ctrl+dot1",),
		"kb:control+b": ("br(kgsbm_serial):ctrl+dot1+dot2",),
		"kb:control+c": ("br(kgsbm_serial):ctrl+dot1+dot4",),
		"kb:control+d": ("br(kgsbm_serial):ctrl+dot1+dot4+dot5",),
		"kb:control+e": ("br(kgsbm_serial):ctrl+dot1+dot5",),
		"kb:control+f": ("br(kgsbm_serial):ctrl+dot1+dot2+dot4",),
		"kb:control+g": ("br(kgsbm_serial):ctrl+dot1+dot2+dot4+dot5",),
		"kb:control+h": ("br(kgsbm_serial):ctrl+dot1+dot2+dot5",),
		"kb:control+i": ("br(kgsbm_serial):ctrl+dot2+dot4",),
		"kb:control+j": ("br(kgsbm_serial):ctrl+dot2+dot4+dot5",),
		"kb:control+k": ("br(kgsbm_serial):ctrl+dot1+dot3",),
		"kb:control+l": ("br(kgsbm_serial):ctrl+dot1+dot2+dot3",),
		"kb:control+m": ("br(kgsbm_serial):ctrl+dot1+dot3+dot4",),
		"kb:control+n": ("br(kgsbm_serial):ctrl+dot1+dot3+dot4+dot5",),
		"kb:control+o": ("br(kgsbm_serial):ctrl+dot1+dot3+dot5",),
		"kb:control+p": ("br(kgsbm_serial):ctrl+dot1+dot2+dot3+dot4",),
		"kb:control+q": ("br(kgsbm_serial):ctrl+dot1+dot2+dot3+dot4+dot5",),
		"kb:control+r": ("br(kgsbm_serial):ctrl+dot1+dot2+dot3+dot5",),
		"kb:control+s": ("br(kgsbm_serial):ctrl+dot2+dot3+dot4",),
		"kb:control+t": ("br(kgsbm_serial):ctrl+dot2+dot3+dot4+dot5",),
		"kb:control+u": ("br(kgsbm_serial):ctrl+dot1+dot3+dot6",),
		"kb:control+v": ("br(kgsbm_serial):ctrl+dot1+dot2+dot3+dot6",),
		"kb:control+w": ("br(kgsbm_serial):ctrl+dot2+dot4+dot5+dot6",),
		"kb:control+x": ("br(kgsbm_serial):ctrl+dot1+dot3+dot4+dot6",),
		"kb:control+y": ("br(kgsbm_serial):ctrl+dot1+dot3+dot4+dot5+dot6",),
		"kb:control+z": ("br(kgsbm_serial):ctrl+dot1+dot3+dot5+dot6",),
		"kb:alt+a": ("br(kgsbm_serial):alt+dot1",),
		"kb:alt+b": ("br(kgsbm_serial):alt+dot1+dot2",),
		"kb:alt+c": ("br(kgsbm_serial):alt+dot1+dot4",),
		"kb:alt+d": ("br(kgsbm_serial):alt+dot1+dot4+dot5",),
		"kb:alt+e": ("br(kgsbm_serial):alt+dot1+dot5",),
		"kb:alt+f": ("br(kgsbm_serial):alt+dot1+dot2+dot4",),
		"kb:alt+g": ("br(kgsbm_serial):alt+dot1+dot2+dot4+dot5",),
		"kb:alt+h": ("br(kgsbm_serial):alt+dot1+dot2+dot5",),
		"kb:alt+i": ("br(kgsbm_serial):alt+dot2+dot4",),
		"kb:alt+j": ("br(kgsbm_serial):alt+dot2+dot4+dot5",),
		"kb:alt+k": ("br(kgsbm_serial):alt+dot1+dot3",),
		"kb:alt+l": ("br(kgsbm_serial):alt+dot1+dot2+dot3",),
		"kb:alt+m": ("br(kgsbm_serial):alt+dot1+dot3+dot4",),
		"kb:alt+n": ("br(kgsbm_serial):alt+dot1+dot3+dot4+dot5",),
		"kb:alt+o": ("br(kgsbm_serial):alt+dot1+dot3+dot5",),
		"kb:alt+p": ("br(kgsbm_serial):alt+dot1+dot2+dot3+dot4",),
		"kb:alt+q": ("br(kgsbm_serial):alt+dot1+dot2+dot3+dot4+dot5",),
		"kb:alt+r": ("br(kgsbm_serial):alt+dot1+dot2+dot3+dot5",),
		"kb:alt+s": ("br(kgsbm_serial):alt+dot2+dot3+dot4",),
		"kb:alt+t": ("br(kgsbm_serial):alt+dot2+dot3+dot4+dot5",),
		"kb:alt+u": ("br(kgsbm_serial):alt+dot1+dot3+dot6",),
		"kb:alt+v": ("br(kgsbm_serial):alt+dot1+dot2+dot3+dot6",),
		"kb:alt+w": ("br(kgsbm_serial):alt+dot2+dot4+dot5+dot6",),
		"kb:alt+x": ("br(kgsbm_serial):alt+dot1+dot3+dot4+dot6",),
		"kb:alt+y": ("br(kgsbm_serial):alt+dot1+dot3+dot4+dot5+dot6",),
		"kb:alt+z": ("br(kgsbm_serial):alt+dot1+dot3+dot5+dot6",),
		"kb:.": ("br(kgsbm_serial):dot2+dot5+dot6",),
		"kb::": ("br(kgsbm_serial):dot2+dot5",),
		"kb:;": ("br(kgsbm_serial):dot2+dot3",),
		"kb:,": ("br(kgsbm_serial):dot2",),
		"kb:-": ("br(kgsbm_serial):dot3+dot6",),
		"kb:?": ("br(kgsbm_serial):dot2+dot3+dot6",),
		"kb:!": ("br(kgsbm_serial):dot2+dot3+dot5",),
		"kb:'": ("br(kgsbm_serial):dot3",),
	}
}

class BrailleDisplayDriver(BrailleDisplayDriver):
	name = "kgsbm_serial"
	description = _(u"KGS BrailleMemo series") + " " + _(u"serial port")
	allowAutomatic = False
	allowSerial = True
	allowUnavailablePorts = False

	def __init__(self, port=None):
		super(BrailleDisplayDriver,self).__init__(port=port)
		self.gestureMap = inputCore.GlobalGestureMap(kgsBmSerialGestureMapData)
