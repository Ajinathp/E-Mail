import win32com.client as win32
import os
from datetime import datetime

def send_email_via_outlook(to, cc, files):
    """
    Send email with multiple attachments via Outlook.
    - to: recipient email (string)
    - cc: cc email(s) (string, comma-separated if multiple)
    - files: list of file paths to attach
    """

    # Current date in DD-MM-YYYY format
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Build subject line from file names + current date
    file_names = [os.path.basename(f) for f in files]
    subject = f"{' , '.join(file_names)} - {current_date}"

    # Build body with current date
    body = f"Hello,\n\nPlease find the attached reports for dated {current_date}.\n\nRegards,\nShivani"

    # Create Outlook mail item
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = to
    mail.CC = cc
    mail.Subject = subject
    mail.Body = body

    # Attach all files
    for f in files:
        if os.path.exists(f):
            mail.Attachments.Add(f)

    mail.Send()
    print(f"Email sent successfully to {to} with CC {cc} and files {file_names}")


# ---------------- Example Usage ----------------

if __name__ == "__main__":
    # Example 1: Two files in one email
    files1 = [
        r"D:\\k\\MD_Dashboards_20-01-2026.xlsx",
        r"D:\\k\\SR Snapshot_20-01-2026.xlsx"
    ]
    send_email_via_outlook(
        to="ajinathp@gmail.com;ajinathp@outlook.com",
        cc="b.dnyaneshwar@gmail.com",
        files=files1
    )

    # Example 2: One file in another email
    files2 = [
        r"D:\\k\\MIS_Reports_20-01-2026y.xlsx"
    ]
    send_email_via_outlook(
        to="pajinath@ymail.com;b.dnyaneshwar@gmail.com",
        cc="ajinathp@gmail.com;ajinathp@outlook.com",
        files=files2
    )
