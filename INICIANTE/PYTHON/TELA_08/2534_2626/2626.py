PEDRA = 'pedra'
PAPEL = 'papel'
TESOU = 'tesoura'

def is_draw(a, b, c):
    if a == PEDRA and b == PEDRA and c == PEDRA:
        return True
    if a == PAPEL and b == PAPEL and c == PAPEL:
        return True
    if a == TESOU and b == TESOU and c == TESOU:
        return True
    if a == PEDRA and b == PAPEL and c == TESOU:
        return True
    if a == PEDRA and b == TESOU and c == PAPEL:
        return True
    if a == PAPEL and b == PEDRA and c == TESOU:
        return True
    if a == PAPEL and b == TESOU and c == PEDRA:
        return True
    if a == TESOU and b == PAPEL and c == PEDRA:
        return True
    if a == TESOU and b == PEDRA and c == PAPEL:
        return True
    if a == TESOU and b == TESOU and c == PAPEL:
        return True
    if a == TESOU and b == PAPEL and c == TESOU:
        return True
    if a == PAPEL and b == TESOU and c == TESOU:
        return True
    if a == PAPEL and b == PAPEL and c == PEDRA:
        return True
    if a == PAPEL and b == PEDRA and c == PAPEL:
        return True
    if a == PEDRA and b == PAPEL and c == PAPEL:
        return True
    if a == PEDRA and b == PEDRA and c == TESOU:
        return True
    if a == PEDRA and b == TESOU and c == PEDRA:
        return True
    if a == TESOU and b == PEDRA and c == PEDRA:
        return True
    return False

def is_winner(a, b, c):
    if a == TESOU and b == PAPEL and c == PAPEL:
        return True
    if a == PEDRA and b == TESOU and c == TESOU:
        return True
    if a == PAPEL and b == PEDRA and c == PEDRA:
        return True
    return False

while True:
    try:
        dodo, leo, pepper = input().lower().strip().split()
        if is_draw(dodo, leo, pepper):
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        elif is_winner(dodo, leo, pepper):
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        elif is_winner(leo, dodo, pepper):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif is_winner(pepper, leo, dodo):
            print("Urano perdeu algo muito precioso...")
        else:
            raise ValueError("invalid game")
    except:
        break
