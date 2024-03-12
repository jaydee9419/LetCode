from datetime import datetime
def today():
    # Get today's date
    today_date = datetime.now()

    # Format the date as "dd/mm/yyyy"
    formatted_date = today_date.strftime("%d/%m/%Y")

    # Print the formatted date
    return formatted_date
