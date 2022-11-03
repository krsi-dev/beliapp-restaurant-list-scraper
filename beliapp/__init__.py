import csv
import requests

def scrape(username=None) -> str:

    # Get user data using username
    response = requests.get("https://beli.cleverapps.io/api/user/member", params={
        "username__iexact": username
    })
    
    # Check results
    data = response.json()["results"]

    # If no result return None
    if not data:
        return None
    
    # Get the first result
    # id, first_name, last_name, created_dt, username, photo, urls
    user = data[0]

    # Get user list
    response = requests.get(f"https://beli.cleverapps.io/api/rank-list/{user['id']}")
    
    data = response.json()

    with open(f"{username}.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f, delimiter=",")

        headers = ["name", "status", "location", "price", "score", "cuisines"]
        writer.writerow(headers)

        
        for dat in data:
            business_name = dat["business__name"]
            business_status = dat["business__status"]
            business_score = dat["score"]

            business_location = " ".join([
                dat["business__neighborhood"] or "",
                dat["business__city"] or "",
                dat["business__country"] or ""
            ])

            business_cuisines = " ".join(dat["business__cuisines"])
            business_price = "".join(["★" for x in range(dat["business__price"] or 0)])
            
            writer.writerow([
                business_name,
                business_status,
                business_location,
                business_price,
                business_score,
                business_cuisines
            ])

        f.close()
