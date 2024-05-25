### reactの`.env`の優先順位
以下より抜粋。
- https://coders-shelf.com/create-react-app-env-variables/
    ```
    Files on the left have more priority than files on the right:
    
    npm start: .env.development.local, .env.local, .env.development, .env
    npm run build: .env.production.local, .env.local, .env.production, .env
    npm test: .env.test.local, .env.test, .env (note .env.local is missing)
    ```

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
- 参考
    - https://www.npmjs.com/package/crypto-js
    - https://stackoverflow.com/questions/11889329/word-array-to-string
    - https://stackoverflow.com/questions/47766755/using-crypto-js-in-react 

### javascriptのフォーマッタ(prettier)

- https://prettier.io/
- インストール (ついでにlinterも)

  ```
  npm init @eslint/config
  npm install --save-dev --save-exact prettier
  npm install --save-dev eslint-config-prettier
  ```

- 使用例
  ```
  (チェックのみ)
  node_modules\.bin\prettier src --check

  (ファイル修正あり)
  node_modules\.bin\prettier src --write
  ```

- 行当たり文字数オプション
  ```
    --print-width <int>      The line length where Prettier will try wrap.
                             Defaults to 80.
  ```
  
- カンマの設定
```
  --trailing-comma es5   ：3.0.0以前のデフォルト 
  --trailing-comma all   ：3.0.0以降のデフォルト 
```

### pythonのフォーマッタ(black)

- https://github.com/psf/black

- インストール
  ```
  pip install black
  ```

- 使用例
  ```
  black --check .
  ```

- 行当たり文字数オプション
  ```
    -l, --line-length INTEGER       How many characters per line to allow.
                                    [default: 88]
  ```

### pythonのフォーマッタ(autopep8)
- https://pypi.org/project/autopep8/

- インストール
```
$ pip install --upgrade autopep8
```

- 使用例(チェックのみ)
```
autopep8.exe . -r --diff
```

- 使用例(ファイル置換)
```
autopep8.exe . -r --in-place
```

### VSCodeにprettierインストールと設定
https://zenn.dev/k_kazukiiiiii/articles/670ebae0005872
- VSCodeを起動して`Prettier -Code formatter`をインストールする。
- VSCodeのsettingを開く (ctrl, でも開ける)
    - `default formatter`で設定を検索
    - `Editor: Default Formatter`で`Prettier Code Formatter`を選択

- `save`で設定を検索
    - `Text Editor`の`Formatting`のところで`Format On Save`にチェックをいれる

### VSCodeにblackのインストールと設定
- `Black Formatter`をインストール

### VSCodeにautopep8のインストールと設定
- `autopep8`をインストール

### prettierとblackをつかるようにsettings.jsonを書き換える
```
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

prettier 3.0のデフォルト設定に合わせる(カンマの設定が変更)
```
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  "prettier.trailingComma": "all"
}
```

### prettierとautopep8をつかるようにsettings.jsonを書き換える
```
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.autopep8"
  },
  "prettier.trailingComma": "all"
}

```


### Bearerによるコードのセキュリティチェック
- 公式サイト
    - https://github.com/Bearer/bearer
    - https://docs.bearer.com/reference/commands/#bearer_scan

- インストール
    ```
    curl -LO https://github.com/Bearer/bearer/releases/download/v1.43.6/bearer_1.43.6_linux_amd64.tar.gz
    tar xvfz bearer_1.43.6_linux_amd64.tar.gz
    ```

- SAST (Static Application Security Testing) のチェック
    ```
    bearer scan <target dir> --scanner=sast -f html --output <html filename>
    ```

- シークレット文字列の埋め込みのチェック
    ```
    bearer scan <target dir> --scanner=secrets -f html --output <html filename>
    ```
