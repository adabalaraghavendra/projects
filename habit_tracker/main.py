import requests
from datetime import datetime

pixel_endpoint = "https://pixe.la/v1/users"

TOKEN = "loveyourajufromstephen"
USERNAME = "purna"
GRAPHID = "graph1"
user_params = {
"token":TOKEN,
"username":USERNAME,
"agreeTermsOfService": "yes",
"notMinor": "yes"
}


#response = requests.post(url=pixel_endpoint,json=user_params)
#print(response.text)


graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"


graph_params = {
    "id":GRAPHID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"sora"

}
headers = {
    "X-USER-TOKEN": TOKEN
}

#graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(graph_response.text)

data_entry_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPHID}"
DATE = datetime().now()

data_parama = {
    "date":DATE,
    "quantity":input("Enter the Kilometers Cycling today: "),
}


#data_responce = requests.post(url=data_entry_endpoint,json=data_parama,headers=headers)
#print(data_responce.text)

update_endpoint =  f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}"

params = {
    "quantity":"5"
}

#responce = requests.put(url=update_endpoint,json=params,headers=headers)
#print(responce.text)

delete =f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}"

#responce = requests.delete(url=delete,headers=headers)
#print(responce.text)