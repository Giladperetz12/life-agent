import json
from pathlib import Path


def load_malis():
    path = Path("data/mails.json")
    with path.open("r", encoding="utf-8") as f:
        mails = json.load(f)
    return mails


def count_unread_mails(mails):
    unread_count = 0
    for mail in mails:
        if not mail.get("is_read", False):
            unread_count += 1
    return unread_count


def decide_action(unread_count):
    if unread_count > 0:
        return "SHOW_MAIL_SUMMARY"
    else:
        return "IDLE"


def show_mails_summary(mails):
    print("Daily mail summary:")
    for mail in mails:
        status = "UNREAD" if not mail.get("is_read", False) else "READ"
        print(f"- {mail.get('subject', 'No subject')} [{status}]")

def act(action, mails):
    if action == "SHOW_MAIL_SUMMARY":
        show_mails_summary(mails)
    elif action == "IDLE":
        print("No action needed")


def main():
    malis = load_malis()
    unred_count = count_unread_mails(malis)
    action = decide_action(unred_count)
    print(f"Unread mails : {unred_count}")
    print(f"Agent decision : {action}")
    print()
    act(action, malis)


if __name__ == '__main__':
    main()
