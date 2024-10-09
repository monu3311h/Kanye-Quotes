# import requests
#
# response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
# data = response.json()
# print(data['longitude'])

# from tkinter import *
# import requests
#
# def get_a_kanye_joke():
#     response = requests.get(url="https://api.kanye.rest")
#     data = response.json()
#     canvas.itemconfig(my_text, text=data['quote'])
#
#
# window = Tk()
# window.config(padx=100, pady=100)
# canvas = Canvas(width=300, height=414)
# bg_image = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image = bg_image)
# my_text = canvas.create_text(150, 150, text="",width=250, font=("Arial", 15))
# canvas.grid(column=1, row=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_btn = Button(image=kanye_img, highlightthickness=0, command=get_a_kanye_joke)
# kanye_btn.grid(column=1, row=2)
#
# window.mainloop()


# import requests
# from datetime import datetime
# my_lat = 26.912434
# my_long = 75.787270
#
#
# def is_iss_overhead():
#     response = requests.get("http://api.open-notify.org/iss-now.json")
#
#     data = response.json()
#
#     iss_latitude = float(data['iss_position']['latitude'])
#     iss_longitude = float(data['iss_position']['longitude'])
#
#     if my_lat-5<= iss_latitude <= my_long+5 and my_long-5<= iss_longitude<= my_long+5:
#         return True
#
#
# parameters = {
#     "lat": my_lat,
#     "lng": my_long,
#     'formatted': 0
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters )
# response.raise_for_status()
#
# data = response.json()
#
# def is_night():
#     sunrise = data['results']['sunrise']
#     sunset = data['results']['sunset']
#     time_now = datetime.now().hour
#     if time_now >= sunset and time_now <= sunrise:
#         return True
# import smtplib
# my_email = "myfake116@gmail.com"
# password = "MyFake$789"
#
# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="fakeid78@yahoo.com", msg="Hello")
# connection.close()