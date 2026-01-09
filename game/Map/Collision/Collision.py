A_coord = [60, 60]
B_coord = [64, 64]
A_sprite = {'img': 0, 'u': 0, 'v': 0, 'w': 8, 'h': 8, 'colkey': 0}
B_sprite = {'img': 0, 'u': 8, 'v': 0, 'w': 8, 'h': 8, 'colkey': 0}


def chevauchement_pixels(A_coord, B_coord, A_sprite, B_sprite):
    max_x1 = max(A_coord[0], B_coord[0])
    max_y1 = max(A_coord[1], B_coord[1])
    min_x2 = min(A_coord[0] + A_sprite['w'], B_coord[0] + B_sprite['w'])
    min_y2 = min(A_coord[1] + A_sprite['h'], B_coord[1] + B_sprite['h'])

    chevauchement = False

    if max_x1 < min_x2 and max_y1 < min_y2:
        for y in range(max_y1, min_y2):
            for x in range(max_x1, min_x2):
                A_couleur = pyxel.images[A_sprite['img']].pget(x - A_coord[0], y - A_coord[1])
                B_couleur = pyxel.images[B_sprite['img']].pget(x - B_coord[0], y - B_coord[1])
                if A_couleur != A_sprite['colkey'] and B_couleur != B_sprite['colkey']:
                    chevauchement = True

    return chevauchement

if chevauchement == True:
    A_sprite['colkey'] = 1
    B_sprite['colkey'] = 1