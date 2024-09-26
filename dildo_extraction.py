import requests
import psycopg2

articl = input()
def data_extracrion(): #на выходе отдает данные по артикулу, назвонию и цене
    url = 'https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-12695438&spp=30&ab_testing=false&nm=' + str(articl)
    headers = {
        'Authorization': f'Bearer {'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjcyMDc0MTMsInZlcnNpb24iOjIsInVzZXIiOiI4NDg5MjI0MyIsInNoYXJkX2tleSI6IjIiLCJjbGllbnRfaWQiOiJ3YiIsInNlc3Npb25faWQiOiI3ODQzZTA1NWI4MDY0YmVjOGQ0ZTk2ZTMyMWI2ODY2YyIsInVzZXJfcmVnaXN0cmF0aW9uX2R0IjoxNjc0MDQ3ODQyLCJ2YWxpZGF0aW9uX2tleSI6ImUzNmI2ZjY1OWJjYzYzMTk0Nzg3NjYwOTA4MDgyZTRkNTAyNmE1MjE5MTQ0ZDMxMTEyMjVlMjk0MjkwNjI5ODUiLCJwaG9uZSI6ImRXMVJuN2xSVDdJeUFVZ1NaYjB5RkE9PSJ9.INr7u6cqVleDLUt43ThSLIK7nhTHsCv7s5inX5_Mr4v46M5pc0_JSKCenCUFHPaMcj8J4cxs2q0CYF1wOgORPQHaU3gnfYxvbhWiVOJBCk60slonOL_j9ioXjDdglntq5f2NULRzP8w0G2vzmqQOxC8jWh3MuTLJfu26L3nbId6jJb2W6hRB67pv9esTyx6igl4-Oth1ku4gPn6Y1zZOeGw_S1WBhLqt4RgLHbzvTGC-PslxSCVmeooSUte3RlONv8-60vhKkgeUrUDfspPO23NtqYRexhAwX1gmxtpCSmYFqg0QKVs_Rc8Z80ldyCJbMkpC7F0jmbLfmnMoDGwMZQ'}',
    }

    pr_extr = requests.get(url, headers=headers).json()

    r = requests.get('https://basket-05.wbbasket.ru/vol870/part87060/' + str(articl) + '/info/ru/card.json', auth=('user', 'pass')).json()

    nm = r['nm_id']
    nm_name = r['imt_name']
    price = pr_extr['data']['products'][0]['sizes'][0]['price']['product']/100

    return nm, nm_name, price
def sql_insert(): #на выходе делает инсерт в базу
    insrt = "insert into penises (nm, nmname, price) values (" + "'" + str(data_extracrion()[0]) + "'" + "," + " " + "'" + str(data_extracrion()[1]) + "'" + "," + " " + "'" + str(data_extracrion()[2]) + "'" + ')'

    print(insrt)
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

sql_insert()
