from data import read_data

from ages import get_all_ages, get_the_oldest_age, get_the_youngest_age
from cities import get_all_cities
from countries import get_all_countries
from emails import get_all_emails
from nats import get_all_nats
from phone_numbers import get_all_numbers
from pictures import get_all_pictures_url
from streets import get_all_streets
from user import get_users_by_country
from user import get_users_by_age
from user import get_users_by_city
from user import get_users_by_nat


data = read_data('Data/randomusers.json')

def main():
    ages = get_all_ages(data)
    olest_age = get_the_oldest_age(ages)
    youngest_age = get_the_youngest_age(ages)
    
    cities = get_all_cities(data)
    # print(cities)
    countries = get_all_countries(data)
    # print(countries)
    emailes = get_all_emails(data)
    # print(emailes)
    nats = get_all_nats(data)
    # print(nats)
    phone_numbers = get_all_numbers(data)
    # print(phone_numbers)
    images = get_all_pictures_url(data)
    # print(images)
    streets = get_all_streets(data)
    # print(streets)
    country = get_users_by_nat(data, 'DE')
    # print(by country)
    adults = get_users_by_age(data,51)
    # print(by ages)
    city = get_users_by_city(data,'Coswig')
    # print(by city)
    nat = get_users_by_nat(data,'DE')
    # print((adults))
    
    print(adults)
main()


# DRY - Don't Repeat Yourself