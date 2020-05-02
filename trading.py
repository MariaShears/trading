import click
import journal

@click.group()
def cli():
    pass

@cli.command()
def create_entry():
    """Create a trading journal entry"""
    click.echo('Here is your journal summery')
    journal.create_journal_entry()


# @cli.command()
# @click.option('--journal-id')
# def list_entries(journal_id):
#     """List my a trading journal entries"""
#     journal.list_entries(journal_id)


if __name__ == '__main__':
    cli()