def matrix_mult(a, b, MOD):
    ans = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] = (ans[i][j] + a[i][k] * b[k][j]) % MOD
    return ans

def matrix_power(matrix, exp, MOD):
    if exp == 0:
        return [[1, 0], [0, 1]]
    elif exp == 1:
        return matrix
    else:
        temp = matrix_power(matrix, exp // 2, MOD)
        if exp % 2 == 0:
            return matrix_mult(temp, temp, MOD)
        else:
            return matrix_mult(matrix_mult(temp, temp, MOD), matrix, MOD)

def calculate(n, a, b, f0, f1, m):
    matrix1 = [[a, b], [1, 0]]
    res = matrix_power(matrix1, n - 1, m)
    fnmodm = (res[0][0] * f1 + res[0][1] * f0) % m
    return fnmodm

# Read input
n, a, b, f0, f1, m = map(int, input().split())

# Calculate and output the result
result = calculate(n, a, b, f0, f1, m)
print(result)