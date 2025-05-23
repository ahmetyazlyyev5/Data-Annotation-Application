"""
Solution to the Google Docs challenge from the Data Annotation Application
"""

import urllib.request
from bs4 import BeautifulSoup


# DOC_ID = "2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq"
DOC_ID = "2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z"
url    = f"https://docs.google.com/document/d/e/{DOC_ID}/pub?output=html"
html   = urllib.request.urlopen(url).read()

soup  = BeautifulSoup(html, "html.parser")
rows  = soup.find("table").find_all("tr")[1:] # skip table header

# Build dictionary and record max x and y
# key = (x, y)
# value = char
points = {}
max_x = 0
max_y = 0
for row in rows:
    cells = row.find_all("td")
    x = int(cells[0].text)
    char = cells[1].text.strip()
    y = int(cells[2].text)
    points[(x, y)] = char
    if x > max_x: max_x = x
    if y > max_y: max_y = y

# Render the message
for y in range(max_y, -1, -1):
    line = []
    for x in range(max_x + 1):
        line.append(points.get((x, y), " ")) # empty space if no char
    print("".join(line))
