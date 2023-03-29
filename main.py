from RpaWpp import WppSender

usuario = WppSender(headless=False)
usuario.screen_headless(True)
usuario.get_wpp_site()