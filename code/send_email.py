import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "productioniles@gmail.com"
password = "duvzyggazesiwbiv"

def send_email(link, transcript, title, poster, receiver_email, show):

    # Setup the MIME (Multipurpose Internet Mail Extensions)
    message = MIMEMultipart("alternative")
    message["Subject"] = "Snapchat Show Tracker"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""\
  Hello, a new episode is posted!

  show : {show}
  
  link : {link}

  episode title : {title} 

  transcript : {transcript}

  thumbnail : {poster}
  """

    html = f"""\
  <html>
    <body>
      <p>Hello, a new episode is posted!<br><br>
        show : {show}<br><br>
        link : {link}<br><br>
        episode title : {title}<br><br>
        transcript : {transcript}<br><br>
        thumbnail :<br>
        <img src="{poster}" alt="Description of Image"> <br>
      </p>
    </body>
  </html>
  """

    # Convert these to MIMEText objects and add them to the MIMEMultipart message
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    # Connect to the server and send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
