from textual.app import App, ComposeResult
from textual.widgets import Input
from textual.app import App, ComposeResult, Screen
from textual.widgets import Static, Input, Label, Button, Link, Header
from textual.containers import Container, Horizontal, VerticalScroll, Vertical
from art import text2art
class InputApp(App):
    CSS_PATH = "kahoot.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        ascii_art = text2art("SSHoot!",)
        yield Label(ascii_art, id="land_label")
        yield Input(placeholder="Game PIN", id="game_pin_input")
    def on_mount(self) -> None:
        self.title = "SSHoot!"

if __name__ == "__main__":
    app = InputApp()
    app.run()