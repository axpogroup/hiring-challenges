import asyncio
from generator import Generator

if __name__ == "__main__":
    generator = Generator()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(generator.generate())
