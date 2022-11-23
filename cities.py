def get_all_cities(data: dict) -> list[str]:
    '''get all ages from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of cities.
    '''
    s=[]
    for i in data['results']:
        s.append(i['location']['city'])
    return s