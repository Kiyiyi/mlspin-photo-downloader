import requests
import os

# change property name based on the current property
property = "8-florence-st"
count = 0
url = input("Enter the URL: ").strip()[:-1]

total_images = int(input("Enter the total number of images you want to download: "))


# set the directory to save the images in
save_dir = "C:\\define-path"+property

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
# open the text file containing the image URLs
with open("images.txt", "r") as f:
    urls = f.readlines()

# loop through each URL and download the image
for i in range(total_images):
 # remove any whitespace or newline characters
    filename = "first-last-" + property + "-" + str(i) + ".jpg" # get the filename from the URL
    filepath = os.path.join(save_dir, filename) # create the full file path
    temp_url = url + str(i) # remove any whitespace or newline characters
    response = requests.get(temp_url, stream=True) # send a GET request to the URL
    if response.status_code == 200: # if the request is successful
        with open(filepath, "wb") as f:
            f.write(response.content) # write the image content to the file
        print(f"{filename} downloaded successfully!")
        i += 1
    else:
        print(f"{filename} failed to download.")
        print(url)
