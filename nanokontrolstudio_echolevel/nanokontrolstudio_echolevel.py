from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.MixerComponent import MixerComponent
from _Framework.TransportComponent import TransportComponent
from _Framework.EncoderElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.SliderElement import SliderElement

mixer, transport = None, None

class nanokontrolstudio_echolevel(ControlSurface):

	def __init__(self, c_instance):
		ControlSurface.__init__(self, c_instance)
		with self.component_guard():
			global mixer
			global transport
			track_count = 256 # Allegedly unlimited in Live Suite...
			return_count = 24 # Maximum of 12 Sends and 12 Returns
			mixer = MixerComponent(track_count, return_count)
			transport = TransportComponent()
			self._mainCtrl()

	def _mainCtrl(self):
		self.show_message("Loading Korg nanoKontrol Studio mappings")
		# Main transport controls
		transport.set_record_button(ButtonElement(1, MIDI_CC_TYPE, 0, 81))
		transport.set_loop_button(ButtonElement(1, MIDI_CC_TYPE, 0, 54))
		transport.set_play_button(ButtonElement(1, MIDI_CC_TYPE, 0, 80))
		transport.set_stop_button(ButtonElement(1, MIDI_CC_TYPE, 0, 63))
		transport.set_tap_tempo_button(ButtonElement(1, MIDI_CC_TYPE, 0, 62))
		# Seek/scrub controls: (is_momentary, MIDI_CC_TYPE, channel, CCnum). For this to work, nanoKontrol Studio's jog wheel should be set to: Inc/Dec 2, Acceleration 2.
		transport.set_seek_forward_button(ButtonElement(0, MIDI_CC_TYPE, 0, 83))
		transport.set_seek_backward_button(ButtonElement(0, MIDI_CC_TYPE, 0, 85))
		transport.set_metronome_button(ButtonElement(1, MIDI_CC_TYPE, 0, 58))
		transport.set_arrangement_overdub_button(ButtonElement(1, MIDI_CC_TYPE, 0, 59))
		# nKS' 1st strip is always the current track, set with the Track < and > buttons.
		mixer.set_select_buttons(ButtonElement(1, MIDI_CC_TYPE, 0, 61), ButtonElement(1, MIDI_CC_TYPE, 0, 60))
		mixer.selected_strip().set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 0, 21))
		mixer.selected_strip().set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 0, 29))
		mixer.selected_strip().set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 0, 38))
		mixer.selected_strip().set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 0, 46))
		mixer.selected_strip().set_pan_control(EncoderElement(MIDI_CC_TYPE, 0, 13, Live.MidiMap.MapMode.absolute))
		mixer.selected_strip().set_volume_control(SliderElement(MIDI_CC_TYPE, 0, 2))
		# nKS' 8th strip is always Master. Fader is volume and pot is cue level.
		mixer.master_strip().set_volume_control(SliderElement(MIDI_CC_TYPE, 0, 12))
		mixer.set_prehear_volume_control(EncoderElement(MIDI_CC_TYPE, 0, 20, Live.MidiMap.MapMode.absolute)) # Known as cue/preview in current versions of Live; controls e.g. metronome level in headphones
		# Scene 2 on the nKS should be factory defaults - ie same CCs as Scene 1 but on MIDI Channel 2 (1). This is set up like a conventional 8-track mix control surface.
		mixer.channel_strip(0).set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 1, 21))
		mixer.channel_strip(1).set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 1, 22))
		mixer.channel_strip(2).set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 1, 23))
		mixer.channel_strip(3).set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 1, 24))
		mixer.channel_strip(4).set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 1, 25))
		mixer.channel_strip(5).set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 1, 26))
		mixer.channel_strip(6).set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 1, 27))
		mixer.channel_strip(7).set_mute_button(ButtonElement(1, MIDI_CC_TYPE, 1, 28))
		mixer.channel_strip(0).set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 1, 29))
		mixer.channel_strip(1).set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 1, 30))
		mixer.channel_strip(2).set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 1, 31))
		mixer.channel_strip(3).set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 1, 33))
		mixer.channel_strip(4).set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 1, 34))
		mixer.channel_strip(5).set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 1, 35))
		mixer.channel_strip(6).set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 1, 36))
		mixer.channel_strip(7).set_solo_button(ButtonElement(1, MIDI_CC_TYPE, 1, 37))
		mixer.channel_strip(0).set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 1, 38))
		mixer.channel_strip(1).set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 1, 39))
		mixer.channel_strip(2).set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 1, 40))
		mixer.channel_strip(3).set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 1, 41))
		mixer.channel_strip(4).set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 1, 42))
		mixer.channel_strip(5).set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 1, 43))
		mixer.channel_strip(6).set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 1, 44))
		mixer.channel_strip(7).set_arm_button(ButtonElement(1, MIDI_CC_TYPE, 1, 45))
		mixer.channel_strip(0).set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 1, 46))
		mixer.channel_strip(1).set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 1, 47))
		mixer.channel_strip(2).set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 1, 48))
		mixer.channel_strip(3).set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 1, 49))
		mixer.channel_strip(4).set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 1, 50))
		mixer.channel_strip(5).set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 1, 51))
		mixer.channel_strip(6).set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 1, 52))
		mixer.channel_strip(7).set_shift_button(ButtonElement(1, MIDI_CC_TYPE, 1, 53))
		mixer.channel_strip(0).set_pan_control(EncoderElement(MIDI_CC_TYPE, 1, 13, Live.MidiMap.MapMode.absolute))
		mixer.channel_strip(1).set_pan_control(EncoderElement(MIDI_CC_TYPE, 1, 14, Live.MidiMap.MapMode.absolute))
		mixer.channel_strip(2).set_pan_control(EncoderElement(MIDI_CC_TYPE, 1, 15, Live.MidiMap.MapMode.absolute))
		mixer.channel_strip(3).set_pan_control(EncoderElement(MIDI_CC_TYPE, 1, 16, Live.MidiMap.MapMode.absolute))
		mixer.channel_strip(4).set_pan_control(EncoderElement(MIDI_CC_TYPE, 1, 17, Live.MidiMap.MapMode.absolute))
		mixer.channel_strip(5).set_pan_control(EncoderElement(MIDI_CC_TYPE, 1, 18, Live.MidiMap.MapMode.absolute))
		mixer.channel_strip(6).set_pan_control(EncoderElement(MIDI_CC_TYPE, 1, 19, Live.MidiMap.MapMode.absolute))
		mixer.channel_strip(7).set_pan_control(EncoderElement(MIDI_CC_TYPE, 1, 20, Live.MidiMap.MapMode.absolute))
		mixer.channel_strip(0).set_volume_control(SliderElement(MIDI_CC_TYPE, 1, 2))
		mixer.channel_strip(1).set_volume_control(SliderElement(MIDI_CC_TYPE, 1, 3))
		mixer.channel_strip(2).set_volume_control(SliderElement(MIDI_CC_TYPE, 1, 4))
		mixer.channel_strip(3).set_volume_control(SliderElement(MIDI_CC_TYPE, 1, 5))
		mixer.channel_strip(4).set_volume_control(SliderElement(MIDI_CC_TYPE, 1, 6))
		mixer.channel_strip(5).set_volume_control(SliderElement(MIDI_CC_TYPE, 1, 8))
		mixer.channel_strip(6).set_volume_control(SliderElement(MIDI_CC_TYPE, 1, 9))
		mixer.channel_strip(7).set_volume_control(SliderElement(MIDI_CC_TYPE, 1, 12))

	def disconnect(self):
		ControlSurface.disconnect() # cleanup on d/c
