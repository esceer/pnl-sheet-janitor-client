"""
This is an android client for the pnl-sheet-janitor service.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from pnl_connect.clients.janitor_client import JanitorClient


class PnLConnect(toga.App):

    def startup(self):
        self._janitor_client = JanitorClient()

        main_box = toga.Box(style=Pack(direction=COLUMN))

        title_label = toga.Label(
            'P&L Spreadsheet Connect',
            style=Pack(padding=(5, 2))
        )

        title_box = toga.Box(style=Pack(direction=ROW, padding=5))
        title_box.add(title_label)

        summary_button = toga.Button(
            'P&L Summary',
            on_press=self.get_pnl_summary,
            style=Pack(padding=5)
        )

        main_box.add(title_box)
        main_box.add(summary_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def get_pnl_summary(self, widget):
        summary = self._janitor_client.fetch_summary()
        self.main_window.info_dialog(
            f'P&L Summary',
            f'P&L: {summary["pnl"]:n} Ft\nCar, bike: {summary["car-bike"]:n} Ft\nSavings: {summary["savings"]:n} Ft\nBalance: {summary["balance"]:n} Ft'
        )


def main():
    return PnLConnect()
