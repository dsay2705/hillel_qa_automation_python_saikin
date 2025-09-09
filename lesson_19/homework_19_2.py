import requests
from urllib.parse import quote

class ImageRequester:
    def __init__(self, base_url="http://127.0.0.1:8080"):
        self.base_url = base_url

    def _encode_filename(self, filename):
        return quote(filename)

    def upload_image(self, file_path):
        url = f"{self.base_url}/upload"
        with open(file_path, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(url, files=files)
        return response

    def get_image_url(self, filename):
        encoded_filename = self._encode_filename(filename)
        url = f"{self.base_url}/image/{encoded_filename}"
        headers = {'Content-Type': 'text'}
        response = requests.get(url, headers=headers)
        return response

    def get_image_file(self, filename):
        encoded_filename = self._encode_filename(filename)
        url = f"{self.base_url}/image/{encoded_filename}"
        headers = {'Content-Type': 'image'}
        response = requests.get(url, headers=headers)
        return response

    def delete_image(self, filename):
        encoded_filename = self._encode_filename(filename)
        url = f"{self.base_url}/delete/{encoded_filename}"
        response = requests.delete(url)
        return response

filename = "mars_photo1.jpg"

image_requester = ImageRequester()

upload_responce = image_requester.upload_image(filename)
print("Upload:", upload_responce.status_code, upload_responce.json())

get_url_responce = image_requester.get_image_url(filename)
print("Get URL:", get_url_responce.status_code, get_url_responce.json())

get_file_responce = image_requester.get_image_file(filename)
if get_file_responce.ok:
    with open(f"downloaded_{filename}", "wb") as f:
        f.write(get_file_responce.content)
    print("Get File: Downloaded", filename)
else:
    print("Get File: Error", get_file_responce.status_code)

delete_responce = image_requester.delete_image(filename)
print("Delete:", delete_responce.status_code, delete_responce.json())