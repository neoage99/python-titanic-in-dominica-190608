import sqlite3

class MemberDao:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')

    def create(self):
        # cursor = self.conn.execute("DROP TABLE MEMBER")
        # self.conn.commit()
        query = """
            create TABLE IF NOT EXISTS MEMBER(
                USERID VARCHAR(10) PRIMARY KEY, 
                PASSWORD VARCHAR(10),
                PHONE VARCHAR(10),
                REGDATE DATE DEFAULT CURRENT_TIMESTAMP
                );
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_many(self):
        data = [
            ('lee', '1', '010-3333-4444'),
            ('kim', '1', '010-3322-1111'),
            ('park', '1', '010-4422-2222'),
        ]
        stmt = "INSERT INTO MEMBER(USERID, PASSWORD, PHONE) VALUES(?,?,?)"
        self.conn.executemany(stmt,data)
        self.conn.commit()

    def fetch_one(self):
        cursor = self.conn.execute("SELECT * FROM MEMBER WHERE USERID LIKE 'lee'")
        row = cursor.fetchone()
        print('이씨')
        print(row)

    def fetch_all(self):
        cursor = self.conn.execute("SELECT * FROM MEMBER")
        rows = cursor.fetchall()
        count = 0
        for i in rows:
            count += 1

        print("총회원수: %d" %(count))

    def login(self, userid, password):
        query = """
            SELECT * FROM MEMBER
            WHERE USERID LIKE ? 
                AND PASSWORD LIKE ? 
        """
        data = [userid, password]
        cursor = self.conn.execute(query, data)
        row = cursor.fetchone()
        print("로그인 회원정보: {}".format(row))
        return row


