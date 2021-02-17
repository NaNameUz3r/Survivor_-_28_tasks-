#!/usr/bin/env python3


def SynchronizingTables(N, ids, salary):

    sorted_ids = sorted(ids)
    sorted_sal = sorted(salary)

    table_dict = dict(zip(sorted_ids, sorted_sal))
    
    recovered_salary = []
    for id in range(N): 
        accord_value = table_dict.get(ids[id])
        recovered_salary.append(accord_value)

    return recovered_salary
