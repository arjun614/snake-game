from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen= Screen()
screen.setup(width=600, height=600)
screen.title("my snake game")
screen.bgcolor('black')

snake= Snake()
food= Food()
scoreboard= Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh() 
        snake.extend_snake()
        scoreboard.increase_score()
    
    #collison with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on= False
        scoreboard.game_over()
    
    #collision with own tail
    for segment in snake.segments:
        if segment== snake.head:
            pass
        elif  snake.head.distance(segment)<10:
            scoreboard.reset()
    
        
 







screen.exitonclick()