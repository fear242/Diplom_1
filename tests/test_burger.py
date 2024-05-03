class TestBurger:

    def test_burger_creation(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_burger_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    def test_burger_remove_ingredient(self, full_burger):
        full_burger.remove_ingredient(0)
        assert len(full_burger.ingredients) == 1

    def test_burger_move_ingredient(self, full_burger, mock_sauce):
        full_burger.move_ingredient(0, 1)
        assert full_burger.ingredients[1] == mock_sauce

    def test_burger_get_price_with_ingredients(self, full_burger):
        assert full_burger.get_price() == 800

    def test_burger_get_receipt(self, full_burger):
        assert full_burger.get_receipt() == ('(==== white bun ====)\n'
                                             '= sauce sour cream =\n'
                                             '= filling dinosaur =\n'
                                             '(==== white bun ====)\n'
                                             '\n'
                                             'Price: 800')
