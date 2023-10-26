import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),

    (1, 1, -1,),
    (1, 1, 1,),
    (-1, 1, 1,),
    (-1, 1, -1,),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),


    (2, 1),
    (2, 3),
    (2, 6),

    (4, 5),
    (4, 7),

    (6, 5),
    (6, 7),

    (3,7),
    (1,5)
)

surfaces = (
    (0, 1, 2, 3),
    (0, 1, 5, 4),
    (0, 4, 7, 3),
    (4, 5, 6, 7),
    (3, 2, 6, 7),
    (1, 5, 6, 2)
)

colors = (
    (1, 0, 0),
    (1, 1, 0),
    (1, 0, 1),
    (0, 0, 1),
    (0, 1, 1),
    (0, 1, 0)
)

def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        for i, vertex in enumerate(surface):
            glColor3fv(colors[i])
            # glColor3fv((1.0, 1.0, 1.0))
            glVertex3fv(vertices[vertex])
    glEnd()

def light():
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 0)) # źródło światła left, top, front

    # Ustawienie koloru światła otoczenia
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1.0, 0.0, 0.0, 1.0))

    # Ustawienie koloru światła rozproszonego
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.0, 0.0, 1.0, 1.0))

    # Ustawienie koloru światła wypukłego
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 1.0, 0.0, 1.0))
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE )

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)


    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    glTranslatef(0.5,0,0)

                if event.key == pygame.K_DOWN:
                    glTranslatef(-0.5,0,0)

        glRotatef(1, 1, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        light()
        pygame.display.flip()
        pygame.time.wait(10)

main()
