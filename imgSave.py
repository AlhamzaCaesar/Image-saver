import requests
input("Press Enter to start....")
img_url = input("Type the url of the image (do copy image link and paste here) : ")
img_name = input("Type the name of the image : ")
r = requests.get(img_url)
with open(img_name+".png","wb") as f:
    f.write(r.content)
