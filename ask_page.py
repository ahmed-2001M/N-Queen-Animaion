import pygame as pg

bg_white = (112,128,144)		# chess black square bg color
bg_black = (47,79,79)


def ask(screen):
	screen.fill(bg_black)
	pg.display.update()
	clock = pg.time.Clock()
	font = pg.font.Font(None, 32)
	done = False
	inp = ""
	while not done:
		for event in pg.event.get():
			surf = font.render("Enter dimension of chessboard then press ENTER: "+inp, True, (0,0,0), bg_black)
			rect = surf.get_rect()
			rect.center = (400, 100)
			screen.blit(surf,rect)
			pg.display.update()
			if event.type == pg.QUIT:
				done = True
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					done = True
				elif event.key == pg.K_BACKSPACE:
					inp = inp[:-1]
				else:
					inp+=event.unicode
	return inp
	# clock.tick(30)