import turtle as t
import time
import food as f
import snake as s   
import scoreboard as sb


moving_speed = 0.065


#score maintaining


# SCREEN SETUP
scr = t.Screen()
scr.bgcolor("black")
scr.setup(width=600, height=400)
scr.tracer(0)

snake = s.Snake()
food = f.Food()
food.refresh()
scr.update()

# BINDING KEYS
scr.listen()
scr.onkey(snake.up, "w")
scr.onkey(snake.left, "a")
scr.onkey(snake.down, "s")
scr.onkey(snake.right, "d")


scoring = sb.Scoreboard()

game_is_on = True 

while game_is_on:
    time.sleep(moving_speed)
    
    snake.move()

    if snake.list_tut[0].distance(food.xcor(),food.ycor()) < 15:
        moving_speed -= 0.0025
        food.refresh()
        snake.food_eaten()
        scoring.update()
    scr.update()

    head = snake.list_tut[0]
    for segment in snake.list_tut[1:len(snake.list_tut)]: 
        if head.distance(segment) < 10:
            game_is_on = False
            break

scr.update()

scr.exitonclick()
