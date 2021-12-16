import requests
from bs4 import BeautifulSoup

def request(url: str) -> dict:
    page = requests.get(url)

    if not page.ok: #catch errors
        return {"Error fetching data": page.status_code}

    # get page HTML
    soup = BeautifulSoup(page.content, "html.parser")
    
    #parsing for specific data
    resorts = ['Eldora Mountain Resort', 'Winter Park', 'Copper Mountain', 
                'Steamboat', 'Arapahoe Basin Ski Area']
    data = {}
    table = soup.find("table", class_="styles_table__2G-4E")
    results = table.find_all("tr", {"class":["styles_row__wYlY6 styles_other__eO-mR",
                                            "styles_row__wYlY6"]})
    
    #loop thru table HTML and add to the data dict
    for result in results:
        resort = result.find("span", class_="h4 styles_h4__318ae")
        if resort.text not in resorts: continue
        conditionsRaw = result.find_all("td")
        conditions = []
        for entry in conditionsRaw:
            field = entry.find("span", class_="h4 styles_h4__318ae")
            conditions.append(field.text)

        #change conditions[0] to have date included
        snowfallDate = conditionsRaw[0].find("time")
        snowfall = conditions[0] + " on " + snowfallDate.text

        data[resort.text] = {
            "Last Snowfall": snowfall,
            "Base Depth": conditions[1],
            "Open Trails": conditions[2],
            "Open Lifts": conditions[3]
        }
    return data

if __name__ == '__main__':
    print(request("https://www.onthesnow.com/colorado/skireport"))
