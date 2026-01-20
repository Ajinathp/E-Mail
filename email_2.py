import smtplib
import os
from email.message import EmailMessage
from datetime import datetime

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587

SENDER_EMAIL = os.environ.get("SMTP_USER")
SENDER_PASS = os.environ.get("SMTP_PASS")


def send_email(to_list, cc_list, files):
    current_date = datetime.now().strftime("%d-%m-%Y")
    file_names = [os.path.basename(f) for f in files]

    subject = f"{' , '.join(file_names)} - {current_date}"
    body = f"""Hello,

Please find the attached reports for dated {current_date}.

Regards,
Shivani
"""

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(to_list)
    msg["Cc"] = ", ".join(cc_list)
    msg["Subject"] = subject
    msg.set_content(body)

    for f in files:
        if os.path.exists(f):
            with open(f, "rb") as fp:
                data = fp.read()
            msg.add_attachment(
                data,
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(f),
            )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASS)
        server.login("ajinathp@outlook.com", "Adhi@123#")
        server.send_message(msg)

    print("Email sent successfully.")


if __name__ == "__main__":
    files1 = [
        r"D:\k\MD_Dashboards_20-01-2026.xlsx",
        r"D:\k\SR Snapshot_20-01-2026.xlsx"
    ]

    send_email(
        to_list=["ajinathp@gmail.com", "ajinathp@outlook.com"],
        cc_list=["b.dnyaneshwar@gmail.com"],
        files=files1
    )
