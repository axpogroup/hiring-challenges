import json
import asyncio
import logging
import datetime
import random
import paho.mqtt.client as mqtt
from settings import get_settings


class Generator:
    def __init__(self):
        self.settings = get_settings()
        self.mqtt_client = mqtt.Client()
        self.topic = "energy_flow_in_and_out_switzerland_electricity_per_second"

    def generate_data(self):
        data = {
            "Datetime": datetime.datetime.utcnow().isoformat(),
            "AT_CH_kWh": random.randint(0, 2198)/24/60/60*1000,
            "DE_CH_kWh": random.randint(0, 6246)/24/60/60*1000,
            "FR_CH_kWh": random.randint(0, 23635)/24/60/60*1000,
            "IT_CH_kWh": random.randint(0, 3436)/24/60/60*1000,
            "CH_AT_kWh": random.randint(0, 1681)/24/60/60*1000,
            "CH_DE_kWh": random.randint(0, 5246)/24/60/60*1000,
            "CH_FR_kWh": random.randint(0, 4451)/24/60/60*1000,
            "CH_IT_kWh": random.randint(0, 5399)/24/60/60*1000,
            "Nettoimport": random.randint(-8676, 22636)/24/60/60*1000
        }
        return data

    async def generate(self):
        logging.basicConfig(level=self.settings.logging_level)

        if self.settings.mqtt.username:
            self.mqtt_client.username_pw_set(
                self.settings.mqtt.username, self.settings.mqtt.password
            )

        self.mqtt_client.connect(self.settings.mqtt.host, self.settings.mqtt.port)

        while True:
            payload = json.dumps(self.generate_data(), default=str)
            self.mqtt_client.publish(self.topic, payload)

            logging.info(f"{self.topic}: {payload}")
            await asyncio.sleep(1)
