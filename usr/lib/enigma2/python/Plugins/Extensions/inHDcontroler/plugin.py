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
config.plugins.inHD.Colors = ConfigSelection(default="classic", choices = [
				("classic", _("Classic")),
				("fresh", _("Fresh"))
				])
config.plugins.inHD.Infobar = ConfigSelection(default="bigpicon-classic", choices = [
        ("bigpicon-classic", _("BigPicon Classic ")),
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
				("bigpicon", _("Big Picon")),
				("nopicon", _("No Picon")),
				("picon", _("Classic"))
				])				
config.plugins.inHD.ChannelSelectionnext = ConfigSelection(default="no", choices = [
				("yes", _("Yes")),
				("no", _("No"))
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
config.plugins.inHD.Eventview = ConfigSelection(default="bigpicon", choices = [
				("picon-classic", _("Picon Classic")),
				("bigpicon", _("Big Picon")),
				("nopicon", _("No Picon"))
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
        ("80", _("80")),
        ("85", _("85")),
        ("90", _("90")),
        ("95", _("95")),
        ("100", _("100")),
        ("105", _("105")),
        ("110", _("110")),
        ("115", _("115")),
        ("120", _("120"))
        ])
config.plugins.inHD.EPGSelDesc = ConfigSelection(default="100", choices = [
        ("80", _("80")),
        ("85", _("85")),
        ("90", _("90")),
        ("95", _("95")),
        ("100", _("100")),
        ("105", _("105")),
        ("110", _("110")),
        ("115", _("115")),
        ("120", _("120"))
        ])
config.plugins.inHD.EvDesc = ConfigSelection(default="100", choices = [
        ("80", _("80")),
        ("85", _("85")),
        ("90", _("90")),
        ("95", _("95")),
        ("100", _("100")),
        ("105", _("105")),
        ("110", _("110")),
        ("115", _("115")),
        ("120", _("120"))
        ])
config.plugins.inHD.GraphDesc = ConfigSelection(default="100", choices = [
        ("80", _("80")),
        ("85", _("85")),
        ("90", _("90")),
        ("95", _("95")),
        ("100", _("100")),
        ("105", _("105")),
        ("110", _("110")),
        ("115", _("115")),
        ("120", _("120"))
        ])
config.plugins.inHD.SIDesc = ConfigSelection(default="100", choices = [
        ("80", _("80")),
        ("85", _("85")),
        ("90", _("90")),
        ("95", _("95")),
        ("100", _("100")),
        ("105", _("105")),
        ("110", _("110")),
        ("115", _("115")),
        ("120", _("120"))
        ])
		
def main(session, **kwargs):
	session.open(inHDsetup)

def Plugins(**kwargs):
	return PluginDescriptor(name="infinityHD Controler", description=_("Configuration tool for infinityHD-nbox skin. Mod by herpoi"), where = PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)

#######################################################################

class inHDsetup(ConfigListScreen, Screen):
	skin = """
    <screen name="inHDsetup" position="center,center" size="780,600" title="infinityHD Controler GIT">
      <ePixmap position="117,0" size="546,202" pixmap="infinityHD-nbox/menu/infinityHD-nbox-logo.png" alphatest="blend" transparent="1" />
      <eLabel font="Regular;22" foregroundColor="foreground" halign="left" position="49,570" size="120,26" text="Cancel" />
      <eLabel font="Regular;22" foregroundColor="foreground" halign="left" position="209,570" size="120,26" text="Save" />
      <ePixmap alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/buttons/red.png" position="10,567" size="30,30" />
      <ePixmap alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/buttons/green.png" position="170,567" size="30,30" />      
      <widget name="config" position="15,187" scrollbarMode="showOnDemand" size="750,350" />
    </screen>"""

	def __init__(self, session):
		self.release = "-git"
		Screen.__init__(self, session)
		self.session = session
		self.datei = "/usr/local/share/enigma2/infinityHD-nbox/skin.xml"
		self.daten = "/usr/lib/enigma2/python/Plugins/Extensions/inHDcontroler/data/"
		list = []
		list.append(getConfigListEntry(_("Font:"), config.plugins.inHD.Font))
		list.append(getConfigListEntry(_("EPG font size on Channel Selection screen [%]:"), config.plugins.inHD.ChSelDesc))
		list.append(getConfigListEntry(_("EPG font size on Second Infobar screen [%]:"), config.plugins.inHD.SIDesc))
		list.append(getConfigListEntry(_("EPG font size on EPG Selection screen [%]:"), config.plugins.inHD.EPGSelDesc))
		list.append(getConfigListEntry(_("EPG font size on Event View screen [%]:"), config.plugins.inHD.EvDesc))
		list.append(getConfigListEntry(_("EPG font size on GraphMultiEPG screen [%]:"), config.plugins.inHD.GraphDesc))
		list.append(getConfigListEntry(_("Colors:"), config.plugins.inHD.Colors))
		list.append(getConfigListEntry(_("Infobar:"), config.plugins.inHD.Infobar))
		list.append(getConfigListEntry(_("Infobar Footer:"), config.plugins.inHD.InfobarFooter))
		list.append(getConfigListEntry(_("Second Infobar:"), config.plugins.inHD.SecondInfobar))
		list.append(getConfigListEntry(_("Second Fnfobar Footer:"), config.plugins.inHD.SecondInfobarFooter))
		list.append(getConfigListEntry(_("Channel Selection side:"), config.plugins.inHD.Side))
		list.append(getConfigListEntry(_("Channel Selection picon:"), config.plugins.inHD.Picon))
		list.append(getConfigListEntry(_("Channel Selection rows:"), config.plugins.inHD.Rows))
		list.append(getConfigListEntry(_("Show next events on Channel Selection screen:"), config.plugins.inHD.ChannelSelectionnext))
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
			head_file = self.daten + "skin-head-" + config.plugins.inHD.Colors.value + ".xml"
			skFile = open(head_file, "r")
			head_lines = skFile.readlines()
			skFile.close()
			for x in head_lines:
				skin_lines.append(x)
				
			fonts_file = self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + ".xml"
			skFile = open(fonts_file, "r")
			fonts_lines = skFile.readlines()
			skFile.close()
			for x in fonts_lines:
			  skin_lines.append(x)
				
			fonts_file = self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-chseldesc-" + config.plugins.inHD.ChSelDesc.value + ".xml"
			skFile = open(fonts_file, "r")
			fonts_lines = skFile.readlines()
			skFile.close()
			for x in fonts_lines:
			  skin_lines.append(x)
				
			fonts_file = self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-epgseldesc-" + config.plugins.inHD.EPGSelDesc.value + ".xml"
			skFile = open(fonts_file, "r")
			fonts_lines = skFile.readlines()
			skFile.close()
			for x in fonts_lines:
			  skin_lines.append(x)
				
			fonts_file = self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-evdesc-" + config.plugins.inHD.EvDesc.value + ".xml"
			skFile = open(fonts_file, "r")
			fonts_lines = skFile.readlines()
			skFile.close()
			for x in fonts_lines:
			  skin_lines.append(x)
				
			fonts_file = self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-graphdesc-" + config.plugins.inHD.GraphDesc.value + ".xml"
			skFile = open(fonts_file, "r")
			fonts_lines = skFile.readlines()
			skFile.close()
			for x in fonts_lines:
			  skin_lines.append(x)

			fonts_file = self.daten + "fonts/skin-fonts-" + config.plugins.inHD.Font.value + "-sidesc-" + config.plugins.inHD.SIDesc.value + ".xml"
			skFile = open(fonts_file, "r")
			fonts_lines = skFile.readlines()
			skFile.close()
			for x in fonts_lines:
			  skin_lines.append(x)
			  
			fonts_file = self.daten + "fonts/skin-fonts-subtitles.xml"
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
			
			
			if config.plugins.inHD.SecondInfobarFooter.value=="ecmsatsig":
				secondinfobar_file = self.daten + "secondinfobar-" + config.plugins.inHD.SecondInfobar.value + "-ecm.xml"
			else: 
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
				skn_file = skn_file + config.plugins.inHD.Picon.value + "-" + config.plugins.inHD.Side.value + ".xml"	
			else:	
				skn_file = skn_file + config.plugins.inHD.Picon.value + "-" + config.plugins.inHD.Side.value + "-nonext.xml"
			skFile = open(skn_file, "r")
			file_lines = skFile.readlines()
			skFile.close()
			for x in file_lines:
				skin_lines.append(x)	

			skn_file = self.daten + "channel2-"
			skn_file = skn_file + config.plugins.inHD.Side.value + "-" + config.plugins.inHD.Rows.value + ".xml"	
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
		

