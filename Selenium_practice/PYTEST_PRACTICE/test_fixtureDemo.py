import pytest


# Instead of writing down setup in each function inside the class the below line will make sure to use the setup in all the available function at once.
@pytest.mark.usefixtures('setup')
class TestExample:

    def test_fixtureDemo(self):
        print('I will execute steps in fixture demo method 01')

    def test_fixtureDemo1(self):
        print('I will execute steps in fixture demo method 02')

    def test_fixtureDemo2(self):
        print('I will execute steps in fixture demo method 03')
