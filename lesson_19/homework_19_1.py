import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)
data = response.json()

photos = data['photos'][:2]

for i, photo in enumerate(photos, start=1):
    img_url = photo['img_src']
    img_data = requests.get(img_url).content
    filename = f"mars_photo{i}.jpg"
    with open(filename, 'wb') as f:
        f.write(img_data)
    print(f"File: {filename} - Saved")