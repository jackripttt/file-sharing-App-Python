import requests
import logging
from tqdm import tqdm

def download_file(url, filename):
    try:
        # Send a GET request to the specified URL.
        response = requests.get(url, stream=True)
        total_size_in_bytes= int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        
        # Write the content of the response to a file. The 'wb' argument signifies
        # that the file is opened for writing in binary mode.
        with open(filename, 'wb') as f:
            for data in response.iter_content(chunk_size=1024):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            logging.error("ERROR, something went wrong")
        
        logging.info(f'Successfully downloaded {filename} from {url}')
    except Exception as e:
        logging.error(f'Failed to download {filename} from {url}. Error: {e}')

def download_files(urls, filenames):
    # Ensure that the number of URLs matches the number of filenames.
    assert len(urls) == len(filenames), "Mismatch between number of URLs and filenames."
    # Download each file.
    for url, filename in zip(urls, filenames):
        download_file(url, filename)

# Replace the lists with your files' URLs and names.
urls = ['http://localhost:8000/myfile1.txt', 'http://localhost:8000/myfile2.txt']
filenames = ['myfile1.txt', 'myfile2.txt']
download_files(urls, filenames)
