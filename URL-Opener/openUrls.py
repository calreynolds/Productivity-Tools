import webbrowser
import validators

url1 = "http://www.google.com"

def open_urls(input_file):
    urls = open(input_file, "r").readlines()

    if len(urls) == 0:
        print("No files were sent my way. What a sad play.")
        return

    i = 0
    for url in urls:
        if not validators.url(url):
            print(url, "was not a valid URL. Skipping.")
            continue
        if i == 0:
            webbrowser.open(url)
        else:
            webbrowser.open_new_tab(url)
        print("Opened", url)
    print("Done!")

def main():
    open_urls("input.txt")

main()
