## import pytest
## from click.testing import CliRunner
## from app.commands import sample_data
## 
## def test_load_command_help(test_client):
##     runner = CliRunner()
##     result = runner.invoke(sample_data.cli, ['load', '--help'])
##     assert result.exit_code == 0
##     assert '--subreddit' in result.output
##     assert '--count' in result.output
## 
## def test_load_command_with_invalid_count(test_client):
##     runner = CliRunner()
##     result = runner.invoke(sample_data.cli, ['load', '--count', 'invalid'])
##     assert result.exit_code != 0
## 
## def test_load_command_help_no_args(test_client):
##     runner = CliRunner()
##     result = runner.invoke(sample_data.cli, ['load', '--help'])
##     assert '--subreddit' in result.output
