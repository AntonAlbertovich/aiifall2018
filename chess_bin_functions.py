import sys
import os
import re
import pickle
import shutil
import time

def write_file(file_name):
   input_file = open("mega_chess.bin", "rb")
   game_data = pickle.load(input_file)
   new_bin_file = open("mega_chess.bin", "wb")
   with open(file_name, "r") as ins:
       array = []
       start = 0
       for line in ins:
          
          if(line[0] !=""):
             sub_array = []
             
             line = re.sub('[]]', '', line) 
             sub_line = line.rstrip('\n')
             if(line[0] == "["):
                sub_line = re.sub('[[]', '', sub_line)
                sub_line = re.sub('["]', '', sub_line)
                sub_line = sub_line.split(" ")
                array.append(sub_line)
             elif(len(line[0]) != 0):
                sub_line = re.sub('[#]', '', sub_line)
                sub_line = sub_line.split(".")
                j = len(sub_line)
                x = 0
                cell = []
                for i in range(1, j):
                   temp = sub_line[i]
                   temp = temp.split(" ")
                   x = (len(temp))
                   for part in range(0, x):
                      if(temp[part] != ''):
                         try:
                            int(temp[part])
                         except ValueError:
                            cell.append(temp[part])
                array.append(cell)


   start = 0
   next_array = []
   final_array = []
   for i in range(0, len(array)):
      if(len(array[i]) != 0):
         if(array[i][0] == 'Event'):
            next_array.append(array[i])
         elif(array[i][0] == 'Site'):
            next_array.append(array[i])
         elif(array[i][0] == 'Date'):
            next_array.append(array[i])
         elif(array[i][0] == 'EventDate'):
            next_array.append(array[i])
         elif(array[i][0] == 'Round'):
            next_array.append(array[i])
         elif(array[i][0] == 'Result'):
            next_array.append(array[i])
         elif(array[i][0] == 'White'):
            next_array.append(array[i])
         elif(array[i][0] == 'Black'):
            next_array.append(array[i])
         elif(array[i][0] == 'ECO'):
            next_array.append(array[i])
         elif(array[i][0] == 'WhiteElo'):
            next_array.append(array[i])
         elif(array[i][0] == 'BlackElo'):
            next_array.append(array[i])
         elif(array[i][0] == 'PlyCount'):
            next_array.append(array[i])
            j = i + 2
            sub_array = []
            while(len(array[j]) != 0):
               for k in range(0, len(array[j])):
                  sub_array.append(array[j][k])
               j = j +1
            next_array.append(sub_array)
            final_array.append(next_array)
            next_array = []

   filter_array1 = []
   for i in range(0, len(final_array)):
      if(final_array[i][0][0] == 'Event') and (len(final_array[i]) == 13):
         passfail = 0
         for j in range(0, len(final_array[i][12])):
            if('{' in final_array[i][12][j]):
               passfail = 1
         if(passfail == 0):
            filter_array1.append(final_array[i])


   print("Done with file")
   print(file_name)
   game_data.append(filter_array1)
   pickle.dump(game_data, new_bin_file)
   input_file.close()
   new_bin_file.close()



def read_file():
   input_file = open("mega_chess.bin", "rb")
   game_data = pickle.load(input_file)


   for i in range(0, len(game_data)):
      for j in range(0, len(game_data[i])):
         print("-------------------------------------------------------------------")
         print(game_data[i][j])
         print("-------------------------------------------------------------------")

   input_file.close()

def read_file_sizes():
   input_file = open("mega_chess.bin", "rb")
   game_data = pickle.load(input_file)
   total_games = 0
   for i in range(0, len(game_data)):
         
         print("Games:", len(game_data[i]))
         total_games = total_games + len(game_data[i])
         print("-------------------------------------------------------------------")

   print("Total games in this new mega_chess.bin file: ", total_games)
   input_file.close()

def read_file_total_moves():
   input_file = open("mega_chess.bin", "rb")
   game_data = pickle.load(input_file)
   total_moves = 0
   start_time = time.time()
   for i in range(0, len(game_data)):
      for j in range(0, len(game_data[i])):
         
         total_moves = total_moves + int(game_data[i][j][11][1])

   print("-------------------------------------------------------------------")
   print("Total moves in this mega_chess.bin file: ", total_moves)
   print("clocked in %s seconds" % (time.time() - start_time))
   input_file.close()

def print_a_game(file, game):
    start_time = time.time()
    input_file = open("mega_chess.bin", "rb")
    game_data = pickle.load(input_file)
    print("clocked in %s seconds" %(time.time() - start_time))

    for i in range(0, len(game_data[file][game])):
        print("----------------------------------------------------------")
        print(game_data[file][game][i])
        print("----------------------------------------------------------")
    #    for j in range(0, len(game_data[file][game][i])):
    #        print(game_data[file][game][i][j])
    print("clocked in %s seconds" %(time.time() - start_time))
    input_file.close()

   

