import requests

programming_language = input("Choose programming language to check the most popular projects on GitHub: ")

url = f'https://api.github.com/search/repositories?q=language:{programming_language}&sort=stars'

r = requests.get(url)

if r.status_code == 200:
    print("Successfully connection")
else:
    print("Connection error, enter programming language correctly !")

response_dict = r.json()
print(f'Total number of "{programming_language}" repositories:', response_dict['total_count'])

repository_dict = response_dict['items']
print("Returned repository", len(repository_dict))

for response_dict in repository_dict:
    print('\n')
    print("Name:", response_dict['name'])
    print("Owner:", response_dict['owner']['login'])
    print("Stars:", response_dict['stargazers_count'])
    print("Repository address:", response_dict['html_url'])
    print("Description:", response_dict['description'])
