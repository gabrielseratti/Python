def solution(number):
    soma = 0;
    # number = int(input())
    if (number < 0):
        return 0;
    else:
        for numbers in range(0, number):
            if numbers % 3 == 0 or numbers % 5 == 0:
                soma += numbers;
    return soma;

print(solution(-1));