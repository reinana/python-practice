import sys

# ユーザーの入力を標準出力に出力する
sys.stdout.write("好きな食べ物は？ ")
sys.stdout.flush()
# ユーザーの入力を標準入力から受け取る
user_input = sys.stdin.readline().rstrip()
# 入力を標準出力に出力する
sys.stdout.write(user_input)
sys.stdout.flush()
