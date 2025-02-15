import requests
# pip install requests

websitelink = "https://jsonguide.technologychannel.org/info.json"


resp = requests.get(websitelink)
convert_to_dict = resp.json()


print(convert_to_dict['description'])


# content = convert_to_dict["description"]

# for data in convert_to_dict:
#     print(data['description'])

# f = open("result.txt","w")
# f.write(content)
# f.close()
# print("File write successful")


   