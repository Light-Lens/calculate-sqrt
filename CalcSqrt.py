import sys

def sqrt(x, y): return (y**2 + x) / (2 * y)
print("Type a number you want to find the square root of otherwise type 'quit' to exit.")

ans = 1
prev_ans = 0
input_num = input("> ")
sys.exit() if input_num.lower() == "quit" else None
for _ in range(1000):
	ans = sqrt(float(input_num), ans)
	if prev_ans == ans: break

	prev_ans = ans
	print(ans)
