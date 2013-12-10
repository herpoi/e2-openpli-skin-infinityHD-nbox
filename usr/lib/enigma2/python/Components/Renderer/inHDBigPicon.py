##
## Picon renderer by Gruffy .. some speedups by Ghost
## XPicon mod by iMaxxx
## XPicon mod by Misenko
## inHDBigPicon mod by herpoi
##
from Renderer import Renderer
from enigma import ePixmap
from enigma import iServiceInformation, iPlayableService, iPlayableServicePtr
from Tools.Directories import fileExists, SCOPE_SKIN_IMAGE, SCOPE_CURRENT_SKIN, resolveFilename
from Components.config import config

class inHDBigPicon(Renderer):
	searchPaths = ('/media/hdd/BigPicon/%s/','/usr/share/enigma2/BigPicon/%s/','/media/usb/BigPicon/%s/','/media/hdd/XPicons/%s/','/media/img/XPicons/%s/','/media/usb/XPicons/%s/','/usr/share/enigma2/XPicons/%s/','/usr/share/enigma2/%s/', '/media/usb/%s/')

	def __init__(self):
		Renderer.__init__(self)
		self.path = "picon"
		self.nameCache = { }
		self.pngname = ""

	def applySkin(self, desktop, parent):
		attribs = [ ]
		for (attrib, value) in self.skinAttributes:
			if attrib == "path":
				self.path = value
			else:
				attribs.append((attrib,value))
		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, parent)

	GUI_WIDGET = ePixmap

	def changed(self, what):
		if self.instance:
			pngname = ""
			if what[0] != self.CHANGED_CLEAR:
				
				sname = self.source.text
				pos = sname.rfind(':')
				if pos != -1:
					sname = sname[:pos].rstrip(':').replace(':','_')
				pngname = self.nameCache.get(sname, "")
				if pngname == "":
					pngname = self.findPicon(sname)
					if pngname != "":
						self.nameCache[sname] = pngname
			if pngname == "": # no picon for service found
				pngname = self.nameCache.get("default", "")
				if pngname == "": # no default yet in cache..
					pngname = self.findPicon("bigpicon_default")
					if pngname == "":
						tmp = resolveFilename(SCOPE_CURRENT_SKIN, "bigpicon_default.png")
						if fileExists(tmp):
							pngname = tmp
						else:
							pngname = resolveFilename(SCOPE_SKIN_IMAGE, "skin_default/picon_default.png")
					self.nameCache["default"] = pngname
			if self.pngname != pngname:
				if pngname:
					self.instance.setScale(1)
					self.instance.setPixmapFromFile(pngname)
					self.instance.show()
				else:
					self.instance.hide()
				self.pngname = pngname
				
	def findPicon(self, serviceName):
		for path in self.searchPaths:
			pngname = (path % self.path) + serviceName + ".png"
			if fileExists(pngname):
				return pngname
		return ""

