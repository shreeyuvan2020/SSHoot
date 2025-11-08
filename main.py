import asyncio
from kahoot import KahootClient
from kahoot.packets.server.question_start import QuestionStartPacket
async def question_start(packet: QuestionStartPacket):
    image_url = packet.get("nextGameBlockData")
    print(image_url)
async def main():
    client = KahootClient()
    client.on("question_start", question_start)
    game_pin = input("Enter the game PIN: ")
    await client.join_game(game_pin=game_pin, username='your_username')
asyncio.run(main())