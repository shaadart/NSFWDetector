import requests
r = requests.post(
    "https://api.deepai.org/api/nsfw-detector",
    data={
        'image': 'https://1.bp.blogspot.com/-cLwPQ03JX54/XPXPxnR_PlI/AAAAAAAAh8o/SWG-RSAPBS4FaYLMeN_AdG5QJYugofA_ACLcBGAs/s1600/IMG_0831.JPG',
    },
    headers={'api-key': '3c18f715-5de6-4a18-b734-41714fe6a214'}
)
print(r.json())

