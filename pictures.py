def get_all_pictures_url(data: dict) -> list[str]:
    '''get all pictures_url from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of pictures_url.
    '''
    picture=[]
    for pic in data['results']:
        picture.append(pic['picture']['large'])
    return picture
