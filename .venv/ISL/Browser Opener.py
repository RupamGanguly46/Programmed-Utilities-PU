# import webbrowser
#
# def open_ip_webpage(ip_address):
#     # Construct the URL from the IP address
#     url = f"http://{ip_address}"
#
#     # Open the URL in the default web browser
#     webbrowser.open(url)
#
#
# # Example IP address
# ip = ""  # Replace this with the IP address you want to open
# open_ip_webpage(ip)

import webbrowser


def open_ip_webpage_in_specific_browser(ip_address, browser_path):
    url = f"http://{ip_address}"

    # Get the specific browser and open the URL
    browser = webbrowser.get(browser_path)
    browser.open(url)


# Example IP address and browser path (Google Chrome in this case)
ip = "192.168.1.1"  # Replace this with the IP address you want to open
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"  # Replace with your browser path

open_ip_webpage_in_specific_browser(ip, chrome_path)
