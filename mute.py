__version__ = '1.0'
__author__  = 'Spoon & Gac'

import b3
import b3.events

class MutePlugin(b3.plugin.Plugin):
	_adminPlugin = None
	requiresConfigFile = False

	def onStartup(self):
		self._adminPlugin = self.console.getPlugin("admin")
		if not self._adminPlugin:
			return False

		self._adminPlugin.registerCommand(self, 'mute', 100, self.cmd_mute)
		self.registerEvent(b3.events.EVT_CLIENT_SAY)
		self.registerEvent(b3.events.EVT_CLIENT_TEAM_SAY)
		self.registerEvent(b3.events.EVT_CLIENT_AUTH)

	def onEvent(self, event):
		if event.type == b3.events.EVT_CLIENT_AUTH:
			cursor = self.console.storage.query("SELECT * FROM muted_players WHERE client_id = '%s'" % event.client.cid)
			r = cursor.getRow()
			if cursor.rowcount > 0:
				muted = r['muted']
				event.client.setvar(self, 'muted', muted)
			else:
				event.client.setvar(self, 'muted', 0)
		if event.type == b3.events.EVT_CLIENT_SAY or event.type == b3.events.EVT_CLIENT_TEAM_SAY:
			event.data = "**********"
			if event.client.var(self, 'muted', 0).value == 1:
				self._adminPlugin.warnClient(event.client, 'You are not allowed to talk', None, False, '', 1)
			else:
				return False

	def cmd_mute(self, data, client=None, cmd=None):
		input = self._adminPlugin.parseUserCmd(data)
		if input:
			# input[0] is the player id
			sclient = self._adminPlugin.findClientPrompt(input[0], client)
			if not sclient:
			# a player matchin the name was not found, a list of closest matches will be displayed
			# we can exit here and the user will retry with a more specific player
				return False
		else:
			client.message('^7Invalid data, try !help mute')
			return False

		if not len(input[1]):
			client.message('^7Missing data, try !help mute')
			return False

		m = input[1]
		cursor = self.console.storage.query("SELECT * FROM muted_players WHERE client_id = '%s'" % sclient.cid);

		if m in ('on','1'):
			if cursor.rowcount  == 0:
				insert = self.console.storage.query("""INSERT INTO muted_players (client_id, admin_id, muted) VALUES ('%s', 0, 1)""" % sclient.cid)
				sclient.message('^3You are now muted, shut up!')
				client.message('^3%s ^1MUTED^3!' % sclient.exactName)
				sclient.var(self, 'muted', 0).value = 1
				sclient.setvar(self, 'muted', 1)
			elif cursor.rowcount > 0:
				data = cursor.getRow()
				if data['muted'] == 0:
					insert = self.console.storage.query("""UPDATE muted_players SET muted = 1 WHERE client_id = %s """ % sclient.cid)
					sclient.message('^3You are now muted, shut up!')
					client.message('^3%s ^1MUTED^3!' % sclient.exactName)
					sclient.var(self, 'muted', 0).value = 1
					sclient.setvar(self, 'muted', 1)
				else:
					client.message('Player %s is already muted' % sclient.exactName)
			else:
				client.message('Player %s is already muted' % sclient.exactName)
		elif m in ('off', '0'):
			if cursor.rowcount  == 0:
				client.message('Player %s is NOT muted' % sclient.exactName)
			elif cursor.rowcount > 0:
				data = cursor.getRow()
				if data['muted'] == 1:
					insert = self.console.storage.query("""UPDATE muted_players SET muted = 0 WHERE client_id = %s """ % sclient.cid)
					sclient.message('^3You have been unmuted!')
					client.message('^3%s ^2UNMUTED^3!' % sclient.exactName)
					sclient.var(self, 'muted', 0).value = 0
					sclient.setvar(self, 'muted', 0)
				else:
					client.message('Player %s is NOT muted' % sclient.exactName)
			else:
				client.message('Player %s is NOT muted' % sclient.exactName)
		else:
			client.message('^7Invalid or missing data, try !help mute')
