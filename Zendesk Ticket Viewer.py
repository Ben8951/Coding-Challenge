print("Zendesk Ticket Viewer")

menu_item = 0

while menu_item != 4:
    print ("=======Main Menu=======")
    print ("1. View all tickets.")
    print ("2. Display ticket list.")
    print ("3. Display Individual tickets.")
    print ("4. Exit Program.")
    menu_item = int(input("Selection>  "))

    if menu_item == 1:
        from urllib.parse import urlencode
        import requests

        # Set the request parameters
        url = 'https://zccinterns.zendesk.com/api/v2/tickets'
        user = 'seekins8951@outlook.com'
        pwd = 'P!PPer89'

        # Do the HTTP get request
        response = requests.get(url, auth=(user, pwd))

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        # Decode the JSON response into a dictionary and use the data
        zendesk = response.json()

        # Example 1: Print the name of the first group in the list
        print('Ticket subject:', zendesk['tickets'][3]['subject'])

        # Example 2: Print the name of each group in the list
        ticket_list = zendesk['tickets']
        for ticket in ticket_list:
            print(ticket, 'subject')










