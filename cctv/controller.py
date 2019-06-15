from cctv.model import CCTVModel

class CCTVController:
    def __init__(self):
        self._m = CCTVModel()

    def test(self):
        m = self._m
        m.hook_process()