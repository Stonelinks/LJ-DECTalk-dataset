from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import os
import tempfile

def _process_utterance(out_dir, index, wav_path, text):
    print("processing", wav_path)
    dectalk_dir=os.path.join(os.getcwd(), "dectalk")
    with tempfile.NamedTemporaryFile('w') as fp1:
        fp1.write(text)
        fp1.flush()
        with tempfile.NamedTemporaryFile('w') as fp2:
            fp2.write("""cd %s
wine say.exe -w %s < %s
""" % (dectalk_dir, wav_path, fp1.name))
            fp2.flush()
            os.system("sh %s" % fp2.name)

if __name__ == "__main__":
    # executor = ProcessPoolExecutor(max_workers=1)
    executor = ProcessPoolExecutor(max_workers=int(cpu_count() * .75))
    futures = []
    index = 1
    in_dir=os.path.join(os.getcwd(), "dataset")
    out_dir=os.path.join(os.getcwd(), "dataset")
    with open(os.path.join(in_dir, 'metadata.csv'), encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('|')
            wav_path = os.path.join(in_dir, 'wavs', '%s.wav' % parts[0])
            text = parts[2]
            futures.append(executor.submit(partial(_process_utterance, out_dir, index, wav_path, text)))
            index += 1

    for future in futures:
        future.result()