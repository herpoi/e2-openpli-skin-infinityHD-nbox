#######################################################################
#
#    MyMetrix 
#    Coded by iMaxxx (c) 2013
#
#######################################################################
#
#  Mod by herpoi 2013 for infinityHD-nbox
#  Support: https://github.com/herpoi/infinityHD-nbox
#
########################################################################
#
#  This plugin is licensed under the Creative Commons 
#  Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
#  or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#  Alternatively, this plugin may be distributed and executed on hardware which
#  is licensed by Dream Multimedia GmbH.
#
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially 
#  distributed other than under the conditions noted above.
#
#######################################################################

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.ChoiceBox import ChoiceBox
from Screens.Console import Console
from Screens.Standby import TryQuitMainloop
from Components.ActionMap import ActionMap
from Components.AVSwitch import AVSwitch
from Components.config import config, configfile, ConfigYesNo, ConfigSubsection, getConfigListEntry, ConfigSelection, ConfigNumber, ConfigText, ConfigInteger, ConfigBoolean, ConfigNothing, ConfigSlider
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.Language import language
from Tools.Directories import fileExists
from skin import parseColor
from os import environ, listdir, remove, rename, system
from Components.Pixmap import Pixmap
import urllib
import gettext
from enigma import ePicLoad
from __init__ import _

config.plugins.inHD  = ConfigSubsection()
config.plugins.inHD.Colors = ConfigSelection(default="classic", choices = [
				("classic", _("Classic")),
				("fresh", _("Fresh"))
				])
config.plugins.inHD.Infobar = ConfigSelection(default="bigpicon-classic", choices = [
				("bigpicon-classic", _("Big Picon Classic")),
				("bigpicon-classic-lite", _("Big Picon Classic Lite")),
				("picon-classic", _("Picon Classic")),
				("bigpicon-updown", _("Big Picon Up Down")),
				("picon-updown", _("Picon Up Down")),
				("nopicon-classic", _("No Picon Classic")),
				("nopicon-bigclock", _("No Picon BigClock")),
				("nopicon-updown", _("No Picon Up Down"))
				])
config.plugins.inHD.SecondInfobar = ConfigSelection(default="moreepg", choices = [
				("classic", _("Classic")),
				("compact", _("Compact")),
				("moreepg", _("More EPG"))
				])
config.plugins.inHD.Side = ConfigSelection(default="right", choices = [
				("right", _("Right")),
				("left", _("Left"))
				])
config.plugins.inHD.Picon = ConfigSelection(default="bigpicon", choices = [
				("bigpicon", _("Big Picon - 220x132")),
				("nopicon", _("No Picon")),
				("picon", _("Classic - 100x60"))
				])				
config.plugins.inHD.ChannelSelectionNumberNext = ConfigSelection(default="2", choices = [
				("0", _("0")),
				("1", _("1")),
				("2", _("2")),
				("3", _("3"))
				])	
config.plugins.inHD.Rows = ConfigSelection(default="rows14", choices = [
				("rows14", _("14")),
				("rows16", _("16")),
				("rows19", _("19"))
				])		
config.plugins.inHD.EpgSelection = ConfigSelection(default="bigpicon-right", choices = [
				("picon-right", _("Picon Right")),
				("bigpicon-right", _("Big Picon Right")),
				("nopicon-right", _("No Picon Right")),
				("picon-left", _("Picon Left")),
				("bigpicon-left", _("Big Picon Left")),
				("nopicon-left", _("No Picon Left")),
				("picon-up", _("Picon Up")),
				("bigpicon-up", _("Big Picon Up")),
				("nopicon-up", _("No Picon Up"))
				])
config.plugins.inHD.Eventview = ConfigSelection(default="nopicon", choices = [
				("picon-classic", _("Picon Classic")),
				("bigpicon", _("Big Picon")),
				("nopicon", _("No Picon"))
				])
config.plugins.inHD.NumberZap = ConfigSelection(default="center", choices = [
				("center", _("Center")),
				("center-picon", _("BigPicon Center")),
				("topleft", _("Top Left")),
				("topleft-picon", _("BigPicon Top Left")),
				("topright", _("Top Right")),
				("topright-picon", _("BigPicon Top Right")),
				("bottomleft", _("Bottom Left")),
				("bottomleft-picon", _("BigPicon Bottom Left")),
				("bottomright", _("Bottom Right")),
				("bottomright-picon", _("BigPicon Bottom Right"))
				])        				
config.plugins.inHD.InfobarFooter = ConfigSelection(default="ctsig", choices = [
				("ctsig", _("CAID/Tuner/Signal")),
				("etsig", _("ECM/Tuner/Signal")),
				("ecminfo", _("ECM Only")),
				("satsig", _("Sat Info/Signal"))
				])		
config.plugins.inHD.SecondInfobarFooter = ConfigSelection(default="satsig", choices = [
				("ctsig", _("CAID/Tuner/Signal")),
				("etsig", _("ECM/Tuner/Signal")),
				("ecminfo", _("ECM Only")),
				("satsig", _("Sat Info/Signal")),
				("ecmsatsig", _("ECM/Sat Info/Signal"))
				])		
config.plugins.inHD.Font = ConfigSelection(default="aller", choices = [
				("ubuntu", _("Ubuntu")),
				("aller", _("Aller")),
				("roboto", _("Roboto")),
				("cool", _("Cool"))
				])
config.plugins.inHD.ChSelDesc = ConfigSelection(default="100", choices = [
				("80", _("80%")),
				("85", _("85%")),
				("90", _("90%")),
				("95", _("95%")),
				("100", _("100%")),
				("105", _("105%")),
				("110", _("110%")),
				("115", _("115%")),
				("120", _("120%"))
				])
config.plugins.inHD.EPGSelDesc = ConfigSelection(default="100", choices = [
				("80", _("80%")),
				("85", _("85%")),
				("90", _("90%")),
				("95", _("95%")),
				("100", _("100%")),
				("105", _("105%")),
				("110", _("110%")),
				("115", _("115%")),
				("120", _("120%"))
				])
config.plugins.inHD.EvDesc = ConfigSelection(default="100", choices = [
				("80", _("80%")),
				("85", _("85%")),
				("90", _("90%")),
				("95", _("95%")),
				("100", _("100%")),
				("105", _("105%")),
				("110", _("110%")),
				("115", _("115%")),
				("120", _("120%"))
				])
config.plugins.inHD.GraphDesc = ConfigSelection(default="100", choices = [
				("80", _("80%")),
				("85", _("85%")),
				("90", _("90%")),
				("95", _("95%")),
				("100", _("100%")),
				("105", _("105%")),
				("110", _("110%")),
				("115", _("115%")),
				("120", _("120%"))
				])
config.plugins.inHD.SIDesc = ConfigSelection(default="100", choices = [
				("80", _("80%")),
				("85", _("85%")),
				("90", _("90%")),
				("95", _("95%")),
				("100", _("100%")),
				("105", _("105%")),
				("110", _("110%")),
				("115", _("115%")),
				("120", _("120%"))
				])
config.plugins.inHD.VolumeBar = ConfigSelection(default="vertical", choices = [
				("vertical", _("Vertical")),
				("horizontal", _("Horizontal"))
				])
config.plugins.inHD.WindowStyle = ConfigSelection(default="new", choices = [
				("new", _("New")),
				("classic", _("Classic"))
				])
config.plugins.inHD.ShowFooter = ConfigSelection(default="True", choices = [
				("True", _("Yes")),
				("False", _("No"))
				])
				
def main(session, **kwargs):
	session.open(inHDsetup)

def Plugins(**kwargs):
	return PluginDescriptor(name="inHD Controler", description=_("Configuration tool for infinityHD-nbox"), where = PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)

#######################################################################

class inHDsetup(Screen, ConfigListScreen):
	skin = """
    <screen name="inHDsetup" position="center,center" size="980,650" title="inHD Controler GIT">
      <ePixmap position="217,0" size="546,202" pixmap="infinityHD-nbox/menu/infinityHD-nbox-logo.png" alphatest="blend" transparent="1" />
      <eLabel font="Regular;22" foregroundColor="foreground" halign="left" position="49,570" size="120,26" text="Cancel" />
      <eLabel font="Regular;22" foregroundColor="foreground" halign="left" position="209,570" size="120,26" text="Save" />
      <eLabel font="Regular;22" foregroundColor="foreground" halign="left" position="369,570" size="120,26" text="Restart GUI" />
      <ePixmap alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/buttons/red.png" position="10,567" size="30,30" />
      <ePixmap alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/buttons/green.png" position="170,567" size="30,30" />      
      <ePixmap alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/buttons/yellow.png" position="330,567" size="30,30" />      
      <widget name="config" position="15,187" scrollbarMode="showOnDemand" size="950,350" />
    </screen>"""

	def __init__(self, session, args = None):
		Screen.__init__(self, session)
		self.session = session
		self.onChangedEntry = [ ]
		self.datei = "/usr/share/enigma2/infinityHD-nbox/skin.xml"
		self.dateiTMP = "/usr/share/enigma2/infinityHD-nbox/skin.xml.tmp"
		self.daten = "/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/"
		self.release = "-git"
		self.skin_lines = []
		
		self.list = [ ]
		ConfigListScreen.__init__(self, self.list, session = session, on_change = self.changedEntry)
		self.createSetup()

		self["actions"] = ActionMap(["OkCancelActions", "DirectionActions", "InputActions", "ColorActions"],
									{
									"left": self.keyLeft,
									"down": self.keyDown,
									"up": self.keyUp,
									"right": self.keyRight,
									"red": self.exit,
									"yellow": self.reboot,
									"blue": self.showInfo,
									"green": self.save,
									"cancel": self.exit}, -2)

	def createSetup(self):								
		self.list = []
		self.list.append(getConfigListEntry(_("============ Fonts & colors ============"), ))
		self.list.append(getConfigListEntry(_("Font:"), config.plugins.inHD.Font))
		self.list.append(getConfigListEntry(_("EPG font size on Channel Selection screen:"), config.plugins.inHD.ChSelDesc))
		self.list.append(getConfigListEntry(_("EPG font size on Second Infobar screen:"), config.plugins.inHD.SIDesc))
		self.list.append(getConfigListEntry(_("EPG font size on EPG Selection screen:"), config.plugins.inHD.EPGSelDesc))
		self.list.append(getConfigListEntry(_("EPG font size on Event View screen:"), config.plugins.inHD.EvDesc))
		self.list.append(getConfigListEntry(_("EPG font size on GraphMultiEPG screen:"), config.plugins.inHD.GraphDesc))
		self.list.append(getConfigListEntry(_("Colors:"), config.plugins.inHD.Colors))
		self.list.append(getConfigListEntry(_("============ Infobar ============"), ))
		self.list.append(getConfigListEntry(_("Infobar:"), config.plugins.inHD.Infobar))
		if config.plugins.inHD.Infobar.value == "bigpicon-classic-lite":
			config.plugins.inHD.ShowFooter.value = "False"
		else:
			self.list.append(getConfigListEntry(_("Show footer in Infobar:"), config.plugins.inHD.ShowFooter))
			if config.plugins.inHD.ShowFooter.value == "True":
				self.list.append(getConfigListEntry(_("Infobar Footer:"), config.plugins.inHD.InfobarFooter))
		self.list.append(getConfigListEntry(_("============ Second Infobar ============"), ))
		self.list.append(getConfigListEntry(_("Second Infobar:"), config.plugins.inHD.SecondInfobar))
		self.list.append(getConfigListEntry(_("Second Infobar Footer:"), config.plugins.inHD.SecondInfobarFooter))
		self.list.append(getConfigListEntry(_("============ Channel Selection ============"), ))
		self.list.append(getConfigListEntry(_("Channel Selection side:"), config.plugins.inHD.Side))
		self.list.append(getConfigListEntry(_("Picon size:"), config.plugins.inHD.Picon))
		self.list.append(getConfigListEntry(_("Channel Selection rows:"), config.plugins.inHD.Rows))
		self.list.append(getConfigListEntry(_("How many next events to show on Channel Selection screen:"), config.plugins.inHD.ChannelSelectionNumberNext))
		self.list.append(getConfigListEntry(_("============ Other ============"), ))
		self.list.append(getConfigListEntry(_("EPG Selection:"), config.plugins.inHD.EpgSelection))
		self.list.append(getConfigListEntry(_("Event View:"), config.plugins.inHD.Eventview))
		self.list.append(getConfigListEntry(_("Number Zap:"), config.plugins.inHD.NumberZap))
		self.list.append(getConfigListEntry(_("Volume Bar:"), config.plugins.inHD.VolumeBar))
		self.list.append(getConfigListEntry(_("Window Style:"), config.plugins.inHD.WindowStyle))

		self["config"].list = self.list
		self["config"].l.setList(self.list)

	def changedEntry(self):
		for x in self.onChangedEntry:
			x()
			
	def keyLeft(self):	
		ConfigListScreen.keyLeft(self)
		self.createSetup()

	def keyRight(self):
		ConfigListScreen.keyRight(self)
		self.createSetup()
	
	def keyDown(self):
		self["config"].instance.moveSelection(self["config"].instance.moveDown)
		
	def keyUp(self):
		self["config"].instance.moveSelection(self["config"].instance.moveUp)
	
	def reboot(self):
		restartbox = self.session.openWithCallback(self.restartGUI,MessageBox,_("Do you really want to restart GUI now?"), MessageBox.TYPE_YESNO)
		restartbox.setTitle(_("Restart GUI"))
		
	def showInfo(self):
		self.session.open(MessageBox, _("Information"), MessageBox.TYPE_INFO)

	def save(self):
		for x in self["config"].list:
			if len(x) > 1:
        			x[1].save()
			else:
       				pass

		########### READING DATA FILES
		try:
			# Head & Colors
			self.appendSkinFile(self.daten + "skin-head-" + config.plugins.inHD.Colors.value + ".xml")
			# Window Style
			self.appendSkinFile(self.daten + "windowstyle-" + config.plugins.inHD.WindowStyle.value + ".xml")
			# Font Type
			self.appendSkinFile(self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + ".xml")
			# EPG Font Size
			self.appendSkinFile(self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-chseldesc-" + config.plugins.inHD.ChSelDesc.value + ".xml")
			self.appendSkinFile(self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-epgseldesc-" + config.plugins.inHD.EPGSelDesc.value + ".xml")
			self.appendSkinFile(self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-evdesc-" + config.plugins.inHD.EvDesc.value + ".xml")
			self.appendSkinFile(self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-graphdesc-" + config.plugins.inHD.GraphDesc.value + ".xml")
			self.appendSkinFile(self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-sidesc-" + config.plugins.inHD.SIDesc.value + ".xml")
			self.appendSkinFile(self.daten + "fonts/skin-fonts-subtitles.xml")
			# Infobar
			if config.plugins.inHD.ShowFooter.value=="True":
				self.appendSkinFile(self.daten + "infobar-" + config.plugins.inHD.Infobar.value + ".xml")
			else:
				self.appendSkinFile(self.daten + "infobar-" + config.plugins.inHD.Infobar.value + "-nofooter.xml")
			# Infobar Footer
			if config.plugins.inHD.ShowFooter.value=="True":
				self.appendSkinFile(self.daten + "footer-infobar-" + config.plugins.inHD.InfobarFooter.value + ".xml")
			else:
				self.appendSkinFile(self.daten + "footer-infobar-dummy.xml")
			# Second Infobar
			if config.plugins.inHD.SecondInfobarFooter.value=="ecmsatsig":
				self.appendSkinFile(self.daten + "secondinfobar-" + config.plugins.inHD.SecondInfobar.value + "-ecm.xml")
			else: 
				self.appendSkinFile(self.daten + "secondinfobar-" + config.plugins.inHD.SecondInfobar.value + ".xml")
			# Second Infobar Footer
			if config.plugins.inHD.SecondInfobar.value=="compact":
				self.appendSkinFile(self.daten + "footer-infobar-dummy.xml")
			else:	
				self.appendSkinFile(self.daten + "footer-infobar-" + config.plugins.inHD.SecondInfobarFooter.value + ".xml")
			# Channel Selection 1
			self.appendSkinFile(self.daten + "channel1-" + config.plugins.inHD.Picon.value + "-" + config.plugins.inHD.Side.value + "-nonext.xml")
			# Channel Selection 1a
			self.appendSkinFile(self.daten + "channel1a-next" + config.plugins.inHD.ChannelSelectionNumberNext.value + "-" + config.plugins.inHD.Side.value + ".xml")
			# Channel Selection 2
			self.appendSkinFile(self.daten + "channel2-" + config.plugins.inHD.Side.value + "-" + config.plugins.inHD.Rows.value + ".xml")
			# EPG Selection
			self.appendSkinFile(self.daten + "epg-" + config.plugins.inHD.EpgSelection.value + ".xml")
			# EventView
			self.appendSkinFile(self.daten + "eventview-" + config.plugins.inHD.Eventview.value + ".xml")
			# NumberZap
			self.appendSkinFile(self.daten + "numberzap-" + config.plugins.inHD.NumberZap.value + ".xml")
			# Movie Player & Movie Selection
			if config.plugins.inHD.Infobar.value=="bigpicon-classic" or config.plugins.inHD.Infobar.value=="bigpicon-updown":
				self.appendSkinFile(self.daten + "movie-bigpicon.xml")
			elif config.plugins.inHD.Infobar.value=="bigpicon-classic-lite":
				self.appendSkinFile(self.daten + "movie-bigpicon-lite.xml")
			else:
				self.appendSkinFile(self.daten + "movie-picon.xml")
			# Volume Bar
			self.appendSkinFile(self.daten + "volumebar-" + config.plugins.inHD.VolumeBar.value + ".xml")
			# Virtual Zap
			if config.plugins.inHD.ShowFooter=="True":
				self.appendSkinFile(self.daten + "vzap-" + config.plugins.inHD.Infobar.value + ".xml")
			else:
				self.appendSkinFile(self.daten + "vzap-" + config.plugins.inHD.Infobar.value + "-nofooter.xml")
			# Skin rest
			self.appendSkinFile(self.daten + "skin-rest.xml")
			
			xFile = open(self.datei, "w")
			for xx in self.skin_lines:
				xFile.writelines(xx)
			xFile.close()
			self.skin_lines = []
			if config.plugins.inHD.Infobar.value=="bigpicon-classic" or config.plugins.inHD.Infobar.value=="bigpicon-updown":
				system("rm -f /usr/share/enigma2/infinityHD-nbox/picon_default.png && ln -s /usr/share/enigma2/infinityHD-nbox/bigpicon_default.png /usr/share/enigma2/infinityHD-nbox/picon_default.png")
			else:
				system("rm -f /usr/share/enigma2/infinityHD-nbox/picon_default.png && ln -s /usr/share/enigma2/infinityHD-nbox/stdpicon_default.png /usr/share/enigma2/infinityHD-nbox/picon_default.png")
			self.session.open(MessageBox, _("Successfully creating Skin!"), MessageBox.TYPE_INFO, timeout=5)

		except:
			self.session.open(MessageBox, _("Error creating Skin!"), MessageBox.TYPE_ERROR)
			configfile.save()
			restartbox = self.session.openWithCallback(self.restartGUI,MessageBox,_("GUI needs a restart to apply a new skin.\nDo you want to Restart the GUI now?"), MessageBox.TYPE_YESNO)
			restartbox.setTitle(_("Restart GUI"))

	def restartGUI(self, answer):
		if answer is True:
			configfile.save()
			self.session.open(TryQuitMainloop, 3)
		else:
			self.close()
			
	def appendSkinFile(self,appendFileName):
		skFile = open(appendFileName, "r")
		file_lines = skFile.readlines()
		skFile.close()	
		for x in file_lines:
			self.skin_lines.append(x)
			

	def exit(self):
		for x in self["config"].list:
			if len(x) > 1:
					x[1].cancel()
			else:
       				pass
		self.close()
