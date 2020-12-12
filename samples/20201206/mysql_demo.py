import pymysql



conn = pymysql.connect(
    host = '127.0.0.1',
    port= 3306,
    user = 'root',
    password='',
    database='interface_test_db',
    charset= 'utf8'
)



cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = '''
select * from case_info,case_step_info,requests_info 
where case_info.case_id = case_step_info.case_id and case_step_info.requests_id = requests_info.requests_id and case_info.is_run = '是'
order by case_info.case_id,case_step_info.case_step_id;

'''
cursor.execute(sql)
a=cursor.fetchall()
for a in a:
    print(a)