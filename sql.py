
import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password="abhijith25197",
    database='sep_2026'
)

cur=conn.cursor()
#sql="create table emp_details(id int primary key,name varchar(15),salary int,dept varchar(20))"
#sql="insert  into emp_details values(1,'arun',25000,'python')"
#sql="insert  into emp_details values(2,'arjun',30000,'java')"
#sql="insert  into emp_details values(3,'aravind',35000,'sql')"
#sql="insert  into emp_details values(4,'arjun',40000,'python')"

sql="select * from emp_details"

cur.execute(sql)

rows=cur.fetchmany(3)
print(rows)
for i in rows:
    print(i[0],i[1],i[2],i[3])

#rows=cur.fetchone()
#print(rows[0],rows[1],rows[2],rows[3])

#rows=cur.fetchall()
#print(rows)
#for i in rows:
#    print(i[0],i[1],i[2],i[3])

conn.commit()

cur.close()
conn.close()