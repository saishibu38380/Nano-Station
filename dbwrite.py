import pymysql

def todb (data):

	conn =pymysql.connect(database="OceanNet",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO nanostation(signalstrength,noisefloor,ccq,distance,pos) VALUES(%(signalstrength)s,%(noisefloor)s,%(ccq)s,%(distance)s,%(pos)s);",data)
	conn.commit()
	conn.close()
