## 参考サイト
- https://wiki.postgresql.org/wiki/Locale_data_changes
- https://stackoverflow.com/questions/16817925/unicode-character-default-collation-table
- https://lists.debian.org/debian-glibc/2019/03/msg00030.html
- https://blog.noellabo.jp/entry/2020/11/08/145740


### ubuntuの場合
- glibcバージョン
```
libc-bin                         2.35-0ubuntu3.1                         amd64        GNU C Library: Binaries
libc6:amd64                      2.35-0ubuntu3.1                         amd64        GNU C Library: Shared librarie
```

- ソート結果
```
$ LC_COLLATE=en_US.UTF-8 sort w.txt
① 123
123
-１２３
１２３
１abc
１p
１Test456
１TTT
① これは？
２z
３c
４５６
４b
５a
-789
789
Ａ123
abc
 ＣＣＣ
-compa
cont
def
^ＫＫＫ
softbank
softbank
stu
T
t1234
Ｔdame?
Test
Tこれは？
-これは？
```

### amazon linuxの場合
- glibcバージョン
glibc-2.26-64.amzn2.0.2.x86_64

- ソート結果
```
$ LC_COLLATE=en_US.UTF-8 sort a
^ＫＫＫ
 ＣＣＣ
-１２３
-これは？
① これは？
１２３
４５６
123
Ａ123
① 123
789
-789
５a
abc
１abc
４b
３c
-compa
cont
Ｔdame?
def
１p
softbank
softbank
stu
T
Tこれは？
t1234
Test
１Test456
１TTT
２z
```
