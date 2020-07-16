def text_recognition(str0, f):
    start = 0
    n = len(str0)
    sentence = []

    while start != n:
        for last_letter in range(n, start, -1):
            if str0[start:last_letter] in f:
                sentence.append(str0[start:last_letter])
                start = last_letter
                break
            elif last_letter - start == 1:
                sentence.append(str0[start:last_letter])
                start = last_letter
                break
    return sentence

def text_recognition_reverse(str0, f):
    n = len(str0)
    end = n
    sentence = []

    while end != 0:
        for item in range(0, end):
            if str0[item:end] in f:
                sentence.append(str0[item:end])
                end = item
                break
            elif end - item == 1:
                sentence.append(str0[item:end])
                end = item
                break
    return sentence[::-1]

def text_recognition_both(direct, reverse, f):
    d = 0
    for i in direct:
        if i in f:
            d += 1

    r = 0
    for i in reverse:
        if i in f:
            r += 1

    if d < r: return reverse
    else: return direct

try:
    with open('1000.txt', 'r') as f:
        lines = f.readlines()
    sent = []
    for item in lines:
        sent.append(item.split()[0].lower())
    r = text_recognition_reverse('peopletableworldcar', sent)
    d = text_recognition('peopletableworldcar', sent)
    print(f'Reverse recognition: {r}')
    print(f'Direct recognition{d}')
    print('The best choice: ',text_recognition_both(d, r, sent))

finally:
    f.close()
