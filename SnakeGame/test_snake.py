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

    def test_si_hay_colision_de_serpiente_consigo_misma_el_juego_se_resetea(self) -> None:
        if len(self.snk.positions) > 2:
            self.snk.reset()
        self.assertTrue(self.snk.reset())

    def test_posicion_inicial_serpiente(self) -> None:
        self.assertEqual(self.snk.get_head_position(), (screen_width / 2, screen_height / 2))
        self.assertEqual(self.snk.get_head_position(), (480 / 2, 480 / 2))
        self.assertEqual(self.snk.get_head_position(), (240.0, 240.0))

    def test_posicion_de_serpiente_varia(self) -> None:
        self.assertNotEqual(self.snk.get_head_position(), (screen_width / 2, screen_height / 2))
        self.assertNotEqual(self.snk.get_head_position(), (480 / 2, 480 / 2))
        self.assertNotEqual(self.snk.get_head_position(), (240.0, 240.0))

    def test_colision_de_serpiente_consigo_misma(self) -> None:
        if len(self.snk.positions) > 2:
            self.snk.length = 1
        self.assertTrue(self.snk.length == 1)

    def test_si_hay_colision_de_serpiente_consigo_misma_el_juego_se_resetea(self) -> None:
        if len(self.snk.positions) > 2:
            self.snk.reset()
        self.assertTrue(self.snk.reset())

    def test_colision_de_serpiente_con_paredes(self) -> None:
        pass

    # Test fruta
    def test_creacion_de_fruta(self) -> None:
        self.assertTrue(self.fruit.position)
        self.assertTrue(self.fruit.get_food_position())

    def test_aparicion_de_fruta_al_azar(self) -> None:
        self.assertTrue(self.fruit.randomize_position() is None)

    def test_colision_de_fruta_y_serpiente(self) -> None:
        self.assertTrue(self.snk.get_head_position() == self.fruit.get_food_position())
        self.assertEquals(self.snk.get_head_position(), self.fruit.get_food_position())

    # Test marcador
    def test_score_empieza_en_cero(self) -> None:
        self.assertTrue(self.snk.score == 0)

    def test_highscore_empieza_en_cero(self) -> None:
        self.assertTrue(self.snk.highscore == 0)

    def test_score_y_highscore_son_iguales(self) -> None:
        self.assertEquals(self.snk.highscore, self.snk.score)

    def test_highscore_es_mayor_que_score(self) -> None:
        self.assertTrue(self.snk.highscore > self.snk.score)
        
    def test_aumento_de_score_cuando_come_fruta(self) -> None:
        self.snk.score = 0
        if self.snk.get_head_position() == self.fruit.position:
            self.snk.score += 1
        self.assertTrue(self.snk.score == 1)

    def test_highscore_se_actualiza_cuando_score_lo_supera(self) -> None:
        if self.snk.highscore <= self.snk.score:
            self.snk.highscore = self.snk.score
        self.assertEquals(self.snk.highscore, self.snk.score)


if __name__ == '__main__':
    unittest.main()


