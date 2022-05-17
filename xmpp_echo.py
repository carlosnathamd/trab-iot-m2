import asyncio, logging, json, os, sys, inspect;
from slixmpp import ClientXMPP;

CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())));
print("[*] DIRECTORY: ", CURRENTDIR);

class EchoBot(ClientXMPP):
	def __init__(self, jid, password):
		ClientXMPP.__init__(self, jid, password);
		self.add_event_handler("Iniciar sessão", self.session_start);
		self.add_event_handler("Menssagem", self.message);

	def session_start(self, event):
		print("[-] Sessão Iniciada");
		self.send_presence();
		self.get_roster();

	def message(self, msg):
		printf("[|] Mensagem: ", msg["body"], " por ", msg["from"]);
		if msg['type'] in ('chat', 'normal'):
			print("[+] Sera respondido.");
			msg.reply("Recebi: " + msg["body"]).send();

if __name__ == '__main__':
	#logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s %(message)s");
	CONFIG = json.loads(open(CURRENTDIR + "/data/config.json").read());
	xmpp = EchoBot(CONFIG['username'], CONFIG['password']);
	xmpp.connect();
	xmpp.process();

