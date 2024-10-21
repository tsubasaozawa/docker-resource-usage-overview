import subprocess
import matplotlib.pyplot as plt
import os

# docker system df コマンドの実行結果取得
def get_docker_df_data():
    try:
        result = subprocess.run(['docker', 'system', 'df'], stdout=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error executing docker system df: {e}")
        return ""

# コマンド出力をパースして必要なデータを抽出
def parse_docker_df_data(data):
    lines = data.splitlines()  # データ内における改行文字までの部分を1要素とする配列を作成
    categories = ["Images", "Containers", "Local Volumes", "Build Cache"]
    values = []

    for category in categories:
        for line in lines:
            if line.startswith(category):
                replaced_line = line.replace(category, '').lstrip()  # 文字列からカテゴリー名を空文字で置換し、その後の冒頭空白文字を削除
                size_str = replaced_line.split()[2]
                # print("size_str: ", size_str)
                values.append(convert_to_mb(size_str))  # サイズをMBに変換
                break
    return categories, values

# 単位付きのサイズをMBに変換する関数
def convert_to_mb(size):
    unit = size[-2:]  # 単位だけ取得
    value = size[:-2]  # 単位を除いた値だけ取得

    try:
        value = float(value)
    except ValueError:
        print(f"Invalid size value: {size}")
        return 0

    if unit == 'kB':
        return value / 1024
    elif unit == 'MB':
        return value
    elif unit == 'GB':
        return value * 1024
    elif unit == 'TB':
        return value * 1024**2
    else:
        print(f"Unknown unit: {unit}")
        return 0

# パーセンテージとサイズ情報を表示するカスタム関数
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        size = pct * total / 100.0
        return f'{pct:.1f}% ({size:.1f} MB)'
    return my_format

# グラフを生成して保存
def create_pie_chart(categories, values):
    # ホスト側にマウントされたoutputディレクトリにファイルを保存する
    output_dir = '/usr/src/app/output'
    os.makedirs(output_dir, exist_ok=True)  # outputディレクトリがない場合は作成
    plt.figure(figsize=(6, 6))

    # パーセンテージとサイズ情報を表示
    plt.pie(values, labels=categories, autopct=autopct_format(values), startangle=90)
    plt.title("Docker System Resource Usage")
    plt.savefig(os.path.join(output_dir, "docker_usage.png"))

    print("Graph saved as docker_usage.png")

# メイン処理
if __name__ == "__main__":
    docker_data = get_docker_df_data()
    if docker_data:
        print('The result data of executing docker system df command:\n', docker_data)

        categories, values = parse_docker_df_data(docker_data)
        create_pie_chart(categories, values)
    else:
        print("Failed to retrieve docker system df data.")
