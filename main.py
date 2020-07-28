score = 0 
def Start(): 
  PlayerOne = str(input(" Choose the first number..."))
  if PlayerOne == "first":
    print("PlayerOne starts")

def Add():
  s = 0
  PlayerMove = str(input("add one or two each move..."))
  if PlayerMove == "1":
    s += 1
    print(score)
  if PlayerMove == "2": 
    s += 2 
    print(score)
  return s

Start()

while score < 20:
  score = score + Add()

