#R Vemulapalli, A Agarwala, “A Compact Embedding for Facial Expression Similarity”, CoRR, abs/1811.11283, 2018.

def check_username():

  with open("app/username.dat", "r") as reader:
    username = reader.read()
    if username == '':
      return False, None
    else:
      return True, username

def write_username(username):

  with open("app/username.dat", "w") as writer:
      writer.write(username)
