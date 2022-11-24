def get_users_by_country(data: dict, country: str) -> list[dict]:
    '''get users by country
    
    Args:
        data (dict): users data
        country (str): country name

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
    user = []
    for i in data['results']:
        if i['location']['country'] == str(country):
            first = i['name']['first']
            last = i['name']['last']
            title = i['name']['title']
            age = i['dob']['age'] 
            user.append(f'{title}.{first} {last} age:{age}')
    return user
        

def get_users_by_age(data: dict, age: int) -> list[dict]:
    '''get users by age
    
    Args:
        data (dict): users data
        age (int): age

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
    all = []
    for i in data['results']:
        if i['dob']['age']  == age:
            title = i['name']['title']
            name = i['name']['first']
            last = i['name']['last']
            how_old = i['dob']['age']
            all.append(f'{title}.{name} {last}, age:{how_old}')
    return all

def get_users_by_city(data: dict, city: str) -> list[dict]:
    '''get users by city
    
    Args:
        data (dict): users data
        city (str): city name

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
    user = []
    for i in data['results']:
        if i['location']['city'] == str(city):
            first = i['name']['first']
            last = i['name']['last']
            title = i['name']['title']
            age = i['dob']['age'] 
            user.append(f'{title}.{first} {last} age:{age}')
    return user


def get_users_by_nat(data: dict, nat: str) -> list[dict]:
    '''get users by nat
    
    Args:
        data (dict): users data
        nat (str): user nat

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
    user = []
    for i in data['results']:
        if i['nat'] == str(nat):
            first = i['name']['first']
            last = i['name']['last']
            title = i['name']['title']
            age = i['dob']['age'] 
            user.append(f'{title}.{first} {last} age:{age}')
    return user
    
