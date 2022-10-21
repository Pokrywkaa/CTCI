def generate_parens(remaining):
    res = []
    if remaining == 0:
        res.append('')
    else:
        prev = generate_parens(remaining-1)
        for el in prev:
            for i in range(len(el)):
                if el[i] == '(':
                    s = insert_inside(el, i)
                    res.append(s)
            res.append('()'+el)
    return set(res)

def insert_inside(str, left_index):
    left = str[0:(left_index+1)]
    right = str[(left_index+1):len(str)]
    return left + '()' + right


def add_paren(l, left_rem, right_rem, s, index):
    if left_rem < 0 or right_rem < left_rem:
        return
    if left_rem == 0 and right_rem == 0:
        elem = ''.join(s)
        l.append(elem)
    else:
        s[index] = '('
        add_paren(l, left_rem-1, right_rem, s, index+1)
        s[index] = ')'
        add_paren(l, left_rem, right_rem-1, s, index+1)

def generate_parens2(n):
    res = []
    s = ['*'] * n * 2
    add_paren(res, n, n, s, 0)
    return res    

print(generate_parens(3))
print(generate_parens2(3))

