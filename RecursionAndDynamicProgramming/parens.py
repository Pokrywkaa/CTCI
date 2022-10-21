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

print(generate_parens(3))

