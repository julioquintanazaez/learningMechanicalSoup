import mechanicalsoup
import os
import wget

browser = mechanicalsoup.StatefulBrowser()

url = "https://images.google.com/"

browser.open(url)

print(browser.get_url())

#get HTML
print(browser.get_current_page())

#Target the search input
browser.select_form()
print(browser.get_current_form().print_summary())

#search for term
search_term = "cat"
browser["q"] = sesrch_term

#submit/click search
browser.launch_browser()
response = browser.submit_selected()

print("New url", browser.get_url())
print("My responese:", response.text[:500])

#Open a new url
new_url = browser.get_url()
browser.open(new_url)

#Get the HTML
page = browser.get_current_page()
all_images = page.find_all("img")

print(all_images)

#Target the source attribute
image_source = []
for image in all_images:
    _image = image.get("src")
    image_source.append(_image)

print(image_source)

#Remove rong format url from the list
image_source = [image for image in image_source if image.startwith("https")]
print(image_source)

path = os.getcwd()
path = os.path.join(path, search_terms + "s")

#Creat th dicectory
os.mkdir(path)

print(path)

#Download images
counter = 0
for image in image_source:
    save_as = os.path.join(path, search_terms + str(counter) + "jpg")
    wget.download(image, save_as)
    counter += 1