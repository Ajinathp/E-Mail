import smtplib, os
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email_smtp(to, cc, files):
    current_date = datetime.now().strftime("%d-%m-%Y")
    file_names = [os.path.basename(f) for f in files]
    subject = f"{' , '.join(file_names)} - {current_date}"
    body = f"Hello,\n\nPlease find the attached reports for {current_date}.\n\nRegards,\nShivani"

    msg = MIMEMultipart()
    msg['From'] = "ajinathp@outlook.com"
    msg['To'] = 'ajinathp@gmail.com'
    msg['Cc'] = cc
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    for f in files:
        if os.path.exists(f):
            with open(f, "rb") as fp:
                part = MIMEApplication(fp.read(), Name=os.path.basename(f))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(f)}"'
                msg.attach(part)

    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login("your_outlook_email@example.com", "your_password_or_app_password")
        server.send_message(msg)

    print(f"Email sent successfully to {to} with CC {cc} and files {file_names}")
