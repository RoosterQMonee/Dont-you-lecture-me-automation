import os, sys, re


interpereter_args = ''.join(sys.argv)
pattern = r"-[a-zA-Z0-9]*"

args = re.findall(pattern, interpereter_args)

generated_function = """

def generate_{} (arg):
    output_file.write(f"{}@{}|")

"""


if os.path.exists(os.path.join(os.getcwd(), "/sequence.txt")):
    print("[ - ] Universal sequence file does not exist.")
    print("[ + ] Generating backup file...")

    with open('./sequence.txt', 'w', encoding='utf-8') as sequence_file:
        sequence_file.write('!speed@700|!volume@100|!stop@4|!loopmany@4|!loop|!looptarget|!cut|!combine|!jump@1|!target@1|!flash|!startpos|_pause|boom|bruh|bong|💀|👏|🐶|👽|🔔|💢|💨|🚫|🍕|eight|e|❗|buzzer|🚨|🌄|📲|gun|hitmarker|👌|whatsapp|gnome|💿|🎉|🎻|pan|slip|whipcrack|explosion|americano|SLAM|op|21|stopposting|morshu|granddad|hehehehaw|yoda|necoarc|subaluwa|oof|smw_coin|smw_1up|smw_spinjump|smw_stomp2|smw_kick|smw_stomp|yahoo|sm64_hurt|bup|thwomp|sm64_painting|smm_scream|mariopaint_car|mariopaint_plane|mariopaint_baby|mariopaint_swan|mariopaint_cat|mariopaint_dog|mariopaint_gameboy|mariopaint_flower|mariopaint_star|smw_yoshi|mariopaint_luigi|mariopaint_mario|shaker|hammer|sidestick|ride2|buttonpop|skipshot|otto_on|otto_off|otto_happy|otto_stress|adofaicymbal|midspin|adofaikick|samurai|rdmistake|tonk|preecho|tab_rooms|tab_decorations|tab_actions|tab_rows|tab_sounds|cowbell|karateman_throw|karateman_offbeat|karateman_hit|karateman_bulb|ook|choruskid|builttoscale|perfectfail|🌟|hoenn|🎺|gaster|toby|undertale_crack|undertale_hit|undertale_encounter|megalovania|fnf_death|fnf_right|fnf_up|fnf_down|fnf_left|gdcrash|gdcrash_orbs|gd_coin|gd_orbs|gd_diamonds|bwomp|isaac_hurt|isaac_dead|isaac_mantle|terraria_star|terraria_pot|terraria_reforge|amogus|amongdrip|amongus|flipnote|ultrainstinct|celeste_diamond|celeste_death|celeste_spring|celeste_dash|DEFEAT|YOU|BABA|noteblock_harp|noteblock_bass|noteblock_snare|noteblock_click|noteblock_bell|noteblock_chime|noteblock_banjo|noteblock_pling|noteblock_xylophone|noteblock_bit|minecraft_explosion|minecraft_bell|boom@60')

else:
    print("[ * ] Sequence file found.")


try:
    os.mkdir('./system')

except:
    print("[ * ] System folder already exists.")


os.chdir('./system')


with open("__init__.py", "w") as system_file:
    system_file.write("#[ ! ] Generated language interpereter\n\nwith open(\"generated.txt\", 'w') as f: f.write(' ')\noutput_file = open(\"generated.txt\", 'a')\ndef finalize(): output_file.close()\n\n")


def check_utf_char(char):
    utf = {"💀":"skull", "👏":"clap", "🐶":"dog", "👽":"alien", "🔔":"bell", "💢":"x", "💨":"wind", "🚫":"no", "🍕":"pizza", "❗":"exclamation", "🚨":"siren", "🌄":"sunshine", "📲":"cellphone", "👌":"okhand", "💿":"disc", "🎉":"party", "🎻":"violin", "🌟":"star", "🎺":"horn"}
    for key in utf.keys():
        if char == key:
            return utf[key]

    return char


def check_system_char(char):
    if char.startswith('!') or "@" in char:
        return char.split("@")[0].replace('!', '')+"_system"

    else:
        return char


with open('../sequence.txt', 'r', encoding='utf-8') as data_file:
    sequence = data_file.read()
    sequence = sequence.split("|")

    with open("__init__.py", "a", encoding='utf-8') as output_file:
        for piece in sequence:
            print(f"[ * ] Generating function for {piece}...")
            func_name = check_utf_char(piece)
            func_name = check_system_char(func_name)
            if "_system" in func_name:
                output_file.write(generated_function.format(func_name, "!"+func_name.replace('_system', ''), "{arg}"))

            else:
                output_file.write(generated_function.format(func_name, func_name, "{arg}"))
