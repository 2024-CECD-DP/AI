import itertools
import networkx as nx
import matplotlib.pyplot as plt

# 각 해시태그 리스트
hashtags1 = ["#food", "#travel", "#fitness", "#foodie", "#photography", "#nature", "#fashion", "#art", "#love",
             "#music"]
hashtags2 = ["#travel", "#nature", "#photography", "#food", "#traveling", "#adventure", "#explore", "#wanderlust",
             "#landscape", "#vacation", "#foodie", "#fitness", "#fun"]
hashtags3 = ["#food", "#fitness", "#healthy", "#cooking", "#nutrition", "#health", "#diet", "#workout", "#recipes",
             "#gym", "#foodie", "#travel"]
hashtags4 = ["#music", "#art", "#fashion", "#photography", "#artist", "#painting", "#design", "#style", "#creative",
             "#drawing", "#photography", "#travel"]
hashtags5 = ["#love", "#travel", "#foodie", "#photography", "#fashion", "#friends", "#fun", "#happy", "#smile",
             "#memories", "#traveling", "#food"]
hashtags6 = ["#food", "#recipes", "#cooking", "#foodporn", "#yum", "#delicious", "#eat", "#homemade", "#chef",
             "#dinner", "#foodie", "#travel"]
hashtags7 = ["#travel", "#adventure", "#explore", "#wanderlust", "#nature", "#photography", "#vacation", "#trip",
             "#travelgram", "#traveling", "#food", "#fitness"]
hashtags8 = ["#fitness", "#health", "#workout", "#exercise", "#gym", "#fitfam", "#healthy", "#motivation", "#training",
             "#running", "#fitness", "#foodie"]
hashtags9 = ["#photography", "#nature", "#landscape", "#art", "#travel", "#beautiful", "#photooftheday", "#sky",
             "#sunset", "#beach", "#photography", "#food"]
hashtags10 = ["#food", "#music", "#love", "#fashion", "#photography", "#travel", "#art", "#fun", "#friends", "#happy",
              "#traveling", "#foodie"]

# 모든 해시태그를 담을 빈 리스트 생성
all_hashtags = []

# 모든 해시태그를 담은 리스트 생성
for i in range(1, 2):
    all_hashtags.extend(eval(f"hashtags{i}"))

# 그래프 생성
G = nx.Graph()

# 해시태그 간의 관계 파악 및 가중치 증가
for hashtag_list in [hashtags1, hashtags2, hashtags3, hashtags4, hashtags5, hashtags6, hashtags7, hashtags8, hashtags9,
                     hashtags10]:
    for hashtag1, hashtag2 in itertools.combinations(hashtag_list, 2):
        if G.has_edge(hashtag1, hashtag2):
            # 이미 엣지가 존재하면 가중치를 1 증가시킴
            G[hashtag1][hashtag2]['weight'] += 1
        else:
            # 새로운 엣지 생성
            G.add_edge(hashtag1, hashtag2, weight=1)

# 결과 출력
for edge in G.edges(data=True):
    print(edge)

# 노드의 크기 계산
node_size = [100 * G.degree[node] for node in G]

# 엣지의 가중치를 기반으로 엣지 색상 설정
edge_colors = [d['weight'] for u, v, d in G.edges(data=True)]

# 그래프 그리기
fig, ax = plt.subplots(figsize=(15, 15))  # 그래프 크기 조정
pos = nx.spring_layout(G, seed=42)  # 그래프 레이아웃 설정
nx.draw(G, pos, with_labels=True, node_size=500, edge_color=edge_colors, cmap=plt.cm.Blues, node_color='pink')

# 색상 막대기 추가
sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(edge_colors), vmax=max(edge_colors)))
sm.set_array([])
plt.colorbar(sm, ax=ax, label='Edge Weight')

# 그래프 출력
plt.title('Hashtag Network Graph')
plt.show()

# 최대 스패닝 트리 계산
max_spanning_tree = nx.maximum_spanning_tree(G)

# 최대 스패닝 트리를 그래프로 그리기
fig, ax = plt.subplots(figsize=(15, 15))
pos = nx.spring_layout(max_spanning_tree)
nx.draw(max_spanning_tree, pos, with_labels=True, node_size=500, edge_color='green', node_color='pink')

# 그래프 출력
plt.title('Maximum Spanning Tree of Hashtag Network')
plt.show()
