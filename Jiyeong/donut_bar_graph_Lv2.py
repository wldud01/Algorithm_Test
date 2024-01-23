# 도넛과 막대 그래프
# level 2

def solution(edges):
    exchange_counts = {}
    for a, b in edges:
        # setdefault 키가 존재하지 않을 경우 기본 값을 설정, 이미 존재하는 경우 현재 값을 사용
        # [나가는 간산, 들어오는 간선]
        exchange_counts.setdefault(a, [0, 0])
        exchange_counts.setdefault(b, [0, 0])

        exchange_counts[a][0] += 1  # a가 b에게 준 횟수
        exchange_counts[b][1] += 1  # b가 a에게 받은 횟수
    # print(exchange_counts)
    created_vertex, bar_graphs, figure_eights = 0, 0, 0

    for vertex, (given, received) in exchange_counts.items():
        # 들어오는 간선이 없으면 생성자
        if given >= 2 and received == 0:
            created_vertex = vertex
        # 나가는 간선은 없고 받는 간선만 있다면 막대
        elif given == 0 and received > 0:
            bar_graphs += 1
        # 나가는 간선이 2개 이상이고 받는 간선도 2개 이상이면 8자
        elif given >= 2 and received >= 2:
            figure_eights += 1

    # 도넛 그래프의 수는 생성된 정점에서 준 횟수에서 막대 그래프와 8자 그래프의 수를 빼서 계산
    # 즉 생성자에서 나간 edge 중에 남는 edge
    donut_graphs = exchange_counts[created_vertex][0] - bar_graphs - figure_eights

    return [created_vertex, donut_graphs, bar_graphs, figure_eights]
