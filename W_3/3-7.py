A = {
    'apple': 10,
    'banana': 5,
    'cherry': 7
}

B = {
    'banana': 8,
    'cherry': 6,
    'date': 4
}

C = {}
keys = set(A.keys()).union(B.keys())

for key in keys:
    if key in A and key in B:
        C[key] = max(A[key], B[key])
    elif key in A:
        C[key] = A[key]
    elif key in B:
        C[key] = B[key]

print("Từ điển C theo quy tắc là:", C)
