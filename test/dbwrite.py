import pymysql

def todb (data):

	conn =pymysql.connect(database="OceanNet",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO seatrail(ss,nf,ccq,d,pos,lat,lon,mode,dir) VALUES(%(ss)s,%(nf)s,%(ccq)s,%(d)s,%(pos)s,%(lat)s,%(lon)s,%(mode)s,%(dir)s);",data)
	conn.commit()
	conn.close()
