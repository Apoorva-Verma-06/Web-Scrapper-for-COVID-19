

#################################################################################


# importing required modules
from bs4 import BeautifulSoup
import requests 
import texttable as tt
from csv import writer
from time import gmtime,strftime
import time

#function for adding a new row in csv file
def append_list_as_row(file_name, list_of_element):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as file_obj:
        # Create a object from csv module
        csv_writer = writer(file_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_element)


# URL for scrapping the COVID-19 data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# getting the content of URL
html = requests.get(url) 
soup = BeautifulSoup(html.text, 'html.parser') 

found_data = [] 

# soup.find_all('td') will scrape every element stored in the variable soup using the td tag
cont = iter(soup.find_all('td')) 

# This loop will keep repeating till there is data available in the iterator(cont) 
while True: 
	try: 
		country = next(cont).text 
		confirmed = next(cont).text 
		deaths = next(cont).text 
		continent = next(cont).text
		#This will help to convert the string to int as the present 'confirmed' stores values like 406,651
		confirmed=confirmed.replace(',','');
		deaths=deaths.replace(',','');

		#adding the data parsed to the 'found_data' list
		found_data.append(( 
			country, 
			int(confirmed), 
			int(deaths), 
			continent 
		)) 

	# When there are no more elements left
	except StopIteration: 
		break

# Sorting done according to the number of confirmed cases
found_data.sort(key = lambda row: row[1], reverse = True)

#printing only the top 50 countries' data for COVID-19 
i=0
print_data=[]
for item in found_data:
	if i<50:
		print_data.append(item)
	else:
		break
	i=i+1



# create texttable object 
table = tt.Texttable() 
table.add_rows([(None, None, None, None)] + print_data)  # Add an empty row at the beginning for the headers 
table.set_cols_align(('c', 'c', 'c', 'c'))  # 'c' denotes center allignment of variables 
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent ')) 

print(table.draw())

#updating the stored values in the file

#storing the time at which data was retrieved
t=time.strftime("%a, %d %b %Y %I:%M:%S %p", time.gmtime())
t=t+" GMT"
row_contents=[t]
append_list_as_row('data.csv', row_contents)


#storing the parsed data in the 'data' file
row_contents=[' Country ', ' Number of cases ', ' Deaths ', ' Continent ']
append_list_as_row('data.csv', row_contents)
for data in found_data:
	row_contents=[]
	for item in data:
		i=str(item)
		row_contents.append(i)
	append_list_as_row('data.csv', row_contents)

	
row_contents=[' ']
append_list_as_row('data.csv', row_contents)


###############################################################################