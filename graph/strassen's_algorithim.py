"""
Strassen’s Algorithm is a method to multiply two square matrices faster than the normal (naive) method.

Normal matrix multiplication
Time complexity:
O(n3)

Strassen’s Algorithm
Time complexity:
O(nlog2​7)≈O(n2.807)
So it is faster than the normal approach.
"""

def strassen(A,B):
    if len(A) == 2 and len(A[0]) == 2:
        a,b,c,d = A[0][0],A[0][1],A[1][0],A[1][1]
        e,f,g,h = B[0][0],B[0][1],B[1][0],B[1][1]

        m1 = a * (f - h)
        m2 = (a + b) * h
        m3 = (c + d) * e
        m4 = d * (g - e)
        m5 = (a + d) * (e + h)
        m6 = (b - d) * (g + h)
        m7 = (a - c) * (e + f)

        c11 = m5 + m4 -m2 + m6
        c12 = m1 + m2 
        c21 = m3 + m4 
        c22 = m1 + m5 - m3 -m7

        return [
            [c11,c12],
            [c21,c22]
        ]
    else:
        print("Not a valid matrix.\n use 2x2 matrix.")


#matrix multiplication using traditional method.
def multi(A,B):
    row_A = len(A)
    col_A = len(A[0])
    row_B = len(B)
    col_B = len(B[0])

    if col_B == row_A:
        result = [[0 for _ in range(col_B) ] for _ in range(row_A)]

        for i in range(row_A):
            for j in range(col_B):
                for k in range(col_A):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    
    else:
        print("Multiplication not possible.")

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = strassen(A, B)
#result = multi(A,B)
print("Strassen result:", result)

#