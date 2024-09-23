#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:07:44 2024

@author: yanzhu
"""

#problem-set-03

# no other imports needed
from collections import defaultdict
import math
#

### PART 1: SEARCHING UNSORTED LISTS

# search an unordered list L for a key x using iterate



def test_isearch():
    assert isearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert isearch([], 2) == (2 in [])

def isearch(L, x):

    return iterate(lambda state, elem: state or (elem == x), False, L)

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])



test_isearch()

def rsearch(L, x):
    if len(L) == 0:
        return False
    
    blist = [item == x for item in L]
    return reduce(lambda a, b: a or b, False, blist)

def test_rsearch():
    assert rsearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert rsearch([], 2) == (2 in [1, 3, 5])

def reduce(f, id_, a):
    print(a)
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

test_rsearch()

def ureduce(f, id_, a):
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        return f(reduce(f, id_, a[:len(a)//3]),
                 reduce(f, id_, a[len(a)//3:]))



### PART 2: DOCUMENT INDEXING

def run_map_reduce(map_f, reduce_f, docs):
    # done. do not change me.
    """    
    The main map reduce logic.
    
    Params:
      map_f......the mapping function
      reduce_f...the reduce function
      docs.......list of input records
    """
    # 1. call map_f on each element of docs and flatten the results
    # e.g., [('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1), ('sam', 1), ('is', 1), ('ham', 1)]
    pairs = flatten(list(map(map_f, docs)))
    # 2. group all pairs by by their key
    # e.g., [('am', [1, 1]), ('ham', [1]), ('i', [1, 1]), ('is', [1]), ('sam', [1, 1])]
    groups = collect(pairs)
    # 3. reduce each group to the final answer
    # e.g., [('am', 2), ('ham', 1), ('i', 2), ('is', 1), ('sam', 2)]
    return [reduce_f(g) for g in groups]


def doc_index_map(doc_tuple):
    """
    Params:
      doc_tuple....a tuple (docstring, docid)
    Returns:
      a list of tuples of form (word, docid), where token is a whitespace delimited element of this string.

    Note that the returned list can contain duplicates.
    E.g.
    >>> doc_index_map('document one is cool is it', 0)
    [('document', 0), ('one', 0), ('is', 0), ('cool', 0), ('is', 0), ('it', 1)]    
    """
    ### done. do not change me.
    doc, docid = doc_tuple[0], doc_tuple[1]
    return [(token, docid) for token in doc.split()]

def dedup(a, b):
    """
    Return a concatenation of two lists without any duplicates.
    Assume that input lists a and b are already sorted and deduplicated.
    """
    # Ensure both a and b are lists, even if they are single integers
    if not isinstance(a, list):
        a = [a]
    if not isinstance(b, list):
        b = [b]
    
    return sorted(list(set(a) | set(b)))
            
    
def doc_index_reduce(group):
    """
    Fix this function to instead call the reduce and dedup functions
    to return the _unique_ list of document ids that this word appears in.
    
    Params:
      group...a tuple of the form (word, list_of_docids), indicating the docids containing this word, with duplicates.
    Returns:
      tuple of form (word, list_of_docids), where duplicate docids have been removed.
      
    >>> doc_index_reduce(['is', [0,0,1,2]])
    ('is', [0,1,2])
    """
    # fix this line
    

    word, docids = group
  # Use reduce with dedup to eliminate duplicates from the docids list
    unique_docids = reduce(dedup, [], docids)
    return (word, unique_docids)
    ###
    
def test_dedup():
    assert dedup([1,2,3], [3,4,5]) == [1,2,3,4,5]
    assert dedup([1,2,3], [5,6]) == [1,2,3,5,6]
    
test_dedup() 
    
def test_doc_index_reduce():
    assert doc_index_reduce(['is', [0,0,1,2]]) == ('is', [0,1,2])
    assert doc_index_reduce(['is', [0,0,0,0,1,1,1,1,1,1,2,2,2,2]]) == ('is', [0,1,2])

test_doc_index_reduce()

def test_index():
    res = run_map_reduce(doc_index_map, doc_index_reduce,
               [('document one is cool is it', 0),
                ('document two is also cool', 1),
                ('document three is kinda neat', 2)
               ])    
    assert res == [('also', [1]),
                   ('cool', [0, 1]),
                   ('document', [0, 1, 2]),
                   ('is', [0, 1, 2]),
                   ('it', [0]),
                   ('kinda', [2]),
                   ('neat', [2]),
                   ('one', [0]),
                   ('three', [2]),
                   ('two', [1])]
    

def collect(pairs):
    """
    Implements the collect function (see text Vol II Ch2)
    >>> collect([('i', 1), ('am', 1), ('sam', 1), ('i', 1)])
    [('am', [1]), ('i', [1, 1]), ('sam', [1])]    
    """
    ### done
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())


def plus(x, y):
    # done. do not change me.
    return x + y

    
def flatten(sequences):
    # done. do not change me.
    return iterate(plus, [], sequences)




### PART 3: PARENTHESES MATCHING

#### Iterative solution
def parens_match_iterative(mylist):

    result = iterate(parens_update, 0, mylist)
    return result == 0


def parens_update(current_output, next_input):

    if current_output == -1:
        return -1
    if next_input == '(':
        return current_output + 1
    elif next_input == ')':
        if current_output > 0:
            return current_output - 1
        else:
            return -1
    else:
        return current_output  # 


def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False
    assert parens_match_iterative([]) == True

test_parens_match_iterative()

#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parentheses are matched, False otherwise.
    """
    # Step 1: Map each element of the list using paren_map
    mapped_list = list(map(paren_map, mylist))
    
    # Step 2: Use scan to calculate the prefix sums
    prefix_sums, total_sum = scan(lambda x, y: x + y, 0, mapped_list)
    
    # Step 3: Use reduce to find the minimum value in the prefix sums
    min_prefix_sum = reduce(min_f, 0, prefix_sums)
    
    # Step 4: Return True if the parentheses are matched (total_sum == 0 and min_prefix_sum >= 0)
    return total_sum == 0 and min_prefix_sum >= 0

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(', 'a', ')', '(', ')']) == True
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_scan(['(', '(', ')']) == False
    assert parens_match_scan(['(', 'a', ')', ')', '(']) == False
    assert parens_match_scan([]) == True

#### Divide and conquer solution
test_parens_match_scan()


def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses.
    """

    if len(mylist) == 0:
        return (0, 0)
    if len(mylist) == 1:
        if mylist[0] == '(':
            return (0, 1)
        elif mylist[0] == ')':
            return (1, 0)
        else:
            return (0, 0)

    middle = len(mylist) // 2
    left_unmatched_right, left_unmatched_left = parens_match_dc_helper(mylist[:middle])
    right_unmatched_right, right_unmatched_left = parens_match_dc_helper(mylist[middle:])

    total_unmatched_right = left_unmatched_right + max(0, right_unmatched_right - left_unmatched_left)

    total_unmatched_left = right_unmatched_left + max(0, left_unmatched_left - right_unmatched_right)
    
    return (total_unmatched_right, total_unmatched_left)

    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
    assert parens_match_dc(['(', 'a', ')', '(', ')']) == True
    assert parens_match_dc(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_dc(['(', '(', ')']) == False
    assert parens_match_dc(['(', 'a', ')', ')', '(']) == False
    assert parens_match_dc([]) == True 
test_parens_match_dc()
