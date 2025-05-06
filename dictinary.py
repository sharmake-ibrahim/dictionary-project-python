import requests




"""             Understanding Common API Status Codes
Every API request to a web server returns a status code indicating the outcome of the request. Here are some common codes relevant to GET requests:

200: Everything went okay, and the result has been returned (if any).
301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names or changes an endpoint name.
400: The server thinks you made a bad request. This happens when you send incorrect data or make other client-side errors.
401: The server thinks you're not authenticated. Many APIs require login credentials, so this happens when the correct credentials are not sent.
403: The resource you're trying to access is forbidden. You don’t have the right permissions to see it.
404: The resource you tried to access wasn’t found on the server.
503: The server is not ready to handle the request. """

def handle_dictionary():
    
    input_txt_value= str(input("enter a word: "))

    while True:
        if input_txt_value  != "":
            break
        else:
              
         input_txt_value= str(input("enter a word: "))

    res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{input_txt_value}")


    data = res.json()


    # print(data[0])
    
    if res.status_code == 200:
        print(f"Word: {data[0]["word"]}")

        for rec in data[0]["meanings"]:
            print(f"Part of Speech: {rec["partOfSpeech"]}")
            print(f"Definition: {rec["definitions"][0]["definition"]: >20}")
            # print(rec)
            
    elif res.status_code == 404:
        print("That word doesn't exits !")
    
        

handle_dictionary()