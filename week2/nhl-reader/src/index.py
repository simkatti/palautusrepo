from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.console import Console
from rich.table import Table
import rich.box


def main():
    while True:
        print("[italic]NHL statistics by nationality[/italic]")
        season = input("Select season: [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25]")
        if season == "exit":
            print('have a nice day')
            return
        nationality = input("Select nationality: [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR]")
        if nationality == "exit":
            print('have a nice day')
            return
        print(f'Top scores of {nationality} season {season}')


        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        console = Console()
        table = Table(show_header=True, header_style="bold white", style='white', box=rich.box.SQUARE) 
        
        table.add_column("name", style='blue')
        table.add_column("team", style='red')
        table.add_column("goals", style='yellow')
        table.add_column("assists",style='yellow')
        table.add_column("points", style='green')
        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))
        console.print(table)

main()
