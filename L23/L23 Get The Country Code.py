country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '0977'
                }

#search dictionary for country code of Nepal
print("Country Code for Nepal is ")
print(country_code.get('Nepal','Not Found'))

print()

#search dictionary for country code of Japan
print("Country Code for Japan is ")
print(country_code.get('Japan','Not Found'))