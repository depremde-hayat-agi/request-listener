from collections import defaultdict


class Device:
    def __init__(self, id, lat=None, long=None):
        self.messages_seen = set()
        self.lat = lat
        self.long = long
        self.to_push_message = []
        self.message_sent_devices = defaultdict(set)
        self.id = id

    def receive(self, message):
        if message not in self.messages_seen:
            self.messages_seen.add(self.hash(message))
            self.to_push_message.append(message)
        else:
            pass

    def send(self, available_devices, message):
        for d in available_devices:
            d.receive(message)
            self.message_sent_devices[message.hash_key].add(d.id)






