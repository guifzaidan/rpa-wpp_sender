from RpaWpp import WppSender

usuario = WppSender()
usuario.screen_status(False)
usuario.get_wpp_site()
usuario.get_page_screenshot()