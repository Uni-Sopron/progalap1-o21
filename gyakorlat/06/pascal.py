def pascal_next_row(row):
    if row == []:
        return [1]
    next = [1]
    #for i in range(len(row)-1):
    #    next.append(row[i] + row[i+1])
    next += [row[i] + row[i+1] for i in range(len(row)-1)]
    next.append(1)
    return next

def pascal_lines(num_lines):
    lines = []
    next_row = []
    for i in range(num_lines):
        next_row = pascal_next_row(next_row)
        #print(next_row)
        lines.append(next_row)
    return lines

def print_centered_lines(lines):
    last_line_str = ''
    for num in lines[-1]:
        last_line_str += str(num) + ' '
    width = len(last_line_str)
    for i in range(len(lines)):
        #print((len(lines) - i - 1) * ' ', end='')
        #print(lines[i])
        #for num in lines[i]:
        #    print(num, end=' ')
        #print('')
        line_str = ''
        for num in lines[i]:
            line_str += str(num) + ' '
        left_padding = (width - len(line_str)) // 2
        print(left_padding*' ' + line_str)

pascal = pascal_lines(20)
#print(pascal)
print_centered_lines(pascal)
