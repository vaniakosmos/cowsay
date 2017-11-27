MAX_WIDTH = 40
BODY = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
""".strip('\n')
EYES_MAPPER = {
    'b': '==',
    'd': 'XX',
    'g': '$$',
    'p': '@@',
    's': '**',
    't': '--',
    'w': 'OO',
    'y': '..',
    'o': 'oO'
}


def soft_wrap_text(text: str, width=MAX_WIDTH):
    words = text.split()[::-1]
    lines = []
    line = ''
    while words:
        word = words.pop()
        if len(word) > width:
            head = word[:width]
            tail = word[width:]
            if tail:
                words.append(tail)
            words.append(head)
            continue

        if len(line + word) <= width:
            line += ' ' + word
        else:
            words.append(word)
            lines.append(line.strip())
            line = ''
    if line:
        lines.append(line.strip())
    text = '\n'.join(lines)
    return text


def hard_wrap_text(text: str, width=MAX_WIDTH):
    lines = []
    while text:
        head = text[:width]
        text = text[width:]
        lines.append(head)
    text = '\n'.join(lines)
    return text


def cloud_wrap_text(text: str):
    lines = text.split('\n')

    ma = max([len(l) for l in lines])
    top = '_' * (ma + 2)
    top = f' {top} \n'
    bot = '¯' * (ma + 2)
    bot = f' {bot} \n'

    if len(lines) == 1:
        res = top + f'< {lines[0]} >\n' + bot
        return res

    res = []
    for i, line in enumerate(lines):
        line = line.ljust(ma)
        if i == 0:
            line = f'/ {line} \\'
        elif i == len(lines) - 1:
            line = f'\\ {line} /'
        else:
            line = f'| {line} |'
        res.append(line)

    res = '\n'.join(res)
    res = f'{top}{res}\n{bot}'
    return res


def test():
    text = 'bla1 bla2 hurma1 bla3 bla4 hurma2 bla5 bla6 hurma3 bla7 bla8 hurma4 bla9 bla0 hurma5'
    res = soft_wrap_text(text)
    assert len(text.split()) == len(res.split())

    text = 'bla bla hurma bla abcdlkfjdslkfjdslkjfldskjfkldsjflkdksjflds abcdlkfjdslkfjdslkjfldskjfkldsjflkdksjflds'
    res = soft_wrap_text(text)
    assert len(text.split()) + 2 == len(res.split())


def get_body(eyes='oo', tongue='  '):
    if len(eyes) != 2:
        eyes = 'oo'
    if len(tongue) != 2:
        tongue = '  '
    body = BODY.split('\n')

    eyes_line = body[1]
    eyes_line = eyes_line[:13] + eyes + eyes_line[15:]
    body[1] = eyes_line

    tongue_line = body[3]
    tongue_line = tongue_line[:13] + tongue + tongue_line[15:]
    body[3] = tongue_line

    return '\n'.join(body)


def map_eyes(eyes_type=None):
    if eyes_type in EYES_MAPPER:
        return get_body(EYES_MAPPER[eyes_type])
    return BODY


def main():
    text = 'bla1 bla2 hurma1 bla3 bla4 hurma2 bla5 bla6 hurma3 bla7 bla8 hurma4 bla9 bla0 hurma5'
    res = soft_wrap_text(text, width=1)
    res = cloud_wrap_text(res)
    print(res + get_body('oo', '()'))


if __name__ == '__main__':
    main()
