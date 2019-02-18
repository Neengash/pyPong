from ..bar import Bar

class TestBar(object):

    def test_update_pos_no_acceleration(self):
        bar = Bar(0, 0, None, None)
        bar.vely = 5
        bar.update()

        assert 5 == bar.posy

    def test_update_pos_no_base_speed(self):
        bar = Bar(0, 5, None, None)

        assert 5 == bar.posy
        assert 0 == bar.vely
        assert 0 == bar.accy

        bar.vely = 0
        bar.accy = 10
        bar.update()

        assert 15 == bar.posy
        assert 10 == bar.vely
        assert 10 == bar.accy

    def test_update_speed_and_accel(self):
        bar = Bar(0, 5, None, None)

        assert 5 == bar.posy
        assert 0 == bar.vely
        assert 0 == bar.accy

        bar.vely = 5
        bar.accy = 10
        bar.update()

        assert 20 == bar.posy
        assert 15 == bar.vely
        assert 10 == bar.accy
