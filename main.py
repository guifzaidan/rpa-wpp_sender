from RpaWpp import WppSender

usuario = WppSender(headless=False)
usuario.screen_headless(True)
usuario.get_wpp_site()

contatos = ["5531995526168","5531995526168"]
nomes = ["Guilherme","Gui"]

usuario.send_messages("Testando uma mensagem", contatos)