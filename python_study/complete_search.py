import sys

C = [0] * 100
def getMinSum(A, B, D = 0):
    getMinSum.Length = len(A) - 1
    getMinSum.answer = sys.maxsize

    #
    # 기저사례: leaf-node에 도달하면 계산후 결과를 반환한다.
    #
    if D == getMinSum.Length:
        l=0
        for i in range(0, getMinSum.Length + 1) :
            if C[i]==0 :
                l =i
                break

        return A[D]*B[l]

    eval = 0
    min = sys.maxsize # mininum value for sub tree

    for i in range(0, getMinSum.Length + 1) :
        if C[i] == 1:
            continue

        C[i]=1
        eval = (A[D] * B[i]) + getMinSum(A, B, D + 1)
        C[i]=0

        if min > eval:
            min = eval

    if D == 0 :
        if getMinSum.answer > min:
            getMinSum.answer = min
            return getMinSum.answer

    return min;


#아래 코드는 출력을 위한 테스트 코드입니다.
sys.setrecursionlimit(10000)

tA = []
tB = []

tA.append(1)
tA.append(2)
tA.append(3)

#tA.append(6740);
#tA.append(8454);
#tA.append(8201);
#tA.append(5030);
#tA.append(8105);
#tA.append(9807);
#tA.append(4443);
#tA.append(4586);
#tA.append(5483);
#tA.append(6327);

#tB.append(2583);
#tB.append(1103);
#tB.append(6129);
#tB.append(1657);
#tB.append(9081);
#tB.append(2948);
#tB.append(9709);
#tB.append(704);
#tB.append(2929);
#tB.append(6094);
tB.append(4)
tB.append(5)
tB.append(6)

print(getMinSum(tA,tB))
