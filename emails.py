def get_all_emails(data: dict) -> list[str]:
    '''get all emails from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of emails.
    '''
    d=[]
    m=data['results']
    for s in m:
        d.append(s['email'])
    return d
