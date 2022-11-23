def get_all_countries(data: dict) -> list[str]:
    '''get all ages from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of countries.
    '''
    # creat an empty list
    countries = []
    # loop each user 
    for user in data['results']:countries.append(user['location']['country'])
    # append countries to list
    return  countries 