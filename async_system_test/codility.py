def solution(A, B):
    mapping = {'t': 10, 'j': 11, 'q': 12, 'k': 13, 'a': 14}
    digital_A = map(lambda x: int(x) if x.isdigit() else mapping[x.lower()], A)
    digital_B = map(lambda x: int(x) if x.isdigit() else mapping[x.lower()], B)
    return len([a for a, b in zip(digital_A, digital_B) if a > b])

if __name__ == '__main__':
    print(solution('a586qk23a84q', 'jj653kk2q25j'))
    print(solution('23a84q', 'k2q25j'))
