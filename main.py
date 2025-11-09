import asyncio
from kahoot import KahootClient
from kahoot.packets.server.question_start import QuestionStartPacket

async def question_start(packet: QuestionStartPacket):
    packet = list(vars(packet).items())
    print(f"Question started: {packet}")

async def main(game_pin: int):
    client = KahootClient()
    client.on("question_start", question_start)
    await client.join_game(game_pin=game_pin, username='your_username')