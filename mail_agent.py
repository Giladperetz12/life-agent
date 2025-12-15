import json
from pathlib import Path


def load_mails():
    path = Path("data/mails.json")
    with path.open("r", encoding="utf-8") as f:
        mails = json.load(f)
    if not mails:
        print("No mails found.")
        mails = []
    return mails

def count_unread_mails(mails):
    return sum(1 for mail in mails if not mail.get("is_read", False))


def count_important_mails(mails):
    return sum(1 for mail in mails if mail.get("is_important", False))
