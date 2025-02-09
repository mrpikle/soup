# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
import typing


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "mrpikle",  # TODO: Your Battlesnake Username
        "color": "#880112",  # TODO: Choose color
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:
    
    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    # We've included code to prevent your Battlesnake from moving backwards
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"
    width = game_state["board"]["width"] - 1
    height = game_state["board"]["height"] - 1
    food = game_state["board"]["food"]
    print(len(game_state["you"]["body"]))
    for i in range(len(game_state["you"]["body"]) - 2):
        my_tails = game_state["you"]["body"][(i+2)]
        if my_head["y"] + 1 == my_tails["y"] and my_head["x"] == my_tails["x"]:
            is_move_safe["up"] = False
        if my_head["y"] - 1 == my_tails["y"] and my_head["x"] == my_tails["x"]:
            is_move_safe["down"] = False
        if my_head["x"] + 1 == my_tails["x"] and my_head["y"] == my_tails["y"]:
            is_move_safe["right"] = False
        if my_head["x"] - 1 == my_tails["x"] and my_head["y"] == my_tails["y"]:
            is_move_safe["left"] = False
        
        print("left:" + str(is_move_safe["left"]))
        print("right:" + str(is_move_safe["right"]))
        print("up:" + str(is_move_safe["up"]))
        print("down:" + str(is_move_safe["down"]))
        print(str(my_tails["x"]) + ":" + str(my_tails["y"]))
        print(" ")
    print(str(my_head["x"]) + ":" + str(my_head["y"]))
    if my_neck["x"] < my_head["x"]:  # Neck is left of head, don't move left
        is_move_safe["left"] = False
    elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
        is_move_safe["right"] = False
    elif my_neck["y"] < my_head["y"]:  # Neck is below head, don't move down
        is_move_safe["down"] = False
    elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
        is_move_safe["up"] = False
        #print("test")
        #print(my_head["y"])
    #if my_head["y"] + 1 == my_tails["y"]:
    #    print(my_tails["y"])
    if my_head["y"] + 1 > height:
        is_move_safe["up"] = False
    if my_head["y"] - 1 < 0:
        is_move_safe["down"] = False
    if my_head["x"] + 1 > width:
        is_move_safe["right"] = False
    if my_head["x"] - 1 < 0:
        is_move_safe["left"] = False
    print("left:" + str(is_move_safe["left"]))
    print("right:" + str(is_move_safe["right"]))
    print("up:" + str(is_move_safe["up"]))
    print("down:" + str(is_move_safe["down"]))

    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
    # board_width = game_state['board']['width']
    # board_height = game_state['board']['height']

    # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
    # my_body = game_state['you']['body']

    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    # opponents = game_state['board']['snakes']

    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}
    foodnum = 0
    # Choose a random move from the safe ones
    for e in range(len(food)):
        if food[foodnum]["x"] == 0 or food[foodnum]["y"] == 0 or food[foodnum]["y"] == height or food[foodnum]["x"] == width:
            if foodnum + 1 in range(len(food)):
                foodnum += 1
    print(food[foodnum])
    if food[foodnum]["x"] < my_head["x"] and is_move_safe["left"] and food[foodnum]["x"] != 0:
        next_move = "left"
    elif food[foodnum]["y"] < my_head["y"] and is_move_safe["down"] and food[foodnum]["y"] != 0:
        next_move = "down"
    elif food[foodnum]["y"] > my_head["y"] and is_move_safe["up"] and food[foodnum]["y"] != height:
        next_move = "up"
    elif food[foodnum]["x"] > my_head["x"] and is_move_safe["right"] and food[foodnum]["x"] != width:
        next_move = "right"
    else:
        next_move = random.choice(safe_moves)

    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
    # food = game_state['board']['food']

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})
