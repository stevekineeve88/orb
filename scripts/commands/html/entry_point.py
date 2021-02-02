import click
import os
from modules.Util.db_connection import DBConnection
from modules.Word.managers.DictionaryManager import DictionaryManager
from modules.Word.repositories.dictionary_repo import DictionaryRepo
from scripts.commands.html.actions.search import search


@click.group()
@click.option('--db_host', help='Database host', default=None)
@click.option('--db_user', help='Database user', default=None)
@click.option('--db_pass', help='Database password', default=None)
@click.option('--db_port', help='Database port', default=None)
@click.option('--db_name', help='Database name', default=None)
@click.pass_context
def html(ctx, db_host, db_user, db_pass, db_port, db_name):
    ctx.obj[DictionaryManager] = DictionaryManager(
        dictionary_repo=DictionaryRepo(
            db_connection=DBConnection(
                host=db_host or os.environ["POSTGRES_HOST"],
                port=db_port or os.environ["POSTGRES_PORT"],
                database=db_name or os.environ["POSTGRES_DB"],
                user=db_user or os.environ["POSTGRES_USER"],
                password=db_pass or os.environ["POSTGRES_PASS"],
            )
        )
    )


html.add_command(search)
