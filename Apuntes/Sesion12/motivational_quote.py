import datetime as dt
import smtplib
import random

# Poder enviar una cita al azar por correo comprobando el dia en que estamos.

with open("quotes.txt") as motivational:
    quotes_list = [line.strip() for line in motivational.readlines()]  # Guardo las citas sin saltos de línea

now = dt.datetime.now()
dia_semana = now.weekday()
quote = []

if dia_semana == 1:
    quote = random.choice(quotes_list)

my_email = "pruebapython83@gmail.com"
password = "password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="pruebapython84@yahoo.com",
                        msg=f"Subject:quote of day\n\n{quote}")
