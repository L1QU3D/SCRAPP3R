import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Replace this URL with the website you want to scrape
url="https://example.com/"

# Send a GET request to the URL
response = requests.get(url)

# Create a Tkinter window
window = tk.Tk()
window.title("Web Scraping Results")

# Create a Text widget to display the extracted text
text_widget = tk.Text(window)
text_widget.pack()

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the text on the page
    all_text = soup.get_text()

    # Insert the extracted text into the Text widget
    text_widget.insert(tk.END, all_text)
else:
    error_message = f"Failed to retrieve the page. Status code: {response.status_code}"
    text_widget.insert(tk.END, error_message)

# Start the Tkinter main loop to display the window
window.mainloop()
