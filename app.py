from datetime import *
import time
import alert
import webscraper

#top level application

def runApp(name: str, email: str):
    while True:
        #time guard
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        print(currentTime)
        if currentTime.startswith("02:0"):
            #fetch data from webscraper
            url = "https://www.onthesnow.com/colorado/skireport"
            data = webscraper.request(url)

            #make decently formatted email body
            subject = "Daily Resort Summary"
            to = email
            today = date.today()
            d = today.strftime("%B %d, %Y")
            body = f"Hello {name}, below is the report for {d}.\n\n\n\n"
            for resort in data:
                conditions = data.get(resort)
                snowfall = conditions.get("Last Snowfall")
                base = conditions.get("Base Depth")
                trails = conditions.get("Open Trails")
                lifts = conditions.get("Open Lifts")
                body += f"{resort}:\n\tLast Snowfall: {snowfall}\n\tBase Depth: {base}\n\tOpen Trails: {trails}\n\tOpen Lifts: {lifts}\n\n"
            alert.sendMessage(subject, body, to)
            print("Alert Sent")
            time.sleep(10*60)


if __name__ == '__main__':
    runApp("Max", "mwhite7112@gmail.com")

