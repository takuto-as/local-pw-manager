# 概要
ローカルパスワード管理
オフラインにデータベースを起動しパスワードを管理する

# 初回設定

Dockerでの実行

```sh
cd .
mkdir ./db/data
docker-compose build
```

# コンテナ起動停止

docker-compose でのコンテナ起動

```sh
docker-compose up -d
```

docker-compose でのコンテナ停止

```sh
docker-compose down
```


## ディレクトリ構成

### React

https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md

↑こちらを参考にした↑

```
src
|
+-- assets            # assets folder can contain all the static files such as images, fonts, etc.
|
+-- components        # shared components used across the entire application
|
+-- config            # all the global configuration, env variables etc. get exported from here and used in the app
|
+-- features          # feature based modules
|
+-- hooks             # shared hooks used across the entire application
|
+-- lib               # re-exporting different libraries preconfigured for the application
|
+-- providers         # all of the application providers
|
+-- routes            # routes configuration
|
+-- stores            # global state stores
|
+-- test              # test utilities and mock server
|
+-- types             # base types used across the application
|
+-- utils             # shared utility functions
```

