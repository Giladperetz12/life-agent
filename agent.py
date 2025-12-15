from calendar_agent import find_overlaps, load_events
from mail_agent import load_mails, count_unread_mails, count_important_mails
from actions import show_mail_summary, show_important_mails, show_calendar_conflicts, idle
import time

AGENT_INTERVAL_SECONDS = 10


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
    else:
        idle()


def run_agent_cycle():
    mails = load_mails()
    events = load_events()

    unread_count = count_unread_mails(mails)
    important_count = count_important_mails(mails)
    conflicts = find_overlaps(events)

    action = decide_action(
        unread_count=unread_count,
        important_count=important_count,
        conflicts=conflicts
    )

    print("----- Agent Cycle -----")
    print(f"Unread mails: {unread_count}")
    print(f"Important mails: {important_count}")
    print(f"Calendar conflicts: {len(conflicts)}")
    print(f"Agent decision: {action}\n")

    act(action, mails, conflicts)


def main():
    print("Life Agent started. Running every 10 seconds.\n")
    try:
        while True:
            run_agent_cycle()
            print("\nAgent sleeping...\n")
            time.sleep(AGENT_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nAgent stopped by user.")


if __name__ == "__main__":
    main()
