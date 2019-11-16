class Catalog:

    class filter_product:
        accept_filter = {'xpath': "//button[@id='button-filter']"}
        input_product_name = {'css': "#input-name"}


    class productList:
        product_list = {'css': '#form-product'}
        product_table = {'css': product_list['css'] + ' > div > table > tbody'}
        first_line = {'css': product_table['css'] + ' > tr:nth-child(1)'}
        edit_product = {'xpath': "//a[@data-original-title='Edit']"}
        product_check_box = {'css': "input[name='selected[]']"}


    class navigation:
        main_menu = {'css': "#column-left"}
        catalog_outs = {'id': "menu-catalog"}
        catalog_list = {'css': 'ul#collapse1'}


    class edit_products:
        catalog_list = {'css': 'ul#collapse1'}
        products = {'css': catalog_list['css'] + ' > li:nth-child(2)'}
        page_header = {'css': "div.page-header"}
        product_buttons_menu = {'css': 'div.pull-right '}
        add_new_product = {'css': product_buttons_menu['css'] + " > [data-original-title='Add New']"}
        delete_product = {'css': product_buttons_menu['css'] + " > [data-original-title='Delete']"}


    class catalog_download:
        catalog_list = {'css': 'ul#collapse1'}
        downloads = {'css': catalog_list['css'] + ' > li:nth-child(8)'}
        download_buttons_menu = {'css': 'div.pull-right '}
        add_new_button = {'css': download_buttons_menu['css'] + " > [data-original-title='Add New']"}
