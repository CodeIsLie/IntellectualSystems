# MIT 6.034 Lab 1: Rule-Based Systems

from production import IF, AND, OR, NOT, THEN, run_conditions
import production as lab
from tester import make_test, get_tests, type_encode, type_decode
from data import *
import random
random.seed()
lab_number = 1

try:
    set()
except NameError:
    from sets import Set as set, ImmutableSet as frozenset


### TEST 13 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given a hypothesis and an empty set of
# rules.  The goal tree should contain only the hypothesis.

def backchain_to_goal_tree_1_getargs():
    return [ (),  'stuff'  ]

def backchain_to_goal_tree_1_testanswer(val, original_val = None):
    return ( val == 'stuff' or val == [ 'stuff' ])

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_1_getargs,
          testanswer = backchain_to_goal_tree_1_testanswer,
          expected_val = "'stuff'",
          name = "backchain_to_goal_tree"
          )


### TEST 14 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given the hypothesis 'alice is an
# albatross' and using the zookeeper_rules.

def tree_map(lst, fn):
    if isinstance(lst, (list, tuple)):
        return fn([ tree_map(elt, fn) for elt in lst ])
    else:
        return lst

def backchain_to_goal_tree_2_getargs():
    return [ zookeeper_rules, 'alice is an albatross' ]

result_bc_2 = OR('alice is an albatross',
                 AND(OR('alice is a bird',
                        'alice has feathers',
                        AND('alice flies',
                            'alice lays eggs')),
                     'alice is a good flyer'))

def backchain_to_goal_tree_2_testanswer(val, original_val = None):
    return ( tree_map(type_encode(val), frozenset) ==
             tree_map(type_encode(result_bc_2), frozenset))

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_2_getargs,
          testanswer = backchain_to_goal_tree_2_testanswer,
          expected_val = str(result_bc_2)
          )


### TEST 15 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given the hypothesis 'geoff is a giraffe'
# and using the zookeeper_rules.

def backchain_to_goal_tree_3_getargs():
    return [ zookeeper_rules,  'geoff is a giraffe'  ]

result_bc_3 = OR('geoff is a giraffe',
                 AND(OR('geoff is an ungulate',
                        AND(OR('geoff is a mammal',
                               'geoff has hair',
                               'geoff gives milk'),
                            'geoff has hoofs'),
                        AND(OR('geoff is a mammal',
                               'geoff has hair',
                               'geoff gives milk'),
                            'geoff chews cud')),
                     'geoff has long legs',
                     'geoff has long neck',
                     'geoff has tawny color',
                     'geoff has dark spots'))

def backchain_to_goal_tree_3_testanswer(val, original_val = None):
    return ( tree_map(type_encode(val), frozenset) ==
             tree_map(type_encode(result_bc_3), frozenset))

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_3_getargs,
          testanswer = backchain_to_goal_tree_3_testanswer,
          expected_val = str(result_bc_3)
          )


### TEST 16 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given the hypothesis 'gershwin could not
# ask for anything more' and using the rules defined in
# backchain_to_goal_tree_4_getargs() below.

def backchain_to_goal_tree_4_getargs():
    return [ [ IF( AND( '(?x) has (?y)',
                        '(?x) has (?z)' ),
                   THEN( '(?x) has (?y) and (?z)' ) ),
               IF( '(?x) has rhythm and music',
                   THEN( '(?x) could not ask for anything more' ) ) ],
             'gershwin could not ask for anything more' ]

result_bc_4 = OR('gershwin could not ask for anything more',
                 'gershwin has rhythm and music',
                 AND('gershwin has rhythm',
                     'gershwin has music'))

def backchain_to_goal_tree_4_testanswer(val, original_val = None):
    return ( tree_map(type_encode(val), frozenset) ==
             tree_map(type_encode(result_bc_4), frozenset) )

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_4_getargs,
          testanswer = backchain_to_goal_tree_4_testanswer,
          expected_val = str(result_bc_4)
          )


### TEST 17 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given the hypothesis 'zot' and using the
# rules defined in ARBITRARY_EXP below.

ARBITRARY_EXP = (
    IF( AND( 'a (?x)',
             'b (?x)' ),
        THEN( 'c d' '(?x) e' )),
    IF( OR( '(?y) f e',
            '(?y) g' ),
        THEN( 'h (?y) j' )),
    IF( AND( 'h c d j',
             'h i j' ),
        THEN( 'zot' )),
    IF( '(?z) i',
        THEN( 'i (?z)' ))
    )

def backchain_to_goal_tree_5_getargs():
    return [ ARBITRARY_EXP, 'zot' ]

result_bc_5 = OR('zot',
                 AND('h c d j',
                     OR('h i j', 'i f e', 'i g', 'g i')))

def backchain_to_goal_tree_5_testanswer(val, original_args = None):
    return ( tree_map(type_encode(val), frozenset) ==
             tree_map(type_encode(result_bc_5), frozenset))

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_5_getargs,
          testanswer = backchain_to_goal_tree_5_testanswer,
          expected_val = str(result_bc_5)
          )
