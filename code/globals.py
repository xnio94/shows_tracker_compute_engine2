import textwrap


def pri(s):
    with open('/opt/app/logs', 'a') as f:
        f.write(str(s) + '\n')
    print(s)

def pri2(s):
    wrapped_text = '\n'.join(textwrap.wrap(s, 170))
    with open('/opt/app/logs', 'a') as f:
        f.write(wrapped_text + '\n')
    print('\n'.join(textwrap.wrap(s, 170)))


batch_duration = 7 # need to be < 10
minute = "m"
