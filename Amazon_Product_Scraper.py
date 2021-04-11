# This program allows the user to enter a URL from an Amazon's product page
# It will grab all the names of the products, the prices of each product, and the link to each product
# The grabbed information will neatly displayed in a csv file (E.g Microsoft Excel)
# By: Eric Qian

from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import build_opener 


# URl to web scrape from
# Use search bar in Amazon to find the product you want, replace the URL below, only works with Amazon.com
# This URL grabs iPhone information, but you can enter whatever you want
page_url = "https://www.amazon.com/s?k=toys&ref=nb_sb_noss_1"

# opens the connection and downloads html page from url
opener = build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
uClient = opener.open(page_url)

# parses html into a soup data structure to traverse html
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the Amazon.com store page, stores it into an array, reference by index
containers = page_soup.findAll("div", {"class": "a-section a-spacing-medium"})

# name the output file to write to local disk, comma separated values file
out_filename = "BitCamp2021Hack.csv"

# header of csv file to be written
headers = "Product Name, Price, URL Link \n"

# opens file and can overwrite existing files, writes headers
f = open(out_filename, "w+")
f.write(headers)

# loops over each product and grabs the name and price of each product
for container in containers:

    # finds all link tags "a" from within the first div, stores into an array
    title_name = container.findAll("a", {"class": "a-link-normal a-text-normal"})

    # finds the name of the product and stores it into a variable, displays text
    try:
        product_name = title_name[0].span.text
    except:
        prduct_name = "Does not exist."

    # finds all "span" tags where the price is displayed
    price = container.findAll("span", {"class": "a-offscreen"})

    # finds the price of the product and stores it into a variable, displays text
    try:
        price_number = price[0].text
    except:
        price_number = "No Price Indicated."

    # find all "div" tags where there is a hyperlink
    link_to_website = container.findAll("div", {"class": "a-section a-spacing-none a-spacing-top-small"})

    # finds the link for the product and stores it into a variable
    try:
        link = link_to_website[0].h2.a["href"]
    except:
        try:
            link = link_to_website[0].div.a["href"]
        except:
            link = "Link Doesn't Exist."

    # prints the dataset to console, for testing purposes
    print("Name: " + product_name + "\n")
    print("Price: " + price_number + "\n")
    print("Link:" + link + "\n")

    # writes to the csv file with the information found
    # some products have commas in the name, since CSV files are separated by commas, this will separate the name in the file which will become disorganized
    f.write(product_name.replace(",", "") + ", " + price_number + ", " + "https://www.amazon.com" + link + "\n")

f.close()  # Close the file
