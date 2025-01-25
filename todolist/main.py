import click

from app import TodoApp

@click.group()
@click.pass_context
@click.option('--list','-l',is_flag=True, help='List Tasks after Update.')
def cli(ctx,list):
    """A Simple CLI-based To-Do app."""
    ctx.ensure_object(dict)
    ctx.obj['app'] = TodoApp()
    ctx.obj['list'] = list

@cli.command()
@click.argument('task_name')
@click.pass_context
def add(ctx, task_name):
    """Add new Task."""
    app = ctx.obj['app']
    app.add_task(title=task_name)
    click.echo(f'Task {task_name} added Succesfully.')
    
    if ctx.obj['list']:
        ctx.invoke(list)

@cli.command()
@click.pass_context
def list(ctx):
    """List all Tasks."""
    app = ctx.obj['app']
    todo_list = app.list_tasks()
    click.echo(f'Tasks:')
    for todo in todo_list:
        if todo.is_done:
            done_symbol = '[X]'
        else:
            done_symbol = '[ ]'
        click.echo(f'{done_symbol} | {todo.title}')
        click.echo(30 * '-')
        click.echo(f'{todo.description}')

@cli.command()
@click.pass_context
@click.argument('task_name')
def flip(ctx, task_name):
    """Set/Unset checkmark of Task"""
    app = ctx.obj['app']
    app.flip_is_done(task_name)
    click.echo(f"Succesfully Set/Unset is_done of Task {task_name}!")

    if ctx.obj['list']:
        ctx.invoke(list)

@cli.command()
@click.pass_context
@click.argument('task_name')
@click.argument('task_description')
def set_description(ctx, task_name, task_description):
    """Overwrite Description of Task."""
    app = ctx.obj['app']
    app.set_description(task_name, task_description)
    click.echo(f"Succesfully Set description of Task {task_name} to {task_description}!")
    
    if ctx.obj['list']:
        ctx.invoke(list)

if __name__ == '__main__':
    cli()
