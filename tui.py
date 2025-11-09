from textual.app import App, ComposeResult
from textual.widgets import Input
from textual.app import App, ComposeResult, Screen
from textual.widgets import Static, Input, Label, Button, Link, Header
from textual.containers import Container, Horizontal, VerticalScroll, Vertical
from art import text2art
from main import main
import asyncio
class InputApp(App):
    CSS_PATH = "kahoot.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        ascii_art = text2art("SSHoot!",)
        yield Label(ascii_art, id="land_label")
        yield Input(placeholder="Game PIN", id="game_pin_input")
    def on_input_submitted(self, event: Input.Submitted) -> None:
        game_pin = int(event.value)
        print("yooooo")
        asyncio.create_task(main(game_pin))
    def on_mount(self) -> None:
        self.title = "SSHoot!"

if __name__ == "__main__":
    app = InputApp()
    app.run()