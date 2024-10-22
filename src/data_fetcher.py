import subprocess

# 指定されたシステムコマンドを実行して出力結果を返す
def get_system_data(cmd):
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")