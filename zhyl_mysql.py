import pymysql
def connect():
    try:
        db = pymysql.connect(host = 'rm-3xeehik4682r3cky33o.mysql.rds.aliyuncs.com',
                     port=3306,
                     user='insurance_readonly',
                     passwd='n5n7pT^LwT',
                     db='insurance-2019-prod')
        return db
    except Exception:
        raise Exception("数据库连接失败")
