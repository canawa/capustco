import sqlite3 as sq

cars = ('Запорожец', 10000)

def readImage(n):
	try:
		with open(f'images/{n}.png', 'rb') as f:
			return f.read()
	except Exception as e:
		print(e)
		return False


with sq.connect('cars.db') as con:
	con.row_factory = sq.Row
	cur = con.cursor()

	cur.execute('CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY, image BLOB)')


	with open('cars.sql', 'w') as f:
		for sql in con.iterdump():
			f.write(sql + '\n')