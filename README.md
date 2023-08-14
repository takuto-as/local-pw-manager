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