from visual_player.viewer import PlotDiar
#import App

def runscript():
    speakerSlice = {'0': [{'start': 568, 'stop': 1000}, {'start': 2867, 'stop': 4056}],
                    '1': [{'start': 4200, 'stop': 5000}]}
    wav_path = 'Vitamin_A_8k_3.wav'
    p = PlotDiar(map=speakerSlice, wav=wav_path, gui=True, size=(6, 3))
    p.draw()
    p.plot.show()

# runscript()
