def add_user(sn:dict, username:str, fullname:str) -> bool:
try:
        if username in sn:
            return False                   # user existed before, so nothing is added
        sn[username] = (fullname, [])      # new user starts with an empty friend list
        return True

def add_friend(sn:dict, user1:str, user2:str) -> bool:


def get_friends(sn:dict, user1:str, distance:int) -> list:


def save_network(filename:str, sn:dict) -> None:


def load_network(filename:str) -> dict:



def main():