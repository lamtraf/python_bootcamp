# from turtle import Turtle, Screen
# #turtle graphics is a module to make actions with object
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(200)

# my_screen = Screen()
# print(my_screen.canvheight)
# #method from turtle module. when you click on the screen, it exits.
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# table.field_names = ["Pokemon Name","Type"]
# table.add_row(["Pikachu","Electric"])
# table.add_row(["Squirtle","Water"])
# table.add_row(["Charmander","Fire"])
table.add_column("Pokemon",["Pikachu", "Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)