#!/bin/env python
import json
import csv
import requests


url = "https://api.meraki.com/api/v1/"




def get_networks(organizationId):
    response = requests.get(url + "organizations/" + organizationId + "/networks", headers=headers)
    response = response.json()
    networks = []
    for id in response:
        networks.append(id["id"])
    print("Got networks...")
    return(networks)


def get_logs(networks):
    filename = input("Enter output CSVfile name: ")
    data_file = open(filename, 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    print("Writing logs...")

    for networkId in networks:
        response = requests.get(url + "networks/" + networkId + "/events?productType=appliance&perPage=1000", headers=headers)
        response = response.json()
        if "events" in response:
            for emp in response["events"]:
                if count == 0:
    
                    
                    header = emp.keys()
                    csv_writer.writerow(header)
                    count += 1
    
       
                csv_writer.writerow(emp.values())
  
    data_file.close()


def get_orgs():
    response = requests.get(url + "organizations/", headers=headers)
    response = response.json()
    pos = 1
    print("Select the organization: ")
    for i in response:
        print(str(pos) + ") " + i["name"])
        pos += 1
    answer =input("Select Organization: ")
    answer = int(answer) -1
    try:
        print("Setting Organization to: " + response[answer]["name"])
        return(response[answer]["id"])
    except:
        print("Invalid Option.  Please try again.")
        get_orgs()


api_key = input("Paste your Meraki API Key: ")

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}

organizationId = get_orgs()
networks = get_networks(organizationId)
get_logs(networks)







