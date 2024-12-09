print('''  ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
''')

print("Welcome to Treasure Island. Your mission is to find the treasure! ")

l_or_r = input("Where do you want to go first? Choose l for left or r for right. ")

if not l_or_r == 'l':
    print("Uh oh ): Your fell into a hole. Game Over.")

else:
    s_or_w = input("What do you want to do next swim or wait? Choose s for swim or w for wait ")
    if not s_or_w == 'w':
        print("Oh noo! You got attacked by a trout. Game Over ): ")
    else:
        door = input("Which door do you want to select? Choose r for red, b for blue or y for yellow ")
        if door == 'b':
            print("You got eaten by beasts. Game Over ): ")
            print("Good try!")
        elif door == 'r':
            print("You got burned by fire. Game Over ): ")
            print("That is one way to die")
        elif door == 'y':
            print("You WIN!!!!!!!!!!")
            print("WOHOOOOOOOOOOOOOOOOOOOOOO")
        else :
            print("You did not follow instructions game over......")
        
