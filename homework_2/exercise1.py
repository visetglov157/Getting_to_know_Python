while True:
    n = int(input('enter the number of couins: '))
    if n == 1:
        print("It's just one coin")
        break
    else:
        heads = 0
        tails = 0
    for i in range(n):
        a = int(input('Heads(1) or Tails(2) - '))
        if a == 1:
            heads += 1
        else:
            tails += 1
    if heads > tails:
        print(f"Flip {tails} from tails to heads")
        break
    elif heads < tails:
        print(f"Flip {heads} from heads to tails")
        break
    else:
        print("The number of coins is the same")
        break