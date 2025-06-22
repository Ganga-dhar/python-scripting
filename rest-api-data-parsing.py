import requests

def httpendpoint(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    



if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    data = httpendpoint(url)
    if data:
        print("Data retrieved successfully:")
        print(data)
        if 'completed' in data:
            print("Todo item:")
            print(f"Title: {data['title']}")
            print(f"Completed: {data['completed']}")
        else:
            print("No todo item found in the data.")
    else:
        print("Failed to retrieve data.")
