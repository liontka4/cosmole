import random
import time
exit = True
while (exit == True):
	def print_p():
		global en_vec
		if en_vec == 1:
			print("Складка движется по орбите:")
			print("ЮГ -> СЕВЕР")
			print("")
		elif en_vec == 2:
			print("Складка движется по орбите:")
			print("СЕВЕР -> ЮГ")
			print("")
		elif en_vec == 3:
			print("Складка движется по орбите:")
			print("ЗАПАД -> ВОСТОК")
			print("")
		else:
			print("Складка движется по орбите:")
			print("ВОСТОК -> ЗАПАД")
			print("")

	def radar():
		global command2, en_vec
		global map
		change = False
		for i in range(4):
			if change == True:
				break
			for j in range(4):
				jE = j
				jW = j
				iN = i
				iS = i
				iE = j
				iW = j
				jN = i
				jS = i
			
				##ЮГ
				if i + 1 <= 3:
					iS = i + 1
				else:
					iS = 0
				#СЕВЕР
				if i - 1 >= 0:
					iN = i - 1
				else:
					iN = 3	
				#ВОСТОК
				if j + 1 <= 3:
					jE = j + 1
				else:
					jE = 0
				#ЗАПАД	
				if j - 1 >= 0:
					jW = j - 1
				else:
					jW = 3

				if map[i][j] == 1:				
					if map[iN][j] == 2:
						if command2 == "r":
							print("Складка замечена на:")
							print("CЕВЕРЕ")
							print("")
							change = True
							break
						elif command2 == "p":
							print_p()
							change = True
							break
					elif map[iN][jE] == 2:
						if command2 == "r":
							print("Складка замечена на:")
							print("СЕВЕРО-ВОСТОКЕ")
							print("")
							change = True
							break
						elif command2 == "p":
							print_p()
							change = True
							break
					elif map[iS][jW] == 2:
						if command2 == "r":
							print("Складка замечена на:")
							print("ЮГО-ЗАПАДЕ")
							print("")
							change = True
							break
						elif command2 == "p":
							print_p()
							change = True
							break
					elif map[i][jE] == 2:
						if command2 == "r":
							print("Складка замечена на:")
							print("ВОСТОКЕ")
							print("")
							change = True
							break
						elif command2 == "p":
							print_p()
							change = True
							break
					elif map[iS][jE] == 2:
						if command2 == "r":
							print("Складка замечена на:")
							print("ЮГО-ВОСТОКЕ")
							print("")
							change = True
							break
						elif command2 == "p":
							print_p()
							change = True
							break
					elif map[iS][j] == 2:
						if command2 == "r":
							print("Складка замечена на:")
							print("ЮГЕ")
							print("")
							change = True
							break
						elif command2 == "p":
							print_p()
							change = True
							break
					elif map[i][jW] == 2:
						if command2 == "r":
							print("Складка замечена на:")
							print("ЗАПАДЕ")
							print("")
							change = True
							break
						elif command2 == "p":
							print_p()
							change = True
							break
					elif map[iN][jW] == 2:
						if command2 == "r":
							print("Складка замечена на:")
							print("CЕВЕРО-ЗАПАДЕ")
							print("")
							change = True
							break
						elif command2 == "p":
							print_p()
							change = True
							break
					else:
						print("Складки поблизости нет")
						change = True
						break
		change = False
						
	def move():
		global command
		global command2
		global g_o
		change = False
		if command == "n":
			print("")
			print("КРОТ ДВИЖЕТСЯ НА СЕВЕР")
			print("")
			for i in range(4):
				if change == True:
					break
				for j in range(4):
					if map[i][j] == 1:
						if i == 0:
							if map[3][j] != 2:
								map[i][j] = 0
								map[3][j] = 1
								change = True
								break
							else:
								print("")
								print("ВЫ ПОГЛОЩЕНЫ СКЛАДКОЙ")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
						else:
							if map[i - 1][j] != 2:
								map[i - 1][j] = 1
								map[i][j] = 0
								change = True
								break
							else:
								print("")
								print("ВЫ ПОГЛОЩЕНЫ СКЛАДКОЙ")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
		elif command == "s":
			print("")
			print("КРОТ ДВИЖЕТСЯ НА ЮГ")
			print("")
			for i in range(4):
				if change == True:
					break
				for j in range(4):
					if map[i][j] == 1:
						if i == 3:
							if map[0][j] != 2:
								map[i][j] = 0
								map[0][j] = 1
								change = True
								break
							else:
								print("")
								print("ВЫ ПОГЛОЩЕНЫ СКЛАДКОЙ")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
						else:
							if map[i + 1][j] != 2:
								map[i + 1][j] = 1
								map[i][j] = 0	
								change = True
								break
							else:
								print("")
								print("ВЫ ПОГЛОЩЕНЫ СКЛАДКОЙ")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
		elif command == "e":
			print("")
			print("КРОТ ДВИЖЕТСЯ НА ВОСТОК")
			print("")
			for i in range(4):
				for j in range(4):
					if map[i][j] == 1:
						if j == 3:
							if map[i][0] != 2:
								map[i][0] = 1
								map[i][j] = 0
								break
							else:
								print("")
								print("ВЫ ПОГЛОЩЕНЫ СКЛАДКОЙ")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
								
						else:
							if map[i][j + 1] != 2:
								map[i][j + 1] = 1
								map[i][j] = 0
								break
							else:
								print("")
								print("ВЫ ПОГЛОЩЕНЫ СКЛАДКОЙ")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
								
		elif command == "w":
			print("")
			print("КРОТ ДВИЖЕТСЯ НА ЗАПАД")
			print("")
			for i in range(4):
				for j in range(4):
					if map[i][j] == 1:
						if j == 0:
							if map[i][3] != 2:
								map[i][3] = 1
								map[i][j] = 0
								break
							else:
								print("")
								print("ВЫ ПОГЛОЩЕНЫ СКЛАДКОЙ")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
								
						else:
							if map[i][j - 1] != 2:
								map[i][j - 1] = 1
								map[i][j] = 0
								break
							else:
								print("")
								print("ВЫ ПОГЛОЩЕНЫ СКЛАДКОЙ")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
								
		change = False

	def en_move():
		global map
		global g_o
		global en_vec
		change = False
	#c юга на север
		if en_vec == 1:
			for i in range(4):
				if change == True:
					break
				for j in range(4):
					if map[i][j] == 2:
						if i == 0:
							if map[3][j] == 1:
								print("")
								print("СКЛАДКА ПОГЛОТИЛА ВАС")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
							else:
								map[3][j] = 2
								map[i][j] = 0
								change = True
								break
						else:
							if map[i - 1][j] == 1:
								print("")
								print("СКЛАДКА ПОГЛОТИЛА ВАС")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
							else:
								map[i - 1][j] = 2
								map[i][j] = 0
								change = True
								break
	# c севера на юг
		elif en_vec == 2:
			for i in range(4):
				if change == True:
					break
				for j in range(4):
					if map[i][j] == 2:
						if i == 3:
							if map[0][j] == 1:
								print("")
								print("СКЛАДКА ПОГЛОТИЛА ВАС")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
							else:
								map[0][j] = 2
								map[i][j] = 0
								change = True
								break
						else:
							if map[i + 1][j] == 1:
								print("")
								print("СКЛАДКА ПОГЛОТИЛА ВАС")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
							else:
								map[i + 1][j] = 2
								map[i][j] = 0	
								change = True
								break
	#c востока на запад
		elif en_vec == 4:
			for i in range(4):
				for j in range(4):
					if map[i][j] == 2:
						if j == 0:
							if map[i][3] == 1:
								print("")
								print("СКЛАДКА ПОГЛОТИЛА ВАС")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
							else:
								map[i][3] = 2
								map[i][j] = 0
								break
						else:
							if map[i][j - 1] == 1:
								print("")
								print("СКЛАДКА ПОГЛОТИЛА ВАС")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
							else:
								map[i][j - 1] = 2
								map[i][j] = 0
								break
		else:
	#c запада на восток
			for i in range(4):
				for j in range(4):
					if map[i][j] == 2:
						if j == 3:
							if map[i][0] == 1:
								print("")
								print("СКЛАДКА ПОГЛОТИЛА ВАС")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
							else:
								map[i][0] = 2
								map[i][j] = 0
								break
						else:
							if map[i][j + 1] == 1:
								print("")
								print("СКЛАДКА ПОГЛОТИЛА ВАС")
								print("")
								g_o = True
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
							else:	
								map[i][j + 1] = 2
								map[i][j] = 0
								break
		change = False
							
	def check_map():
		print(map[0][0],map[0][1],map[0][2],map[0][3])
		print(map[1][0],map[1][1],map[1][2],map[1][3])
		print(map[2][0],map[2][1],map[2][2],map[2][3])
		print(map[3][0],map[3][1],map[3][2],map[3][3])
		print("(1 - Крот, 2 - складка)")
		
	def check_map1():
		print("")
		print(map1[0][0],map1[0][1],map1[0][2],map1[0][3])
		print(map1[1][0],map1[1][1],map1[1][2],map1[1][3])
		print(map1[2][0],map1[2][1],map1[2][2],map1[2][3])
		print(map1[3][0],map1[3][1],map1[3][2],map1[3][3])
		print("")
		
	def exit_check():
		global g_o
		global command2
		global exit
		if command2 == "q":
			exit = False
			g_o = True

	def dvij():
		global map
		global map1
		global command
		global command2
		global g_o
		global level
		change = False
		if command2 == "q":
			g_o = True
		elif command2 == "n" or command2 == "s" or command2 == "e" or command2 == "w":
			command = command2
			move()
		elif command2 == "r" or command2 == "p":
			move()
			if level <= 2:
				radar()
			else:
				broken = random.randint(1,2)
				if broken == 2:
					radar()
				else: 
					print("ПЕРЕБОЙ qВ РАБОТЕ ПРИБОРОВ")
		elif command2 == "jn":
			print("")
			print("СОВЕРШАЕТСЯ СВЕРХСВЕТОВОЙ ПРЫЖОК")
			time.sleep(0.7)
			print(".")
			time.sleep(0.7)
			for i in range(4):
				if change == True:
					break
				for j in range(4):
					if map[i][j] == 1:
						if i == 0:
							if map[3][j] == 2:
								map1[3][j] = "*"
								lvl_up()
								change = True
								break
							else:
								print("ПРЫЖОК В ПУСТОТУ . АВАРИЯ")
								print("")
								x = input("Нажмите клавишу Enter")
								g_o = True
								print("")
								print("")
								print("")
						else:
							if map[i - 1][j] == 2:
								map1[i - 1][j] = "*"
								lvl_up()
								change = True
								break
							else:
								print("ПРЫЖОК В ПУСТОТУ . АВАРИЯ")
								print("")
								x = input("Нажмите клавишу Enter")
								g_o = True
			
		elif command2 == "js":
			print("")
			print("СОВЕРШАЕТСЯ СВЕРХСВЕТОВОЙ ПРЫЖОК")
			time.sleep(0.7)
			print(".")
			time.sleep(0.7)
			for i in range(4):
				if change == True:
					break
				for j in range(4):
					if map[i][j] == 1:
						if i == 3:
							if map[0][j] == 2:
								map1[0][j] = "*"
								lvl_up()
								change = True
								break
							else:
								print("ПРЫЖОК В ПУСТОТУ . АВАРИЯ")
								print("")
								x = input("Нажмите клавишу Enter")
								g_o = True
						else:
							if map[i + 1][j] == 2:
								map1[i + 1][j] = "*"
								lvl_up()
								change = True
								break
							else:
								print("ПРЫЖОК В ПУСТОТУ . АВАРИЯ")
								print("")
								x = input("Нажмите клавишу Enter")
								g_o = True
		
		elif command2 == "je":
			print("")
			print("СОВЕРШАЕТСЯ СВЕРХСВЕТОВОЙ ПРЫЖОК")
			time.sleep(0.7)
			print(".")
			time.sleep(0.7)
			for i in range(4):
				if change == True:
					break
				for j in range(4):
					if map[i][j] == 1:
						if j == 3:
							if map[i][0] == 2:
								map1[i][0] = "*"
								lvl_up()
								change = True
								break
							else:
								print("ПРЫЖОК В ПУСТОТУ . АВАРИЯ")
								x = input("Нажмите клавишу Enter")
								g_o = True
						else:
							if map[i][j + 1] == 2:
								map1[i][j + 1] = "*"
								lvl_up()
								change = True
								break
							else:
								print("ПРЫЖОК В ПУСТОТУ . АВАРИЯ")
								print("")
								x = input("Нажмите клавишу Enter")
								g_o = True
		
		elif command2 == "jw":
			print("")
			print("СОВЕРШАЕТСЯ СВЕРХСВЕТОВОЙ ПРЫЖОК")
			time.sleep(0.7)
			print(".")
			time.sleep(0.7)
			for i in range(4):
				if change == True:
					break
				for j in range(4):
					if map[i][j] == 1:
						if j == 0:
							if map[i][3] == 2:
								map1[i][3] = "*"
								lvl_up()
								change = True
								break
							else:
								print("ПРЫЖОК В ПУСТОТУ . АВАРИЯ")
								print("")
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
								g_o = True
						else:
							if map[i][j - 1] == 2:
								map1[i][j - 1] = "*"
								lvl_up()
								change = True
								break
							else:
								print("ПРЫЖОК В ПУСТОТУ . АВАРИЯ")
								print("")
								x = input("Нажмите клавишу Enter")
								print("")
								print("")
								print("")
								g_o = True
		elif command2 == "h":
			print("")
			print("КРОТ ЗАВИСАЕТ НА МЕСТЕ")
			print("")
		else:
			move()
			 
	
	def lvl_up():
		global map
		global level
		global first
		global en_vec
		global sub_start_x
		global sub_start_y
		global en_start_x
		global en_start_y
		global g_o
		global my_vec
		global command
		time.sleep(0.7)
		print(".")
		time.sleep(0.7)
		print("ПЕРЕХОД")
		time.sleep(0.7)
		print(".")
		time.sleep(0.7)	
		print(".")
		first = True
		if level <= 3:
			level += 1
			map = [[0,0,0,0],
					[0,0,0,0],
					[0,0,0,0],
					[0,0,0,0]]
			en_vec = random.randint(1,4)
			sub_start_x = random.randint(0,3)
			sub_start_y = random.randint(0,3)
			map[sub_start_y][sub_start_x] = 1
			while(True):
				en_start_x = random.randint(0,3)
				en_start_y = random.randint(0,3)
				if map[en_start_y][en_start_x] != 1:
					map[en_start_y][en_start_x] = 2
					break
			g_o = False
			first = True
			my_vec = random.randint(1,4)
			if my_vec == 1:
				command = "n"
			elif my_vec == 2:
				command = "w"
			elif my_vec == 3:
				command = "e"
			else:
				command = "s"	
	
	
	#ПРОГРАММА

	
	map = [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]]
		
	map1 = [["","","",""],
		["","","",""],
		["","","",""],
		["","","",""]]

	en_vec = random.randint(1,4)
	sub_start_x = random.randint(0,3)
	sub_start_y = random.randint(0,3)
	map[sub_start_y][sub_start_x] = 1
	while(True):
		en_start_x = random.randint(0,3)
		en_start_y = random.randint(0,3)
		if map[en_start_y][en_start_x] != 1:
			map[en_start_y][en_start_x] = 2
			break
	g_o = False
	exit = False
	first = True
	level = 1
	my_vec = random.randint(1,4)
	if my_vec == 1:
		command = "n"
	elif my_vec == 2:
		command = "w"
	elif my_vec == 3:
		command = "e"
	else:
		command = "s"	





	print("")
	print("")
	print("._.    __                _____        ")
	print("| |   / /  ___   ____   /     \   ___ ")
	print("|_| / /   / _ \ / ___\ /  \ /  \ / _ \ ")
	print("|-|  \ \ ( <_> )  \___/    Y    ( <_> )")
	print("| |   \_\ \___/ \____/\____|__  /\___/")  
	print("|_|._.    __           ___________    ")     
	print("   | |   / /______   __\__    ___/   ")      
	print("   |_| / /  \____ \ / _ \|    |    ")   
	print("   |-|  \ \ |  |_> > <_> )    |     ")    
	print("   | |   \_\|   __/ \___/|____|     ")    
	print("   |_|      |__|                    ")    
	print("")
	print("        игра Тимофея Усикова    ")
	print("                2022 г. ")
	print("")
	print("")
	time.sleep(1)
	print(" - Исследование космоса достигает")
	print("пределов: открыты пространственные")
	print("складки. Капитан, вам поручается")
	print("управление космическим кораблём Крот")
	print("для их исследования. Используйте")
	print("при переходе сверхсветовой ускоритель.")
	print("Но помните, если рывок будет направлен")
	print("вне складки, произойдёт авария.")
	print("")
	print("")
	time.sleep(1)
	print("КОМАНДЫ")
	print("")
	print("n  - north      - курс на север")
	print("jn - jump north - прыжок на север")
	print("s  - south      - курс на юг")
	print("js - jump south - прыжок на юг")
	print("e  - east       - курс на восток")
	print("je - jump east  - прыжок на восток")
	print("w  - west       - курс на запад")
	print("jw - jump west  - прыжок на запад")
	print("h  - hold       - зависнуть на месте")
	print("p  - periscope  - перископ")
	print("r  - radar      - радар")
	print("q  - close      - выход")
	print("")
	print("Нажмите клавишу Enter")
	print("")
	x = input()
	if(x == "q"):
		exit = False
		break
	print("")
	print("")
	print("")
	while (True):
		if first == False:
			if level == 1:
				check_map()
			en_move()
			if g_o == True:
				break
			print("")
			time.sleep(0.7)
			print(".")
			time.sleep(0.7)
			print(".")
			time.sleep(0.7)
			print("Складка изменила положение!!!")
			time.sleep(0.7)
			print(".")
			time.sleep(0.7)
			print(".")
		else:
			if level == 1:
				print("")
				print("ПРЕДВАРИТЕЛЬНЫЙ ОТЧЁТ")
				print("Складка находится в зоне видимости.")
				print("Все приборы в исправности.")
				print("Команда Крота готовится к сверхсветовому прыжку.")
			elif level == 2:
				print("")
				print("ПОСЛЕ ПЕРЕХОДА")
				time.sleep(0.7)
				print("Мы прошли через складку. Свет исчез, ничего не видно.")
				time.sleep(0.7)
				print("Однако радар и перископ продолжают работать.")
				time.sleep(0.7)
				print("Поблизости эта же или другая складка.")
				time.sleep(0.7)
				print("Единственная возможность как-то выбраться отсюда - нырнуть в неё.")
				time.sleep(0.7)
			elif level == 3:
				print("")
				print("ОЧЕРЕДНОЙ ОТЧЁТ")
				time.sleep(1)
				print("Очередной переход...")
				time.sleep(1)
				print("Приборы начинают отказывать...")
				time.sleep(1)
				print("Надежды мало...")
				time.sleep(1)
			else:
				print("")
				print("Нам удалось вернуться домой. Здесь, на Земле, когда я смотрю на ночное небо, то говорю себе:")
				check_map1()
				print(" - Где-то с другой стороны... есть созвездие твоего пути.")
				print("")
				print("")
				x = input("Нажмите клавишу Enter")
				print("")
				print("")
				print("")
				break	
		print("")	
		print("|------------------------------")	
		command2 = input("| command: ")
		print("|------------------------------")
		time.sleep(1)
		exit_check()
		if g_o == True:
			break
		first = False
		dvij()
		if g_o == True:
			break


