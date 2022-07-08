import unittest
import sys
import random
import pygame

from snake import Snake, Food, screen_width, screen_height

class TestSnake(unittest.TestCase):
    def setUp(self) -> None:
        snk = Snake()
        fruit = Food()
        self.snk = snk
        self.fruit = fruit

    # Test juego
    def test_ejecucion_del_juego(self) -> None:
        self.assertTrue(pygame.init())

    def test_juego_se_resetea_al_perder(self) -> None:
        if self.snk.reset():
            self.snk.length = 1
            self.snk.positions = [((screen_width / 2), (screen_height / 2))]
            self.snk.score = 0
        self.assertTrue(self.snk.length == 1)
        self.assertTrue(self.snk.positions == (screen_width / 2, screen_height / 2))
        self.assertTrue(self.snk.score == 0)

    # Test serpiente
    def test_correcta_creacion_de_la_serpiente(self) -> None:
        self.assertTrue(self.snk.get_head_position())

    def test_posicion_inicial_serpiente(self) -> None:
        self.assertEqual(self.snk.get_head_position(), (screen_width / 2, screen_height / 2))
        self.assertEqual(self.snk.get_head_position(), (480 / 2, 480 / 2))
        self.assertEqual(self.snk.get_head_position(), (240.0, 240.0))

    def test_posicion_de_serpiente_varia(self) -> None:
        self.assertNotEqual(self.snk.get_head_position(), (screen_width / 2, screen_height / 2))
        self.assertNotEqual(self.snk.get_head_position(), (480 / 2, 480 / 2))
        self.assertNotEqual(self.snk.get_head_position(), (240.0, 240.0))

