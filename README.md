# nanoKontrolStudio Ableton script

### A minimalist MIDI (not MCU) control surface script for using the Korg nanoKontrol Studio with Ableton Live

## Background

_**Please note:** I work almost exclusively in Live's Arrangement view, so if you prefer a Session view workflow, this script probably isn't for you!_

I bought the nanoKontrol Studio mostly on the strength of the jog wheel, having seen a video of someone demonstrating its use with Ableton Live. Having a proper transport section that's not dependent on window focus or complicated global AHK scripts and - even better - can be operated wirelessly while tracking instruments live is a big draw. Having some faders, buttons and knobs that can be arbitrarily assigned on a per-project basis is also good - ideal for fast automation of orchestral libraries' mod and expression parameters, for example. Replicating a mix console in a small form factor is way less important to me these days (same goes for live performance control).

I was disappointed, therefore, to learn that Live only supports the jog wheel if you connect using the Mackie Control (MCU) protocol, which the nKS can be switched to. MCU and HUI have always been a nightmare in my experience, and even when they work I get frustrated that I can't section off a block of physical controls as being fair game for arbitrary mappings. (Actually I didn't learn that the nKS supported MCU until _after_ I'd done this script; I just thought Live didn't support the jog wheel at all and that I'd imagined watching that demo video...)

## Overview

This project consists of a scene set file and a remote script. The scene set (**nks_AbletonLive_echolevel.nktrl_st_set**) should be loaded into the Korg Kontrol Editor, available from Korg's website, and then written to the nanoKontrol Studio. It'll overwrite scenes 1 and 2 but frankly doesn't change much from the factory defaults. Crucially it changes the jog wheel settings to 'Inc/Dec 2' mode and an acceleration value of 2. It also makes the transport section on scene 2 use the global channel option rather than MIDI channel 2. I've also changed the LED mode on both scenes to 'external', which means it should get illumination feedback on toggle buttons from Live where relevant. No fancy RGB - the nKS LEDs are all plain white. Which makes quite a nice change...

The remote script is pretty straightforward and should be easily tweakable.

**Scene 1** sets up:
* Stop, Play, Record and Cycle (Loop toggle) buttons as you'd expect, and since Live uses a double-press of Stop to return the playhead to the start, I'm using the full-rewind button for Tap Tempo instead.
* Track < and > buttons to cycle through Ableton Live's tracks/groups
* << button to Metronome On/Off and >> button to Arrangement Overdub
* Marker navigation, so Set adds or deletes a Locator and <| and |> navigate between locators
* The first channel strip on the nKS is _always_ the current track, which is selected via the Track < and > buttons. This means you can treat channel 1 a bit like a Faderport, and make rapid adjustments (albeit one at a time) to different tracks without having to move your hand or look over at the control surface. Might not suit you, but it suits me!
* The last channel fader is _always_ the master track, with the fader controlling Master volume and the knob controlling Cue/Preview level (typically metronome click volume independently of monitor output)

All the physical controls on tracks 2-7, plus the track 8 buttons, are freely mappable to whatever you want on a per-project basis. In my case I usually map faders 6 and 7 to expression controls in sample libraries, and knobs 2 and 3 to synth cut/res controls, or whatever.

You can still map favourite functions in the normal 'simple' way, using Live's MIDI Map button and saving the project as your default template for future use.

**Scene 2** is exactly the same for the transport section, but the channel section maps to tracks 1-8 in Live as you'd normally expect from a control surface. It doesn't do track bank offsets (I'm not sure if that's possible in Arrangement view - please let me know if you've worked it out), but it does the job on small projects. If you regularly need to do an intensive hands-on mix of 32+ channel projects, then there are probably better scripts (or surfaces) out there for you.

Since Ableton Live compiles any uncompiled Python scripts on launch, you can easily tweak this script in place to add or change functionality. For example, you could copy and paste the entire channel_strip(n) section and update the strip and channel numbers to assign Scenes 3, 4 and 5 on the nKS to Live channels 9 and above. I find Korg's one-way Set cycling behaviour a bit too irritating to want to work like this, but YMMV. When you make a change, re-open a saved Set or create a new Set to get Live to recompile the script - a full restart of Live usually isn't necessary. You should see a notification message in yellow at the bottom of the screen (if not, something's gone wrong).  


## Installation

Install the Korg Kontrol Editor from Korg's site and follow their instructions for communicating with your hardware, opening the .nktrl_st_set file, and writing it to the device.

Then copy the nanokontrolstudio_echolevel directory to "C:\ProgramData\Ableton\Live[whatever version]\Resources\MIDI Remote Scripts" on Windows 10, or even better, [follow Ableton's own instructions (Win and Mac)](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts) to install it to your User Library, independent of Live version and hopefully a bit more update-proof. Note: this is tested on Live 10 and the Live 11 Beta.

The above link also shows you how to select the script under Control Surface in Preferences, and you'll also need to set nanoKontrol Studio as the Input and Output. Enable it for Track and Remote in the main MIDI I/O section too, so you can easily create simple MIDI mappings yourself.
