import json
import os

from pymongo import MongoClient
import socket
import struct


client = MongoClient("mongodb://127.0.0.1:3001")
db = client.meteor
coll = db.locations

# coll.drop()
# os.sys.exit()
TCP_IP = '192.168.128.45'
TCP_PORT = 4444
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


def getCar(data, index):
    return struct.unpack_from('!idd', data, 4 + index * 20)

def getNumberOfCars(data):
    return struct.unpack_from('!i', data)

while True:
    data = s.recv(BUFFER_SIZE)
    for index in range(0, getNumberOfCars(data)[0]):
        id, x, y = getCar(data, index)
        print id, x, y
        coll.find_one_and_update({'id': id}, {'$set': {'x': x, 'y': y}})



