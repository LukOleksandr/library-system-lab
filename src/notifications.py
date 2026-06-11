from interfaces import Notifier


class EmailAlert(Notifier):
    def __init__(self, email: str):
        self.email = email

    def update(self, message: str) -> None:
        print(
            f"EmailAlert: Надіслано лист на {self.email}: {message}"
        )


class ConsoleNotifier(Notifier):
    def update(self, message: str) -> None:
        print(f"ConsoleNotifier: {message}")
