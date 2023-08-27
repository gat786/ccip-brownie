import json

receiver_abi = []
sender_abi = []

with open("abi/Receiver.json") as f:
    receiver_abi = f.read()
    receiver_abi = json.loads(receiver_abi)
    
with open("abi/Sender.json") as f:
    sender_abi = f.read()
    sender_abi = json.loads(sender_abi)


