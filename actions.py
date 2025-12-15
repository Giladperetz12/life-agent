def show_mail_summary(mails):
    print("📬 Daily Mail Summary")
    for mail in mails:
        status = "UNREAD" if not mail.get("is_read", False) else "READ"
        subject = mail.get("subject", "No subject")
        print(f"- {subject} [{status}]")


def show_important_mails(mails):
    print("⭐ Important Emails")
    for mail in mails:
        if mail.get("is_important", False):
            subject = mail.get("subject", "No subject")
            print(f"-{subject}")


def idle():
    print("No action needed. Agent is idle.")
