from countryinfo import CountryInfo

country_name = input("Enter your Country Name: ")
country = CountryInfo(country_name)

print("Capital is: ", country.capital())
print("Curriencie is: ", country.currencies())
print("Population is", country.population())
print("Language is: ", country.languages())
print("Area is: ", country.area())
print("Country's Native Name: ", country.native_name())
print("State Name's: ", country.provinces())
print("Country Region: ", country.region())
print("Country timezones: ", country.timezones())