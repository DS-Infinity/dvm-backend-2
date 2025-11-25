from .models import Station
from collections import deque

from collections import deque

def shortest_route(start, end):
    dq = deque()
    dq.append(start)

    dist = {start.id: 0}
    parent = {start.id: None}   # to reconstruct path

    while dq:
        station = dq.popleft()

        if station.id == end.id:
            break

        for nxt in station.neighbors.all():

            # 0-cost if same physical station but different line
            edge_cost = 0 if (station.name == nxt.name and station.line != nxt.line) else 1
            new_cost = dist[station.id] + edge_cost

            if nxt.id not in dist or new_cost < dist[nxt.id]:
                dist[nxt.id] = new_cost
                parent[nxt.id] = station

                if edge_cost == 0:
                    dq.appendleft(nxt)
                else:
                    dq.append(nxt)

    # reconstruct path
    if end.id not in parent:
        return None

    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parent[cur.id]

    return list(reversed(path))