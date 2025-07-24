from midiutil import MIDIFile

# MIDIノート番号の定義（中央のド=C4=60）
# オクターブ4
C4, D4, E4, F4, G4, A4, B4_flat, B4 = 60, 62, 64, 65, 67, 69, 70, 71 # C4を60に修正
# オクターブ5
C5, D5, E5, F5 = 72, 74, 76, 77
# オクターブ3
A3_flat, A3, B3_flat, B3, C3, D3, E3, F3, G3 = 56, 57, 58, 59, 48, 50, 52, 53, 55
# オクターブ2
F2 = 41 # <-- この行を追加しました

# 楽譜の情報
# トラック、チャンネル、時間、音の長さ、音の高さ、ベロシティ（音の強さ）
# 右手パート (メロディ)
right_hand_notes = [
    # 1-4小節
    {'pitch': F4, 'time': 0, 'duration': 1}, {'pitch': A4, 'time': 1, 'duration': 1}, {'pitch': C5, 'time': 2, 'duration': 1}, {'pitch': A4, 'time': 3, 'duration': 1},
    {'pitch': C5, 'time': 4, 'duration': 1}, {'pitch': C5, 'time': 5, 'duration': 1}, {'pitch': A4, 'time': 6, 'duration': 1}, {'pitch': F4, 'time': 7, 'duration': 1},
    {'pitch': G4, 'time': 8, 'duration': 1}, {'pitch': G4, 'time': 9, 'duration': 1}, {'pitch': A4, 'time': 10, 'duration': 1}, {'pitch': G4, 'time': 11, 'duration': 1},
    {'pitch': E4, 'time': 12, 'duration': 2}, {'pitch': C4, 'time': 14, 'duration': 1}, {'pitch': D4, 'time': 15, 'duration': 1},

    # 5-8小節
    {'pitch': E4, 'time': 16, 'duration': 1}, {'pitch': F4, 'time': 17, 'duration': 1}, {'pitch': G4, 'time': 18, 'duration': 1}, {'pitch': A4, 'time': 19, 'duration': 1},
    {'pitch': B4_flat, 'time': 20, 'duration': 1}, {'pitch': A4, 'time': 21, 'duration': 1}, {'pitch': G4, 'time': 22, 'duration': 1}, {'pitch': F4, 'time': 23, 'duration': 1},
    {'pitch': E4, 'time': 24, 'duration': 1}, {'pitch': D4, 'time': 25, 'duration': 1}, {'pitch': C4, 'time': 26, 'duration': 1}, {'pitch': D4, 'time': 27, 'duration': 1},
    {'pitch': F4, 'time': 28, 'duration': 3}, {'pitch': G4, 'time': 31, 'duration': 1},

    # 9-12小節
    {'pitch': A4, 'time': 32, 'duration': 1}, {'pitch': A4, 'time': 33, 'duration': 1}, {'pitch': B4_flat, 'time': 34, 'duration': 1}, {'pitch': C5, 'time': 35, 'duration': 1},
    {'pitch': D5, 'time': 36, 'duration': 1}, {'pitch': C5, 'time': 37, 'duration': 1}, {'pitch': B4_flat, 'time': 38, 'duration': 1}, {'pitch': A4, 'time': 39, 'duration': 1},
    {'pitch': G4, 'time': 40, 'duration': 1}, {'pitch': F4, 'time': 41, 'duration': 1}, {'pitch': E4, 'time': 42, 'duration': 1}, {'pitch': D4, 'time': 43, 'duration': 1},
    {'pitch': C4, 'time': 44, 'duration': 4},
]

# 左手パート (伴奏)
left_hand_notes = [
    # 1-4小節
    {'pitch': F3, 'time': 0, 'duration': 2}, {'pitch': C4, 'time': 0, 'duration': 2}, {'pitch': F3, 'time': 2, 'duration': 2}, {'pitch': C4, 'time': 2, 'duration': 2},
    {'pitch': F3, 'time': 4, 'duration': 2}, {'pitch': A3, 'time': 4, 'duration': 2}, {'pitch': F3, 'time': 6, 'duration': 2}, {'pitch': A3, 'time': 6, 'duration': 2},
    {'pitch': C3, 'time': 8, 'duration': 2}, {'pitch': G3, 'time': 8, 'duration': 2}, {'pitch': E3, 'time': 8, 'duration': 2},
    {'pitch': C3, 'time': 10, 'duration': 2}, {'pitch': G3, 'time': 10, 'duration': 2}, {'pitch': E3, 'time': 10, 'duration': 2},
    {'pitch': C3, 'time': 12, 'duration': 4}, {'pitch': G3, 'time': 12, 'duration': 4}, {'pitch': C4, 'time': 12, 'duration': 4},

    # 5-8小節
    {'pitch': C3, 'time': 16, 'duration': 2}, {'pitch': A3, 'time': 16, 'duration': 2}, {'pitch': C4, 'time': 16, 'duration': 2},
    {'pitch': F3, 'time': 18, 'duration': 2}, {'pitch': A3, 'time': 18, 'duration': 2}, {'pitch': C4, 'time': 18, 'duration': 2},
    {'pitch': G3, 'time': 20, 'duration': 2}, {'pitch': B3_flat, 'time': 20, 'duration': 2}, {'pitch': D4, 'time': 20, 'duration': 2},
    {'pitch': C3, 'time': 22, 'duration': 2}, {'pitch': E3, 'time': 22, 'duration': 2}, {'pitch': G3, 'time': 22, 'duration': 2},
    {'pitch': F3, 'time': 24, 'duration': 2}, {'pitch': A3, 'time': 24, 'duration': 2}, {'pitch': C4, 'time': 24, 'duration': 2},
    {'pitch': B3_flat, 'time': 26, 'duration': 1}, {'pitch': G3, 'time': 26, 'duration': 1},
    {'pitch': C4, 'time': 27, 'duration': 1}, {'pitch': A3, 'time': 27, 'duration': 1},
    {'pitch': F3, 'time': 28, 'duration': 4}, {'pitch': C3, 'time': 28, 'duration': 4},

    # 9-12小節
    {'pitch': F3, 'time': 32, 'duration': 2}, {'pitch': C4, 'time': 32, 'duration': 2}, {'pitch': F3, 'time': 34, 'duration': 2}, {'pitch': A3_flat, 'time': 34, 'duration': 2},
    {'pitch': G3, 'time': 36, 'duration': 2}, {'pitch': D4, 'time': 36, 'duration': 2}, {'pitch': F3, 'time': 38, 'duration': 2}, {'pitch': C4, 'time': 38, 'duration': 2},
    {'pitch': C3, 'time': 40, 'duration': 2}, {'pitch': G3, 'time': 40, 'duration': 2}, {'pitch': B3_flat, 'time': 40, 'duration': 2},
    {'pitch': A3, 'time': 42, 'duration': 2}, {'pitch': F3, 'time': 42, 'duration': 2}, {'pitch': C3, 'time': 42, 'duration': 2},
    {'pitch': F2, 'time': 44, 'duration': 4}, {'pitch': F3, 'time': 44, 'duration': 4},
]

# MIDIファイルの設定
track_melody = 0
track_harmony = 1
channel = 0
tempo = 104  # 楽譜の指示「活発に(J=104)」より
volume = 100 # 音の強さ (0-127)

# MIDIオブジェクトの作成 (2トラック)
midi = MIDIFile(2) 
midi.addTempo(track_melody, 0, tempo)
midi.addTempo(track_harmony, 0, tempo)

# 右手パートのノートを追加
for note in right_hand_notes:
    midi.addNote(track_melody, channel, note['pitch'], note['time'], note['duration'], volume)

# 左手パートのノートを追加
for note in left_hand_notes:
    midi.addNote(track_harmony, channel, note['pitch'], note['time'], note['duration'], volume - 15) # 伴奏の音量を少し下げる

# MIDIファイルを保存
with open("toin-kai-kaika.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("MIDIファイル 'toin-kai-kaika.mid' が生成されました。")