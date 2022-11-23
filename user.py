def get_users_by_country(data: dict, country: str) -> list[dict]:
    '''get users by country
    
    Args:
        data (dict): users data
        country (str): country name

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
