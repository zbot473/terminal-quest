# challenge_5.py
#
# Copyright (C) 2014-2016 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A chapter of the story
from linux_story.StepTemplate import StepTemplate
from linux_story.step_helper_functions import unblock_commands_with_cd_hint
from linux_story.story.terminals.terminal_cd import TerminalCd


class StepTemplateCd(StepTemplate):
    TerminalClass = TerminalCd


# ----------------------------------------------------------------------------------------


class Step1(StepTemplateCd):
    story = [
        ("{{wb:Mum:}} {{Bb:\"Hi sleepyhead, breakfast is nearly ready. Can you go and grab your Dad? "
          "I think he's in the}} {{bb:garden}}{{Bb:.\"}}\n"),
        ("Let's look for your {{bb:Dad}} in the {{bb:garden}}."),
        ("First we need to {{lb:leave}} the {{bb:kitchen}} using {{yb:cd ..}}\n")
    ]
    start_dir = "~/my-house/kitchen"
    end_dir = "~/my-house"
    commands = ["cd ..", "cd ../"]
    hints = [("{{rb:To leave the kitchen, type}} {{yb:cd ..}}")]

    def block_command(self, line):
        return unblock_commands_with_cd_hint(line, self.commands)

    def __next__(self):
        return 5, 2


class Step2(StepTemplateCd):
    story = [
        ("You are back in the main hall of your house.\n"),
        ("Can you see your {{bb:garden}}? Have a {{lb:look around}} you.\n")
    ]
    start_dir = "~/my-house"
    end_dir = "~/my-house"
    commands = "ls"
    hints = [("{{rb:Type}} {{yb:ls}} {{rb:to look around you.}}")]

    def __next__(self):
        return 5, 3


class Step3(StepTemplateCd):
    story = [
        ("You see doors to the {{bb:garden}}, {{bb:kitchen}}, {{bb:my-room}} and {{bb:parents-room}}."),
        ("{{lb:Go}} into your {{bb:garden}}.\n")
    ]
    start_dir = "~/my-house"
    end_dir = "~/my-house/garden"
    commands = ["cd garden", "cd garden/"]
    hints = [("{{rb:Type}} {{yb:cd garden}} {{rb:to go into the garden.}}")]

    def block_command(self, line):
        return unblock_commands_with_cd_hint(line, self.commands)

    def __next__(self):
        return 5, 4


class Step4(StepTemplateCd):
    story = [
        ("Use {{yb:ls}} to {{lb:look}} in the {{bb:garden}} for your {{bb:Dad}}.\n")
    ]
    start_dir = "~/my-house/garden"
    end_dir = "~/my-house/garden"
    commands = "ls"
    hints = [("{{rb:To look for your Dad, type}} {{yb:ls}} {{rb:and press}} {{ob:Enter}}{{rb:.}}")]

    def __next__(self):
        return 5, 5


class Step5(StepTemplateCd):
    story = [
        ("The {{bb:garden}} looks beautiful at this time of year."),
        ("Hmmm...but you can't see him anywhere."),
        ("Maybe he's in the {{bb:greenhouse}}."),
        ("\n{{lb:Go}} inside the {{bb:greenhouse}}.\n")
    ]
    start_dir = "~/my-house/garden"
    end_dir = "~/my-house/garden/greenhouse"
    commands = ["cd greenhouse", "cd greenhouse/"]
    hints = [("{{rb:To go to the greenhouse, type}} {{yb:cd greenhouse}}")]

    def block_command(self, line):
        return unblock_commands_with_cd_hint(line, self.commands)

    def __next__(self):
        return 5, 6


class Step6(StepTemplateCd):
    story = [
        ("Is he here? {{lb:Look around}} with {{yb:ls}} to find out.\n")
    ]
    start_dir = "~/my-house/garden/greenhouse"
    end_dir = "~/my-house/garden/greenhouse"
    commands = "ls"
    hints = [("{{rb:Type}} {{yb:ls}} {{rb:to look for your Dad.}}")]

    def __next__(self):
        return 5, 7


class Step7(StepTemplateCd):
    story = [
        ("Your {{bb:Dad}} has been busy, there are loads of vegetables here."),
        ("Hmmmm. He's not here. But there is something odd.\n"),
        ("You see a {{bb:note}} on the ground. Use {{yb:cat note}} to {{lb:read}} what it says.\n")
    ]
    start_dir = "~/my-house/garden/greenhouse"
    end_dir = "~/my-house/garden/greenhouse"
    commands = "cat note"
    hints = [("{{rb:Type}} {{yb:cat note}} {{rb:to see what the note says!}}")]

    def __next__(self):
        return 5, 8


class Step8(StepTemplateCd):
    story = [
        ("Huh? That's weird."),
        ("But going back is super easy. Just type {{yb:cd ..}} to go back the way you came.\n")
    ]
    start_dir = "~/my-house/garden/greenhouse"
    end_dir = "~/my-house/garden"
    commands = ["cd ..", "cd ../"]
    hints = [("{{rb:Type}} {{yb:cd ..}} {{rb:to go back to the garden.}}")]

    def block_command(self, line):
        return unblock_commands_with_cd_hint(line, self.commands)

    def __next__(self):
        return 5, 9


class Step9(StepTemplateCd):
    story = [
        ("You're back in the garden. Use {{yb:cd ..}} again to {{lb:go back}} to the house.\n"),
        ("{{gb:Top tip: Press the}} {{ob:UP}} {{gb:arrow key to replay your previous command.}}\n")
    ]
    start_dir = "~/my-house/garden"
    end_dir = "~/my-house"
    commands = ["cd ..", "cd ../"]
    hints = [("{{rb:Type}} {{yb:cd ..}} {{rb:to go back to the house.}}")]

    def block_command(self, line):
        return unblock_commands_with_cd_hint(line, self.commands)

    def __next__(self):
        return 5, 10


class Step10(StepTemplateCd):
    story = [
        ("Now {{lb:go}} back into the {{bb:kitchen}} and see {{bb:Mum}}.\n")
    ]
    start_dir = "~/my-house"
    end_dir = "~/my-house/kitchen"
    commands = ["cd kitchen", "cd kitchen/"]
    hints = [("{{rb:Type}} {{yb:cd kitchen}} {{rb:to go back to the kitchen.}}")]

    def block_command(self, line):
        return unblock_commands_with_cd_hint(line, self.commands)

    def __next__(self):
        return 6, 1
