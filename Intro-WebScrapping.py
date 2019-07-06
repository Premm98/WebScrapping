from bs4 import BeautifulSoup
import requests
import pandas as pd

## defining website address, from where to scrape data
website_address = "http://quotes.toscrape.com"
result = requests.get(website_address)
# print(result)

soup = BeautifulSoup(result.text, "html.parser")
# print(soup)

quotes_list = soup.findAll("div", {"class": "quote"})
# print(quotes_list)

quotations_list = []
authors_list = []
tags_list = []
for quote in quotes_list:
    quotation = quote.find("span", {"class": "text"})
    quotations_list.append(quotation.text)

    author = quote.find("small", {"class": "author"})
    authors_list.append(author.text)

    tags = quote.findAll("a", {"class": "tag"})
    new_tags  = ""
    for tag in tags:
        new_tags = new_tags + tag.text + ","
    tags_list.append(new_tags)

quotation_dict = {
    'Quotation': quotations_list,
    'Author': authors_list,
    'Tags': tags_list
}

quotation_dict = pd.DataFrame(quotation_dict)
print(quotation_dict)
quotation_dict.to_csv("NewQuotations.csv")