def solution(n, words):
    # 사용된 단어의 집합
    used_words = set()
    # 이전 단어의 끝 알파벳 (최초는 첫 단어의 첫 알파벳)
    prev_alp = words[0][0]
    
    for i, word in enumerate(words):
        # 이전 단어의 끝과 일치하지 않거나, 이미 사용된 단어인 경우
        if word in used_words or word[0] != prev_alp:
            # 현재 번호화 차례 리턴
            return [(i%n) + 1, (i//n) + 1]
        # 정상의 경우 user_words에 추가 및 이전 단어 끝 알파벳 업데이트
        else:
            used_words.add(word)
            prev_alp = word[-1]
    # 이상없는 경우 [0, 0] 리턴
    return [0, 0]
    