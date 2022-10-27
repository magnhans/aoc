from IPython import embed

with open("1_input.txt", "r") as f:
    l = f.readlines()

    totalt = 0

    prev = int(l[0])
    for i in range(1, len(l)):
        next = int(l[i])
        totalt += next > prev
        prev = next

    print(totalt)
