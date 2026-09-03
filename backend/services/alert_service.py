from datetime import datetime
from datetime import timedelta

from backend.services.alert_state import (
    last_alert_times
)

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SENDER_EMAIL = " "
SENDER_PASSWORD = " "

RECEIVER_EMAIL = " "


def send_alert(
    machine_id,
    probability,
    root_causes,
    recommendations
):

    cooldown_minutes = 1

    current_time = datetime.now()

    if machine_id in last_alert_times:

        last_sent = last_alert_times[machine_id]

        elapsed = current_time - last_sent

        if elapsed < timedelta(minutes=cooldown_minutes):

            remaining = (
                timedelta(minutes=cooldown_minutes)
                - elapsed
            )

            print(
                f"[ALERT SKIPPED] "
                f"Machine {machine_id} | "
                f"{remaining.seconds}s remaining"
            )

            return False

    subject = (
        f"⚠ Predictive Maintenance Alert "
        f"(Machine {machine_id})"
    )

    body = f"""
Machine ID: {machine_id}

Failure Probability:
{round(probability * 100, 2)}%

Root Causes:
{chr(10).join(root_causes)}

Recommendations:
{chr(10).join(recommendations)}
"""

    msg = MIMEMultipart()

    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject

    msg.attach(
        MIMEText(body, "plain")
    )

    try:

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            SENDER_EMAIL,
            SENDER_PASSWORD
        )

        server.send_message(msg)

        server.quit()

        last_alert_times[machine_id] = current_time

        print(
            f"[ALERT SENT] Machine {machine_id}"
        )

        return True

    except Exception as e:

        print(
            f"[ALERT ERROR] {e}"
        )

        return False