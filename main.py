from amazon.amazon_test import AmazonTest

with AmazonTest() as bot:
    bot.land_first_page()
    # bot.login()
    # bot.search()
    bot.add_to_cart()


