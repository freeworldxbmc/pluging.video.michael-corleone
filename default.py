import sys
import os
import json
import urllib
import urllib2
import urlparse
import xbmcaddon
import xbmcgui
import xbmcplugin
import load_channels
import hashlib
import re
import time
import xbmc
import net
import server
import config
import shutil

from t0mm0.common.addon import Addon
from metahandler import metahandlers

addon_id = 'plugin.video.stalker'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
ADDON2=xbmcaddon.Addon(id='plugin.video.stalker')
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
iconlm = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'iconlm.png'))
iconhdm = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'iconhdm.png'))
iconts = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'iconts.png'))
icons = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icons.png'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
directory = xbmc.translatePath('special://home/userdata/addon_data/script.tvguidetecbox/')
destinaddons = xbmc.translatePath('special://home/userdata/addon_data/script.tvguidetecbox/addons.ini')
destinsets = xbmc.translatePath('special://home/userdata/addon_data/script.tvguidetecbox/settings.xml')
metaset = selfAddon.getSetting('enable_meta')

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addondir    = xbmc.translatePath( addon.getAddonInfo('profile') ) 

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
go = True;

xbmcplugin.setContent(addon_handle, 'movies')

net = net.Net()
dialog = xbmcgui.Dialog()

user = selfAddon.getSetting('username')
passw = selfAddon.getSetting('password')

if user == '' or passw == '':
	dialog.ok(addon_id, 
	dialog.ok(addon_id, 
	ret = dialog.yesno
	if ret == 1:
		keyb = xbmc.Keyboard('' ')
		keyb.doModal()
		if (keyb.isConfirmed()):
			search = keyb.getText()
			username=search
			keyb = xbmc.Keyboard('', '')
			keyb.doModal()
			if (keyb.isConfirmed()):
				search = keyb.getText()
				password=search
				selfAddon.setSetting('username',username)
				selfAddon.setSetting('password',password)
	else:quit()

def Main():
	addDir(
	addDir(
	addDir(                                                 
	addDir(
	addDir(
	xbmc.executebuiltin('')

def Ivue():
	if not os.path.exists(directory):
		dialog.ok(addon_id, '
		dialog.notification(addonname, 'please install and run ivue tv guide at least once', xbmcgui.NOTIFICATION_ERROR );
	
	if os.path.exists(directory):
		addonsini = urllib.URLopener()
		addonsini.retrieve destinaddons)
		addonsini = urllib.URLopener()
		addonsini.retrieve(", destinsets)
		addDir(' '',fanart)
	xbmc.executebuiltin('')
  
def GetContent():
	user = selfAddon.getSetting('username')
	passw = selfAddon.getSetting('password')
	headers={'VXNlci1BZ2VudA=='.decode('base64'):'QXBhY2hlLUh0dHBDbGllbnQvVU5BVkFJTEFCTEUgKGphdmEgMS40KQ=='.decode('base64'),
			 'Q29udGVudC1UeXBl'.decode('base64'):'YXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVk'.decode('base64'),
			 'YXBwLXNlc3Npb24='.decode('base64'):'Mjc1ZjI2ZTMyMTcyNmI5YTk5ZThkOTVjM2VmZTg4YWI='.decode('base64'),
			 'Q29ubmVjdGlvbg=='.decode('base64'):'S2VlcC1BbGl2ZQ=='.decode('base64'),
			 'SG9zdA=='.decode('base64'):'dWt0dm5vdy5kZXNpc3RyZWFtcy50dg=='.decode('base64')}
	net.http_POST('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1sb2dpbiZ1c2VybmFtZT0='.decode('base64')+user+'&password='+passw,'',headers=headers)
	net.http_POST('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfcGFja2FnZV9uYW1l'.decode('base64'),'',headers=headers)
	net.http_POST('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYW5ub3Vj'.decode('base64'),'',headers=headers)
	net.http_POST('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfcGFja2FnZV9uYW1l'.decode('base64'),'',headers=headers)
	response=net.http_POST('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9'.decode('base64')+user,'',headers=headers)
	response=response.content.replace('none','Ch')
	channels=json.loads(response)
	return channels

def GetChannels(url):
	channels = GetContent()
	data=channels['channel']
	for item in data:
		name=item['name']
		if name==None:name='Channel'
		thumb=item['img']
		cat=item['cat_id']
		thumb='aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv'.decode('base64')+thumb
		if url=='0':
			addLink(name,'url',2,thumb,fanart)
		if cat==url:
			addLink(name,'url',2,thumb,fanart)
	xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
	xbmc.executebuiltin('Container.SetViewMode(50)')

def GetStreams(name):
	channels = GetContent()
	data=channels['channel']
	streamname=[]
	streamurl=[]
	streamthumb=[]
	for item in data:
		thumb=item['img']
		if item['name'] == name:			
			streamurl.append( item['stream_url'] )
			streamurl.append( item['stream_url2'] )
			streamurl.append( item['stream_url3'] )
			streamname.append( 'Stream 1' )
			streamname.append( 'Stream 2' )
			streamname.append( 'Stream 3' )
			streamthumb.append( thumb )
			streamthumb.append( thumb )
			streamthumb.append( thumb )		
	select = dialog.select(name,streamname)
	if select == -1:
		return
	else:
		url = streamurl[select]
		iconimage = 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv'.decode('base64')+streamthumb[select]
		ok=True
		liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
		xbmc.Player().play(url, liz, False)
		return ok

def addLink(name,url,mode,iconimage,fanart,description=''):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
		liz.setProperty('fanart_image', fanart)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		return ok

def addDir(name,url,mode,iconimage,fanart,description=''):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
		liz.setProperty('fanart_image', fanart)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok

def get_params():
		param=[]
		paramstring=sys.argv[2]
		if len(paramstring)>=2:
				e4=sys.argv[2]
				cleanedparams=e4.replace('?','')
				if (e4[len(e4)-1]=='/'):
						e4=e4[0:len(e4)-2]
				pairsofparams=cleanedparams.split('&')
				param={}
				for i in range(len(pairsofparams)):
						splitparams={}
						splitparams=pairsofparams[i].split('=')
						if (len(splitparams))==2:
								param[splitparams[0]]=splitparams[1]	
		return param
		   
e4=get_params()
url=None
name=None
mode=None
iconimage=None
description=None

try:url=urllib.unquote_plus(e4["url"])
except:pass
try:name=urllib.unquote_plus(e4["name"])
except:pass
try:mode=int(e4["mode"])
except:pass
try:iconimage=urllib.unquote_plus(e4["iconimage"])
except:pass

if mode==None or url==None or len(url)<1:Main()
elif mode==1:GetChannels(url)
elif mode==2:GetStreams(name)
elif mode==3:Ivue()


def addPortal(portal):

	if portal['url'] == '':
		return;

	url = build_url({
		'mode': 'genres', 
		'portal' : json.dumps(portal)
		});
	
	cmd = 'XBMC.RunPlugin(' + base_url + '?mode=cache&stalker_url=' + portal['url'] + ')';	
	
	li = xbmcgui.ListItem(portal['name'], iconImage='DefaultProgram.png')
	li.addContextMenuItems([ ('Clear Cache', cmd) ]);

	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	
	
def build_url(query):
	return base_url + '?' + urllib.urlencode(query)


def homeLevel():
	global portal_1, portal_2, portal_3, go;
	
	#todo - check none portal

	if go:
		addPortal(portal_1);
		addPortal(portal_2);
		addPortal(portal_3);
	
		xbmcplugin.endOfDirectory(addon_handle);

def genreLevel():
	
	try:
		data = load_channels.getGenres(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		
		return;

	data = data['genres'];
		
	url = build_url({
		'mode': 'vod', 
		'portal' : json.dumps(portal)
	});
			
	li = xbmcgui.ListItem('VoD', iconImage='DefaultVideo.png')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	
	
	for id, i in data.iteritems():

		title 	= i["title"];
		
		url = build_url({
			'mode': 'channels', 
			'genre_id': id, 
			'genre_name': title.title(), 
			'portal' : json.dumps(portal)
			});
			
		if id == '10':
			iconImage = 'OverlayLocked.png';
		else:
			iconImage = 'DefaultVideo.png';
			
		li = xbmcgui.ListItem(title.title(), iconImage=iconImage)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
		

	xbmcplugin.endOfDirectory(addon_handle);

def vodLevel():
	
	try:
		data = load_channels.getVoD(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;
	
	
	data = data['vod'];
	
		
	for i in data:
		name 	= i["name"];
		cmd 	= i["cmd"];
		logo 	= i["logo"];
		
		
		if logo != '':
			logo_url = portal['url'] + logo;
		else:
			logo_url = 'DefaultVideo.png';
				
				
		url = build_url({
				'mode': 'play', 
				'cmd': cmd, 
				'tmp' : '0', 
				'title' : name.encode("utf-8"),
				'genre_name' : 'VoD',
				'logo_url' : logo_url, 
				'portal' : json.dumps(portal)
				});
			

		li = xbmcgui.ListItem(name, iconImage=logo_url, thumbnailImage=logo_url)
		li.setInfo(type='Video', infoLabels={ "Title": name })

		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_UNSORTED);
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
	xbmcplugin.endOfDirectory(addon_handle);

def channelLevel():
	stop=False;
		
	try:
		data = load_channels.getAllChannels(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;
	
	
	data = data['channels'];
	genre_name 	= args.get('genre_name', None);
	
	genre_id_main = args.get('genre_id', None);
	genre_id_main = genre_id_main[0];
	
	if genre_id_main == '10' and portal['parental'] == 'true':
		result = xbmcgui.Dialog().input('Parental', hashlib.md5(portal['password'].encode('utf-8')).hexdigest(), type=xbmcgui.INPUT_PASSWORD, option=xbmcgui.PASSWORD_VERIFY);
		if result == '':
			stop = True;

	
	if stop == False:
		for i in data.values():
			
			name 		= i["name"];
			cmd 		= i["cmd"];
			tmp 		= i["tmp"];
			number 		= i["number"];
			genre_id 	= i["genre_id"];
			logo 		= i["logo"];
		
			if genre_id_main == '*' and genre_id == '10' and portal['parental'] == 'true':
				continue;
		
		
			if genre_id_main == genre_id or genre_id_main == '*':
		
				if logo != '':
					logo_url = portal['url'] + '/stalker_portal/misc/logos/320/' + logo;
				else:
					logo_url = 'DefaultVideo.png';
				
				
				url = build_url({
					'mode': 'play', 
					'cmd': cmd, 
					'tmp' : tmp, 
					'title' : name.encode("utf-8"),
					'genre_name' : genre_name,
					'logo_url' : logo_url,  
					'portal' : json.dumps(portal)
					});
			

				li = xbmcgui.ListItem(name, iconImage=logo_url, thumbnailImage=logo_url);
				li.setInfo(type='Video', infoLabels={ 
					'title': name,
					'count' : number
					});

				xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li);
		
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_PLAYLIST_ORDER);
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_PROGRAM_COUNT);
		
		
		xbmcplugin.endOfDirectory(addon_handle);

def playLevel():
	
	dp = xbmcgui.DialogProgressBG();
	dp.create('Channel', 'Loading ...');
	
	title 	= args['title'][0];
	cmd 	= args['cmd'][0];
	tmp 	= args['tmp'][0];
	genre_name 	= args['genre_name'][0];
	logo_url 	= args['logo_url'][0];
	
	try:
		if genre_name != 'VoD':
			url = load_channels.retriveUrl(portal['mac'], portal['url'], portal['serial'], cmd, tmp);
		else:
			url = load_channels.retriveVoD(portal['mac'], portal['url'], portal['serial'], cmd);

	
	except Exception as e:
		dp.close();
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;

	
	dp.update(80);
	
	title = title.decode("utf-8");
	
	title += ' (' + portal['name'] + ')';
	
#	li = xbmcgui.ListItem(title, iconImage=logo_url); <modified 9.0.19
	li = xbmcgui.ListItem(title, iconImage='DefaultVideo.png', thumbnailImage=logo_url);
	li.setInfo('video', {'Title': title, 'Genre': genre_name});
	xbmc.Player().play(item=url, listitem=li);
	
	dp.update(100);
	
	dp.close();


mode = args.get('mode', None);
portal =  args.get('portal', None)


if portal is None:
	portal_1 = config.portalConfig('1');
	portal_2 = config.portalConfig('2');
	portal_3 = config.portalConfig('3');	

else:
	portal = json.loads(portal[0]);

#  Modification to force outside call to portal_1 (9.0.19)

	portal_2 = config.portalConfig('2');
	portal_3 = config.portalConfig('3');	

	if not ( portal['name'] == portal_2['name'] or portal['name'] == portal_3['name'] ) :
		portal = config.portalConfig('1');

	

if mode is None:
	homeLevel();

elif mode[0] == 'cache':	
	stalker_url = args.get('stalker_url', None);
	stalker_url = stalker_url[0];	
	load_channels.clearCache(stalker_url, addondir);

elif mode[0] == 'genres':
	genreLevel();
		
elif mode[0] == 'vod':
	vodLevel();

elif mode[0] == 'channels':
	channelLevel();
	
elif mode[0] == 'play':
	playLevel();
	
elif mode[0] == 'server':
	port = addon.getSetting('server_port');
	
	action =  args.get('action', None);
	action = action[0];
	
	dp = xbmcgui.DialogProgressBG();
	dp.create('IPTV', 'Just A Second ...');
	
	if action == 'start':
	
		if server.serverOnline():
			xbmcgui.Dialog().notification(addonname, 'Server already started.\nPort: ' + str(port), xbmcgui.NOTIFICATION_INFO );
		else:
			server.startServer();
			time.sleep(5);
			if server.serverOnline():
				xbmcgui.Dialog().notification(addonname, 'Server started.\nPort: ' + str(port), xbmcgui.NOTIFICATION_INFO );
			else:
				xbmcgui.Dialog().notification(addonname, 'Server not started. Wait one moment and try again. ', xbmcgui.NOTIFICATION_ERROR );
				
	else:
		if server.serverOnline():
			server.stopServer();
			time.sleep(5);
			xbmcgui.Dialog().notification(addonname, 'Server stopped.', xbmcgui.NOTIFICATION_INFO );
		else:
			xbmcgui.Dialog().notification(addonname, 'Server is already stopped.', xbmcgui.NOTIFICATION_INFO );
			
	dp.close();





	
xbmcplugin.endOfDirectory(int(sys.argv[1]))
