from calender_agent import find_overlaps, load_events
from mail_agent import load_mails, count_unread_mails, count_important_mails
from actions import show_mail_summary, show_important_mails, show_calendar_conflicts, idle


def decide_action(unread_count, important_count, conflicts):
    if conflicts:
        return "SHOW_CONFLICTS"
    if important_count > 0:
        return "SHOW_IMPORTANT_MAILS"
    if unread_count > 0:
        return "SHOW_MAIL_SUMMARY"
    return "IDLE"


def act(action, mails, conflicts):
    if action == "SHOW_CONFLICTS":
        show_calendar_conflicts(conflicts)
    elif action == "SHOW_IMPORTANT_MAILS":
        show_important_mails(mails)
    elif action == "SHOW_MAIL_SUMMARY":
        show_mail_summary(mails)
    elif action == "IDLE":
        idle()


def main():
    mails = load_mails()
    events = load_events()

    unread_count = count_unread_mails(mails)
    important_count = count_important_mails(mails)
    conflicts = find_overlaps(events)
    action = decide_action(unread_count, important_count, conflicts)

    print(f"Unread mails: {unread_count}")
    print(f"Important mails: {important_count}")
    print(f"Calender conflicts: {len(conflicts)}")
    print(f"Agent decision: {action}")
    print()

    act(action, mails, conflicts)


if __name__ == "__main__":
    main()
