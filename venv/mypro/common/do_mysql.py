import pymysql


class DoMysql:

    def __init__(self, host=None, username=None, password=None, port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.mysql = pymysql.connect(host=self.host, username=self.username, password=self.password, port=self.port)
        self.cursor = self.mysql.cursor()

    def fetchone(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()

    def fetchall(self, sql):
        self.cursor.execute(sql)

        self.mysql.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    mysql = DoMysql()
