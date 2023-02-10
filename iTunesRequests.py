import os
import requests
import json

url = 'https://itunes.apple.com/gb/rss/customerreviews/id=1500780518/sortBy=mostRecent/json'
r = requests.get(url)
data = r.json()

while (True):
     print("1)Print the ['feed']['author']")
     print("2)Print the ['feed']['updated']")
     print("3)Print the ['feed']['rights']")
     print("4)Print the ['feed']['title']")
     print("5)Print the ['feed']['icon']")
     print("6)Print the ['feed']['author']['uri]")
     print("7)Print the ['feed']['entry'][5]['im:rating]")
     print("8)Print the ['feed']['entry'][5]['content]")
     print("9) Exit")

     your_choice = int(input("Enter your choice: "))
     
     if your_choice == 1:
        print(data['feed']['author'])
        print()
        
     elif your_choice == 2:
        print(data['feed']['updated'])
        print()

     elif your_choice == 3:
        print(data['feed']['rights'])
        print()

     elif your_choice == 4:
        print(data['feed']['title'])
        print()

     elif your_choice == 5:
        print(data['feed']['icon'])
        print()

     elif your_choice == 6:
        print(data['feed']['author']['uri']) 
        print()

     elif your_choice == 7:
       print(data['feed']['entry'][5]['im:rating'])
       print()

     elif your_choice == 8:
        print(data['feed']['entry'][5]['content'])
        print()

     elif your_choice == 9:
        break
        print()
        

     else:
        print("Invalid choice")
        print()
