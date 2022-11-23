def get_all_numbers(data: dict) -> list[str]:
    '''get all phone numbers from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of phone numbers.
    '''
    # create an empty list
    numbers = []
    # loop each user
    for user in data['results']:numbers.append(user['phone'])
    # append phone numbers to numbers 
    return numbers
