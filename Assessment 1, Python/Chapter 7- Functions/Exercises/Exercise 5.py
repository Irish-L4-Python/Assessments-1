def describe_city(city, country='Japan'): #defines the variable "describe_city(city, country='Japan'):"
    msg = f"{city.title()} is in {country.title()}." #assigns the variable "msg" the statement in this line and the "city" and "country"
    print(msg)

describe_city('Saitama') #stores the data in this line to "describe_city"
describe_city('Hiroshima', 'Italy') #stores the data in this line to "describe_city"
describe_city('Osaka') #stores the data in this line to "describe_city"