import json
import datetime
import random
import asyncio
import logging
import paho.mqtt.client as mqtt


class Sensor:
    def __init__(self, id: str, range: tuple, interval_ms: int):
        self.id = id
        self.range = range
        self.interval_ms = interval_ms

    async def generate(self, mqtt_client: mqtt.Client, topic: str):
        while True:
            data = {
                "id": self.id,
                "dt": datetime.datetime.utcnow().isoformat(),
                "value": random.randint(*self.range),
            }

            payload = json.dumps(data, default=str)

            logging.info(f"{topic}: {payload}")

            mqtt_client.publish(topic, payload)
            await asyncio.sleep(self.interval_ms / 1000)
