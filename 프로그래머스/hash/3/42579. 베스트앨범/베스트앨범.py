def solution(genres, plays):
    albums = {}
    best = []
    
    
    # genre별로 i와 plays를 저장할 순 없을까? - 중첩 딕셔너리?
    for idx, genre in enumerate(genres):
        # 바깥 key가 되는 genre가 없으면 key로 genre와 value로 빈 딕셔너리 생성 / 있으면 반환 기존 딕셔너리 반환
        # genre의 value인 딕셔너리에 key (idx)와 값(재생 횟수)을 넣음
        albums.setdefault(genre, {})[idx] = plays[idx]
        
        """
        [위는 아래의 식과 같음]
        inner = albums.setdefault(genre, {})
        inner[idx] = plays[idx]
        
        [setdefault를 사용하지 않으면 아래와 같이 작성]
        if genre not in albums:
            albums[genre] = {}

        albums[genre][idx] = plays[idx]
        """
      
    # 바깥 키 안의 숫자(Value)들의 합을 기준으로 내림차순 정렬
    albums = sorted(
        albums.items(),
        key=lambda x: sum(x[1].values()),
        reverse=True
    )
    
    # 장르를 하나씩 돌며, 안쪽 딕셔너리의 값을 기준으로 정렬하여 songs에 저장
    for genre, songs in albums:
        songs = sorted(
            songs.items(),
            key=lambda x: (-x[1], x[0]) # 재생횟수를 내림차순, 값이 같으면 오름차순
        )
        
        # songs에서 최대 2개씩 best에 저장
        best.extend(idx for idx, _ in songs[:2])    # 슬라이싱은 범위를 벗어나도 에러발생 X
        
    return best
        
            
        