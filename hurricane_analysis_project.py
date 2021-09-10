# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

# This function returns a new list of updated damages where the recorded data is converted
# to float values and the missing data is retained as "Damages not recorded".
def update_damages(damages):
    updated_damages = []
    for element in damages:
        if element == 'Damages not recorded':
            updated_damages.append(0.0) #This means Damages not recorded
        elif "M" in element:
            repl = element.replace("M","")
            elem_float = float(repl)*1000000
            updated_damages.append(elem_float)
            #print("Element equals: " + element)
        elif "B" in element:
            repl = element.replace("B", "")
            elem_float = float(repl)*1000000000
            updated_damages.append(elem_float)
    return(updated_damages)

# Testing the function
# print(update_damages(damages))



# write your construct hurricane dictionary function here:

# This function constructs a dictionary made out of the lists.
# The keys are the names of the hurricanes, the values are dictionaries containing 
# a key for each piece of data
def construct_dict(names, months, years, winds, areas, damages, deaths):
    data_dict = {}
    for index in range(len(names)):
        data_dict[names[index]] = {'Name': names[index], 'Month': months[index], 'Year': years[index], 
                           'Max Sustained Wind': winds[index], 'Areas Affected': areas[index],
                           'Damage': damages[index], 'Deaths': deaths[index]}
    return data_dict

# Testing the last function
dict = construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
# print(dict["Cuba I"])
# print(dict)
# print(dict.keys())
# print(list(dict.values()))
# print(list(dict.values())[0])
# print(list(dict.values())[0]['Year'])
# len(dict)
# print(1942 in dict.values())
# print(dict["Cuba I"])


# write your construct hurricane by year dictionary function here:

def dict_by_year(my_dict):
    new_dict = {}
    for index in range(len(my_dict)):
        # temp_list = []
        
        year = list(my_dict.values())[index]['Year']
        name = list(my_dict.values())[index]['Name']
        # print(year)
        # print(name)
        
        if year in new_dict:
            new_dict[year].append(my_dict[name])
        else:
            new_dict[year] = []
            # print("New item at dictionary")
            # print(new_dict)
            # print(new_dict[year])
            new_dict[year].append(my_dict[name])
            # print("Appended to the list")
    return new_dict

# Testing the function
sorted_dict = dict_by_year(dict)
# print(sorted_dict[1933])






# write your find most affected area function here:

# write your count affected areas function here:
# "Mexico" in areas_affected
# print(list(range(len(areas_affected))))

def count_areas(areas_affected):
    new_dict = {}
    for q in range(len(areas_affected)):
        for j in range(len(areas_affected[q])):
            counter = 0
            area = areas_affected[q][j]
            for list in areas_affected:
                counter += list.count(area)
            new_dict[area] = counter
    return new_dict


# print(count_areas(areas_affected))
      
            
            

# write your greatest number of deaths function here:

    #this function finds and prints the hurracain with the greatest deaths and shows
    # the number of deaths
def num_deaths(names, deaths):
    max_value = max(deaths)
    max_index = deaths.index(max_value)
    max_hurr = names[max_index]
    max_deaths = deaths[max_index]
    
    print("The hurracain " + max_hurr + " casued the greatest number of deaths with " + 
          str(max_value) + " defunctions.")

# num_deaths(names, deaths)

# cat_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
# print(cat_dict[0])
# cat_dict[0].append("Hola")
# print(cat_dict[0])


# write your catgeorize by mortality function here:
    
# mortality_scale = {0: 0,
#                    1: 100,
#                    2: 500,
#                    3: 1000,
#                    4: 10000}

def cat_mortality(names, deaths):
    cat_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    rating = 0
    for number in deaths:
        if number == 0:
            rating = 0
        elif 0 < number <= 100:
            rating = 1
        elif 100 < number <= 500:
            rating = 2
        elif 500 < number <= 1000:
            rating = 3
        elif 1000 < number <= 10000:
            rating = 4
        else:
            rating = 5
        
        hurr_index = deaths.index(number)
        cat_dict[rating].append(names[hurr_index])
    return cat_dict

# print(cat_mortality(names, deaths))


    
# write your greatest damage function here:
num_damages = update_damages(damages)
def find_max_damage(names, damages):
    max_value = max(damages)
    max_index = damages.index(max_value)
    max_hurr = names[max_index]
    max_damage = damages[max_index]
    
    print("The hurracain " + max_hurr + " casued the greatest damages with " + 
          str(max_damage) + " USD($).")
    

# find_max_damage(names, num_damages)






# write your catgeorize by damage function here:

# damage_scale = {0: 0,
#                 1: 100000000,
#                 2: 1000000000,
#                 3: 10000000000,
#                 4: 50000000000}    
def cat_damages(names, damages):
    cat_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    rating = 0
    for index in range(len(damages)):
        number = damages[index]
        if number == 0.0:
            rating = 0
            # print("number: " + str(number) + " rating: " + str(rating) + " index:" + str(damages.index(number)))
        elif 0.0 < number <= 100000000:
            rating = 1
            # print("number: " + str(number) + " rating: " + str(rating) + " index:" + str(damages.index(number)))
        elif 100000000 < number <= 1000000000:
            rating = 2
        elif 1000000000 < number <= 10000000000:
            rating = 3
        elif 10000000000 < number <= 50000000000:
            rating = 4
        else:
            rating = 5
        
        # hurr_index = damages.index(number)
        cat_dict[rating].append(names[index])
    return cat_dict

print(cat_damages(names, num_damages))

print(num_damages)
# print(names[15])
    

