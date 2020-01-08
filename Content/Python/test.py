import unreal
project = u'Unreal Python'

# The short X.Y version
version = u'{{Version}}'
# The full version, including alpha/beta/rc tags
release = u'{{Version}} (Experimental)'
print(project)
print(version)
print(release)
print("thank you.")

import webbrowser

#webbrowser.open('http://google.com')

obj = unreal.MediaPlayer() #(name='NewMediaPlayer')
obj.set_desired_player_name('NewMediaPlayer')
# Modifying a property directly can have different results
# than changing settings in the Editor UI.
# Generally you'll want to avoid setting these values directly, like this:
#obj.play_on_open = True
# This way of accessing the property will have exactly the same
# result as changing the setting in the Editor UI:
obj.set_editor_property("play_on_open", False)
v1 = unreal.Vector()
v1.x = 10
v2 = unreal.Vector(10, 20, 30)
v3 = (v1 + v2) * 2
print v3
print obj.play_on_open
print obj.get_desired_player_name()


#for i in range(1000000):
  #  print i

import unreal
total_frames = 10000000
text_label = "Working!"
with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
    slow_task.make_dialog(True)               # Makes the dialog visible, if it isn't already
    for i in range(total_frames):
        if slow_task.should_cancel():         # True if the user has pressed Cancel in the UI
            break
        slow_task.enter_progress_frame(1)     # Advance progress by one frame.
                                            # You can also update the dialog text in this call, if you want.
        #...                                   # Now do work for the current frame here!