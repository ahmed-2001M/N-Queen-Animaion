import pygame as pg
import queen_algo as qa
import ask_page as ask

bg_white = (112, 128, 144)  # chess black square bg color
bg_black = (47, 79, 79)

width = height = 700

dimension = 6

algo = qa.queen(dimension)

sq_size = height // dimension

max_fps = 60

queen = pg.image.load('R.png')
queen = pg.transform.scale(queen, (sq_size - 10, sq_size - 10))

images = {
    1.0: queen,
}


def main():
    global dimension
    global algo
    global sq_size
    global queen

    pg.init()
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    # -------------------------------------------------------------------------------------------------------
    dimension = int(ask.ask(screen))

    algo = qa.queen(dimension)

    sq_size = height // dimension
    queen = pg.transform.scale(queen, (sq_size - 10, sq_size - 10))

    display_board(screen)


    if (algo.back_track(screen, queen, sq_size, 0)):
        algo.back_track(screen, queen, sq_size, 0)
        pg.display.update()

        algo.print()
        show(screen)
        pg.display.update()
        clock.tick(max_fps)
        pg.display.flip()
    else:
        screen = pg.display.set_mode((800, 200))
        font = pg.font.Font(None, 32)
        surf = font.render("Solution does not Exist!", True, (0, 0, 0), bg_black)
        rect = surf.get_rect()
        rect.center = (400, 100)
        screen.blit(surf, rect)
    pg.display.update()
    # -------------------------------------------------------------------------------------------------------

    running = True
    while running:

        # screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


def display_board(screen):
    colors = [pg.Color("white"), pg.Color("gray")]

    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r + c) % 2)]
            pg.draw.rect(screen, color, pg.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


def show(screen):
    for i in range(dimension):
        for j in range(dimension):

            piece = algo.board[i][j]
            if piece == 1.0:
                screen.blit(queen, (i * sq_size, j * sq_size))
                pg.time.delay(50)
                pg.display.flip()
                pg.display.update()
            else:
                if (i + j) % 2 != 0.0:
                    pg.draw.rect(screen, "gray", pg.Rect(i * sq_size, j * sq_size, sq_size, sq_size))
                    pg.time.delay(50)
                    pg.display.flip()
                    pg.display.update()
                else:
                    pg.draw.rect(screen, "white", pg.Rect(i * sq_size, j * sq_size, sq_size, sq_size))
                    pg.time.delay(50)
                    pg.display.flip()
                    pg.display.update()


if __name__ == '__main__':
    main()
