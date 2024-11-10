import sqlite3
con = sqlite3.connect(":memory:")

con.execute("CREATE TABLE movie(title, name, year, score)")


con.execute('insert into movie values(?, ?, ?, ?)', ('AAA', 'tog', 200, 1))
con.execute('insert into movie values(?, ?, ?, ?)', ('aaa', 'tgt', 200, 1))
con.execute('insert into movie values(?, ?, ?, ?)', ('abc', 'd?', 200, 1))
con.execute('insert into movie values(?, ?, ?, ?)',
            ('bbb', 'ff[A-Z]*g', 200, 1))
con.execute('insert into movie values(?, ?, ?, ?)', ('rrr', 't.gt', 200, 1))
con.execute('insert into movie values(?, ?, ?, ?)', ('dff', 'd]d-', 200, 1))
con.execute('insert into movie values(?, ?, ?, ?)', ('ccc', 'A[*]b', 200, 1))
con.commit()


def escape_str(s):
    r = ''
    special_chars = ['*', '[', ']', '?']
    for c in s:
        if c in special_chars:
            r = r + '[' + c + ']'
        else:
            r = r + c
    return r


s = '[*]'
keyword = '*' + escape_str(s) + '*'
print(keyword)

ret = con.execute(
    'select * from movie where title glob ? or name glob ?', [keyword, keyword])

print(str(ret.fetchall()))
