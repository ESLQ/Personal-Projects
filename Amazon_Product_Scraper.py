# This program allows the user to enter a URL from an Amazon's product page
# It will grab all the names of the products and the prices of each product
# It will neatly display the information in a csv file
# By: Eric Qian 

from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from
# Use search bar in Amazon to find the product you want, replace the URL below, only works with Amazon
# This URL grabs laptop information, but you can enter whatever you want 
page_url = "https://www.amazon.com/s?k=laptops+on+sale&crid=2C4X6Q1OC685C&sprefix=laptop%2Caps%2C152&ref=nb_sb_ss_ts-a-p_3_6"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the Amazon store page, stores it into an array, reference by index
containers = page_soup.findAll("div", {"class": "a-section a-spacing-medium"})

# name the output file to write to local disk, comma separated values file
out_filename = "Amazon_Laptops.csv"

# header of csv file to be written
headers = "Product Name,Price \n"

# opens file, and writes headers
f = open(out_filename, "w+")
f.write(headers)

# loops over each product and grabs the name and price of each product
for container in containers:

    # finds all link tags "a" from within the first div, stores into an array
    title_name = container.findAll("a", {"class": "a-link-normal a-text-normal"})
    # finds the name of the product and stores it into a variable, displays text
    product_name = title_name[0].span.text

    # finds all "span" tags where the price is displayed
    price = container.findAll("span", {"class": "a-offscreen"})
    # finds the price of the product and stores it into a variable, displays text
    price_number = price[0].text

    # prints the dataset to console
    print("Name: " + product_name + "\n")
    print("Price: " + price_number + "\n")

    # writes to the csv file with the information found
    f.write(product_name.replace("\'", "") + ", " + price_number + "\n")

f.close()  # Close the file
