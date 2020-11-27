
#C# Regex matching

# |-------------------------------------------------------------
#T# import the regex module to use regular expressions, it supersedes the re module
import regex

#C# --- Regex functions, methods, and attributes

# |-----
#T# compile a regex object with the compile function, this object has access to the rest of regex functions, methods, and attributes shown here, via dot notation
regex_object1 = regex.compile(r'pattern1') # regex.Regex('pattern1', flags=regex.V0)
search1 = regex_object1.search('str1 pattern1 str2') # <regex.Match object; span=(5, 13), match='pattern1'>

#T# match at the start of the string with the match function, if the match fails then None is returned
# SYNTAX match('pattern1', 'str1')
match1 = regex.match(r'a', 'aabbcc') # <regex.Match object; span=(0, 1), match='a'>

#T# match at any place of the string with the search function, if the match fails then None is returned
# SYNTAX search('pattern1', 'str1')
search1 = regex.search(r'(bc)(cd)', 'aabbccdd') # <regex.Match object; span=(3, 7), match='bccd'>

#T# get a list with the regex groups found with the groups function
search1 = regex.search(r'(bc)(cd)', 'aabbccdd') # <regex.Match object; span=(3, 7), match='bccd'>
tuple1 = search1.groups() # ('bc', 'cd')

#T# get a particular group value with the group function

# SYNTAX group(int1)
#T# int1 is the group number

search1 = regex.search(r'(bc)(cd)', 'aabbccdd')
str1 = search1.group(2) # 'cd'

#T# get the starting position of a group with the start function

# SYNTAX start(int1)
#T# int1 is the group number, this returns a position (the start of the string is 0)

search1 = regex.search(r'(bc)(cd)', 'aabbccdd')
int1 = search1.start(2) # 5

#T# get a list with all global matches with the findall function
list1 = regex.findall(r'text', 'strtextstrtextstr') # ['text', 'text']

#T# get a Scanner object that contains all the non overlapping matches as Match objects, and that can be iterated in a for loop with the finditer function
scanner1 = regex.finditer(r'text', 'strtextstrtextstr') # <_regex.Scanner object at 0x22983b0>
list1 = []
for it1 in scanner1: list1.append(it1) # list1 == [<regex.Match object; span=(3, 7), match='text'>, <regex.Match object; span=(10, 14), match='text'>]

#T# get a list without the matches with the split function
list1 = regex.split(r'text', 'strtextstrtextstr') # ['str', 'str', 'str']

#T# substitute matches with a replacement string with the sub function
str1 = regex.sub(r'text', 'TEXT', 'strtextstrtextstr') # 'strTEXTstrTEXTstr'

#T# the Match objects have a few properties and methods

#T# the groups method returns a tuple where each element is the match of a group
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
tuple1 = search1.groups() # ('s', 'tr', '1')

#T# the span method returns the start and end positions of a group, or of the match if no group is input as argument
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
tuple1 = search1.span(1) # (0, 1)

#T# the group method returns the contents of single groups, or the whole match if no group is input as argument
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
str1 = search1.group(2) # 'tr'

#T# the string property contains the string being analyzed, i.e. the one that the regex is being applied on, the input string
search1 = regex.search(r'(s)(tr)(1)', 'textstr1text') # <regex.Match object; span=(4, 8), match='str1'>
str1 = search1.string # 'textstr1text'
# |-----

#C# --- Characters

# |-----
#T# the dot . is used to match any char
search1 = regex.search(r'.', 'str1') # <regex.Match object; span=(0, 1), match='s'>

#T# to match an operator as a literal char, it must be escaped with a backslash \
search1 = regex.search(r'\.', 'str1.') # <regex.Match object; span=(4, 5), match='.'>

#T# the escaped char \s matches one whitespace (space, tab, newline)
search1 = regex.search(r'\sb', 'a b') # <regex.Match object; span=(1, 3), match=' b'>

#T# the escaped char \S matches one non whitespace
search1 = regex.search(r'\Sc', 'a bc') # <regex.Match object; span=(2, 4), match='bc'>

#T# the escaped char \w matches one alphanumeric character or an underscore
search1 = regex.search(r'\w', '_a5.') # <regex.Match object; span=(0, 1), match='_'>

#T# the escaped char \W matches one non alphanumeric character nor an underscore
search1 = regex.search(r'\W', '_a5.') # <regex.Match object; span=(3, 4), match='.'>

#T# the escaped char \d matches one digit
search1 = regex.search(r'\d', 'a5b') # <regex.Match object; span=(1, 2), match='5'>

#T# the escaped char \D matches one non digit
search1 = regex.search(r'\D', '5bc') # <regex.Match object; span=(1, 2), match='b'>

#T# the escaped char \X matches one unicode char
search1 = regex.search(r'\w\X', 'a\u2446b') # <regex.Match object; span=(0, 2), match='a⑆'>

#T# to match a particular unicode char, use either \uHex1, \UHex1Hex2, the unicode char itself, or \N{name1}, Hex1 and Hex2 are hexadecimal numbers of four digits that represent the unicode char being matched, name1 is the char's name in the Unicode standard
search1 = regex.search(r'\u2446b', 'a⑆b') # <regex.Match object; span=(1, 3), match='⑆b'>
search1 = regex.search(r'\U0001F306', '\U0001F306') # <regex.Match object; span=(0, 1), match='🌆'>
search1 = regex.search(r'a⑆', 'a⑆b') # <regex.Match object; span=(0, 2), match='a⑆'>
search1 = regex.search(r'\N{OCR BRANCH BANK IDENTIFICATION}', 'a⑆b') # <regex.Match object; span=(1, 2), match='⑆'>

#T# unicode properties are matched in general with \p{prop1} where prop1 stands for the unicode property being matched, a char with said property will be matched

#T# unicode categories are matched with \p{categ1}, categ1 can be one of the following
#T#     L, matches a letter char, such as 's'
#T#     Ll, matches a lowercase letter char, such as 's'
#T#     Lu, matches an uppercase letter char, such as 'S'
#T#     Lt, matches a titlecase letter char, such as 'ǅ' \u01C5
#T#     L&, matches a lowercase, uppercase, or titlecase letter char, such as 'ǅ'
#T#     Lm, matches a modifier letter char, such as 'ʱ' \u02B1
#T#     Lo, matches a type other letter char, such as 'ƻ' \u01BB
#T#     M, matches a combining mark char (like diacritics), such as the breve in 'ă' a\u0306
#T#     Mc, matches an spacing combining mark char, such as 'ೄ' \u0CC4
#T#     Me, matches an enclosing mark char, such as 'a꙲' a\uA672
#T#     Mn, matches a nonspacing mark char, such as 'ả' a\u0309
#T#     N, matches a numeric char, such as '୬' \u0B6C
#T#     Nd, matches a decimal digit char, such as '߈' \u07C8
#T#     Nl, matches a number letter char, such as 'ↈ' \u2188
#T#     No, matches a type other number char, such as '௲' \u0BF2
#T#     P, matches a punctuation char, such as '⸗' \u2E17
#T#     Pc, matches a punctuation connector char, such as '﹏' \uFE4F
#T#     Pd, matches a punctuation dash char, such as '⸻' \u2E3B
#T#     Pe, matches a punctuation close char, such as '⟧' \u27E7
#T#     Pf, matches a punctuation final quote char, such as '»' \u00BB
#T#     Pi, matches a punctuation initial quote char, such as '⸄' \u2E04
#T#     Ps, matches a punctuation open char, such as '⁅' \u2045
#T#     Po, matches a type other punctuation char, such as '¶' \u00B6
#T#     S, matches a symbol char, such as '⌨' \u2328"
#T#     Sc, matches a symbol currency char, such as '֏' \u058F
#T#     Sk, matches a symbol modifier char, such as '˧' \u02E7
#T#     Sm, matches a symbol math char, such as '؆' \u0606
#T#     So, matches a type other symbol char, such as '۩' \u06E9
#T#     Z, matches a separator char, such as \u205F
#T#     Zl, matches a separator line char, such as \u2028
#T#     Zp, matches a separator paragraph char, such as \u2029
#T#     Zs, matches a separator space char, such as ' ' \u0020
#T#     C, matches a control char, such as \uFFF9
#T#     Cf, matches a format control char, such as \u2060
#T#     Co, matches a private use control char, such as \uE000
#T#     Cc, matches a type other control char, such as \u008A
search1 = regex.search(r'\p{L}', 'str1') # <regex.Match object; span=(0, 1), match='s'>
search1 = regex.search(r'\p{Lt}', '\u01C5') # <regex.Match object; span=(0, 1), match='ǅ'>
search1 = regex.search(r'\p{Lm}', '\u02B1') # <regex.Match object; span=(0, 1), match='ʱ'>
search1 = regex.search(r'\p{Lo}', '\u01BB') # <regex.Match object; span=(0, 1), match='ƻ'>
search1 = regex.search(r'a\p{M}', 'a\u0306') # <regex.Match object; span=(0, 2), match='ă'>
search1 = regex.search(r'\p{N}', '\u0B6C') # <regex.Match object; span=(0, 1), match='୬'>
search1 = regex.search(r'\p{P}', '\u2E17') # <regex.Match object; span=(0, 1), match='⸗'>
search1 = regex.search(r'\p{S}', '\u2328') # <regex.Match object; span=(0, 1), match='⌨'>
search1 = regex.search(r'\p{Z}', '\u205F') # <regex.Match object; span=(0, 1), match='\u205f'>
search1 = regex.search(r'\p{C}', '\uFFF9') # <regex.Match object; span=(0, 1), match='\ufff9'>

#T# unicode scripts are matched with \p{script1}, the possible values of script1 are the following (each name represents a script, 'Common' is for chars common to many scripts, 'Inherited' is for chars that inherit their script from a char they accompany, like nonspacing diacritics do): Adlam, Ahom, Anatolian_Hieroglyphs, Arabic, Armenian, Avestan, Balinese, Bamum, Bassa_Vah, Batak, Bengali, Bhaiksuki, Bopomofo, Brahmi, Braille, Buginese, Buhid, Canadian_Aboriginal, Carian, Caucasian_Albanian, Chakma, Cham, Cherokee, Chorasmian, Common, Coptic, Cuneiform, Cypriot, Cyrillic, Deseret, Devanagari, Dives_Akuru, Dogra, Duployan, Egyptian_Hieroglyphs, Elbasan, Elymaic, Ethiopic, Georgian, Glagolitic, Gothic, Grantha, Greek, Gujarati, Gunjala_Gondi, Gurmukhi, Han, Hangul, Hanifi_Rohingya, Hanunoo, Hatran, Hebrew, Hiragana, Imperial_Aramaic, Inherited, Inscriptional_Pahlavi, Inscriptional_Parthian, Javanese, Kaithi, Kannada, Katakana, Kayah_Li, Kharoshthi, Khitan_Small_Script, Khmer, Khojki, Khudawadi, Lao, Latin, Lepcha, Limbu, Linear_A, Linear_B, Lisu, Lycian, Lydian, Mahajani, Makasar, Malayalam, Mandaic, Manichaean, Marchen, Masaram_Gondi, Medefaidrin, Meetei_Mayek, Mende_Kikakui, Meroitic_Cursive, Meroitic_Hieroglyphs, Miao, Modi, Mongolian, Mro, Multani, Myanmar, Nabataean, Nandinagari, New_Tai_Lue, Newa, Nko, Nushu, Nyiakeng_Puachue_Hmong, Ogham, Ol_Chiki, Old_Hungarian, Old_Italic, Old_North_Arabian, Old_Permic, Old_Persian, Old_Sogdian, Old_South_Arabian, Old_Turkic, Oriya, Osage, Osmanya, Pahawh_Hmong, Palmyrene, Pau_Cin_Hau, Phags_Pa, Phoenician, Psalter_Pahlavi, Rejang, Runic, Samaritan, Saurashtra, Sharada, Shavian, Siddham, Sinhala, Sogdian, Sora_Sompeng, Soyombo, Sundanese, Sutton_SignWriting, Syloti_Nagri, Syriac, Tagalog, Tagbanwa, Tai_Le, Tai_Tham, Tai_Viet, Takri, Tamil, Tangut, Telugu, Thaana, Thai, Tibetan, Tifinagh, Tirhuta, Ugaritic, Vai, Wancho, Warang_Citi, Yezidi, Yi, Zanabazar_Square
search1 = regex.search(r'\p{Common}', '5') # <regex.Match object; span=(0, 1), match='5'>
search1 = regex.search(r'\p{Adlam}', "\U0001E904") # <regex.Match object; span=(0, 1), match='𞤄'>
search1 = regex.search(r'\p{Arabic}', "\u060B") # <regex.Match object; span=(0, 1), match='؋'>
search1 = regex.search(r'\p{Lepcha}', "\u1C12") # <regex.Match object; span=(0, 1), match='ᰒ'>
search1 = regex.search(r'\p{Nko}', "\u07D2") # <regex.Match object; span=(0, 1), match='ߒ'>
search1 = regex.search(r'\p{Tibetan}', "\u0F12") # <regex.Match object; span=(0, 1), match='༒'>

#T# unicode blocks are matched with \p{block1}, the possible values of block1 are the following: InAdlam, InAegean_Numbers, InAhom, InAlchemical_Symbols, InAlphabetic_Presentation_Forms, InAnatolian_Hieroglyphs, InAncient_Greek_Musical_Notation, InAncient_Greek_Numbers, InAncient_Symbols, InArabic, InArabic_Extended-A, InArabic_Mathematical_Alphabetic_Symbols, InArabic_Presentation_Forms-A, InArabic_Presentation_Forms-B, InArabic_Supplement, InArmenian, InArrows, InAvestan, InBalinese, InBamum, InBamum_Supplement, InBasic_Latin, InBassa_Vah, InBatak, InBengali, InBhaiksuki, InBlock_Elements, InBopomofo, InBopomofo_Extended, InBox_Drawing, InBrahmi, InBraille_Patterns, InBuginese, InBuhid, InByzantine_Musical_Symbols, InCarian, InCaucasian_Albanian, InChakma, InCham, InCherokee, InCherokee_Supplement, InChess_Symbols, InChorasmian, InCJK_Compatibility, InCJK_Compatibility_Forms, InCJK_Compatibility_Ideographs, InCJK_Compatibility_Ideographs_Supplement, InCJK_Radicals_Supplement, InCJK_Strokes, InCJK_Symbols_and_Punctuation, InCJK_Unified_Ideographs, InCJK_Unified_Ideographs_Extension_A, InCJK_Unified_Ideographs_Extension_B, InCJK_Unified_Ideographs_Extension_C, InCJK_Unified_Ideographs_Extension_D, InCJK_Unified_Ideographs_Extension_E, InCJK_Unified_Ideographs_Extension_F, InCJK_Unified_Ideographs_Extension_G, InCombining_Diacritical_Marks, InCombining_Diacritical_Marks_Extended, InCombining_Diacritical_Marks_for_Symbols, InCombining_Diacritical_Marks_Supplement, InCombining_Half_Marks, InCommon_Indic_Number_Forms, InControl_Pictures, InCoptic, InCoptic_Epact_Numbers, InCounting_Rod_Numerals, InCuneiform, InCuneiform_Numbers_and_Punctuation, InCurrency_Symbols, InCypriot_Syllabary, InCyrillic, InCyrillic_Extended-A, InCyrillic_Extended-B, InCyrillic_Extended-C, InCyrillic_Supplement, InDeseret, InDevanagari, InDevanagari_Extended, InDingbats, InDives_Akuru, InDogra, InDomino_Tiles, InDuployan, InEarly_Dynastic_Cuneiform, InEgyptian_Hieroglyphs, InEgyptian_Hieroglyph_Format_Controls, InElbasan, InElymaic, InEmoticons, InEnclosed_Alphanumeric_Supplement, InEnclosed_Alphanumerics, InEnclosed_CJK_Letters_and_Months, InEnclosed_Ideographic_Supplement, InEthiopic, InEthiopic_Extended, InEthiopic_Extended-A, InEthiopic_Supplement, InGeneral_Punctuation, InGeometric_Shapes, InGeometric_Shapes_Extended, InGeorgian, InGeorgian_Extended, InGeorgian_Supplement, InGlagolitic, InGlagolitic_Supplement, InGothic, InGrantha, InGreek_and_Coptic, InGreek_Extended, InGujarati, InGunjala_Gondi, InGurmukhi, InHalfwidth_and_Fullwidth_Forms, InHangul_Compatibility_Jamo, InHangul_Jamo, InHangul_Jamo_Extended-A, InHangul_Jamo_Extended-B, InHangul_Syllables, InHanifi_Rohingya, InHanunoo, InHatran, InHebrew, InHigh_Private_Use_Surrogates, InHigh_Surrogates, InHiragana, InIdeographic_Description_Characters, InIdeographic_Symbols_and_Punctuation, InImperial_Aramaic, InIndic_Siyaq_Numbers, InInscriptional_Pahlavi, InInscriptional_Parthian, InIPA_Extensions, InJavanese, InKaithi, InKana_Extended-A, InKana_Supplement, InKanbun, InKangxi_Radicals, InKannada, InKatakana, InKatakana_Phonetic_Extensions, InKayah_Li, InKharoshthi, InKhitan_Small_Script, InKhmer, InKhmer_Symbols, InKhojki, InKhudawadi, InLao, InLatin-1_Supplement, InLatin_Extended-A, InLatin_Extended-B, InLatin_Extended-C, InLatin_Extended-D, InLatin_Extended-E, InLatin_Extended_Additional, InLepcha, InLetterlike_Symbols, InLimbu, InLinear_A, InLinear_B_Ideograms, InLinear_B_Syllabary, InLisu, InLisu_Supplement, InLow_Surrogates, InLycian, InLydian, InMahajani, InMahjong_Tiles, InMakasar, InMalayalam, InMandaic, InManichaean, InMarchen, InMasaram_Gondi, InMathematical_Alphanumeric_Symbols, InMathematical_Operators, InMayan_Numerals, InMedefaidrin, InMeetei_Mayek, InMeetei_Mayek_Extensions, InMende_Kikakui, InMeroitic_Cursive, InMeroitic_Hieroglyphs, InMiao, InMiscellaneous_Mathematical_Symbols-A, InMiscellaneous_Mathematical_Symbols-B, InMiscellaneous_Symbols, InMiscellaneous_Symbols_and_Arrows, InMiscellaneous_Symbols_and_Pictographs, InMiscellaneous_Technical, InModi, InModifier_Tone_Letters, InMongolian, InMongolian_Supplement, InMro, InMultani, InMusical_Symbols, InMyanmar, InMyanmar_Extended-A, InMyanmar_Extended-B, InNabataean, InNandinagari, InNew_Tai_Lue, InNewa, InNKo, InNumber_Forms, InNushu, InNyiakeng_Puachue_Hmong, InOgham, InOl_Chiki, InOld_Hungarian, InOld_Italic, InOld_North_Arabian, InOld_Permic, InOld_Persian, InOld_Sogdian, InOld_South_Arabian, InOld_Turkic, InOptical_Character_Recognition, InOriya, InOrnamental_Dingbats, InOsage, InOsmanya, InOttoman_Siyaq_Numbers, InPahawh_Hmong, InPalmyrene, InPau_Cin_Hau, InPhags-pa, InPhaistos_Disc, InPhoenician, InPhonetic_Extensions, InPhonetic_Extensions_Supplement, InPlaying_Cards, InPrivate_Use_Area, InPsalter_Pahlavi, InRejang, InRumi_Numeral_Symbols, InRunic, InSamaritan, InSaurashtra, InSharada, InShavian, InShorthand_Format_Controls, InSiddham, InSinhala, InSinhala_Archaic_Numbers, InSmall_Form_Variants, InSmall_Kana_Extension, InSogdian, InSora_Sompeng, InSoyombo, InSpacing_Modifier_Letters, InSpecials, InSundanese, InSundanese_Supplement, InSuperscripts_and_Subscripts, InSupplemental_Arrows-A, InSupplemental_Arrows-B, InSupplemental_Arrows-C, InSupplemental_Mathematical_Operators, InSupplemental_Punctuation, InSupplemental_Symbols_and_Pictographs, InSupplementary_Private_Use_Area-A, InSupplementary_Private_Use_Area-B, InSutton_SignWriting, InSyloti_Nagri, InSymbols_and_Pictographs_Extended-A, InSymbols_for_Legacy_Computing, InSyriac, InSyriac_Supplement, InTagalog, InTagbanwa, InTags, InTai_Le, InTai_Tham, InTai_Viet, InTai_Xuan_Jing_Symbols, InTakri, InTamil, InTamil_Supplement, InTangut, InTangut_Components, InTangut_Supplement, InTelugu, InThaana, InThai, InTibetan, InTifinagh, InTirhuta, InTransport_and_Map_Symbols, InUgaritic, InUnified_Canadian_Aboriginal_Syllabics, InUnified_Canadian_Aboriginal_Syllabics_Extended, InVai, InVariation_Selectors, InVariation_Selectors_Supplement, InVedic_Extensions, InVertical_Forms, InWancho, InWarang_Citi, InYezidi, InYi_Radicals, InYi_Syllables, InYijing_Hexagram_Symbols, InZanabazar_Square
search1 = regex.search(r'\p{InBasic_Latin}', '&') # <regex.Match object; span=(0, 1), match='&'>
search1 = regex.search(r'\p{InLatin-1_Supplement}', '\u00A7') # <regex.Match object; span=(0, 1), match='§'>
search1 = regex.search(r'\p{InGurmukhi}', '\u0A07') # <regex.Match object; span=(0, 1), match='ਇ'>
search1 = regex.search(r'\p{InMusical_Symbols}', '\U0001D121') # <regex.Match object; span=(0, 1), match='𝄡'>

#T# the escaped char \t matches one tab char
search1 = regex.search(r'\tc', 'ab    c') # <regex.Match object; span=(2, 4), match='\tc'>

#T# the escaped char \r matches one carriage return (this also works in the sed program)
print('ab\rc') # cb
search1 = regex.search(r'\rc', 'ab\rc') # <regex.Match object; span=(2, 4), match='\rc'>

#T# the escaped char \n matches one newline
search1 = regex.search(r'r1\nst', 'str1\nstr2') # <regex.Match object; span=(2, 7), match='r1\nst'>

#T# there is no support for the escaped char \N to match a non newline, it can be replaced with [^\n]
search1 = regex.search(r'[^\n]c', 'ab\ncd') # None

#T# there is no support for the escaped char \h to match an horizontal whitespace (space, tab), it can be approximated by [^\S\n] but a few vertical spaces can be matched this way
search1 = regex.search(r'[^\S\n]b[^\S\n]c', 'a b    c') # <regex.Match object; span=(1, 5), match=' b\tc'>

#T# there is no support for the escaped char \H to match a non horizontal whitespace

#T# the escaped chars \Q and \E escape any characters inside them, but in Python they are not used, the escape function is used instead
search1 = regex.search(regex.escape(r'a.+?'), 'a.+?') # <regex.Match object; span=(0, 4), match='a.+?'>

#T# the escaped char \K removes the part of the match that is to its left
search1 = regex.search(r'str1\n\Kstr2', 'str1\nstr2') # <regex.Match object; span=(5, 9), match='str2'>

#T# comments are introduced with (?# comment1)
search1 = regex.search(r'(?# initial comment)str(?# a number comes next)1', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
# |-----

#C# --- Quantifiers

# |-----
#T# the question mark ? is used as a quantifier to match 0 or 1 of the preceding char
search1 = regex.search(r'r?1', 'str1') # <regex.Match object; span=(2, 4), match='r1'>

#T# the asterisk * is used as a quantifier to match 0 or more of the preceding char
search1 = regex.search(r'r*1', 'st1') # <regex.Match object; span=(2, 3), match='1'>

#T# the plus sign + is used as a quantifier to match 1 or more of the preceding char
search1 = regex.search(r'r+1', 'strrr1') # <regex.Match object; span=(2, 6), match='rrr1'>

#T# the syntax {int1} is used as a quantifier to match the preceding char int1 times
search1 = regex.search(r'r{2}1', 'strrrr1') # <regex.Match object; span=(4, 7), match='rr1'>

#T# the syntax {int1,int2} is used as a quantifier to match the preceding char between int1 and int2 times (as many times as possible), so int2 >= int1, if int2 is omitted then match any amount greater than or equal to int1
search1 = regex.search('r{1,3}1', 'strrrrr1') # <regex.Match object; span=(4, 8), match='rrr1'>
search1 = regex.search(r'r{1,}1', 'strrrrr1') # <regex.Match object; span=(2, 8), match='rrrrr1'>

#T# lazy (non greedy) quantifiers are created with a question mark ? after the operator, works as ??, *?, +?
search1 = regex.search(r'[0-9][0-9]??', '12345') # <regex.Match object; span=(0, 1), match='1'>
search1 = regex.search(r'[0-9]*?', '12345') # <regex.Match object; span=(0, 0), match=''>
search1 = regex.search(r'[0-9]+?', '12345') # <regex.Match object; span=(0, 1), match='1'>

#T# possessive quantifiers add a plus + at the end of the other quantifiers, they are greedy without backtracking, so that after a match fails, it is not checked if less chars would make it succeed, works as *+, ++, {}+
search1 = regex.search(r'a*+', 'aaa') # <regex.Match object; span=(0, 3), match='aaa'>
search1 = regex.search(r'\w++b', 'aaaab') # None #| 'aaaab' would be matched without the possessive quantifier
search1 = regex.search(r'\w{1,7}+F', 'abcdeF') # None #| 'abcdeF' would be matched without the possessive quantifier
# |-----

#C# --- Character classes

# |-----
#T# the syntax [char1char2charN] is called a character class, and used to match any single one of the characters, char1, char2, up to charN
search1 = regex.search(r'[trs]1', 'strr1') # <regex.Match object; span=(3, 5), match='r1'>

#T# using a caret ^ at the start of a character class, negates it
search1 = regex.search(r'[^trs]1', 'strr1') # None

#T# using a dash - between two characters inside a character class, matches any single one character in the range of said two characters
search1 = regex.search(r'[3-u]1', 'strr1') # <regex.Match object; span=(3, 5), match='r1'>

#T# a character class can be one of the POSIX character clases, these are made with a word within colons and a pair of brackets which don't count as the character class brackets
#T#     [:alnum:],  matches one alphanumeric char
#T#     [:alpha:],  matches one alphabetic char
#T#     [:blank:],  matches one space or tab
#T#     [:cntrl:],  matches one control char, like a vertical tab
#T#     [:digit:],  matches one digit
#T#     [:graph:],  matches one visible char
#T#     [:lower:],  matches one lowercase char
#T#     [:print:],  matches one visible char or space
#T#     [:punct:],  matches one punctuation char
#T#     [:space:],  matches one space char
#T#     [:upper:],  matches one uppercase char
#T#     [:xdigit:], matches one hexadecimal digit
search1 = regex.search(r'[[:alnum:]]', 'str1') # <regex.Match object; span=(0, 1), match='s'>

#T# in Python, set operations using nested sets are possible, || for union, && for intersection, -- for difference, ~~ for symmetric difference
search1 = regex.search(r'[[a-z] -- [aeiou]]', 'abc', flags = regex.V1) # <regex.Match object; span=(1, 2), match='b'> #| [a-z] set minus [aeiou] set
search1 = regex.search(r'[[0-7] || [d-h]]', 't5', flags = regex.V1) # <regex.Match object; span=(1, 2), match='5'> #| [0-7] set union [d-h] set
search1 = regex.search(r'[[0-7] && [d-h]]', 't5', flags = regex.V1) # None #| [0-7] set intersected with [d-h] set
search1 = regex.search(r'[[a-p] ~~ [h-z]]', 'mb', flags = regex.V1) # <regex.Match object; span=(1, 2), match='b'> #| [a-p] symmetric difference with [h-z] set
# |-----

#C# --- Groupings

# |-----
#T# the parentheses () are used to capture a group of chars, and treat this group the same as treating a single char
search1 = regex.search(r'(tr)+1', 'strtr1') # <regex.Match object; span=(1, 6), match='trtr1'>

#T# the escaped numbers \1, \2, etc., are used to match (backreference) a captured group, \1 matches the first group, \2 the second, and so on
search1 = regex.search(r'(st)(r1)A\1\2', 'str1Astr1') # <regex.Match object; span=(0, 9), match='str1Astr1'>

#T# a group number from 10 onwards can be backreferenced with \g<int1> where int1 is the group number, this avoids ambiguity
search1 = regex.search(r'(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)\g<11>', 'abcdefghijkk', flags = regex.V1) # <regex.Match object; span=(0, 12), match='abcdefghijkk'>

#T# nested groups are possible as (group1(group2)), they are numbered in order of appearance, so \1 matches group1group2, \2 matches group2
search1 = regex.search(r'(a(b)) \1', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>
search1 = regex.search(r'(a(b)) a\2', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>

#T# named groups are created with (?<group_name1>pattern1) or (?P<group_name1>pattern1) and are matched again (as a backreference) with \g<group_name1> or (?P=group_name1)
search1 = regex.search(r'(?P<group1>ab) \g<group1>', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>
search1 = regex.search(r'(?<group1>ab) \g<group1>', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>
search1 = regex.search(r'(?P<group1>ab) (?P=group1)', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>

#T# the vertical bar | is used for alternation (to match either one of the patterns separated with the vertical bar)
search1 = regex.search(r'st|tr1', 'str1') # <regex.Match object; span=(0, 2), match='st'>

#T# the syntax (?:pattern1) is used to create a non capturing group for pattern1, this means that the match of pattern1 can't be recalled with a backreference like \1, because it doesn't create a group
search1 = regex.search(r'(?:tr)(ab)\1', 'strabab') # <regex.Match object; span=(1, 7), match='trabab'>

#T# the syntax (?>pattern1|pattern2) up to patternN creates an atomic group, this means there is no backtracking, i.e. the match is fixed with the first pattern found from this group, and if it fails there is no checking the remaining patterns, in this sense pattern1 has more priority than pattern2 and so on
search1 = regex.search(r'(?>prio|priorshi)p', 'priorship') # no match #| given that the first pattern 'prio' is matched, the second one 'priorshi' will never be matched due to the atomic group, without '?>' the whole 'priorship' is matched

#T# the syntax (?|(pattern1)|pattern2|(pattern3)(pattern4)) creates a brach reset group, in it, the group numbering resets, this means that if pattern3 is matched then it's group number 1 and pattern4 is group 2, if pattern1 is matched then it's group 1, and if pattern2 is matched there are no groups created
search1 = regex.search(r'(?|A(\d+)|B(\d+)) \1', 'B12 12') # <regex.Match object; span=(0, 6), match='B12 12'>
# |-----

#C# --- Subroutines and conditionals

# |-----
#T# subroutines are a way to reuse regex patterns already created, instead of writing them again

#T# the basic subroutine reuses the numbered groups, a subroutine (?int1) matches the pattern of the numbered group int1
search1 = regex.search(r'(\w\w\w\d) (?1)', 'str1 str2') # <regex.Match object; span=(0, 9), match='str1 str2'>

#T# a named subroutine is the same as before, but using a named group, the named subroutine (?&group_name1) matches the pattern of a named group group_name1
search1 = regex.search(r'(?<group1>str\d) (?&group1)', 'str1 str2') # <regex.Match object; span=(0, 9), match='str1 str2'>

#T# there is no support for relative subroutines

#T# regex patterns can have recursion with (?R), the whole pattern is put in place of (?R), so the ? quantifier should accompany it, as (?R)? to ensure the recursion can end when it doesn't match anymore
search1 = regex.search(r'\w\d(?R)?', 'a1b2') # <regex.Match object; span=(0, 4), match='a1b2'>
search1 = regex.search(r'\w(?R)?\d', 'ab12') # <regex.Match object; span=(0, 4), match='ab12'> #| when used at the start '(?R)?pattern1' Python gives a MemoryError

#T# there is no support for regex code capsules

#T# conditionals allow matching patterns according to an if-then-else conditional, the basic form is (?(if1)(then_patterns1)|(else_patterns1)) note the plural in patterns as each can be several patterns separated by alternation |, if1 is either a lookaround or a group (named or numbered)
search1 = regex.search(r'(?(?=\d+)(123|456)|(abc|def))', '12345') # <regex.Match object; span=(0, 3), match='123'>
search1 = regex.search(r'(\d)(?(1)(2)|(b))', '12345') # <regex.Match object; span=(0, 2), match='12'>
search1 = regex.search(r'(?<group1>\d{2})(?(group1)(34)|(cd))', '12345') # <regex.Match object; span=(0, 4), match='1234'>
# |-----

#C# --- Anchors and boundaries

# |-----
#T# the caret ^ (outside a character class) matches the following chars as an anchor at the start of the line
search1 = regex.search(r'^str', 'str1') # <regex.Match object; span=(0, 3), match='str'>

#T# the escaped char \A matches the beginning of the first line
search1 = regex.search(r'\Astr\d', 'str1\nstr2') # <regex.Match object; span=(0, 4), match='str1'> #| this can only match 'str1', so the pattern '\Astr2' fails

#T# the dollar sign $ matches the preceding chars as an anchor at the end of the line
search1 = regex.search(r'tr1$', 'str1') # <regex.Match object; span=(1, 4), match='tr1'>

#T# the escaped char \Z matches the end of the last line
search1 = regex.search(r'str\d\Z', 'str1\nstr2') # <regex.Match object; span=(5, 9), match='str2'> #| this can only match 'str2', so the pattern 'str1\Z' fails

#T# the escaped char \m matches at the start of a word
search1 = regex.search(r'\mcd', 'ab cd') # <regex.Match object; span=(3, 5), match='cd'>

#T# the escaped char \M matches at the end of a word
search1 = regex.search(r'ab\M', 'ab cd') # <regex.Match object; span=(0, 2), match='ab'>

#T# the escaped char \b matches at a word boundary
search1 = regex.search(r'\bcd', 'ab cd') # <regex.Match object; span=(3, 5), match='cd'>

#T# the escaped char \B matches at a non word boundary
search1 = regex.search(r'\Bcd', 'ab cd') # None

#T# the escaped char \G matches at beginning of the first line or at the end position of the last match, so several matches must be allowed to see the effect
list1 = regex.findall(r'\G\w\d', 'a1b2c3 d4e5f6') # ['a1', 'b2', 'c3']
# |-----

#C# --- Lookarounds

# |-----
#T# the syntax (?=pattern1) is used to create a positive lookahead with pattern1, so pattern1 must appear ahead when finding a match, because pattern1 is not matched
search1 = regex.search(r'r(?=[0-2])\d', 'str1') # <regex.Match object; span=(2, 4), match='r1'> #| only matches r0, r1, or r2

#T# the syntax (?<=pattern1) is used to create a positive lookbehind with pattern1, so pattern1 must appear behind when finding a match, pattern1 is not matched
search1 = regex.search(r'(?<=st)r1', 'str1') # <regex.Match object; span=(2, 4), match='r1'>

#T# the syntax (?!pattern1) is used to create a negative lookahead with pattern1, so pattern1 can't appear ahead when finding a match, because pattern1 is not matched
search1 = regex.search(r'r1(?!00)\d\d', 'str101') # <regex.Match object; span=(2, 6), match='r101'> #| doesn't match in str100

#T# the syntax (?<!pattern1) is used to create a negative lookbehind with pattern1, so pattern1 can't appear behind when finding a match, pattern1 is not matched
search1 = regex.search(r'(?<!st)r1', 'str1') # None
# |-----

#C# --- Regex modifiers

# |-----
#T# regular regex modifiers are passed via the flags kwarg of the regex functions from the regex module, several modifiers can be passed together using the vertical bar operator |, e.g. regex.I | regex.U passes both modifiers

#T# the continuation modifier is not needed in Python, instead, functions like the findall function are used
list1 = regex.findall(r'\G\w\d', 'a1b2c3 d4e5f6') # ['a1', 'b2', 'c3']

#T# the global modifier has no inline version, in Python it is used through functions like the findall function and the finditer function, whereas the match function and the search function do not match globally
scanner1 = regex.finditer(r'text', 'strtextstrtextstr')
list1 = []
for it1 in scanner1: list1.append(it1) # [<regex.Match object; span=(3, 7), match='text'>, <regex.Match object; span=(10, 14), match='text'>]

#T# use the regular case insensitive modifier with the regex.I constant as value for the flags kwarg, this matches lowercase and uppercase letters the same
search1 = regex.search(r'STR1', 'str1', flags = regex.I) # <regex.Match object; span=(0, 4), match='str1'>

#T# use the inline case insensitive modifier (?i), turn it off with (?-i)
search1 = regex.search(r'(?i)ST(?-i)R1', 'stR1', flags = regex.V1) # <regex.Match object; span=(0, 4), match='stR1'>

#T# use the regular multiline modifier with the regex.M constant as value for the flags kwarg, this makes the caret ^ and the dollar sign $ match at the start and end of intermediate lines (all lines actually)
search1 = regex.search(r'^str2$', 'str1\nstr2\nstr3', flags = regex.M) # <regex.Match object; span=(5, 9), match='str2'>

#T# use the inline multiline modifier (?m) with the -z flag, turn it off with (?-m)
search1 = regex.search(r'(?m)^str2$', 'str1\nstr2\nstr3') # <regex.Match object; span=(5, 9), match='str2'>

#T# use the regular dotall modifier with the regex.S constant as value for the flags kwarg, this makes the dot . also match a newline
search1 = regex.search(r'in.*en', 'begin\nend', flags = regex.S) # <regex.Match object; span=(3, 8), match='in\nen'>

#T# use the inline dotall modifier (?s), turn it off with (?-s)
search1 = regex.search(r'(?s)in.*en', 'begin\nend') # <regex.Match object; span=(3, 8), match='in\nen'>

#T# there is no support for the ungreedy modifier

#T# use the regular extended modifier with the regex.X constant as value for the flags kwarg, this ignores whitespace that is not escaped or outside a character class
search1 = regex.search(r'st    r1\ st r2', 'str1 str2', flags = regex.X) # <regex.Match object; span=(0, 9), match='str1 str2'>

#T# use the inline extended modifier (?x), turn it off with (?-x)
search1 = regex.search(r'(?x)st    r1\ st r2', 'str1 str2') # <regex.Match object; span=(0, 9), match='str1 str2'>

#T# there is no support for the extra modifier that throws an error when escaping a character that has no special meaning

#T# use the regular ascii modifier with the regex.A constant as value for the flags kwarg, this makes characters like \w, \s, \d, and similar, to match only ascii chars
list1 = regex.findall(r'\w', 'áüo', flags = regex.A) # ['o']

#T# use the inline ascii modifier (?a), it can't be turned off and must be placed at the start of the pattern
list1 = regex.findall(r'(?a)\w', 'áüo') # ['o']

#T# use the regular unicode modifier with the regex.U constant as value for the flags kwarg, this makes characters like \w, \s, \d, and similar, to match unicode chars, this is the default behavior
list1 = regex.findall(r'\w', 'áüo', flags = regex.U) # ['á', 'ü', 'o']

#T# use the inline unicode modifier (?u), it can't be turned off and must be placed at the start of the pattern
list1 = regex.findall(r'(?u)\w', 'áüo') # ['á', 'ü', 'o']

#T# turn on or off several inline modifiers together, e.g. (?ix-m)
search1 = regex.search(r'(?ix-m)S  T  R1', 'str1', flags = regex.V1) # <regex.Match object; span=(0, 4), match='str1'>

#T# all former inline modifiers shown can be introduced exclusively for the pattern inside the same parentheses of the inline modifier, i.e. (?s:pattern1), (?-s:pattern1) only affects pattern1
search1 = regex.search(r'(?i:STR)1 (?-i:STR)2', 'str1 STR2') # <regex.Match object; span=(0, 9), match='str1 STR2'>
# |-----

# |-------------------------------------------------------------