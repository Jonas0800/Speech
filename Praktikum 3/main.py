from pocketsphinx import Decoder, Config
import os

audio_path = r"Timeline 1.wav"


config = Config()
config.set_string('-hmm', r'C:\Users\Jonas\PycharmProjects\Speech\.venv\Lib\site-packages\pocketsphinx\model\De-de\cmusphinx-cont-voxforge-de-r20171217\model_parameters\voxforge.cd_cont_6000')
config.set_string('-dict', r'C:\Users\Jonas\PycharmProjects\Speech\.venv\Lib\site-packages\pocketsphinx\model\De-de\cmusphinx-voxforge-de.dic')
config.set_string('-lm', r'C:\Users\Jonas\PycharmProjects\Speech\.venv\Lib\site-packages\pocketsphinx\model\De-de\cmusphinx-voxforge-de.lm.bin')


decoder = Decoder(config)

with open(audio_path, 'rb') as f:
    f.seek(44)
    decoder.start_utt()
    while True:
        buf = f.read(1024)
        if not buf:
            break
        decoder.process_raw(buf, False, False)
    decoder.end_utt()

# Ergebnis anzeigen
hypothesis = decoder.hyp()
if hypothesis is not None:
    print("Transkription:", hypothesis.hypstr)
else:
    print("Keine Sprache erkannt.")
