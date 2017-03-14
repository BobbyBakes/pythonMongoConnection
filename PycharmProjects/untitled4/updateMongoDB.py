import json

from pymongo import MongoClient
import socket
import struct

# coll.drop()

client = MongoClient("mongodb://127.0.0.1:3001")
db = client.meteor
coll = db.locations

TCP_IP = '192.168.128.45'
TCP_PORT = 4444
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    data = s.recv(BUFFER_SIZE)
    id, x, y = struct.unpack('!idd', data)
    print id, x, y
    coll.find_one_and_update({'id': id}, {'$set': {'x': x, 'y': y}})
