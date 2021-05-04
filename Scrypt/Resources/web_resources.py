import pandas as pd
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import pyautogui as rb
from selenium import webdriver
from datetime import  date, datetime
from .debug_resources import debugar

#-----------------Variaveis de Ambiente---------------------------------------------------

pathfile_consulta = 'D:\\02.NOVOBOT\\R_CONSULTA_IMOB\\File\\Base_Consulta.csv'
#----------------------------------------------------------------------------------------
print('R_CONSULTA_IMOB\nDesenvolvido por Analytics/Logística (c) Copyright\n')
print('R_CONSULTA_IMOB\nDesenvolvido (c) Copyright\n')

class web_tools:
	
	def __init__(self, driverpath, pathfile, Debug):
		self.driverpaht = driverpath
		self.pathfile = pathfile
		self.Debug = Debug

	def zapimoveis(driverpath, pathfile, Debug = False):
		"""
		Faz consulta no ZAPIMOVEIS.
		Irá sempre buscar os dados em um arquivo 'Base_Consulta.csv' e retornar os resultados no 'Lista_consulta.csv'
		(driverpath = Diretorio do ChromeDriver da versão do navegador,
		pathfile = Diretorio dos arquivos a serem lidos ou salvos,
		Debug = False por padrão)
		"""

		Debug = Debug
		dfconsulta = pd.read_csv(pathfile + 'Base_Consulta.csv', sep = '|')
		ulitma = len((dfconsulta['DSC_BAIRRO']))
		lista_consolidada = []
		try:
			driver = webdriver.Chrome(driverpath)
			driver.maximize_window()
			driver.set_page_load_timeout(220)
			comprar_alugar = 0
			acao = ''
			while comprar_alugar <= 1:
				for k in range(0,ulitma):
					spell_search = str(dfconsulta.iloc[k,0])
					driver.maximize_window()
					driver.get('http://www.zapimoveis.com.br')
					driver.refresh()
					sleep(3)
					if comprar_alugar == 0:
						acao = str('COMPRAR')
						driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[1]/div[1]/div/button[1]').send_keys(Keys.RETURN)
					elif comprar_alugar == 1:
						acao = str('ALUGAR')
						driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[1]/div[1]/div/button[2]').send_keys(Keys.RETURN)
					else:
						pass
					driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys(spell_search)
					sleep(3)
					rb.press('enter')
					status = 0
					while status <= 7:
						sleep(1)
						try:
							elemento = driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/div/section/form/div/div[2]/div/div/p')
							status = 11
						except:
							status += 1
					if status == 11:
						while True:
							sleep(1)
							if elemento.is_displayed() == True:
								break
							else:
								driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys(spell_search)
								sleep(3)
								rb.press('enter')
						driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[2]/button').send_keys(Keys.RETURN)
						busca = driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[2]/div/div/div/input')
						contador = 0
						while contador <= 5:
							try:
								sleep(1)
								if busca.is_displayed() == True:
									driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys(spell_search)
									sleep(3)
									rb.press('enter')
									while True:
										sleep(1)
										if elemento.is_displayed() == True:
											break
										else:
											driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[2]/div/div/div/input').send_keys(spell_search)
											sleep(3)
											rb.press('enter')
									driver.find_element_by_xpath('/html/body/main/section/section[1]/div/section/form/div/div[2]/button').send_keys(Keys.RETURN)
								elif busca.is_displayed() == False:
									contador = 11
							except:
								contador += 1
						t01 = 0
						while t01 <= 3:
							sleep(1)
							try:
								driver.maximize_window()
								m2 = driver.find_element_by_xpath(f'//*[@id="app"]/section/div[3]/div[2]/section/div/div[1]/div/div[2]/div[3]/ul/li[1]/span[2]')
								t01 = 11
							except:
								driver.refresh()
								sleep(3)
								sleep(4)
								rb.hotkey('ctrl', 'shift', 'i')
								t01 +=1
						if t01 >=11:
							Select(driver.find_element_by_xpath('/html/body/main/section/div[3]/div[2]/section/header/div/div/select')).select_by_visible_text('Data Atualização')
							for k in range(2,30):
								try:
									m2 = driver.find_element_by_xpath(f'//*[@id="app"]/section/div[3]/div[2]/section/div/div[{k}]/div/div[2]/div[3]/ul/li[1]/span[2]')
									adress = driver.find_element_by_xpath(f'//*[@id="app"]/section/div[3]/div[2]/section/div/div[{k}]/div/div[2]/div[3]/p')
									hora = str(datetime.now())
									descricao = driver.find_element_by_xpath(f'//*[@id="app"]/section/div[3]/div[2]/section/div/div[{k}]/div/div[2]/div[2]/div/span')
									descGeral = driver.find_element_by_xpath('//*[@id="app"]/section/div[3]/div[2]/section/header/h1/strong')
									string = (f"{spell_search} ; {adress.text} ; {m2.text} ; {acao} ; {hora} ; {descGeral.text} ; {descricao.text}")
									lista_consolidada.append(string)
									debugar.sttus(spell_search, m2.text, adress.text, descricao.text, acao, Debug)
								except:
									pass
						elif t01 <=5:
							for k in range(2,30):
								hora = str(datetime.now())
								string = (f'{spell_search} ; NL ; NL ; {acao} ; {hora} ; NL')
								lista_consolidada.append(string)		
					else:
						hora = str(datetime.now())
						string = (f'{spell_search} ; NL ; NL ; {acao} ; {hora} ; NL')
						lista_consolidada.append(string)
				comprar_alugar += 1
		except Exception as a:
			driver.close()
			driver.quit()
			return a
		finally:
			df = pd.DataFrame(lista_consolidada)
			print(df)
			df.to_csv(pathfile + 'Lista_consulta.csv', sep = ';', index = False, encoding = 'utf_32', header = 0)
			print(df)
			driver.close()
			driver.quit()