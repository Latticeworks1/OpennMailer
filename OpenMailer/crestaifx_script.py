import time
import requests
from tkinter import Tk, Label, Entry, Text, Button

def add_email(email):
    # API endpoint URL for adding email
    url = "https://crestaifx.com/register_auth.php"

    # Headers (excluding Content-Length)
    headers = {
        "Host": "crestaifx.com",
        "Cookie": "_ga=GA1.2.1576816708.1685061166; _gid=GA1.2.523052675.1685061166; _gat=1; PHPSESSID=ebe2b8a7035203faf1ec47cd4500e19c",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://crestaifx.com",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryBjafANwaSJktIWH6",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://crestaifx.com/register.php",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    # Payload data
    payload = f'''------WebKitFormBoundaryBjafANwaSJktIWH6
Content-Disposition: form-data; name="under_reference"

910343
------WebKitFormBoundaryBjafANwaSJktIWH6
Content-Disposition: form-data; name="firstname"

1
------WebKitFormBoundaryBjafANwaSJktIWH6
Content-Disposition: form-data; name="lastname"

1
------WebKitFormBoundaryBjafANwaSJktIWH6
Content-Disposition: form-data; name="country"

Afghanistan
------WebKitFormBoundaryBjafANwaSJktIWH6
Content-Disposition: form-data; name="email"

{email.strip()}
------WebKitFormBoundaryBjafANwaSJktIWH6
Content-Disposition: form-data; name="phone"

1
------WebKitFormBoundaryBjafANwaSJktIWH6
Content-Disposition: form-data; name="pass"

1
------WebKitFormBoundaryBjafANwaSJktIWH6
Content-Disposition: form-data; name="register"


------WebKitFormBoundaryBjafANwaSJktIWH6--
'''

    # Calculate Content-Length dynamically
    content_length = 833 + len(email.strip())

    # Update the Content-Length header
    headers["Content-Length"] = str(content_length)

    # Send the POST request
    response = requests.post(url, headers=headers, data=payload)

    # Check the response status
    if response.status_code == 200:
        print(f"Email {email.strip()} submitted successfully.")
    else:
        print(f"Failed to submit email {email.strip()}. Status code: {response.status_code}")

def send_email(url, recipient_email, subject, message):
    headers = {
        'POST': '/admin/mail.php HTTP/2',
        'Host': 'crestaifx.com',
        'Cookie': '_ga=GA1.2.1576816708.1685061166; _gid=GA1.2.523052675.1685061166; _gat=1; PHPSESSID=ebe2b8a7035203faf1ec47cd4500e19c',
        'Content-Length': '66',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://crestaifx.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://crestaifx.com/admin/mail.php',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    payload = {
        'email': recipient_email,
        'sbj': subject,
        'mess1': message,
        'mess2': '',
        'mess3': '',
        'mess4': '',
        'mess5': '',
        'mail': ''
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        print(f"Email sent to {recipient_email}")
    else:
        print(f"Failed to send email to {recipient_email}. Status code: {response.status_code}")

def send_button_clicked():
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end-1c")

    add_email(recipient_email)
    time.sleep(1)  # Wait for 1 second before sending the email

    send_email(url, recipient_email, subject, message)

    recipient_entry.delete(0, 'end')
    subject_entry.delete(0, 'end')
    message_text.delete("1.0", "end")

if __name__ == "__main__":
    url = 'https://crestaifx.com/admin/mail.php'

    root = Tk()
    root.title("info@CrestAiFx.com Email Sender")

    recipient_label = Label(root, text="Recipient Email:")
    recipient_label.pack()
    recipient_entry = Entry(root)
    recipient_entry.pack()

    subject_label = Label(root, text="Subject:")
    subject_label.pack()
    subject_entry = Entry(root)
    subject_entry.pack()

    message_label = Label(root, text="Message:")
    message_label.pack()
    message_text = Text(root, height=10, width=50)
    message_text.pack()

    send_button = Button(root, text="Send Email", command=send_button_clicked)
    send_button.pack()

    root.mainloop()
