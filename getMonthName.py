def getMonthName():
    """ this function capitalizes the each month in the months liste
    with the list comprehension"""
    months = ['january', 'february','march', 'april']
    converted_months = [x.title() for x in months]
    
    return converted_months
 
