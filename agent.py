from mail_agent import load_mails, count_unread_mails, count_important_mails
from actions import show_mail_summary, show_important_mails, idle


def decide_action(unread_count,important_count):
    if important_count > 0:
        return "SHOW_IMPORTANT_MAILS"
    if unread_count > 0:
        return "SHOW_MAIL_SUMMARY"
    return "IDLE"


def act(action, mails):
    if action == "SHOW_IMPORTANT_MAILS":
        show_important_mails(mails)
    elif action == "SHOW_MAIL_SUMMARY":
        show_mail_summary(mails)
    elif action == "IDLE":
        idle()


def main():
    mails = load_mails()
    unread_count = count_unread_mails(mails)
    important_count = count_important_mails(mails)

    action = decide_action(unread_count,important_count)

    print(f"Unread mails: {unread_count}")
    print(f"Important mails: {important_count}")
    print(f"Agent decision: {action}")
    print()

    act(action, mails)


if __name__ == "__main__":
    main()
