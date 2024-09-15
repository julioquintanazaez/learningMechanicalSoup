import mechanicalsoup

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