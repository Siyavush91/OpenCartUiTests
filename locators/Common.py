class Common:

    class user_login:
        email_input = {'css': '#input-email'}
        password_input = {'css': '#input-password'}
        login_button = {'css': 'input[value=Login]'}

    class search:
        search_field = {'css': "#search"}

    class nav_top:
        link_list = {'css': "#top-links"}
        phone_num = {'css': link_list['css'] + " > ul > li:nth-child(1)"}
        my_account_drop = {'css': link_list['css'] + " > ul > li.dropdown"}
        register_button = {'css': my_account_drop['css'] + " > ul > li:nth-child(1)"}
        login_button = {'css': my_account_drop['css'] + " > ul > li:nth-child(2)"}
        wish_list = {'css': link_list['css'] + " > ul > li:nth-child(3)"}
        shopping_cart = {'css': link_list['css'] + " > ul > li:nth-child(4)"}
        checkout = {'css': link_list['css'] + " > ul > li:nth-child(5)"}
        login_form = {'css': "#content > div > div:nth-child(2) > div"}
