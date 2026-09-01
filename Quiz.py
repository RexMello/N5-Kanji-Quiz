import random
import unicodedata

# ToKini Andy N5 Reading-series quiz
# Each item: lesson, English prompt, Japanese spelling, kana reading, accepted romaji.
# The question NEVER shows the Japanese spelling until after you answer.

VOCAB = [
    # Lesson 1
    (1, "Sun / day", "日", "ひ", ["hi"]),
    (1, "Moon", "月", "つき", ["tsuki"]),
    (1, "Fire", "火", "ひ", ["hi"]),
    (1, "Water", "水", "みず", ["mizu"]),
    (1, "Tree", "木", "き", ["ki"]),
    (1, "Money", "お金", "おかね", ["okane"]),
    (1, "Soil / dirt", "土", "つち", ["tsuchi"]),

    # Lesson 2
    (2, "What", "何", "なに", ["nani", "nan"]),
    (2, "Day of the week", "曜日", "ようび", ["youbi", "yobi"]),
    (2, "What day of the week", "何曜日", "なんようび", ["nanyoubi", "nanyobi"]),
    (2, "Sunday", "日曜日", "にちようび", ["nichiyoubi", "nichiyobi"]),
    (2, "Monday", "月曜日", "げつようび", ["getsuyoubi", "getsuyobi"]),
    (2, "Tuesday", "火曜日", "かようび", ["kayoubi", "kayobi"]),
    (2, "Wednesday", "水曜日", "すいようび", ["suiyoubi", "suiyobi"]),
    (2, "Thursday", "木曜日", "もくようび", ["mokuyoubi", "mokuyobi"]),
    (2, "Friday", "金曜日", "きんようび", ["kinyoubi", "kinyobi"]),
    (2, "Saturday", "土曜日", "どようび", ["doyoubi", "doyobi"]),

    # Lesson 3
    (3, "One", "一", "いち", ["ichi"]),
    (3, "Two", "二", "に", ["ni"]),
    (3, "Three", "三", "さん", ["san"]),
    (3, "Four", "四", "よん / し", ["yon", "shi"]),
    (3, "Five", "五", "ご", ["go"]),
    (3, "Six", "六", "ろく", ["roku"]),
    (3, "Seven", "七", "しち / なな", ["shichi", "nana"]),
    (3, "Eight", "八", "はち", ["hachi"]),
    (3, "Nine", "九", "きゅう", ["kyuu", "kyu"]),
    (3, "Ten", "十", "じゅう", ["juu", "ju"]),

    # Lesson 4
    (4, "April", "四月", "しがつ", ["shigatsu"]),
    (4, "September", "九月", "くがつ", ["kugatsu"]),
    (4, "Eleven", "十一", "じゅういち", ["juuichi", "juichi"]),
    (4, "Twelve", "十二", "じゅうに", ["juuni", "juni"]),
    (4, "November", "十一月", "じゅういちがつ", ["juuichigatsu", "juichigatsu"]),
    (4, "December", "十二月", "じゅうにがつ", ["juunigatsu", "junigatsu"]),

    # Lesson 5
    (5, "Now", "今", "いま", ["ima"]),
    (5, "This month", "今月", "こんげつ", ["kongetsu"]),
    (5, "This year", "今年", "ことし", ["kotoshi"]),
    (5, "One year", "一年", "いちねん", ["ichinen"]),
    (5, "To come", "来る", "くる", ["kuru"]),
    (5, "Next month", "来月", "らいげつ", ["raigetsu"]),
    (5, "Next year", "来年", "らいねん", ["rainen"]),

    # Lesson 6
    (6, "One day (duration)", "一日", "いちにち", ["ichinichi"]),
    (6, "First day of the month", "一日", "ついたち", ["tsuitachi"]),
    (6, "Second day of the month", "二日", "ふつか", ["futsuka"]),
    (6, "Third day of the month", "三日", "みっか", ["mikka"]),
    (6, "Fourth day of the month", "四日", "よっか", ["yokka"]),
    (6, "Fifth day of the month", "五日", "いつか", ["itsuka"]),
    (6, "Sixth day of the month", "六日", "むいか", ["muika"]),
    (6, "Seventh day of the month", "七日", "なのか", ["nanoka"]),
    (6, "Eighth day of the month", "八日", "ようか", ["youka", "yoka"]),
    (6, "Ninth day of the month", "九日", "ここのか", ["kokonoka"]),
    (6, "Tenth day of the month", "十日", "とおか", ["tooka", "toka"]),
    (6, "Nineteenth day of the month", "十九日", "じゅうくにち", ["juukunichi", "jukunichi"]),
    (6, "Twentieth day of the month", "二十日", "はつか", ["hatsuka"]),

    # Lesson 7 - native general counters
    (7, "One thing", "一つ", "ひとつ", ["hitotsu"]),
    (7, "Two things", "二つ", "ふたつ", ["futatsu"]),
    (7, "Three things", "三つ", "みっつ", ["mittsu"]),
    (7, "Four things", "四つ", "よっつ", ["yottsu"]),
    (7, "Five things", "五つ", "いつつ", ["itsutsu"]),
    (7, "Six things", "六つ", "むっつ", ["muttsu"]),
    (7, "Seven things", "七つ", "ななつ", ["nanatsu"]),
    (7, "Eight things", "八つ", "やっつ", ["yattsu"]),
    (7, "Nine things", "九つ", "ここのつ", ["kokonotsu"]),

    # Lesson 8
    (8, "To understand", "分かる", "わかる", ["wakaru"]),
    (8, "One minute", "一分", "いっぷん", ["ippun"]),
    (8, "Two minutes", "二分", "にふん", ["nifun"]),
    (8, "Twenty minutes", "二十分", "にじゅっぷん", ["nijuppun", "nijuuppun"]),
    (8, "Person", "人", "ひと", ["hito"]),
    (8, "Friend", "友達", "ともだち", ["tomodachi"]),
    (8, "Friend (formal)", "友人", "ゆうじん", ["yuujin", "yujin"]),
    (8, "One person", "一人", "ひとり", ["hitori"]),
    (8, "Two people", "二人", "ふたり", ["futari"]),
    (8, "Nine people", "九人", "きゅうにん", ["kyuunin", "kyunin"]),

    # Lesson 9
    (9, "Four o'clock", "四時", "よじ", ["yoji"]),
    (9, "Nine o'clock", "九時", "くじ", ["kuji"]),
    (9, "To rest / take a day off", "休む", "やすむ", ["yasumu"]),
    (9, "Holiday / day off", "休日", "きゅうじつ", ["kyuujitsu", "kyujitsu"]),
    (9, "White", "白い", "しろい", ["shiroi"]),
    (9, "To enter", "入る", "はいる", ["hairu"]),

    # Lesson 10
    (10, "Yen", "円", "えん", ["en"]),
    (10, "Hundred", "百", "ひゃく", ["hyaku"]),
    (10, "Thousand", "千", "せん", ["sen"]),
    (10, "Two thousand yen", "二千円", "にせんえん", ["nisenen"]),
    (10, "Three thousand yen", "三千円", "さんぜんえん", ["sanzenen"]),
    (10, "Ten thousand", "一万", "いちまん", ["ichiman"]),
    (10, "One million yen", "百万円", "ひゃくまんえん", ["hyakumanen"]),

    # Lesson 11
    (11, "To go out / come out", "出る", "でる", ["deru"]),
    (11, "Exit", "出口", "でぐち", ["deguchi"]),
    (11, "Above / up", "上", "うえ", ["ue"]),
    (11, "Below / down", "下", "した", ["shita"]),
    (11, "Hallway", "廊下", "ろうか", ["rouka", "roka"]),
    (11, "Population", "人口", "じんこう", ["jinkou", "jinko"]),
    (11, "Hand", "手", "て", ["te"]),
    (11, "One bite / mouthful", "一口", "ひとくち", ["hitokuchi"]),
    (11, "Skillful / good at", "上手", "じょうず", ["jouzu", "jozu"]),
    (11, "Unskillful / bad at", "下手", "へた", ["heta"]),

    # Lesson 12
    (12, "To read", "読む", "よむ", ["yomu"]),
    (12, "Book", "本", "ほん", ["hon"]),
    (12, "Japan", "日本", "にほん", ["nihon", "nippon"]),
    (12, "Japanese language", "日本語", "にほんご", ["nihongo"]),
    (12, "Country", "国", "くに", ["kuni"]),
    (12, "Sentence / writing", "文", "ぶん", ["bun"]),
    (12, "Japanese person", "日本人", "にほんじん", ["nihonjin"]),

    # Lesson 13
    (13, "To speak / talk", "話す", "はなす", ["hanasu"]),
    (13, "Car", "車", "くるま", ["kuruma"]),
    (13, "Train", "電車", "でんしゃ", ["densha"]),
    (13, "Sign language", "手話", "しゅわ", ["shuwa"]),
    (13, "Correct", "正しい", "ただしい", ["tadashii"]),
    (13, "New Year", "お正月", "おしょうがつ", ["oshougatsu", "oshogatsu"]),
    (13, "Every day", "毎日", "まいにち", ["mainichi"]),
    (13, "Telephone", "電話", "でんわ", ["denwa"]),

    # Lesson 14
    (14, "Small size", "小サイズ", "しょうサイズ", ["shousaizu", "shosaizu"]),
    (14, "Small", "小さい", "ちいさい", ["chiisai"]),
    (14, "Elementary school", "小学校", "しょうがっこう", ["shougakkou", "shogakko"]),
    (14, "Medium size", "中サイズ", "ちゅうサイズ", ["chuusaizu", "chusaizu"]),
    (14, "Middle school", "中学校", "ちゅうがっこう", ["chuugakkou", "chugakko"]),
    (14, "Inside / middle", "中", "なか", ["naka"]),
    (14, "All year round", "一年中", "いちねんじゅう", ["ichinenjuu", "ichinenju"]),
    (14, "Big", "大きい", "おおきい", ["ookii", "okii"]),
    (14, "Large", "大", "だい", ["dai"]),
    (14, "University", "大学", "だいがく", ["daigaku"]),

    # Lesson 15
    (15, "Man", "男", "おとこ", ["otoko"]),
    (15, "Boy", "男の子", "おとこのこ", ["otokonoko"]),
    (15, "Male / boy (Formal)", "男子", "だんし", ["danshi"]),
    (15, "Girl", "女の子", "おんなのこ", ["onnanoko"]),
    (15, "Female / girl (Formal)", "女子", "じょし", ["joshi"]),
    (15, "Egg", "玉子", "たまご", ["tamago"]),
    (15, "King", "王", "おう", ["ou", "o"]),
    (15, "Child", "子供", "こども", ["kodomo"]),
    (15, "Prince", "王子", "おうじ", ["ouji", "oji"]),
    (15, "Queen", "女王", "じょおう", ["joou", "joo"]),

    # Lesson 16
    (16, "A.M. / before noon", "午前", "ごぜん", ["gozen"]),
    (16, "Front / before", "前", "まえ", ["mae"]),
    (16, "Blue", "青", "あお", ["ao"]),
    (16, "After", "後", "あと", ["ato"]),
    (16, "After that", "その後", "そのご", ["sonogo"]),
    (16, "Behind", "後ろ", "うしろ", ["ushiro"]),
    (16, "Red", "赤", "あか", ["aka"]),
    (16, "Oneself / myself", "自分", "じぶん", ["jibun"]),
    (16, "Three years ago", "三年前", "さんねんまえ", ["sannenmae"]),
    (16, "P.M. / afternoon", "午後", "ごご", ["gogo"]),
    (16, "Birthday", "お誕生日", "おたんじょうび", ["otanjoubi", "otanjobi"]),
    (16, "To be born", "生まれる", "うまれる", ["umareru"]),

    # Lesson 17
    (17, "Dog", "犬", "いぬ", ["inu"]),
    (17, "Watchdog", "番犬", "ばんけん", ["banken"]),
    (17, "O'clock / hour suffix", "～時", "～じ", ["ji"]),
    (17, "Sometimes", "時々", "ときどき", ["tokidoki"]),
    (17, "Temple", "お寺", "おてら", ["otera"]),
    (17, "Long", "長い", "ながい", ["nagai"]),

    # Lesson 18
    (18, "To see / look", "見る", "みる", ["miru"]),
    (18, "Observation / field trip", "見学", "けんがく", ["kengaku"]),
    (18, "One pair (of footwear)", "一足", "いっそく", ["issoku"]),
    (18, "Purpose / objective", "目的", "もくてき", ["mokuteki"]),
    (18, "Foot / leg", "足", "あし", ["ashi"]),
    (18, "Ear", "耳", "みみ", ["mimi"]),
    (18, "Eye", "目", "め", ["me"]),

    # Lesson 19
    (19, "Letter / character", "字", "じ", ["ji"]),
    (19, "Rain", "雨", "あめ", ["ame"]),
    (19, "Cancellation / suspension", "中止", "ちゅうし", ["chuushi", "chushi"]),
    (19, "Mountain", "山", "やま", ["yama"]),
    (19, "Mount Fuji", "富士山", "ふじさん", ["fujisan"]),
    (19, "Half", "半分", "はんぶん", ["hanbun"]),
    (19, "River", "川", "かわ", ["kawa"]),
    (19, "High / tall / expensive", "高い", "たかい", ["takai"]),
    (19, "Evening", "夕方", "ゆうがた", ["yuugata", "yugata"]),
    (19, "The rain stops", "雨が止む", "あめがやむ", ["amegayamu"]),
    (19, "To stop something", "止める", "とめる", ["tomeru"]),

    # Lesson 20
    (20, "Early", "早い", "はやい", ["hayai"]),
    (20, "Bamboo", "竹", "たけ", ["take"]),
    (20, "Grass / weeds", "草", "くさ", ["kusa"]),
    (20, "Flower", "花", "はな", ["hana"]),
    (20, "Vase", "花瓶", "かびん", ["kabin"]),
    (20, "Entrance", "入口", "いりぐち", ["iriguchi"]),
    (20, "Rice field", "田んぼ", "たんぼ", ["tanbo", "tambo"]),
    (20, "Input", "入力", "にゅうりょく", ["nyuuryoku", "nyuryoku"]),
    (20, "Name", "名前", "なまえ", ["namae"]),
    (20, "To take out / submit", "出す", "だす", ["dasu"]),
    (20, "Famous", "有名", "ゆうめい", ["yuumei", "yumei"]),

    # Lesson 21
    (21, "Right", "右", "みぎ", ["migi"]),
    (21, "Left", "左", "ひだり", ["hidari"]),
    (21, "Sentence / text", "文章", "ぶんしょう", ["bunshou", "bunsho"]),
    (21, "Literature", "文学", "ぶんがく", ["bungaku"]),
    (21, "Word / language", "言葉", "ことば", ["kotoba"]),
    (21, "To sell", "売る", "うる", ["uru"]),
    (21, "To say", "言う", "いう", ["iu", "yuu"]),

    # Lesson 22
    (22, "Between / interval", "間", "あいだ", ["aida"]),
    (22, "Teacher", "先生", "せんせい", ["sensei"]),
    (22, "To listen / hear / ask", "聞く", "きく", ["kiku"]),
    (22, "Time / hours", "時間", "じかん", ["jikan"]),
    (22, "Ahead / before", "先", "さき", ["saki"]),
    (22, "Newspaper", "新聞", "しんぶん", ["shinbun", "shimbun"]),
    (22, "Splendid / fine", "立派", "りっぱ", ["rippa"]),
    (22, "To stand", "立つ", "たつ", ["tatsu"]),

    # Lesson 23
    (23, "My mother / one's mother", "母", "はは", ["haha"]),
    (23, "Mother", "お母さん", "おかあさん", ["okaasan"]),
    (23, "My father / one's father", "父", "ちち", ["chichi"]),
    (23, "Father", "お父さん", "おとうさん", ["otousan", "otosan"]),
    (23, "To write", "書く", "かく", ["kaku"]),
    (23, "Music", "音楽", "おんがく", ["ongaku"]),
    (23, "Sound", "音", "おと", ["oto"]),
    (23, "Dictionary", "辞書", "じしょ", ["jisho"]),

    # Lesson 24
    (24, "Healthy / energetic", "元気", "げんき", ["genki"]),
    (24, "Electricity", "電気", "でんき", ["denki"]),
    (24, "Thread", "糸", "いと", ["ito"]),
    (24, "Weather", "天気", "てんき", ["tenki"]),
    (24, "Air", "空気", "くうき", ["kuuki", "kuki"]),
    (24, "Sky", "空", "そら", ["sora"]),
    (24, "Grove", "林", "はやし", ["hayashi"]),
    (24, "Forest", "森", "もり", ["mori"]),
    (24, "Forest / woodland", "森林", "しんりん", ["shinrin"]),
    (24, "One long object", "一本", "いっぽん", ["ippon"]),
    (24, "Soap", "石鹸", "せっけん", ["sekken"]),
    (24, "Stone", "石", "いし", ["ishi"]),

    # Lesson 25
    (25, "Town", "町", "まち", ["machi"]),
    (25, "Village", "村", "むら", ["mura"]),
    (25, "To go", "行く", "いく", ["iku", "yuku"]),
    (25, "Bank", "銀行", "ぎんこう", ["ginkou", "ginko"]),
    (25, "Water power / hydropower", "水力", "すいりょく", ["suiryoku"]),
    (25, "Strength / power", "力", "ちから", ["chikara"]),
    (25, "Insect / bug", "虫", "むし", ["mushi"]),
    (25, "To eat", "食べる", "たべる", ["taberu"]),

    # Lesson 26
    (26, "Outside", "外", "そと", ["soto"]),
    (26, "Foreign country", "外国", "がいこく", ["gaikoku"]),
    (26, "Foreigner", "外国人", "がいこくじん", ["gaikokujin"]),
    (26, "North", "北", "きた", ["kita"]),
    (26, "West", "西", "にし", ["nishi"]),
    (26, "South", "南", "みなみ", ["minami"]),
    (26, "East", "東", "ひがし", ["higashi"]),
]


def normalize(text: str) -> str:
    """Normalize spaces, punctuation, case, and common long-vowel spellings."""
    text = text.strip().lower()
    replacements = {
        "ā": "aa", "ī": "ii", "ū": "uu", "ē": "ee", "ō": "ou",
        "â": "aa", "î": "ii", "û": "uu", "ê": "ee", "ô": "ou",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Normalize Unicode and remove separators/punctuation.
    text = unicodedata.normalize("NFKC", text)
    return "".join(ch for ch in text if ch.isalnum() or "ぁ" <= ch <= "ん")


def romaji_variants(reading: str) -> set[str]:
    """Accept careful and casual long-vowel typing: ou/o, uu/u, oo/o."""
    base = normalize(reading)
    variants = {base}
    variants.add(base.replace("ou", "o"))
    variants.add(base.replace("uu", "u"))
    variants.add(base.replace("oo", "o"))
    variants.add(base.replace("ou", "o").replace("uu", "u").replace("oo", "o"))
    return variants


def accepted_answers(item) -> set[str]:
    lesson, english, kanji, kana, romanji = item
    accepted = {normalize(kana.replace(" / ", ""))}

    # If kana contains slash alternatives, accept each side.
    for part in kana.replace("～", "").split("/"):
        accepted.add(normalize(part))

    for r in romanji:
        accepted.update(romaji_variants(r))

    return {a for a in accepted if a}


def choose_lessons() -> tuple[int, int]:
    print("\nChoose the Reading lessons to quiz:")
    print("  Press Enter for all Lessons 1-26")
    print("  Or enter a range such as 1-5, 10-20, or just 20")

    while True:
        raw = input("Lessons: ").strip()
        if not raw:
            return 1, 26

        try:
            if "-" in raw:
                start, end = map(int, raw.split("-", 1))
            else:
                start = end = int(raw)

            if 1 <= start <= end <= 26:
                return start, end
        except ValueError:
            pass

        print("Please enter a valid lesson/range between 1 and 26.")


def choose_question_count(max_questions: int) -> int:
    while True:
        raw = input(
            f"How many questions? (1-{max_questions}, Enter = all): "
        ).strip()

        if not raw:
            return max_questions

        try:
            count = int(raw)
            if 1 <= count <= max_questions:
                return count
        except ValueError:
            pass

        print(f"Please enter a number from 1 to {max_questions}.")


def run_quiz():
    print("=" * 58)
    print("       ToKini Andy N5 Kanji Reading Vocabulary Quiz")
    print("=" * 58)
    print("\nYou see ONLY the English meaning.")
    print("Type the Japanese reading in romaji or hiragana.")
    print("The kanji is revealed only AFTER you answer.")
    print("Correct = +1. Wrong = 0.\n")

    start_lesson, end_lesson = choose_lessons()
    pool = [item for item in VOCAB if start_lesson <= item[0] <= end_lesson]

    count = choose_question_count(len(pool))
    questions = random.sample(pool, count)

    score = 0
    mistakes = []

    for index, item in enumerate(questions, 1):
        lesson, english, kanji, kana, romanji = item

        print("\n" + "-" * 58)
        print(f"Question {index}/{count}   |   Reading Lesson {lesson}")
        print(f"\nMeaning: {english}")

        answer = input("Reading: ").strip()
        normalized_answer = normalize(answer)
        accepted = accepted_answers(item)

        if normalized_answer in accepted:
            score += 1
            print("\n✅ CORRECT! +1")
        else:
            print("\n❌ Incorrect")
            mistakes.append((english, answer, kanji, kana, romanji[0], lesson))

        # Reveal only after the user has answered.
        print(f"Kanji:   {kanji}")
        print(f"Kana:    {kana}")
        print(f"Romaji:  {romanji[0]}")
        print(f"Score:   {score}/{index}")

    percentage = score / count * 100

    print("\n" + "=" * 58)
    print("                    QUIZ COMPLETE")
    print("=" * 58)
    print(f"\nTotal score: {score}/{count}")
    print(f"Percentage:  {percentage:.1f}%")

    if mistakes:
        print("\n" + "=" * 58)
        print("                    REVIEW THESE")
        print("=" * 58)
        for english, your_answer, kanji, kana, romaji, lesson in mistakes:
            shown_answer = your_answer if your_answer else "(blank)"
            print(
                f"\nL{lesson:02d} | {english}\n"
                f"  You wrote: {shown_answer}\n"
                f"  Correct:   {kanji}  {kana}  ({romaji})"
            )
    else:
        print("\n🏆 Perfect score — no mistakes to review!")

    input()

if __name__ == "__main__":
    run_quiz()
