from pyrogram import Client
from pyrogram.raw import functions
import sys, time
import asyncio
import configparser


if 1 > len(sys.argv) :
	print('NoSys');
	exit();

ses    = sys.argv[1].split('.')[0];

config = configparser.ConfigParser()
config.read("jello.ini")

api_id       = config['@VIP_KOPRA']['27530560'];
api_hash = config['@VIP_KOPRA']['c51c73887508a3a722d769ceae4fefd4'];


try :
	app	     = Client(f"sessions/{ses}",api_id=api_id, api_hash=api_hash);
	connect  = app.connect();
	try:
		#while True:
		app.invoke(functions.account.UpdateStatus(
		offline=False
		));
	except Exception as dt :
		print(f"dt _ {dt}");
except Exception as dp :
	print(f"dp _ {dp}");
#app.run();
