import re

def is_pair(s):
    p = re.compile('(\(.+\))')
    if p.match(s):
        return True
    return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))
print(is_pair('world(())((()())())'))
print(is_pair('()'))
print(is_pair('())'))
