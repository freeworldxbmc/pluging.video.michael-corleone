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
import urllib2
import server

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addondir    = xbmc.translatePath( addon.getAddonInfo('profile') ) 
addonset	= ['4d4441364d5545364e7a6b364e5455364e5455364e54553d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMzNhMzEzMzNhMzEzMw=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5463364d5463364d54633d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzIzMDNhMzIzMDNhMzIzMA=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d6a41364d6a41364d54413d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzgzNDNhMzUzNjNhMzQzMw=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5441364d4441364d6a413d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzQzNDNhMzQzNDNhMzQzNA=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d444d364d444d364d444d3d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzAzODNhMzAzODNhMzAzOA=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5449364d7a51364e54593d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMjNhMzMzNDNhMzAzMQ=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5449364d7a51364d44553d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMjNhMzMzNDNhMzEzNw=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5449364d7a51364d546b3d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMjNhMzMzNDNhMzIzMA=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5449364d7a51364d6a553d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMjNhMzMzNDNhMzQzNg=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5449364d7a51364e6a513d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMjNhMzMzNDNhMzYzNg=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5449364d7a51364e6a673d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMjNhMzMzNDNhMzczNg=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5449364d7a51364e7a6b3d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMjNhMzMzNDNhMzgzNQ=='.decode('base64').decode('hex'), '4d4441364d5545364e7a67364d5449364d7a51364f446b3d'.decode('hex').decode('base64'), 'MzAzMDNhMzE0MTNhMzczODNhMzEzMjNhMzMzNDNhMzkzOQ=='.decode('base64').decode('hex')]
eternal		= (random.choice(addonset))
current     = os.getcwd()

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
	import urllib2

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