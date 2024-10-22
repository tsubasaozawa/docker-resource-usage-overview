import matplotlib.pyplot as plt
import os
import numpy as np

# グラフを生成して保存
def create_bar_chart(labels, values):
    # ホスト側にマウントされたoutputディレクトリにファイルを保存する
    output_dir = '/usr/src/app/output'
    os.makedirs(output_dir, exist_ok=True)  # outputディレクトリがない場合は作成

    fig, ax = plt.subplots(figsize=(9, 3)) # outputされるファイルのサイズ設定

    size_list = []
    for value in values:
        size_list.append(convert_size_to_mb(value))

    # 棒グラフの作成
    y_pos = np.arange(len(labels))
    ax.barh(y_pos, size_list, align='center', color='gray')  # 水平棒グラフ
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # 大きい値を上に表示
    ax.set_xlabel('Size (MB)')
    ax.set_title('Docker System Resource Usage')
 
     # 各棒グラフにサイズ情報を表示
    for i, v in enumerate(size_list):
        if v > 0:
            ax.text(v + 10, i, f'{size_list[i]:.3f} MB ({values[i]})', color='black', va='center')
        else:
            ax.text(v + 10, i, f'0.00 MB', color='black', va='center')

    # グラフを保存
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "docker_usage_bar.png"))
    print("Graph saved as docker_usage_bar.png")

# 単位付きのサイズをMBに変換する関数
def convert_size_to_mb(size):
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