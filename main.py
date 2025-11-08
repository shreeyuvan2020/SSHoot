import asyncio
from kahoot import KahootClient
from kahoot.packets.server.question_start import QuestionStartPacket

async def question_start(packet: QuestionStartPacket):
    print(f"Question started: {packet}")

async def main():
    client = KahootClient()
    client.on("question_start", question_start)
    await client.join_game(game_pin=3850352, username='your_username')

# Run the main function
asyncio.run(main())