from midiutil import MIDIFile

def create_touinkai_ka_midi():
    # 楽譜から読み取った音符と長さのリスト
    # (音名, 長さ(拍数)) のタプルのリスト
    # 8分音符 = 0.5拍, 4分音符 = 1拍
    notes = [
        ('C5', 0.5), ('E5', 0.5), ('G5', 0.5), ('G5', 0.5),  # はる と う よう
        ('G5', 0.5), ('A5', 0.5), ('G5', 0.5), ('F5', 0.5),  # の はな の か
        ('E5', 1), ('D5', 1),                             # げ て
        ('C5', 0.5), ('E5', 0.5), ('G5', 0.5), ('G5', 0.5),  # あき の けい
        ('G5', 0.5), ('A5', 0.5), ('G5', 0.5), ('F5', 0.5),  # かん の つ
        ('E5', 1), ('D5', 1),                             # き の
        ('C5', 0.5), ('C5', 0.5), ('D5', 0.5), ('E5', 0.5),  # とび かう こ
        ('F5', 0.5), ('E5', 0.5), ('D5', 0.5), ('C5', 0.5),  # ちょう に か
        ('D5', 1), ('E5', 1),                             # ぜ に
        ('C5', 0.5), ('C5', 0.5), ('D5', 0.5), ('E5', 0.5),  # した ゆく
        ('F5', 0.5), ('E5', 0.5), ('D5', 0.5), ('C5', 0.5),  # みず は がっ
        ('D5', 1), ('C5', 1),                             # き を
        ('B4', 0.5), ('C5', 0.5), ('D5', 0.5), ('D5', 0.5),  # じょう あい
        ('E5', 0.5), ('F5', 0.5), ('G5', 0.5), ('A5', 0.5),  # へい わ に
        ('G5', 0.5), ('F5', 0.5), ('E5', 0.5), ('D5', 0.5),  # みち て みち
        ('C5', 1), ('C5', 1),                             # あ ふ れる
        ('G4', 0.5), ('A4', 0.5), ('B4', 0.5), ('C5', 0.5),  # し ぜん の
        ('B4', 0.5), ('A4', 0.5), ('G4', 0.5), ('F4', 0.5),  # かん けん
        ('G4', 0.5), ('A4', 0.5), ('G4', 0.5), ('F4', 0.5),  # われ ら を
        ('E4', 1), ('G4', 1)                              # しめ し
    ]

    # MIDIファイルの設定
    track    = 0
    channel  = 0
    time     = 0    # 開始時間（拍）
    tempo    = 104  # BPM
    volume   = 100  # 0-127

    # MIDIFileオブジェクトの作成
    MyMIDI = MIDIFile(1)  # 1トラック
    MyMIDI.addTempo(track, time, tempo)

    # 音符をMIDIファイルに追加
    for pitch_name, duration in notes:
        # 音名からMIDIノート番号に変換 (例: C4=60, C5=72)
        # 簡単なマッピング。より正確にはライブラリを使うと良い
        note_map = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
        octave = int(pitch_name[-1])
        note = note_map[pitch_name[:-1]]
        midi_pitch = 12 * (octave + 1) + note
        
        MyMIDI.addNote(track, channel, midi_pitch, time, duration, volume)
        time += duration

    # MIDIファイルを保存
    filename = "touinkai_ka.mid"
    with open(filename, "wb") as output_file:
        MyMIDI.writeFile(output_file)
    
    print(f"MIDIファイル '{filename}' が正常に作成されました。")

if __name__ == '__main__':
    create_touinkai_ka_midi()