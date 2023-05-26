# OpenMailer
Open Mailer

Open Mailer is a Python program that enables users to bypass admin login and send emails using a graphical user interface (GUI). It leverages the requests library for making HTTP requests and provides a simple framework for sending mail via proxy domain.

Features

	•	Easy email sending: Open Mailer simplifies the process of sending emails by providing a user-friendly GUI.
	•	HTTP POST request: The program utilizes the requests.post() function to send the email data as a POST request to the specified URL.
	•	Response display: After sending the email, the program displays the response message received from the server.

Note: Open Mailer is designed to demonstrate potential security vulnerabilities and should not be used for malicious purposes. Sending emails without proper authentication is a violation of ethical and legal standards. Use this program responsibly and with the consent of the website owner.

Requirements

To run Open Mailer, ensure you have the following dependencies installed:

	•	Python 3.x
	•	requests library
	•	tkinter library (usually included with Python)
Usage

	1.	Clone the repository or download the source code.
	2.	Install the required dependencies using the following command:

pip install requests


	3.	Run the program by executing the open_mailer.py file:

python open_mailer.py


	4.	The program window will open, allowing you to choose the site from which you want to send the email.
	5.	Enter the necessary information for the email (e.g., recipient, subject, body) in the provided fields.
	6.	Click the “Send” button to initiate the email sending process.
	7.	If the email is sent successfully (status code 200), a success message will be displayed in an animated scrolling manner.
	8.	If the email sending fails, an error message will be displayed.

Customization

You can customize the program according to your needs. Here are a few suggestions:

	•	Modify the full_url variable to point to a different API or endpoint if necessary.
	•	Adjust the scroll_width and scroll_delay variables in the animate_success_message() function to change the animation speed and scrolling behavior.

Contributing

Contributions to Open Mailer are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
