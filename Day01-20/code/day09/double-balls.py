import random
from rich.console import Console
from rich.table import Table

console = Console()

n = int(input('抽几次'))

table = Table(show_header=True)

for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    red_balls = random.sample(range(1,34),6)
    red_balls.sort()
    blue_ball = random.choice(range(1,17))

    table.add_row(        
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in red_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

console.print(table)