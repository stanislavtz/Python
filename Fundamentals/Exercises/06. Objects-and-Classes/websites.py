class Website:
    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        self.queries = queries
    
    def __str__(self):
        result = f"https://www.{self.host}.{self.domain}"
        if self.queries:
            result += f"/query?=[{']&['.join(self.queries)}]"
        return result

websites = []
data = input()
while data != 'end':
    host = data.split(' | ')[0]
    domain = data.split(' | ')[1]

    queries = None
    if len(data.split(' | ')) == 3:
        queries = data.split(' | ')[2].split(',')
    
    website = Website(host, domain, queries)
    websites.append(website)
    data = input()

for web in websites:
    print(web)