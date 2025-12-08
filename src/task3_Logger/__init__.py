from datetime import datetime
def multiply(a: int, b: int) -> int:
    return a * b

def timestamp() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

class Logger:

    def __init__(self):
        self.entries: list[dict[str, str]] = []

    def log(self, message: str, level: str = "INFO") -> None:
        self.entries.append({
            "message": message,
            "level": level,
            "timestamp": timestamp()
        })

    def get_logs(self) -> list[dict]:
        return self.entries

    def search(self, keyword: str = "", field: str = "message") -> list[dict]:
        if str != "" and field == "message":
            return [obj for obj in self.entries if keyword in obj["message"]]
        if str != "" and field == "level":
            return [obj for obj in self.entries if keyword in obj["level"]]



