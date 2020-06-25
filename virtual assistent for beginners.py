import wolframalpha

client = wolframalpha.Client('PAWLAH-UHVA9RJQL8')

while True:
    query = str(input('Query: '))
    res = client.query(query)
    output = next(res.results).text
    print(output)
