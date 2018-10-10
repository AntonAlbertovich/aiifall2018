import chess_bin_functions
import pickle

new_bin_file = open("mega_chess.bin", "wb")


game_data =[]



pickle.dump(game_data, new_bin_file)
new_bin_file.close()
print("Start")

chess_bin_functions.write_file("deep_blue_example.txt")
print("End")

chess_bin_functions.read_file_sizes()




