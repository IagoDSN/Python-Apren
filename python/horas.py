def calculo(tempo):

    parte = tempo.split(":")

    hor = int(parte[0])
    min = int(parte[1])
    sec = int(parte[2])

    segundos = sec + ((min + (hor * 60)) * 60)
    return segundos


print("segundos:",calculo("01:00:00"))