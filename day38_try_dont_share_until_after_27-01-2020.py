

latin_text = """
Sed ut perspiciatis, unde omnis iste natus error sit
voluptatem accusantium doloremque laudantium, totam
rem aperiam eaque ipsa, quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta
sunt, explicabo. Nemo enim ipsam voluptatem, quia
voluptas sit, aspernatur aut odit aut fugit, sed
quia consequuntur magni dolores eos, qui ratione
voluptatem sequi nesciunt, neque porro quisquam est,
qui dolorem ipsum, quia dolor sit amet consectetur
adipisci[ng] velit, sed quia non numquam [do] eius
modi tempora inci[di]dunt, ut labore et dolore
magnam aliquam quaerat voluptatem. Ut enim ad minima
veniam, quis nostrum exercitationem ullam corporis
suscipit laboriosam, nisi ut aliquid ex ea commodi
consequatur? Quis autem vel eum iure reprehenderit,
qui in ea voluptate velit esse, quam nihil molestiae
consequatur, vel illum, qui dolorem eum fugiat, quo
voluptas nulla pariatur?

At vero eos et accusamus et iusto odio dignissimos
ducimus, qui blanditiis praesentium voluptatum
deleniti atque corrupti, quos dolores et quas
molestias excepturi sint, obcaecati cupiditate non
provident, similique sunt in culpa, qui officia
deserunt mollitia animi, id est laborum et dolorum
fuga. Et harum quidem rerum facilis est et expedita
distinctio. Nam libero tempore, cum soluta nobis est
eligendi optio, cumque nihil impedit, quo minus id,
quod maxime placeat, facere possimus, omnis voluptas
assumenda est, omnis dolor repellendus. Temporibus
autem quibusdam et aut officiis debitis aut rerum
necessitatibus saepe eveniet, ut et voluptates
repudiandae sint et molestiae non recusandae. Itaque
earum rerum hic tenetur a sapiente delectus, ut aut
reiciendis voluptatibus maiores alias consequatur
aut perferendis doloribus asperiores repellat.
"""

print("First 100 characters:\n  {} ...".format(latin_text[:100]))

def normalize_string(s):
    assert type (s) is str
    ###
    ### YOUR CODE HERE
    ###
    import re
    import string
    exclude = set(string.punctuation)
    print(len(s))
    a = ''.join(ch for ch in s if ch not in exclude)
    a = a.lower()
    return a
    
# Demo:
print(latin_text[:100], "...\n=>", normalize_string(latin_text[:100]), "...")
# `normalize_string_test`: Test cell
norm_latin_text = normalize_string(latin_text)
print(len(norm_latin_text))
print(normalize_string("e pluribus.unum basium"))
# assert type(norm_latin_text) is str
# assert len(norm_latin_text) == 1694
# assert all([c.isalpha() or c.isspace() for c in norm_latin_text])
# assert norm_latin_text == norm_latin_text.lower()

# print("\n(Passed!)")

print(norm_latin_text)


from collections import defaultdict
import itertools as it # Hint!

def update_pair_counts (pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict
    ###
    ### YOUR CODE HERE
    ###
    for combination in it.permutations(itemset,2):
        pair_counts[combination] += 1
        
def update_item_counts(item_counts, itemset):
    ###
    ### YOUR CODE HERE
    ###
    for item in itemset:
        item_counts[item] += 1        
        
def filter_rules_by_conf (pair_counts, item_counts, threshold):
    rules = {} # (item_a, item_b) -> conf (item_a => item_b)
    ###
    ### YOUR CODE HERE
    ###
    for k, v in pair_counts.items():
        val = v / item_counts[k[0]]
        if val >= threshold:
            rules[k] = val
    return rules

def find_assoc_rules(receipts, threshold):
    ###
    ### YOUR CODE HERE
    ###
    pair_counts = defaultdict(int)
    item_counts = defaultdict(int)
    for item in receipts:
        update_pair_counts(pair_counts, item)
        update_item_counts(item_counts, item)
    rules = filter_rules_by_conf (pair_counts, item_counts, threshold)
    return rules        
