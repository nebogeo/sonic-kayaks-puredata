import osc,time,random

temp_0 = 17
temp_1 = 17

while 1:
     print(temp_0,temp_1)
     change_0 = (0.5-random.random())*0.5
     change_1 = (0.5-random.random())*0.5
     osc.Message("/tempdiff-0",[change_0]).sendlocal(8889)
     osc.Message("/tempdiff-1",[change_1]).sendlocal(8889)
     osc.Message("/temp-0",[temp_0]).sendlocal(8889)
     osc.Message("/temp-1",[temp_1]).sendlocal(8889)
     temp_0 += change_0
     temp_1 += change_1
     time.sleep(1)
