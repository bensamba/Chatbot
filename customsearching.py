from googleapiclient.discovery import build
#pip install google-api-python-client
my_api_key = "wewewewmakewewwewyourweeown-dtfvyYCYG6"
my_cse_id = "065614846154941395154741:createyourown"
f=0
def google_search(search_term, api_key, cse_id, **kwargs):
    global f
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    except:
        f=1
        return None
    if 'items' in res:    
        return res['items'] 
    else:
        return None
def glasearch(s):
    global f
    results= google_search(s,my_api_key,my_cse_id,num=10)
    if f==1:
        return ("internet connection required for searching")
    #print(f)
    if results is not None:    
        for result in results:
            return (result['title'] + "\n" + result['snippet']+ "\n" +"visit :: "+result['link'])
            #print(result['snippet'])
            #print(result['article']['articlesection'])
            #print("visit :: "+result['link'])
            break
    else :
        return ("not found")
