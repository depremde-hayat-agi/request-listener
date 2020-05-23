import json
import hashlib


class Message:
    def __init__(self, lat, long, distance_to_orig, source_id, chain_distance=5):
        self.lat = lat
        self.long = long
        self.source_id = source_id
        self.chain_distance = chain_distance
        self.message = {'original_lat': self.lat,
                        'original_long': self.long,
                        'id': source_id,
                        'seen_devices': []}
        self.hash_key = None

    def chain(self, device):
        if self.chain_distance >= len(self.message['seen_devices']):
            return self
        else:
            device_dict = {'device_lat': device.lat,
                           'device_long': device.long}
            self.message['seen_devices'].append(device_dict)

    def hash(self):
        m = json.dumps(self.message, sort_keys=True)
        self.hash_key = hashlib.sha224(m).hexdigest()
