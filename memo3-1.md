### reactでハッシュ値を使用
`crypto-js`を使用して、任意の文字列のsha512等のハッシュ値を得ることができる。App.js等のjsファイルで使う例を以下に示す。

- import部分。base64は文字列表示のために使う。
    ```
    import sha512 from 'crypto-js/sha512';
    import Base64 from 'crypto-js/enc-base64';
    ```

- ハッシュ化、値表示部分。
    ```
    const val = sha512("<ハッシュ化したい文字列>").toString(Base64);
    console.log(val);
    ```
