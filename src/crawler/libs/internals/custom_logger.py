import sys

from termcolor import colored
from datetime import datetime
from .crawler_exceptions import CrawlerException
from .timestamp import TIMESTAMP

INFO = 0X01  # INFO LOG TYPE
WARN = 0X02  # WARNNING LOG TYPE
ERR = 0X03  # ERROR LOG TYPE

# LOG_TYPES + COLOUR TABLES
_log_types = {INFO: "INFO", WARN: "WARNING", ERR: "ERROR"}
_colours = {ERR: "magenta", WARN: "yellow", INFO: "green"}

# MESSAGE MUST BE A STRING


def log_says(log_type, message, agent=None):
    """ Custom Logger Class """

    if log_type not in (INFO, WARN, ERR):
        raise CrawlerException("LOG TYPE MUST BE OF 'WARN', 'INFO' AND 'ERR'")

    if not isinstance(message, str):
        raise CrawlerException(
            message="MESSAGE MUST BE A 'STRING'",
            code=50,
            agent="CustomLogger")

    if len(message) < 1:
        raise CrawlerException(
            message="MESSAGE CAN NOT BE AN EMPTY STRING",
            code=51,
            agent="CustomLogger")

    if agent:
        MESSAGE = (
            colored(
                "[",
                "white") +
            colored(
                TIMESTAMP.get_date() +
                " " +
                TIMESTAMP.get_time(),
                "cyan") +
            colored(
                "] [",
                "white") +
            colored(
                str(agent),
                "white") +
            colored(
                "] [",
                "white") +
            colored(
                _log_types[log_type],
                _colours[log_type]) +
            colored(
                "] --> ",
                "white") +
            colored(
                message,
                _colours[log_type]) +
            "\n")
    else:
        MESSAGE = (
            colored(
                "[",
                "white") +
            colored(
                TIMESTAMP.get_date() +
                " " +
                TIMESTAMP.get_time(),
                "cyan") +
            colored(
                "] [",
                "white") +
            colored(
                _log_types[log_type],
                _colours[log_type]) +
            colored(
                "] --> ",
                "white") +
            colored(
                message,
                _colours[log_type]) +
            "\n")

    # write things to stderr ;)
    sys.stderr.write(MESSAGE)
