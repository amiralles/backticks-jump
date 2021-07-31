import sublime, sublime_plugin

# Jumps back and forth between the previous and next cursor positions,
# similarly to vim's bultin backtick-backtick command.
class BackticksJumpCommand(sublime_plugin.WindowCommand):
    BWD=-1
    FWD=1
    next_jump_direction=BWD

    def run(self):
        if self.next_jump_direction == self.FWD:
            self.run_command_on_active_view("jump_forward")
        else:
            self.run_command_on_active_view("jump_back")
        self.toggle_next_jump_direction()

    def toggle_next_jump_direction(self):
        if self.next_jump_direction == self.FWD:
            self.next_jump_direction = self.BWD
        else:
            self.next_jump_direction = self.FWD

    def run_command_on_active_view(self, cmd):
        view = self.window.active_view()
        if view:
            view.run_command(cmd)
        else:
            print("There is no active view.")
