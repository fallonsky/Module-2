import csv
import json
import requests


# this checks to see if this entry already exists in the csv file
def hasData(name):
    with open('data.csv') as file:
        for line in file:
            lineList = line.split(",")
            if name == lineList[0]:
                print("record found")
                return True
        print("record not found")
        return False


# function to write a line into the csv
def write_line(data):
    with open('data.csv', 'a', newline='') as f:
        file = csv.writer(f)
        file.writerow(data)

for i in range(30):
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
    if response and response.status_code == 200:
        json_data = response.json()
        print("data retrieved")

        #reformatting
        json_data = json_data['drinks']
        json_data = json_data[0]

        data = [json_data['strDrink'],
                json_data['strIngredient1'],
                json_data['strIngredient2'],
                json_data['strIngredient3'],
                json_data['strIngredient4'],
                json_data['strIngredient5'],
                json_data['strIngredient6'],
                json_data['strIngredient7'],
                json_data['strIngredient8'],
                json_data['strIngredient9'],
                json_data['strIngredient10'],
                json_data['strIngredient11'],
                json_data['strIngredient12'],
                json_data['strIngredient13'],
                json_data['strIngredient14'],
                json_data['strIngredient15']]

        if not hasData(json_data['strDrink']):
            write_line(data)
            print("data written")
    else:
        print("data not retrieved")
    print(" ")
    print(" ")
    print(" ")
