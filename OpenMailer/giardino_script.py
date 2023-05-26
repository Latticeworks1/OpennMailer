import tkinter as tk
import requests
import time
from art import text2art

def send_request():
    base_url = "http://www.giardino.it/admin/mail.php?url="
    headers = {
        "Host": "www.giardino.it",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Referer": "http://www.giardino.it/admin/mail.php?url=http://www.penis.com",
        "Cookie": "_fbp=fb.1.1685074658364.1896472086; __utma=33950519.141218896.1685074659.1685074659.1685074659.1; __utmc=33950519; __utmz=33950519.1685074659.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=33950519.1.10.1685074659; valid_token=741b0c2f003905d435371991c967e63a"
    }
    email = email_entry.get()
    url = url_entry.get()
    full_url = base_url + url

    data = {
        "email": email,
        "name": "Beste",
        "code": "5754",
        "invio": "Send memo"
    }

    response = requests.post(full_url, headers=headers, data=data)

    if response.status_code == 200:
        success_message = text2art("Success!")
        animate_success_message(success_message)
    else:
        success_message = "Request failed. Please try again."

    response_text.configure(state='normal')
    response_text.delete(1.0, tk.END)
    response_text.insert(tk.END, success_message)
    response_text.configure(state='disabled')

def animate_success_message(success_message):
    scroll_width = 50  # Width of the scrolling window
    scroll_delay = 0.001  # Delay between each scroll step

    # Pad the success message to ensure smooth scrolling
    padded_message = " " * scroll_width + success_message + " " * scroll_width
    message_length = len(padded_message)

    for i in range(message_length - scroll_width + 1):
        animated_message = padded_message[i:i + scroll_width]
        response_text.configure(state='normal')
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, animated_message)
        response_text.configure(state='disabled')
        window.update()
        time.sleep(scroll_delay)

# Create the main window
window = tk.Tk()
window.title("Automated Request")
window.geometry("400x300")

# Create labels
email_label = tk.Label(window, text="Email:")
email_label.pack()
url_label = tk.Label(window, text="URL:")
url_label.pack()

# Create entry fields
email_entry = tk.Entry(window)
email_entry.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create a button
send_button = tk.Button(window, text="Send Request", command=send_request)
send_button.pack()

# Create a text area for displaying the response
response_text = tk.Text(window, height=10, state='disabled')
response_text.pack()

# Start the main event loop
window.mainloop()
