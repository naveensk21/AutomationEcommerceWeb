from amazon.amazon_test import AmazonTest

try:
    with AmazonTest() as bot:
        bot.land_first_page()
        # bot.login()
        bot.search()
        # bot.add_to_cart()
        # bot.checkout()
        bot.apply_filtration()


except Exception as e:
    if "in PATH" in str(e):
        print('You are tyring to run the script from the command line \n'
              'Please add to PATH your Selenium Drivers \n'
              'Linux: \n'
              '     PATH=$PATH:/PATH/toyour/folder/ \n'
              )
    else:
        raise




