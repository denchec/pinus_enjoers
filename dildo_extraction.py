import psycopg2

import requests
import datetime

# фиксируем и выводим время старта работы кода
start = datetime.datetime.now()

'''Возвращает JSON со списком товаров с первой страницы'''
def start_page_extracrion():
    url = 'https://recom.wb.ru/personal/ru/male/v5/search?ab_already_purchase_v2_ts=test&ab_dino_matcher=ab_baseline_boost_09_05&appType=1&curr=rub&dest=-535680&page=1&query=84892243&resultset=catalog&spp=30&suppressSpellcheck=false&uclusters=0'
    headers = {
        'Authorization': f'Bearer {'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjcyMDc0MTMsInZlcnNpb24iOjIsInVzZXIiOiI4NDg5MjI0MyIsInNoYXJkX2tleSI6IjIiLCJjbGllbnRfaWQiOiJ3YiIsInNlc3Npb25faWQiOiI3ODQzZTA1NWI4MDY0YmVjOGQ0ZTk2ZTMyMWI2ODY2YyIsInVzZXJfcmVnaXN0cmF0aW9uX2R0IjoxNjc0MDQ3ODQyLCJ2YWxpZGF0aW9uX2tleSI6ImUzNmI2ZjY1OWJjYzYzMTk0Nzg3NjYwOTA4MDgyZTRkNTAyNmE1MjE5MTQ0ZDMxMTEyMjVlMjk0MjkwNjI5ODUiLCJwaG9uZSI6ImRXMVJuN2xSVDdJeUFVZ1NaYjB5RkE9PSJ9.INr7u6cqVleDLUt43ThSLIK7nhTHsCv7s5inX5_Mr4v46M5pc0_JSKCenCUFHPaMcj8J4cxs2q0CYF1wOgORPQHaU3gnfYxvbhWiVOJBCk60slonOL_j9ioXjDdglntq5f2NULRzP8w0G2vzmqQOxC8jWh3MuTLJfu26L3nbId6jJb2W6hRB67pv9esTyx6igl4-Oth1ku4gPn6Y1zZOeGw_S1WBhLqt4RgLHbzvTGC-PslxSCVmeooSUte3RlONv8-60vhKkgeUrUDfspPO23NtqYRexhAwX1gmxtpCSmYFqg0QKVs_Rc8Z80ldyCJbMkpC7F0jmbLfmnMoDGwMZQ'}',
    }

    extracted_data = requests.get(url, headers=headers).json()
    return extracted_data['data']['products']
print(len((start_page_extracrion())))

def find_values_by_key(json_object):

    for obj in json_object:
        if type(obj) == dict:
            obj = obj.items()
            values = []
            for k, v in obj:
                if k == 'id':
                    values.append(v)
                elif k == 'name':
                    values.append(v)
                elif k == 'sizes':
                    obj = dict(obj)
                    values.append(obj['sizes'][0]['price']['basic'] / 100)
        return values




def sql_insert(x): #на выходе делает инсерт в базу
    insrt = "insert into penises (nm, nmname, price) values (" + "'" + str(find_values_by_key(start_page_extracrion())[0]) + "'" + "," + " " + "'" + str(find_values_by_key(start_page_extracrion())[1]) + "'" + "," + " " + "'" + str(find_values_by_key(start_page_extracrion())[2]) + "'" + ')'

    try:
        conn = psycopg2.connect(dbname='penis_store', user='postgres',
                                password='Mikheev99', host='localhost')
    except:
        print('-')


    cursor = conn.cursor()
    cursor.execute(insrt)
    conn.commit()
    cursor.close()
    conn.close()

pizda = start_page_extracrion()

for i in range(len(start_page_extracrion())):
    sql_insert(find_values_by_key(pizda))

finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
