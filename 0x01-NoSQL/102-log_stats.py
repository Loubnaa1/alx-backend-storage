i#!/usr/bin/env python3
'''Enhanced 12-log_stats.py with added functionality to display the top 10 most frequent IPs from the 'nginx' collection in the 'logs' database.'''

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    

    total_logs = client.logs.nginx.count_documents({})
    print(f'{total_logs} logs')
    

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    index = 0
    while index < len(methods):
        method = methods[index]
        meth_count = client.logs.nginx.count_documents({"method": method})
        print(f'\tmethod {method}: {meth_count}')
        index += 1
    

    count_status_check = client.logs.nginx.count_documents({"method": "GET", "path": "/status"})
    print(f'{count_status_check} status check')
    

    top_ips = client.logs.nginx.aggregate([
        {'$group': {'_id': "$ip", 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ])


    print("IPs:")
    top_ips_list = list(top_ips)
    index = 0
    while index < len(top_ips_list):
        ip_record = top_ips_list[index]
        print(f'\t{ip_record["_id"]}: {ip_record["count"]}')
        index += 1
