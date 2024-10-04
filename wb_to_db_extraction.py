import schedule
import psycopg2
import requests
import datetime
import time
import urllib.parse



def extract_all_pages(string_to_url):
    string_to_url = urllib.parse.quote(string_to_url)
    values = []
    for i in range(1, 101):
        url = 'https://search.wb.ru/exactmatch/ru/male/v7/search?ab_testing=false&appType=1&curr=rub&dest=-535680&page=' + str(i) + '&query=' + string_to_url + '&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false&uclusters=0'
        headers = {
            'Authorization': f'Bearer {'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mjc1NjM2MzcsInZlcnNpb24iOjIsInVzZXIiOiI4NDg5MjI0MyIsInNoYXJkX2tleSI6IjIiLCJjbGllbnRfaWQiOiJ3YiIsInNlc3Npb25faWQiOiI3ODQzZTA1NWI4MDY0YmVjOGQ0ZTk2ZTMyMWI2ODY2YyIsInVzZXJfcmVnaXN0cmF0aW9uX2R0IjoxNjc0MDQ3ODQyLCJ2YWxpZGF0aW9uX2tleSI6ImUzNmI2ZjY1OWJjYzYzMTk0Nzg3NjYwOTA4MDgyZTRkNTAyNmE1MjE5MTQ0ZDMxMTEyMjVlMjk0MjkwNjI5ODUiLCJwaG9uZSI6ImRXMVJuN2xSVDdJeUFVZ1NaYjB5RkE9PSJ9.A3s9h32e_nlxYaYXuZZYgjKYLa44v2tJEFYK0WfynuJtbyPLhqTwqJX01ZcQ1IdfXkpR2PBztDiAn9nGbkovFzrT1NDNKC-vSZ-l1Qu6mMTeHOs5mw1iVljYk5nQF-Hi89Lgu7FgLVuqgUwx_mHCewBtzyyf_rGHEiNj0y0eFxH5v5Kufd5n11fzDoSihZbaxjSmEhv-KeJdLsj46Rx6kzuMrR_74Bp7NbwwoNmr3aPFFCcmZPSXV50-qlELLhlQa21MeXtyJ8smQf5obLxrDVgpgWOokBfytxkjHnpGNQAnB2MMHJtlAwNrojT0qbjMRhNzjx-uJo6B6BYYbJrHew'}',
        }

        extracted_data = requests.get(url, headers=headers).json()

        if 'data' in extracted_data:
            values.append(extracted_data['data']['products'])
        else:
            break

    return values

def find_values_by_key(json_object):
    values = []
    for list_items in json_object:
        for obj in list_items:
            list_for_tupling = []
            if type(obj) == dict:
                obj = obj.items()
                for k, v in obj:
                    if k == 'id':
                        list_for_tupling.append(v)
                    elif k == 'name':
                        list_for_tupling.append(v)
                    elif k == 'sizes':
                        obj = dict(obj)
                        list_for_tupling.append(obj['sizes'][0]['price']['basic'] / 100)
            list_for_tupling = tuple(list_for_tupling)
            values.append(list_for_tupling)
    return values

def sql_insert(data_to_insert):
    insert_query = """
        INSERT INTO penises (nm, nmname, price) 
        VALUES (%s, %s, %s)
    """

    try:
        conn = psycopg2.connect(dbname='penis_store', user='postgres',
                                password='Mikheev99', host='localhost')
    except:
        print('-')


    cursor = conn.cursor()

    cursor.executemany(insert_query, data_to_insert)

    conn.commit()

    cursor.close()
    conn.close()

def truncate_base():
    insert_query = """
            truncate penises
        """
    try:
        conn = psycopg2.connect(dbname='penis_store', user='postgres',
                                password='Mikheev99', host='localhost')
    except:
        print('-')


    cursor = conn.cursor()

    cursor.execute(insert_query)
    conn.commit()
    cursor.close()
    conn.close()

def get_nms_from_db():
    insert_query = """
                select nm from penises
            """
    try:
        conn = psycopg2.connect(dbname='penis_store', user='postgres',
                                password='Mikheev99', host='localhost')
    except:
        print('DATA BASE CONNECTION ERROR')

    cursor = conn.cursor()
    cursor.execute(insert_query)
    values = cursor.fetchall()
    values = [item[0] for item in values]

    return values


def main_task():
    nms_from_db = get_nms_from_db()

    truncate_base()

    counter = 0

    extracted_pages = extract_all_pages(items_to_search)

    extracted_data = find_values_by_key(extracted_pages)

    sql_insert(extracted_data)

    print('База обновлена в ', datetime.datetime.now())


    for i in range(len(extracted_data)):
        if extracted_data[i][0] in nms_from_db:
            counter += 1

    print('Строк изменено: ', counter)

if __name__ == '__main__':
    items_to_search = str(input())
    print('Start at', datetime.datetime.now())
    schedule.every(1).minutes.do(main_task)
    while True:
        schedule.run_pending()
