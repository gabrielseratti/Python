def solution(string):
    reverse = ''
    for x in reversed(string):
        reverse += x;
    return reverse;

print(solution('String'))
