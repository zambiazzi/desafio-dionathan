import math

limite = int(input("Digite o número limite: "))

def primo(n):
    for i in range(1, limite):
        if i <= 1:
            print(" não é primo.")
        if i == 2:
            print(" é primo.")
        j = 3;

        while j <= math.sqrt(n):
            if (i % n == 0):
                print(" não é primo")

            j += 1;

        print(" é primo")

primo(limite);


