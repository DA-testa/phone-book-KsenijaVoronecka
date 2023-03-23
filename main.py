# python3 main.py
# Ksenija Voronecka 221RDC056 (RDCP0)
from collections import defaultdict

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # phone_book = {}
    phone_book = defaultdict(list)
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for key, value in phone_book.items():
                if value == cur_query.number:
                    phone_book.pop(key)
                    phone_book[cur_query.name] = value
                    break
            else: # otherwise, just add it
                phone_book[cur_query.name] = cur_query.number
        elif cur_query.type == 'del':
            for key, value in phone_book.items():
                if value == cur_query.number:
                    phone_book.pop(key)
                    break
        else:
            response = 'not found'
            for key, value in phone_book.items():
                if value == cur_query.number:
                    response = key
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

