import json 
def main(data):
    data = open(data).read()
    data_json = json.loads(data)
    sum = data_json["results"]
    first = sum[-1]["name"]["first"]
    last = sum[-1]["name"]["last"]
    title = sum[-1]["name"]["title"]
    return f"{title} {first} {last}"

print(main('randomuser_data.json'))

def get_fulmane(data):
    data = open(data).read()
    data_list = json.loads(data)
    sum = []
    for user in data_list["results"]:
        first = user["name"]["first"]
        last = user["name"]["last"]
        title = user["name"]["title"]
        sum += [f'{title} {last} {first}']
    return sum

print(get_fulmane("randomuser_data.json"))