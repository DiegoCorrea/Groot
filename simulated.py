from random import choice
from graphviz import Graph


CHANCE = 10


def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
            else:
                m2 = x
    return m2 if count >= 2 else m1


def covert(distance_matrix, song_stages):
    jumper = dict()
    jumper["actual_branch"] = song_stages['start']
    jumper['previous_branch'] = None
    jump_order = [song_stages['start']]
    similarity_list = [1]
    while len(jump_order) - len(set(jump_order)) <= CHANCE:
        #print(str(len(jump_order) - len(set(jump_order))))
        next_branch_to_jump = None
        line = [i for i in distance_matrix[jumper["actual_branch"]]]
        max_next = max(line)
        if max_next == 0.0:
            return {
                'finished': False,
                'jump_order': jump_order,
                'similarity': sum(similarity_list)/len(jump_order)
            }
        if len(jump_order) - len(set(jump_order)) == CHANCE/2 or len(jump_order) - len(set(jump_order)) == CHANCE - 1:
            next_branch_to_jump = [i for i, x in enumerate(line) if i != jumper["actual_branch"]]
        else:
            next_branch_to_jump = [i for i, x in enumerate(line) if x == max_next and i != jumper["actual_branch"]]
        if len(next_branch_to_jump) == 0:
            max_next = second_largest(line)
            if max_next == 0:
                return {
                    'finished': False,
                    'jump_order': jump_order,
                    'similarity': sum(similarity_list) / len(jump_order)
                }
            next_branch_to_jump = choice(
                [i for i, x in enumerate(line)
                 if x == max_next and i != jumper["actual_branch"]]
            )
        else:
            next_branch_to_jump = choice(next_branch_to_jump)
        similarity_list.append(line[next_branch_to_jump])
        jumper['previous_branch'] = jumper['actual_branch']
        jumper["actual_branch"] = next_branch_to_jump
        jump_order.append(next_branch_to_jump)
        if next_branch_to_jump == song_stages['end']:
            return {
                'finished': True,
                'jump_order': jump_order,
                'similarity': sum(similarity_list)/len(jump_order)
            }
    return {
        'finished': False,
        'jump_order': jump_order,
        'similarity': sum(similarity_list) / len(jump_order)
    }


def environment(groot, song_stages, DEBUG=True):
    response = covert(groot.get_distance_matrix(), song_stages)
    time_to_try = 0
    results = dict()
    results['similaridade'] = response['similarity']
    results['final_state'] = response['finished']
    results['total_visitas'] = len(set(response['jump_order']))
    while not response['finished'] and time_to_try <= CHANCE:
        response = covert(groot.get_distance_matrix(), song_stages)
        time_to_try += 1
        results['similaridade'] = response['similarity']
        results['final_state'] = response['finished']
        results['total_visitas'] = len(set(response['jump_order']))
        if DEBUG is True:
            print("Similaridade da lista: " + str(response['similarity']))
            print("Ordem de pulo: " + str(response['jump_order']))
    if DEBUG is True:
        paint_the_root(response['jump_order'])
    return results


def paint_the_root(jumper_list):
    dot = Graph('G', filename='recommendationNodes.gv')
    dot.attr('node', shape='doublecircle')
    dot.attr('node', shape='circle')
    node_before = jumper_list[0]
    for branch in set(jumper_list):
        dot.node(str(branch), str(branch))
    for branch in jumper_list[1:]:
        dot.edge(str(node_before), str(branch))
        node_before = str(branch)
    dot.view()
