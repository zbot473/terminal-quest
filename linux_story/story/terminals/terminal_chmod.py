#!/usr/bin/env python

#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A terminal for one of the challenges

from linux_story.commands_real import shell_command
from linux_story.story.terminals.terminal_nano import TerminalNano


class TerminalChmod(TerminalNano):
    terminal_commands = ["exit", "ls", "cat", "cd",
                         "mv", "echo", "mkdir", "nano", "chmod"]

    def do_chmod(self, line):
        shell_command(self._location.get_real_path(), line, "chmod")

    def complete_chmod(self, text, line, begidx, endidx):
        completions = self._autocomplete_files(text, line, begidx, endidx)
        return completions
