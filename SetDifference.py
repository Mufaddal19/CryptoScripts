with open('ff.txt', 'r') as file1:
    with open('hh.txt', 'r') as file2:
        same = set(file1).difference(file2)

same.discard('\n')

with open('fh.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
