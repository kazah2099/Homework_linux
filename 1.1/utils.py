from rich import print

def add_task(tasks, task):
    tasks.append(task)
    print(f"[green]Task added:[/green] {task}")

def show_tasks(tasks):
    if not tasks:
        print("[yellow]No tasks yet[/yellow]")
        return

    print("\n[bold]Your tasks:[/bold]")

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(tasks, task):
    print(f"[green]Task deleted:[/green] {task}")
    tasks.remove(task)