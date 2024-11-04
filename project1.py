import turtle

def snowflake(t, length, depth):
  if depth == 0:
    t.forward(length)
    return
  snowflake(t, length/3, depth-1)
  t.left(60)
  snowflake(t, length/3, depth-1)
  t.right(120)
  snowflake(t, length/3, depth-1)
  t.left(60)
  snowflake(t, length/3, depth-1)

t = turtle.Turtle()
t.speed(0)  # Set the speed to the fastest
snowflake(t, 300, 3)
turtle.done()
