import requests

def download_file(url, filename):
    # Send a GET request to the specified URL.
    r = requests.get(url, allow_redirects=True)
    # Write the content of the response to a file. The 'wb' argument signifies
    # that the file is opened for writing in binary mode.
    with open(filename, 'wb') as f:
        f.write(r.content)

# Replace 'http://localhost:8000/myfile.txt' with your file's URL and 
# 'myfile.txt' with your file's name.
download_file('http://localhost:8000/myfile.txt', 'myfile.txt')
