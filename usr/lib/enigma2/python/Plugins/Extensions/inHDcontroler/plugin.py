#######################################################################
#
#  Ai-HD-Skins Control for Dreambox/Enigma-2
#  Coded by Vali (c)2009-2011
#  Support: www.dreambox-tools.info
#
#######################################################################
#
#  Mod by Pich 2012
#  Support: www.vuplus-support.org 
#
#######################################################################
#
#  Mod by herpoi 2013 for infinityHD-nbox
#  Support: ...
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
from Components.config import config, ConfigYesNo, ConfigSubsection, getConfigListEntry, ConfigSelection, ConfigText, ConfigInteger
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Tools.Directories import fileExists
from skin import parseColor
from os import system



config.plugins.inHD  = ConfigSubsection()
config.plugins.inHD.Infobar = ConfigSelection(default="classic", choices = [
				("classic", _("Classic")),
				("nopicon-classic", _("Classic No Picon")),
				("nopicon-bigclock", _("BigClock No Picon")),
				("bigpicon", _("Big Picon")),
				("bigpicon-classic", _("Big Picon Classic")),
				("updown", _("Up Down")),
				("nopicon-updown", _("Up Down No Picon"))		
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
config.plugins.inHD.Picon = ConfigSelection(default="Classic", choices = [
				("bigpicon", _("Big Picon")),
				("nopicon", _("No Picon")),
				("classic", _("Classic"))
				])				
config.plugins.inHD.ChannelSelectionnext = ConfigSelection(default="no", choices = [
				("yes", _("Yes")),
				("no", _("No"))
				])		
config.plugins.inHD.Rows = ConfigSelection(default="14", choices = [
				("14", _("14")),
				("16", _("16")),
				("19", _("19"))
				])		
config.plugins.inHD.EpgSelection = ConfigSelection(default="right", choices = [
				("right", _("Right")),
				("right-bigpicon", _("Right Big Picon")),
				("right-nopicon", _("Right No Picon")),
				("left", _("Left")),
				("left-bigpicon", _("Left Big Picon")),
				("left-nopicon", _("Left No Picon")),
				("up", _("Up")),
				("up-bigpicon", _("Up Big Picon")),
				("up-nopicon", _("Up No Picon"))
				])
config.plugins.inHD.Eventview = ConfigSelection(default="classic", choices = [
				("classic", _("Classic")),
				("bigpicon", _("Big Picon")),
				("nopicon", _("No Picon")),
				])
config.plugins.inHD.NumberZap = ConfigSelection(default="center", choices = [
				("center", _("Center")),
				("topleft", _("Top Left")),
				("topright", _("Top Right")),
				("bottomleft", _("Bottom Left")),
				("bottomright", _("Bottom Right"))
				])        				
config.plugins.inHD.InfobarFooter = ConfigSelection(default="ctsig", choices = [
				("ctsig", _("CAID/Tuner/Signal")),
				("etsig", _("ECM/Tuner/Signal")),
				("satsig", _("Sat Info/Signal"))
				])		
config.plugins.inHD.SecondInfobarFooter = ConfigSelection(default="satsig", choices = [
				("ctsig", _("CAID/Tuner/Signal")),
				("etsig", _("ECM/Tuner/Signal")),
				("satsig", _("Sat Info/Signal"))
				])		
config.plugins.inHD.Font = ConfigSelection(default="ubuntu", choices = [
        ("ubuntu", _("Ubuntu")),
        ("roboto", _("Roboto"))
        ])

def main(session, **kwargs):
	session.open(inHDsetup)

def Plugins(**kwargs):
	return PluginDescriptor(name="infinityHD Controler", description=_("Configuration tool for infinityHD-nbox skin. Mod by herpoi"), where = PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)

#######################################################################

class inHDsetup(ConfigListScreen, Screen):
	skin = """
    <screen name="inHDsetup" position="center,center" size="730,600" title="infinityHD Controler 1.0">
      <ePixmap position="92,0" size="546,202" pixmap="infinityHD-nbox/menu/infinityHD-nbox-logo.png" alphatest="on" />
      <eLabel font="Regular;22" foregroundColor="foreground" halign="left" position="49,570" size="120,26" text="Cancel" />
      <eLabel font="Regular;22" foregroundColor="foreground" halign="left" position="209,570" size="120,26" text="Save" />
      <ePixmap alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/buttons/red.png" position="10,567" size="30,30" />
      <ePixmap alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/buttons/green.png" position="170,567" size="30,30" />      
      <widget name="config" position="15,212" scrollbarMode="showOnDemand" size="700,350" />
    </screen>"""

	def __init__(self, session):
		self.release = "-release1.3"
		Screen.__init__(self, session)
		self.session = session
		self.datei = "/usr/local/share/enigma2/infinityHD-nbox/skin.xml"
		self.daten = "/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/"
		list = []
		list.append(getConfigListEntry(_("Font:"), config.plugins.inHD.Font))
		list.append(getConfigListEntry(_("Infobar:"), config.plugins.inHD.Infobar))
		list.append(getConfigListEntry(_("Infobar Footer:"), config.plugins.inHD.InfobarFooter))
		list.append(getConfigListEntry(_("Second Infobar:"), config.plugins.inHD.SecondInfobar))
		list.append(getConfigListEntry(_("Second Infobar Footer:"), config.plugins.inHD.SecondInfobarFooter))
		list.append(getConfigListEntry(_("Channel Side:"), config.plugins.inHD.Side))
		list.append(getConfigListEntry(_("Channel Picon:"), config.plugins.inHD.Picon))
		list.append(getConfigListEntry(_("Channel Rows:"), config.plugins.inHD.Rows))
		list.append(getConfigListEntry(_("Show next events on channel selection screen:"), config.plugins.inHD.ChannelSelectionnext))
		list.append(getConfigListEntry(_("EPG Selection:"), config.plugins.inHD.EpgSelection))
		list.append(getConfigListEntry(_("Event View:"), config.plugins.inHD.Eventview))
		list.append(getConfigListEntry(_("Number Zap:"), config.plugins.inHD.NumberZap))
	
		
		ConfigListScreen.__init__(self, list)
		self["actions"] = ActionMap(["OkCancelActions", "ColorActions"], 
									{
									"red": self.exit, 
									"green": self.save 
									})
#									}, -1)
		self.onLayoutFinish.append(self.UpdateComponents)

	def UpdateComponents(self):
	  if not fileExists(self.datei + self.release):
			system("touch " + self.datei + self.release)

	def save(self):
		if not fileExists(self.datei + self.release):
			for x in self["config"].list:
				x[1].cancel()
			self.close()
			return
		for x in self["config"].list:
			x[1].save()
		try:
			skin_lines = []
			head_file = self.daten + "skin-head.xml"
			skFile = open(head_file, "r")
			head_lines = skFile.readlines()
			skFile.close()
			for x in head_lines:
				skin_lines.append(x)
				
			fonts_file = self.daten + "skin-fonts-" + config.plugins.inHD.Font.value + ".xml"
			skFile = open(fonts_file, "r")
			fonts_lines = skFile.readlines()
			skFile.close()
			for x in fonts_lines:
			  skin_lines.append(x)
			  
			infobar_file = self.daten + "infobar-" + config.plugins.inHD.Infobar.value + ".xml"
			skFile = open(infobar_file, "r")
			infobar_lines = skFile.readlines()
			skFile.close()
			for x in infobar_lines:
				skin_lines.append(x)  
				
			infobarfooter_file = self.daten + "footer-infobar-" + config.plugins.inHD.InfobarFooter.value + ".xml"
			skFile = open(infobarfooter_file, "r")
			infobarfooter_lines = skFile.readlines()
			skFile.close()
			for x in infobarfooter_lines:
				skin_lines.append(x)
				
			secondinfobar_file = self.daten + "secondinfobar-" + config.plugins.inHD.SecondInfobar.value + ".xml"
			skFile = open(secondinfobar_file, "r")
			secondinfobar_lines = skFile.readlines()
			skFile.close()
			for x in secondinfobar_lines:
				skin_lines.append(x)
				
			skn_file = self.daten + "footer-infobar-"
			if config.plugins.inHD.SecondInfobar.value=="compact":
				skn_file = skn_file + "dummy.xml"		
			else:	
				skn_file = skn_file + config.plugins.inHD.SecondInfobarFooter.value + ".xml"
			skFile = open(skn_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)

			skn_file = self.daten + "channel1-"
			if config.plugins.inHD.ChannelSelectionnext.value=="yes":
				skn_file = skn_file + config.plugins.inHD.Side.value + "-" + config.plugins.inHD.Picon.value + ".xml"	
			else:	
				skn_file = skn_file + config.plugins.inHD.Side.value + "-" + config.plugins.inHD.Picon.value + "-nonext.xml"
			skFile = open(skn_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)	

			skn_file = self.daten + "rows-"
			skn_file = skn_file + config.plugins.inHD.Side.value + "-" + config.plugins.inHD.Rows.value + ".xml"	
			skFile = open(skn_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)	
				
			skn_file = self.daten + "channel2-"
			if config.plugins.inHD.ChannelSelectionnext.value=="yes":
				skn_file = skn_file + config.plugins.inHD.Side.value + "-" + config.plugins.inHD.Picon.value + ".xml"	
			else:	
				skn_file = skn_file + config.plugins.inHD.Side.value + "-" + config.plugins.inHD.Picon.value + "-nonext.xml"
			skFile = open(skn_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)	

			skn_file = self.daten + "epg-" + config.plugins.inHD.EpgSelection.value + ".xml"
			skFile = open(skn_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)	
				
			skn_file = self.daten + "eventview-" + config.plugins.inHD.Eventview.value + ".xml"
			skFile = open(skn_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)	
				
			skn_file = self.daten + "numberzap-" + config.plugins.inHD.NumberZap.value + ".xml"
			skFile = open(skn_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)	

			base_file = self.daten + "skin-rest.xml"
			skFile = open(base_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)
			xFile = open(self.datei, "w")
			for xx in skin_lines:
				xFile.writelines(xx)
			xFile.close()
		except:	
			self.session.open(MessageBox, _("Error by processing the skin file !!!"), MessageBox.TYPE_ERROR)
		restartbox = self.session.openWithCallback(self.restartGUI,MessageBox,_("GUI needs a restart to apply a new skin.\nDo you want to Restart the GUI now?"), MessageBox.TYPE_YESNO)
		restartbox.setTitle(_("Restart GUI now?"))

	def restartGUI(self, answer):
		if answer is True:
			self.session.open(TryQuitMainloop, 3)
		else:
			self.close()

	def exit(self):
		for x in self["config"].list:
			x[1].cancel()
		self.close()
		

