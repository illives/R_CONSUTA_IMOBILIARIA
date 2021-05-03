
from Resources.web_resources import web_tools

#-----------------Variaveis de Ambiente---------------------------------------------------
driverpath = 'D:\\02.NOVOBOT\\R_CONSULTA_IMOB\\Driver\\chromedriver.exe'
pathfile = 'D:\\02.NOVOBOT\\R_CONSULTA_IMOB\\File\\'
driverpath = 'D:\\02.GIT_REPOSITORY\\R_CONSULTA_IMOB\\R_CONSUTA_IMOBILIARIA\\Driver\\chromedriver.exe'
pathfile = 'D:\\02.GIT_REPOSITORY\\R_CONSULTA_IMOB\\R_CONSUTA_IMOBILIARIA\\File'
#----------------------------------------------------------------------------------------
print('R_CONSULTA_IMOB\nDesenvolvido por William Souza (c) Copyright\n')

web_tools.zapimoveis(driverpath, pathfile, True)