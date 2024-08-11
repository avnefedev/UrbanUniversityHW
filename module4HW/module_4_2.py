def test_function():
    print('Hello')
    def inner_function():
        print('Я в области видимости test_function')
    inner_function()


test_function()