import sys
import os
import json
import urllib
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import load_channels
import hashlib
import re
import random
import base64

import server

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addondir    = xbmc.translatePath( addon.getAddonInfo('profile') ) 
addonset	= ['MDA6MUE6Nzg6NDI6NDI6NDI='.decode('base64'), 'MDA6MUE6Nzg6NDQ6NDQ6NDQ='.decode('base64'), 'MDA6MUE6Nzg6ODI6ODI6ODI='.decode('base64'), 'MDA6MUE6Nzg6OTk6OTk6OTk='.decode('base64'), 'MDA6MUE6Nzg6MTI6MTI6MTI='.decode('base64'), 'MDA6MUE6Nzg6MjA6MjA6MjA='.decode('base64'), 'MDA6MUE6Nzg6NDM6NDQ6NTE='.decode('base64'), 'MDA6MUE6Nzg6MTA6MDA6MDA='.decode('base64'), 'MDA6MUE6Nzg6MjI6MzM6NDQ='.decode('base64')]
eternal		= (random.choice(addonset))

def portalConfig(number):

	portal = {};
	
	portal['parental'] = addon.getSetting("parental");
	portal['password'] = addon.getSetting("password");
	
	portal['name'] = addon.getSetting("portal_name_" + number);
	portal['url'] = addon.getSetting("portal_url_" + number);
	portal['mac'] = configMac(number);
	portal['serial'] = configSerialNumber(number);
		
	return portal;


def configMac(number):
	global go;
	
	custom_mac = ('Y3VzdG9tX21hY18x'.decode('base64'));
	portal_mac = ('cG9ydGFsX21hY18x'.decode('base64'));
	
	if custom_mac != 'true':
		portal_mac = (eternal);
		
	elif not (custom_mac == 'true' and re.match("WzAtOWEtZl17Mn0oWy06XSlbMC05YS1mXXsyfShcXDFbMC05YS1mXXsyfSl7NH0k".decode('base64'), portal_mac.lower()) != None):
		xbmcgui.Dialog().notification(addonname, 'Custom Mac ' + number + ' is Invalid.', xbmcgui.NOTIFICATION_ERROR );
		portal_mac = '';
		go=False;
		
	return portal_mac;
	
	
def configSerialNumber(number):
	global go;
	
	send_serial = addon.getSetting('send_serial_' + number);
	custom_serial = addon.getSetting('custom_serial_' + number);
	serial_number = addon.getSetting('serial_number_' + number);
	device_id = addon.getSetting('device_id_' + number);
	device_id2 = addon.getSetting('device_id2_' + number);
	signature = addon.getSetting('signature_' + number);

	
	if send_serial != 'true':
		return None;
	
	elif send_serial == 'true' and custom_serial == 'false':
		return {'custom' : False};
		
	elif send_serial == 'true' and custom_serial == 'true':
	
		if serial_number == '' or device_id == '' or device_id2 == '' or signature == '':
			xbmcgui.Dialog().notification(addonname, 'Serial information is invalid.', xbmcgui.NOTIFICATION_ERROR );
			go=False;
			return None;
	
		return {'custom' : True, 'sn' : serial_number, 'device_id' : device_id, 'device_id2' : device_id2, 'signature' : signature};
		
	return None;