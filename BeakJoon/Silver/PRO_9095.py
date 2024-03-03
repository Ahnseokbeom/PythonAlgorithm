import sys

def main():
    dp = [0] * 11
    dp[1], dp[2], dp[3] = 1, 2, 4
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        print(dp[n])

# if __name__ == "__main__":
#     main()
