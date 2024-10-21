# ベースイメージにAlpine Linuxを使用
FROM alpine:latest

# Docker CLIとPython、およびmatplotlibをインストール
RUN apk add --no-cache docker-cli python3 py3-pip py3-matplotlib

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# Pythonスクリプト（app.py）をコンテナにコピー
COPY app.py .

# コンテナ実行時にPythonスクリプトを実行
CMD ["python3", "app.py"]
