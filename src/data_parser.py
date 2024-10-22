# コマンド出力をパースして必要なデータを抽出
def parse_docker_df_data(data):
    result_values = []

    types = ["Images", "Containers", "Local Volumes", "Build Cache"]
    lines = data.splitlines()  # データ内における改行文字までの部分を1要素とする配列を作成

    for t in types:
        for line in lines:
            if line.startswith(t): # lineの冒頭の文字列がタイプの文字列と合致するものだけ処理
                replaced_line = line.replace(t, '').lstrip()  # 文字列からカテゴリー名を空文字で置換し、その後の冒頭空白文字を削除
                size_str = replaced_line.split()[2]

                result_values.append(size_str)
                break
    return types, result_values