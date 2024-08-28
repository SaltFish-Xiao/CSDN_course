from zhyl_mysql import connect
class ClaimReport(object):
    def implement(self,sql):
        db=connect()
        cursor=db.cursor()
        sql = sql
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception():
            print("查询失败")
        cursor.close()
        db.colse()
