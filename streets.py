def get_all_streets(data: dict) -> list[str]:
    '''get all streets from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of streets.
    '''
    s=[]
    for i in data['results']:
        s.append(i['location']['street']['name'])
    return s