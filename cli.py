import click
from colorama import init, deinit
from scripts.commands.html.entry_point import html


@click.group()
@click.pass_context
def entry_point(ctx):
    ctx.ensure_object(dict)


init()
entry_point.add_command(html)
entry_point(obj={})
deinit()
