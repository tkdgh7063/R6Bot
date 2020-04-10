import asyncio
import operator
import r6sapi as api

FOR_COPY = {
    "SLEDGE": "",
    "THATCHER": "",
    "ASH": "",
    "THERMITE": "",
    "TWITCH": "",
    "MONTAGNE": "",
    "GLAZ": "",
    "FUZE": "",
    "BLITZ": "",
    "IQ": "",
    "BUCK": "",
    "BLACKBEARD": "",
    "CAPITAO": "",
    "HIBANA": "",
    "JACKAL": "",
    "YING": "",
    "ZOFIA": "",
    "DOKKAEBI": "",
    "LION": "",
    "FINKA": "",
    "MAVERICK": "",
    "NOMAD": "",
    "GRIDLOCK": "",
    "NOKK": "",
    "AMARU": "",
    "KALI": "",
    "IANA": "",
    "SMOKE": "",
    "MUTE": "",
    "CASTLE": "",
    "PULSE": "",
    "ROOK": "",
    "DOC": "",
    "KAPKAN": "",
    "TACHANKA": "",
    "JAGER": "",
    "BANDIT": "",
    "FROST": "",
    "VALKYRIE": "",
    "CAVEIRA": "",
    "ECHO": "",
    "MIRA": "",
    "LESION": "",
    "ELA": "",
    "VIGIL": "",
    "MAESTRO": "",
    "ALIBI": "",
    "CLASH": "",
    "KAID": "",
    "MOZZIE": "",
    "WARDEN": "",
    "GOYO": "",
    "WAMAI": "",
    "ORYX": ""
}

KR_NAME = {
    "SLEDGE": "슬레지",
    "THATCHER": "대처",
    "ASH": "애쉬",
    "THERMITE": "써마이트",
    "TWITCH": "트위치",
    "MONTAGNE": "몽타뉴",
    "GLAZ": "글라즈",
    "FUZE": "퓨즈",
    "BLITZ": "블리츠",
    "IQ": "아이큐",
    "BUCK": "벅",
    "BLACKBEARD": "블랙비어드",
    "CAPITAO": "카피탕",
    "HIBANA": "히바나",
    "JACKAL": "자칼",
    "YING": "잉",
    "ZOFIA": "조피아",
    "DOKKAEBI": "도깨비",
    "LION": "라이온",
    "FINKA": "핀카",
    "MAVERICK": "매버릭",
    "NOMAD": "노매드",
    "GRIDLOCK": "그리드락",
    "NOKK": "뇌크",
    "AMARU": "아마루",
    "KALI": "칼리",
    "IANA": "야나",
    "SMOKE": "스모크",
    "MUTE": "뮤트",
    "CASTLE": "캐슬",
    "PULSE": "펄스",
    "ROOK": "룩",
    "DOC": "닥",
    "KAPKAN": "캅칸",
    "TACHANKA": "타찬카",
    "JAGER": "예거",
    "BANDIT": "밴딧",
    "FROST": "프로스트",
    "VALKYRIE": "발키리",
    "CAVEIRA": "카베이라",
    "ECHO": "에코",
    "MIRA": "미라",
    "LESION": "리전",
    "ELA": "엘라",
    "VIGIL": "비질",
    "MAESTRO": "마에스트로",
    "ALIBI": "알리바이",
    "CLASH": "클래쉬",
    "KAID": "카이드",
    "MOZZIE": "모지",
    "WARDEN": "워든",
    "GOYO": "고요",
    "WAMAI": "와마이",
    "ORYX": "오릭스"
}

UNIT = {
    "SLEDGE": "SAS",
    "THATCHER": "SAS",
    "ASH": "FBI SWAT",
    "THERMITE": "FBI SWAT",
    "TWITCH": "GIGN",
    "MONTAGNE": "GIGN",
    "GLAZ": "Spetsnaz",
    "FUZE": "Spetsnaz",
    "BLITZ": "GSG-9",
    "IQ": "GSG-9",
    "BUCK": "JTF-2",
    "BLACKBEARD": "Navy SEAL",
    "CAPITAO": "BOPE",
    "HIBANA": "SAT",
    "JACKAL": "GEO",
    "YING": "SDU",
    "ZOFIA": "GROM",
    "DOKKAEBI": "707th SMB",
    "LION": "CBRN",
    "FINKA": "CBRN",
    "MAVERICK": "GSUTR",
    "NOMAD": "GIGR",
    "GRIDLOCK": "SASR",
    "NOKK": "Jaeger Corps,\nSecret Service",
    "AMARU": "APCA,\nFuerzas Especiales",
    "KALI": "NIGHTHAVEN",
    "IANA": "REU",
    "SMOKE": "SAS",
    "MUTE": "SAS",
    "CASTLE": "FBI SWAT",
    "PULSE": "FBI SWAT",
    "ROOK": "GIGN",
    "DOC": "GIGN",
    "KAPKAN": "Spatsnaz",
    "TACHANKA": "Spatsnaz",
    "JAGER": "GSG-9",
    "BANDIT": "GSG-9",
    "FROST": "JTF-2",
    "VALKYRIE": "Navy SEAL",
    "CAVEIRA": "BOPE",
    "ECHO": "SAT",
    "MIRA": "GEO",
    "LESION": "SDU",
    "ELA": "GROM",
    "VIGIL": "707th SMB",
    "MAESTRO": "GIS",
    "ALIBI": "GIS",
    "CLASH": "GSUTR",
    "KAID": "GIGR",
    "MOZZIE": "SASR",
    "WARDEN": "Jaeger Corps,\nSecret Service",
    "GOYO": "APCA,\nFuerzas Especiales",
    "WAMAI": "NIGHTHAVEN",
    "ORYX": "무소속"
}

NAME = {
    "SLEDGE": "Seamus Cowden",
    "THATCHER": "Mike Baker",
    "ASH": "Eliza Cohen",
    "THERMITE": "Jordan Trace",
    "TWITCH": "Emmanuelle Pichon",
    "MONTAGNE": "Gilles Touré",
    "GLAZ": "Timur Glazkov",
    "FUZE": "Shuhrat Kessikbayev",
    "BLITZ": "Elias Kötz",
    "IQ": "Monika Weiss",
    "BUCK": "Sébastien Côté",
    "BLACKBEARD": "Craig Jenson",
    "CAPITAO": "Vicente Souza",
    "HIBANA": "Yumiko Imagawa",
    "JACKAL": "Ryad Ramirez Al-Hassar",
    "YING": "Siu Mei Lin",
    "ZOFIA": "Zofia Bosak",
    "DOKKAEBI": "남은혜",
    "LION": "Olivier Flament",
    "FINKA": "Lera Melnikova",
    "MAVERICK": "Erik Thom",
    "NOMAD": "Sanaa El Maktoub",
    "GRIDLOCK": "Tori Tallyo Fairous",
    "NOKK": "[편집됨]",
    "AMARU": "Azucena Rocio Quispe",
    "KALI": "Jaimini Kalimohan Shah",
    "IANA": "Nienke Meijer",
    "SMOKE": "James Porter",
    "MUTE": "Mark R. Chandar",
    "CASTLE": "Miles Campbell",
    "PULSE": "Jack Estrada",
    "ROOK": "Julien Nizan",
    "DOC": "Gustave Kateb",
    "KAPKAN": "Maxim Basuda",
    "TACHANKA": "Alexsandr Senaviev",
    "JAGER": "Marius Streicher",
    "BANDIT": "Dominic Brunsmeier",
    "FROST": "Tina Lin Tsang",
    "VALKYRIE": "Meghan J. Castellano",
    "CAVEIRA": "Taina Pereira",
    "ECHO": "Masaru Enatsu",
    "MIRA": "Elena María Álvarez",
    "LESION": "Liu Tze Long",
    "ELA": "Elżbieta Bosak",
    "VIGIL": "화철경",
    "MAESTRO": "Adriano Martello",
    "ALIBI": "Aria de Luca",
    "CLASH": "Morowa Evans",
    "KAID": "Jalal El Fassi",
    "MOZZIE": "Max Goose",
    "WARDEN": "Collinn McKinley",
    "GOYO": "César Ruiz Hernández",
    "WAMAI": "Ngũgĩ Muchoki Furaha",
    "ORYX": "Saif Al Hadid"
}

BIRTH = {
    "SLEDGE": "4월 2일",
    "THATCHER": "6월 22일",
    "ASH": "12월 24일",
    "THERMITE": "3월 14일",
    "TWITCH": "10월 12일",
    "MONTAGNE": "10월 11일",
    "GLAZ": "7월 2일",
    "FUZE": "10월 12일",
    "BLITZ": "4월 2일",
    "IQ": "8월 1일",
    "BUCK": "8월 20일",
    "BLACKBEARD": "3월 12일",
    "CAPITAO": "11월 17일",
    "HIBANA": "7월 12일",
    "JACKAL": "2월 29일",
    "YING": "5월 12일",
    "ZOFIA": "1월 28일",
    "DOKKAEBI": "2월 2일",
    "LION": "8월 29일",
    "FINKA": "6월 7일",
    "MAVERICK": "4월 20일",
    "NOMAD": "7월 27일",
    "GRIDLOCK": "8월 5일",
    "NOKK": "[편집됨]",
    "AMARU": "5월 6일",
    "KALI": "8월 21일",
    "IANA": "8월 27일",
    "SMOKE": "5월 14일",
    "MUTE": "10월 11일",
    "CASTLE": "9월 20일",
    "PULSE": "10월 11일",
    "ROOK": "1월 6일",
    "DOC": "9월 16일",
    "KAPKAN": "5월 14일",
    "TACHANKA": "11월 3일",
    "JAGER": "3월 9일",
    "BANDIT": "8월 13일",
    "FROST": "5월 4일",
    "VALKYRIE": "7월 21일",
    "CAVEIRA": "10월 15일",
    "ECHO": "10월 31일",
    "MIRA": "11월 18일",
    "LESION": "7월 2일",
    "ELA": "11월 8일",
    "VIGIL": "1월 17일",
    "MAESTRO": "4월 13일",
    "ALIBI": "12월 15일",
    "CLASH": "6월 7일",
    "KAID": "6월 26일",
    "MOZZIE": "2월 15일",
    "WARDEN": "3월 18일",
    "GOYO": "6월 10일",
    "WAMAI": "6월 1일",
    "ORYX": "7월 3일"
}

HOME = {
    "SLEDGE": "영국 스코틀랜드 존 오 그로츠",
    "THATCHER": "영국 비드포드",
    "ASH": "이스라엘 예루살렘",
    "THERMITE": "미국 텍사스 플라노",
    "TWITCH": "프랑스 낭시",
    "MONTAGNE": "프랑스 보르도",
    "GLAZ": "러시아 블라디보스토크",
    "FUZE": "우즈베키스탄 사마르칸트",
    "BLITZ": "독일 브레멘",
    "IQ": "독일 라이프치히",
    "BUCK": "캐나다 몬트리올",
    "BLACKBEARD": "미국 워싱턴 벨뷰",
    "CAPITAO": "브라질 노바 이구아수",
    "HIBANA": "일본 나고야",
    "JACKAL": "스페인 세우타",
    "YING": "홍콩 센트럴",
    "ZOFIA": "폴란드 브로츠와프",
    "DOKKAEBI": "대한민국 서울",
    "LION": "프랑스 툴루즈",
    "FINKA": "벨라루스 호멜",
    "MAVERICK": "미국 매사추세츠 보스턴",
    "NOMAD": "모로코 마라케시",
    "GRIDLOCK": "호주 센트럴\n퀸즐랜드 롱리치",
    "NOKK": "[편집됨]",
    "AMARU": "페루 푸노주 코하타",
    "KALI": "인도 암렐리",
    "IANA": "네덜란드 캇베이크",
    "SMOKE": "영국 런던",
    "MUTE": "영국 요크",
    "CASTLE": "미국 캘리포니아 셔먼 오크스",
    "PULSE": "미국 노스 캐롤라이나 골즈버로",
    "ROOK": "프랑스 투르",
    "DOC": "프랑스 파리",
    "KAPKAN": "러시아 카브로프",
    "TACHANKA": "러시아 상트페테르부르크",
    "JAGER": "독일 뒤셀도르프",
    "BANDIT": "독일 베를린",
    "FROST": "캐나다 밴쿠버",
    "VALKYRIE": "미국 캘리포니아\n오션사이드",
    "CAVEIRA": "브라질 상파울루",
    "ECHO": "도쿄 스기나미구",
    "MIRA": "스페인 마드리드",
    "LESION": "홍콩 정크 베이\n(청콴우)",
    "ELA": "폴란드 브로츠와프",
    "VIGIL": "[편집됨]",
    "MAESTRO": "이탈리아 로마",
    "ALIBI": "리비아 트리폴리",
    "CLASH": "영국 런던",
    "KAID": "모로코 아룸드",
    "MOZZIE": "호주 포틀랜드",
    "WARDEN": "미국 켄터키 루이빌",
    "GOYO": "멕시코 시날로아 쿨리아칸 로살레스",
    "WAMAI": "케냐 라무",
    "ORYX": "요르단 아즈라크"
}

AGE = {
    "SLEDGE": "35세",
    "THATCHER": "60세",
    "ASH": "33세",
    "THERMITE": "35세",
    "TWITCH": "28세",
    "MONTAGNE": "48세",
    "GLAZ": "30세",
    "FUZE": "34세",
    "BLITZ": "37세",
    "IQ": "38세",
    "BUCK": "36세",
    "BLACKBEARD": "32세",
    "CAPITAO": "49세",
    "HIBANA": "34세",
    "JACKAL": "49세",
    "YING": "33세",
    "ZOFIA": "36세",
    "DOKKAEBI": "29세",
    "LION": "31세",
    "FINKA": "27세",
    "MAVERICK": "36세",
    "NOMAD": "39세",
    "GRIDLOCK": "36세",
    "NOKK": "[편집됨]",
    "AMARU": "48세",
    "KALI": "34세",
    "IANA": "35세",
    "SMOKE": "36세",
    "MUTE": "25세(현재 28세)",
    "CASTLE": "36세",
    "PULSE": "32세",
    "ROOK": "27세",
    "DOC": "39세",
    "KAPKAN": "38세",
    "TACHANKA": "48세",
    "JAGER": "39세",
    "BANDIT": "42세(현재 45세)",
    "FROST": "32세",
    "VALKYRIE": "31세",
    "CAVEIRA": "27세",
    "ECHO": "36세",
    "MIRA": "39세",
    "LESION": "44세",
    "ELA": "31세",
    "VIGIL": "34세",
    "MAESTRO": "45세",
    "ALIBI": "37세",
    "CLASH": "35세",
    "KAID": "58세",
    "MOZZIE": "35세",
    "WARDEN": "48세",
    "GOYO": "31세",
    "WAMAI": "28세",
    "ORYX": "45세"
}

HEIGHT = {
    "SLEDGE": "192cm",
    "THATCHER": "180cm",
    "ASH": "170cm",
    "THERMITE": "178cm",
    "TWITCH": "168cm",
    "MONTAGNE": "190cm",
    "GLAZ": "178cm",
    "FUZE": "180cm",
    "BLITZ": "175 cm",
    "IQ": "175 cm",
    "BUCK": "178cm",
    "BLACKBEARD": "180cm",
    "CAPITAO": "183cm",
    "HIBANA": "173cm",
    "JACKAL": "190cm",
    "YING": "160cm",
    "ZOFIA": "179cm",
    "DOKKAEBI": "169cm",
    "LION": "185cm",
    "FINKA": "171cm",
    "MAVERICK": "180cm",
    "NOMAD": "171cm",
    "GRIDLOCK": "177cm",
    "NOKK": "[편집됨]",
    "AMARU": "189cm",
    "KALI": "170cm",
    "IANA": "157cm",
    "SMOKE": "173cm",
    "MUTE": "185cm",
    "CASTLE": "185cm",
    "PULSE": "188cm",
    "ROOK": "175cm",
    "DOC": "177cm",
    "KAPKAN": "180cm",
    "TACHANKA": "183cm",
    "JAGER": "180cm",
    "BANDIT": "180cm",
    "FROST": "172cm",
    "VALKYRIE": "170cm",
    "CAVEIRA": "177cm",
    "ECHO": "180cm",
    "MIRA": "165cm",
    "LESION": "174cm",
    "ELA": "173cm",
    "VIGIL": "173cm",
    "MAESTRO": "185cm",
    "ALIBI": "171cm",
    "CLASH": "179cm",
    "KAID": "195cm",
    "MOZZIE": "162cm",
    "WARDEN": "183cm",
    "GOYO": "171cm",
    "WAMAI": "187cm",
    "ORYX": "195cm"
}

WEIGHT = {
    "SLEDGE": "95kg",
    "THATCHER": "72kg",
    "ASH": "63kg",
    "THERMITE": "80kg",
    "TWITCH": "58kg",
    "MONTAGNE": "90kg",
    "GLAZ": "79kg",
    "FUZE": "80kg",
    "BLITZ": "75kg",
    "IQ": "70kg",
    "BUCK": "78kg",
    "BLACKBEARD": "84kg",
    "CAPITAO": "86kg",
    "HIBANA": "57kg",
    "JACKAL": "78kg",
    "YING": "52kg",
    "ZOFIA": "72kg",
    "DOKKAEBI": "62kg",
    "LION": "87kg",
    "FINKA": "68kg",
    "MAVERICK": "82kg",
    "NOMAD": "63kg",
    "GRIDLOCK": "102kg",
    "NOKK": "[편집됨]",
    "AMARU": "84kg",
    "KALI": "67kg",
    "IANA": "56kg",
    "SMOKE": "70kg",
    "MUTE": "80kg",
    "CASTLE": "86kg",
    "PULSE": "85kg",
    "ROOK": "72kg",
    "DOC": "74kg",
    "KAPKAN": "80kg",
    "TACHANKA": "86kg",
    "JAGER": "64kg",
    "BANDIT": "68kg",
    "FROST": "63kg",
    "VALKYRIE": "61kg",
    "CAVEIRA": "72kg",
    "ECHO": "72kg",
    "MIRA": "60kg",
    "LESION": "82kg",
    "ELA": "68kg",
    "VIGIL": "73kg",
    "MAESTRO": "87kg",
    "ALIBI": "63kg",
    "CLASH": "73kg",
    "KAID": "98kg",
    "MOZZIE": "57kg",
    "WARDEN": "80kg",
    "GOYO": "83kg",
    "WAMAI": "83kg",
    "ORYX": "130kg"
}

SP = {
    "SLEDGE": 2,
    "THATCHER": 2,
    "ASH": 3,
    "THERMITE": 2,
    "TWITCH": 2,
    "MONTAGNE": 1,
    "GLAZ": 2,
    "FUZE": 1,
    "BLITZ": 2,
    "IQ": 3,
    "BUCK": 2,
    "BLACKBEARD": 2,
    "CAPITAO": 3,
    "HIBANA": 3,
    "JACKAL": 2,
    "YING": 2,
    "ZOFIA": 2,
    "DOKKAEBI": 2,
    "LION": 2,
    "FINKA": 2,
    "MAVERICK": 3,
    "NOMAD": 2,
    "GRIDLOCK": 1,
    "NOKK": 2,
    "AMARU": 2,
    "KALI": 2,
    "IANA": 2,
    "SMOKE": 2,
    "MUTE": 2,
    "CASTLE": 2,
    "PULSE": 3,
    "ROOK": 1,
    "DOC": 1,
    "KAPKAN": 2,
    "TACHANKA": 1,
    "JAGER": 3,
    "BANDIT": 3,
    "FROST": 2,
    "VALKYRIE": 2,
    "CAVEIRA": 3,
    "ECHO": 1,
    "MIRA": 1,
    "LESION": 2,
    "ELA": 3,
    "VIGIL": 3,
    "MAESTRO": 1,
    "ALIBI": 3,
    "CLASH": 1,
    "KAID": 1,
    "MOZZIE": 2,
    "WARDEN": 2,
    "GOYO": 2,
    "WAMAI": 2,
    "ORYX": 2
}

BADGE = {
    "SLEDGE": "https://game-rainbow6.ubi.com/assets/images/badge-sledge.00141f92.png",
    "THATCHER": "https://game-rainbow6.ubi.com/assets/images/badge-thatcher.b1cac8e7.png",
    "ASH": "https://game-rainbow6.ubi.com/assets/images/badge-ash.16913d82.png",
    "THERMITE": "https://game-rainbow6.ubi.com/assets/images/badge-thermite.9010fa33.png",
    "TWITCH": "https://game-rainbow6.ubi.com/assets/images/badge-twitch.83cbfa97.png",
    "MONTAGNE": "https://game-rainbow6.ubi.com/assets/images/badge-montagne.2078ee84.png",
    "GLAZ": "https://game-rainbow6.ubi.com/assets/images/badge-glaz.43dd3bdf.png",
    "FUZE": "https://game-rainbow6.ubi.com/assets/images/badge-fuze.9e7e9222.png",
    "BLITZ": "https://game-rainbow6.ubi.com/assets/images/badge-blitz.cd45df08.png",
    "IQ": "https://game-rainbow6.ubi.com/assets/images/badge-iq.b1acee1a.png",
    "BUCK": "https://game-rainbow6.ubi.com/assets/images/badge-buck.2fc3e097.png",
    "BLACKBEARD": "https://game-rainbow6.ubi.com/assets/images/badge-blackbeard.fccd7e2c.png",
    "CAPITAO": "https://game-rainbow6.ubi.com/assets/images/badge-capitao.6603e417.png",
    "HIBANA": "https://game-rainbow6.ubi.com/assets/images/badge-hibana.c2a8477d.png",
    "JACKAL": "https://game-rainbow6.ubi.com/assets/images/badge-jackal.0326ca29.png",
    "YING": "https://game-rainbow6.ubi.com/assets/images/badge-ying.b88be612.png",
    "ZOFIA": "https://game-rainbow6.ubi.com/assets/images/badge-zofia.2a892bf5.png",
    "DOKKAEBI": "https://game-rainbow6.ubi.com/assets/images/badge-dokkaebi.2f83a34f.png",
    "LION": "https://game-rainbow6.ubi.com/assets/images/badge-lion.69637075.png",
    "FINKA": "https://game-rainbow6.ubi.com/assets/images/badge-finka.71d3a243.png",
    "MAVERICK": "https://game-rainbow6.ubi.com/assets/images/badge-maverick.7eab7c75.png",
    "NOMAD": "https://game-rainbow6.ubi.com/assets/images/badge-nomad.dbd9a315.png",
    "GRIDLOCK": "https://game-rainbow6.ubi.com/assets/images/badge-gridlock.6b572bdc.png",
    "NOKK": "https://game-rainbow6.ubi.com/assets/images/badge-nakk.d3b4f1af.png",
    "AMARU": "https://game-rainbow6.ubi.com/assets/images/badge-amaru.24a70133.png",
    "KALI": "https://game-rainbow6.ubi.com/assets/images/badge-kali.ff0fee46.png",
    "IANA": "https://game-rainbow6.ubi.com/assets/images/badge-iana.6fa68bc8.png",
    "SMOKE": "https://game-rainbow6.ubi.com/assets/images/badge-smoke.874e9888.png",
    "MUTE": "https://game-rainbow6.ubi.com/assets/images/badge-mute.3e4f2b01.png",
    "CASTLE": "https://game-rainbow6.ubi.com/assets/images/badge-castle.378f8f4e.png",
    "PULSE": "https://game-rainbow6.ubi.com/assets/images/badge-pulse.9de627c5.png",
    "ROOK": "https://game-rainbow6.ubi.com/assets/images/badge-rook.eb954a4e.png",
    "DOC": "https://game-rainbow6.ubi.com/assets/images/badge-doc.29fe751b.png",
    "KAPKAN": "https://game-rainbow6.ubi.com/assets/images/badge-kapkan.562d0701.png",
    "TACHANKA": "https://game-rainbow6.ubi.com/assets/images/badge-tachanka.ae7943f0.png",
    "JAGER": "https://game-rainbow6.ubi.com/assets/images/badge-jager.600b2773.png",
    "BANDIT": "https://game-rainbow6.ubi.com/assets/images/badge-bandit.385144d9.png",
    "FROST": "https://game-rainbow6.ubi.com/assets/images/badge-frost.e5362220.png",
    "VALKYRIE": "https://game-rainbow6.ubi.com/assets/images/badge-valkyrie.f87cb6bd.png",
    "CAVEIRA": "https://game-rainbow6.ubi.com/assets/images/badge-caveira.757e9259.png",
    "ECHO": "https://game-rainbow6.ubi.com/assets/images/badge-echo.a77c7d7e.png",
    "MIRA": "https://game-rainbow6.ubi.com/assets/images/badge-mira.22fb72a5.png",
    "LESION": "https://game-rainbow6.ubi.com/assets/images/badge-lesion.07c3d352.png",
    "ELA": "https://game-rainbow6.ubi.com/assets/images/badge-ela.63ec2d26.png",
    "VIGIL": "https://game-rainbow6.ubi.com/assets/images/badge-vigil.4db5385b.png",
    "MAESTRO": "https://game-rainbow6.ubi.com/assets/images/badge-maestro.b6cf7905.png",
    "ALIBI": "https://game-rainbow6.ubi.com/assets/images/badge-alibi.7fba8d33.png",
    "CLASH": "https://game-rainbow6.ubi.com/assets/images/badge-clash.133f243d.png",
    "KAID": "https://game-rainbow6.ubi.com/assets/images/badge-kaid.ae2bfa7a.png",
    "MOZZIE": "https://game-rainbow6.ubi.com/assets/images/badge-mozzie.adeac188.png",
    "WARDEN": "https://game-rainbow6.ubi.com/assets/images/badge-warden.fd12fbd9.png",
    "GOYO": "https://game-rainbow6.ubi.com/assets/images/badge-goyo.3e765688.png",
    "WAMAI": "https://game-rainbow6.ubi.com/assets/images/badge-wamai.4e4bf506.png",
    "ORYX": "https://game-rainbow6.ubi.com/assets/images/badge-oryx.6472c8ee.png"
}

STAT_NAME = {
    "SLEDGE": "파쇄 망치(Breaching Hammer)",
    "THATCHER": "EMP 수류탄(EMP Grenade)",
    "ASH": "파괴탄(Breaching Round)",
    "THERMITE": "발열성 폭약(Exothermic Charge)",
    "TWITCH": "감전 드론(Shock Drone)",
    "MONTAGNE": "확장형 방패(Extendable Shield)",
    "GLAZ": "접이식 조준기(Flip Sight)",
    "FUZE": "접착식 집속탄(Cluster Charge)",
    "BLITZ": "섬광 방패(Flash Shield)",
    "IQ": "전자기기 탐지기(Electronics Detector)",
    "BUCK": "부착식 산탄총(Skeleton Key)",
    "BLACKBEARD": "소총 방패(Rifle-Shield)",
    "CAPITAO": "전술 크로스보우(Tactical Crossbow)",
    "HIBANA": "X-KAIROS",
    "JACKAL": "아이녹스 모델 III(Eyenox Model III)",
    "YING": "칸델라(Candela)",
    "ZOFIA": "KS79 생명선(KS79 Lifeline)",
    "DOKKAEBI": "논리 폭탄(Logic Bomb)",
    "LION": "움직임 감지 드론(EE-ONE-D)",
    "FINKA": "아드레날린 분출(Adrenal Surge)",
    "MAVERICK": "돌파용 토치(Breaching Torch)",
    "NOMAD": "기압탄 발사기(Airjab Launcher)",
    "GRIDLOCK": "트랙스 독침(Trax Stingers)",
    "NOKK": "HEL 존재감 감소기(HEL Presence Reduction)",
    "AMARU": "가라 훅(Garra Hook)",
    "KALI": "LV 폭발형 창(LV Explosive Lance)",
    "IANA": "제미니 복제기(Gemini Replicator)",
    "SMOKE": "원격 가스탄(Remote Gas Grenade)",
    "MUTE": "신호 방해기(Signal Disruptor)",
    "CASTLE": "방탄 패널(Armor Panel)",
    "PULSE": "심장 박동 감지기(Cardiac Sensor)",
    "ROOK": "자극제 권총(Armor Pack)",
    "DOC": "방탄판 팩(Stim Pistol)",
    "KAPKAN": "진입 방지 폭약(Entry Denial Device)",
    "TACHANKA": "탑승형 LMG(Mounted LMG)",
    "JAGER": "선제 방어(Active Defense System)",
    "BANDIT": "고압선(Shock Wire)",
    "FROST": "전술 함정(Welcome Mat)",
    "VALKYRIE": "칠흑의 주시자(Black Eye)",
    "CAVEIRA": "고요한 발걸음(Silent Step)",
    "ECHO": "요괴(Yokai)",
    "MIRA": "검은 거울(Black Mirror)",
    "LESION": "고독(GU)",
    "ELA": "GRZMOT 지뢰(GRZMOT Mine)",
    "VIGIL": "ERC-7",
    "MAESTRO": "악의 눈(Evil Eye)",
    "ALIBI": "프리즈마(Prisma)",
    "CLASH": "CCE 방패(CCE Shield)",
    "KAID": "전기집게발(Rtila Electroclaw)",
    "MOZZIE": "해충 발사기(Pest Launcher)",
    "WARDEN": "응시 스마트 안경(Glance Smart Glasses)",
    "GOYO": "VOLCÁN 방패(VOLCÁN Shield)",
    "WAMAI": "MAG-NET 시스템(Mag-NET System)",
    "ORYX": "라마 질주(Remah Dash)"
}

STAT_INST = {
    "SLEDGE": "파괴할 수 있는 면을 돌파하는데 사용하는 파쇄용 망치입니다.",
    "THATCHER": "범위 내의 모든 전자 기기를 무력화시키는 EMP 수류탄을\n사용합니다.",
    "ASH": "표면에 박혀 자동으로 폭발하는 파괴탄을 발사합니다.",
    "THERMITE": "강화된 벽을 파괴할 수 있는 발열성 폭약을 설치합니다.",
    "TWITCH": "함정을 무력화하거나 적에게 부상을 입히는 감전 드론 두 대를\n사용합니다. 첫 감전 드론은 준비 단계에 전개합니다.",
    "MONTAGNE": "서 있는 상태에서도 온몸이 보호되도록 방패를 확장할 수\n있습니다.",
    "GLAZ": "연기 속에서도 장거리 표적의 윤곽을 표시하는 정교한 이미지\n센서가 탑재된 확대경을 조절하는 장치입니다.",
    "FUZE": "부착 시 벽을 관통하여 반대편에 소형 수류탄들을 방출하는\n집속탄을 사용합니다.",
    "BLITZ": "방탄 방패에 부착된 섬광 장치를 격발하여 일시적으로 적의\n시야를 빼앗을 수 있습니다.",
    "IQ": "벽 등의 장애물을 투과하여 범위 내 모든 전자기기를 감지할 수\n있는 전자기기 탐지기를 사용합니다.",
    "BUCK": "주 무기의 총열 하부에 부착된 산탄총을 사용합니다.",
    "BLACKBEARD": "방패가 손상될 경우 다른 방패로 교체 가능한 방탄 방패를\n소총에 설치합니다.",
    "CAPITAO": "폭발 화살과 초소형 연막탄을 발사하는 전술 크로스보우입니다.",
    "HIBANA": "40mm 구경의 유탄 발사기로, 원거리에서 격발할 수 있는 폭발성\n파편을 발사합니다.",
    "JACKAL": "최근에 남겨진 발자국을 밝히고 감별하여 표적의 위치를\n파악하는 추적용 광학 장치입니다.",
    "YING": "표면에 고정하거나 수류탄처럼 굴릴 수 있는 섬광 집속탄입니다.",
    "ZOFIA": "진탕탄과 충격탄을 발사할 수 있는 쌍열 유탄발사기입니다.",
    "DOKKAEBI": "적의 전화기에 낮은 진동을 일으키는 바이러스를 업로드하여\n잠재적으로 적의 위치가 드러나게 합니다.",
    "LION": "EE-ONE-D 드론은 스캔하는 동안 적의 움직임을 감지하고 적의\n위치에 태그를 지정합니다.",
    "FINKA": "나노봇은 팀원의 HP를 소폭 증가시키고 쓰러진 동료를\n소생시킵니다.",
    "MAVERICK": "매우 조용히 강화된 벽에 구멍을 낼 수 있는 소형 발염\n장치입니다.",
    "NOMAD": "근접 시 폭발하는 부착식 반발형 유탄을 발사하는 소총\n부속품입니다.",
    "GRIDLOCK": "철사 매트를 설치하여 건너가는 적에게 부상을 입히며 이동\n속도를 늦추는 투척용 도구입니다.",
    "NOKK": "주변 카메라와 드론에서 Nøkk의 이미지를 지우며 몇 가지를\n제외한 사용자의 소음을 줄이는 방첩 도구입니다.",
    "AMARU": "라펠 포인트나 열린 해치에 빠르게 접근하거나, 외부 창문을\n통해 진입하기 위해 쓰는 거리 한계가 있는 고장력 그래플링\n건입니다.",
    "KALI": "설정된 반경 안에서 폭발하여 파괴 가능하거나 강화된 표면의\n양쪽에 있는 모든 도구를 파괴하는 총열 하부 기계 투사체입니다.",
    "IANA": "원격으로 조종되는 Iana의 홀로그램 형상을 설치하여 적을\n속이고 정보를 수집한다.",
    "SMOKE": "원격으로 폭발시킬 수 있는 독가스 폭탄을 설치합니다.",
    "MUTE": "일정 범위 내의 원격 폭발형 도구 또는 드론의 신호를\n방해합니다.",
    "CASTLE": "일반 바리케이드보다 단단한 방탄 바리케이드를 설치합니다.",
    "PULSE": "장애물에 관계없이 근거리 내의 심장 박동을 감지합니다.",
    "ROOK": "아군이 무장할 수 있는 방탄판으로 가득 찬 보급 가방을 바닥에 내려놓습니다.",
    "DOC": "원거리에서 자신이나 팀원을 소생시킬 수 있는 피하 주사기를\n발사합니다. 일시적으로 보너스를 부여할 수 있습니다.",
    "KAPKAN": "창문틀과 문틀에 부비트랩을 설치합니다.",
    "TACHANKA": "전방으로부터 머리를 방어하는 방탄 방패가 장착된 탑승형\nLMG를 설치합니다.",
    "JAGER": "선제 방어 시스템를 사용하여 폭발하기 전에 수류탄을\n요격합니다.",
    "BANDIT": "다른 도구에 전기를 통하게 하고 접촉한 모든 대상에 피해를\n주는 전압 증폭기를 설치합니다.",
    "FROST": "격발 시 적을 무력화시키는 기계 함정을 설치합니다.",
    "VALKYRIE": "팀원 모두가 관측 도구를 통해 사용할 수 있는 '칠흑의 주시자'를\n설치합니다.",
    "CAVEIRA": 'Caveira의 맹수와 같은 스텔스 능력, "고요한 발걸음"을 사용하면 적에게 소리없이 접근해 순식간에 해치울 수 있습니다.',
    "ECHO": "음파를 발산하여 방향 감각에 혼란을 주는 제자리비행형\n드론입니다. 요괴는 대원에게 영상을 전송할 수도 있습니다.",
    "MIRA": "파괴 가능한 벽과 강화된 벽에 방탄 평면거울을 설치합니다.\n거울을 사출하여 급작스러운 공격 기회를 노릴 수도 있습니다.",
    "LESION": "혼합물을 주입하여 상대에게 피해를 주고 속도를 제한하는\n은폐형 독지뢰입니다.",
    "ELA": "표면에 고정시킬 수 있는 진탕 접근신관 지뢰로, 청각을\n손상시키고 현기증 효과를 줍니다.",
    "VIGIL": "Vigil은 주변의 장치를 탐지하여 카메라와 드론의 영상에서\n자신의 모습을 제거합니다.",
    "MAESTRO": "고에너지 레이저로 무장한 원격 조종 방탄 카메라입니다.",
    "ALIBI": "포격을 입은 경우 Alibi의 홀로그램을 배치하고 적을 태그합니다.",
    "CLASH": "적을 느리게 만들고 지속 피해를 줄 수 있는 확장형 전기\n방패입니다.",
    "KAID": "작용 반경 내 강화된 벽과 출입문, 철조망, 이동식 엄폐물을\n전화합니다.",
    "MOZZIE": "근처에 있는 적 드론에 달라 붙어 조종 능력을 장악하는 자동\n로봇을 발사합니다.",
    "WARDEN": "가만히 서 있을 때 연막 속 시야 거리가 증가하는 안경입니다.\n활성화하여 섬광탄 눈부심 효과를 줄이거나 섬광탄 효과로부터\n보호받을 수 있습니다.",
    "GOYO": "파괴되면 폭발하여 이동식 엄폐물에 부착되는 소이탄입니다.",
    "WAMAI": "상대의 투사체를 끌어당기고 붙잡아 자폭하여 해당 투사체를 터뜨리는 투척용 접착 도구입니다.",
    "ORYX": "빠른 이동이 가능하고 파괴 가능한 벽을 통과할 수 있으며\n상대를 밀어낼 수 있게 해주는 빠른 질주 능력이다."
}

STAT_ADD = {
    "SLEDGE": "파괴 가능 횟수: 25번\n점수: 파쇄 망치 +5점, 파쇄 망치 보너스 +10점",
    "THATCHER": "개수: 3개\n무력화 범위: 5.2M\n무력화 지속시간: 10초",
    "ASH": "유탄 개수: 2개\n피해량: 50(직격) / 90 ~ 6(폭발 피해)\n폭발 범위: 4M",
    "THERMITE": "개수: 2개\n부착 시간: 2.5초, 폭파 시간: 3초",
    "TWITCH": "개수: 2개\n감전 피해량: 1, 사거리: 7.5M\n충전횟수: 3발, 충전시간: 30초",
    "MONTAGNE": "방패 전개 및 회수 시간: 0.5초",
    "GLAZ": "조준기 전개 및 회수 시간: 0.5초",
    "FUZE": "개수: 3개\n터지는 유탄 개수: 5개\n각 유탄 폭파 반경: 4.2M(2.5M 즉사, 1.7M 폭발피해)\n설치시간: 1.6초",
    "BLITZ": "사용 대기시간: 7초\n사용 횟수: 4번\n섬광 사거리: 5M",
    "IQ": "탐지 범위: 20M",
    "BUCK": "장탄수: 4+1발\n탄약수: 21발\n피해량: 펠렛당 60(1M) ~ 15(14M)\n연사력: 200RPM",
    "BLACKBEARD": "개수: 2개\n방패 내구도: 50\n이동 속도 감소량: 30%",
    "CAPITAO": "①폭발 화살\n화살개수: 2개, 지속시간: 10초\n피해량: 12, 피해 간격: 약 0.3초\n②초소형 연막탄\n화살개수: 2개\n지속시간: 10초",
    "HIBANA": "발사가능횟수: 3회\n파편 개수: 6개\n폭파시간: 5초",
    "JACKAL": "발자국 지속시간: 1분 30초\n추적 가능 횟수: 3번\n추적 지속시간: 최대 20초\n발자국 스캔 거리: 8M\n점수: 아이녹스 추적 지원 +25점",
    "YING": "개수: 3개\n터지는 섬광탄 개수: 7개\n격발 지연시간: 3~1초",
    "ZOFIA": "진탕탄: 2개\n진탕탄 격발 시간: 3초, 범위내 적이 있을 시 즉발\n진탕탄 범위: 약 5M\n방향감각 상실 지속시간: 5초\n충격탄: 2개",
    "DOKKAEBI": "사용 횟수: 2번\n진동 지속시간: 최대 12초",
    "LION": "사용 횟수 횟수: 3회\n준비 시간: 0.5초 간격으로 3회 카운트다운, 총 1.5초\n탐지 시간: 2초\n재사용 대기시간: 15초",
    "FINKA": "사용 가능 횟수: 3번\n버프 지속 시간: 10초\n"
             "HP 20증가, 정조준/지향사격 간 전환시간 25% 감소,\n"
             "총기 반동 50% 및 재장전 시간 25% 감소,\n철조망 위에서 이동 속도 25% 증가,\n섬광 50% 및 진탕 70% 지속시간 감소",
    "MAVERICK": "연료량: 5개\n피해량: 2\n전환 시간: 1.2초",
    "NOMAD": "유탄 개수: 3개\n격발 범위: 2M\n반발 범위: 3M\n전개 시간: 1.5초",
    "GRIDLOCK": "개수: 3개, 모체당 전개 개수: 최대 19개, 피해량: 10",
    "NOKK": "지속 시간: 최대 12초\n충전 시간: 최대 12초",
    "AMARU": "사용 가능 횟수: 4번, 사용 대기 시간: 9초",
    "KALI": "개수: 3개",
    "IANA": "분신 지속 시간: 14초\n충전 시간: 임의로 종료 시 8초 / \n타인에 의해 분신이 파괴되었을 시 30초",
    "SMOKE": "개수: 3개, 피해량: 15~25, 독가스 지속시간: 8초",
    "MUTE": "개수: 4개, 무력화 범위: 수평 2.25M, 수직 2.5M\n전파방해기: 15점",
    "CASTLE": "개수: 3개",
    "PULSE": "감지 범위: 9M, 해제 시간: 0.65초",
    "ROOK": "가방 개수: 1개, 방탄판 개수: 5개, 방어력 증가량: 약 20%",
    "DOC": "주사기 개수: 3개, 회복량: 40, 소생 회복량: 75\n최대 과잉치료량: 140",
    "KAPKAN": "개수: 5개, 피해량: 60 | 51 | 45",
    "TACHANKA": "개수: 1개\n장탄수: 60+1발, 탄약수: 240발\n연사력: 550, 발당 피해량: 66\n방패 내구도: 500",
    "JAGER": "개수: 3개, 요격 횟수: 2회\n점수: 선제 방어 시스템 +20점",
    "BANDIT": "개수: 4개, 배치 시간: 2.5초, 감전 피해량: 3",
    "FROST": "개수: 3개, 함정 내구도: 66",
    "VALKYRIE": "개수: 3개",
    "CAVEIRA": "①잠행\n지속시간: 최대 10초, 재사용 대기시간: 최대 5초\n②심문\n발각 시간: 10초, 전용 무기: LUISON 권총",
    "ECHO": "개수: 2개\n초음파 저장횟수: 2회, 초음파 충전시간: 20초\n방향감각 상실 지속시간: 최소 7초~최대 14초",
    "MIRA": "개수: 2개\n유리 사출시간: 2초",
    "LESION": "개수: 1+7개\n충전시간: 30초, 지속 피해량: 6",
    "ELA": "개수: 3개\n격발 지연시간: 1.5초, 격발 범위: 4M\n방향감각 상실 지속시간: 7초",
    "VIGIL": "지속시간: 최대 12초\n재사용 대기시간: 최대 6초",
    "MAESTRO": "개수: 2개\n레이저 충전수: 20회, 레이저 피해: 5",
    "ALIBI": "개수: 3개",
    "CLASH": "전기 충격 사거리: 약 12M, 전기 충격 용량: 최대 5초\n전기 피해량: 5, 재충전 딜레이: 2초\n피격 시 둔화 지속 시간: 0.5초",
    "KAID": "개수: 2개\n전개 시간: 3.75초, 작동 범위: 1.3M",
    "MOZZIE": "개수: 3개",
    "WARDEN": "충전 시간: 10초",
    "GOYO": "개수: 3개\n폭발 피해: 50 | 42 | 37, 화염 피해: 틱당 12\n화염 지속시간: 10초",
    "WAMAI": "개수: 1+4개, 충전시간: 40초",
    "ORYX": "횟수: 최대 3번\n충전시간: 7초, 질주거리: 5M"
}

STAT = {
    "SLEDGE": "파쇄 망치로 파괴한 수",
    "THATCHER": "EMP 수류탄으로 무력화한 도구",
    "ASH": "파괴탄으로 파괴한 수",
    "THERMITE": "발열성 폭약으로 돌파한 강화재",
    "TWITCH": "감전 드론으로 파괴한 도구",
    "MONTAGNE": "전개한 방패로 막은 총알",
    "GLAZ": "저격 사살",
    "FUZE": "접착식 집속탄으로 처치한 수",
    "BLITZ": "섬광 방패로 실명시킨 적",
    "IQ": "전자기기 탐지기로 포착한 도구",
    "BUCK": "부착식 산탄총으로 처치한 횟수",
    "BLACKBEARD": "방패로 막은 총알 수",
    "CAPITAO": "폭발 화살로 처치한 횟수",
    "HIBANA": "X-KAIROS 파편 폭발",
    "JACKAL": "아이녹스 추적 지원",
    "YING": "터뜨린 칸델라 장비",
    "ZOFIA": "진탕 수류탄 격발",
    "DOKKAEBI": "카메라 해킹",
    "LION": "EE-ONE-D 드론이 적 감지",
    "FINKA": "아드레날린 분출 보너스",
    "MAVERICK": "토치 진입",
    "NOMAD": "폭발한 기압탄",
    "GRIDLOCK": "설치한 트랙스",
    "NOKK": "관측 도구 기만",
    "AMARU": "총 릴 사용 거리",
    "KALI": "LV로 파괴된 도구",
    "IANA": "복제기 사용 후에 처치",
    "SMOKE": "독가스탄으로 처치한 수",
    "MUTE": "비활성화시킨 도구",
    "CASTLE": "배치한 방탄 패널",
    "PULSE": "포착한 심장 박동",
    "ROOK": "팀원이 사용한 방탄 패널",
    "DOC": "팀원 소생",
    "KAPKAN": "진입 방지 폭약으로 처치한 수",
    "TACHANKA": "탑승형 LMG로 사살한 수",
    "JAGER": "선제 방어 시스템으로 파괴한 도구",
    "BANDIT": "고압선으로 처치한 수",
    "FROST": "전술 함정으로 적을 무력화한 횟수",
    "VALKYRIE": "설치한 칠흑의 주시자",
    "CAVEIRA": "",
    "ECHO": "요괴로 인한 적 방향 감각 상실",
    "MIRA": "설치한 검은 거울",
    "LESION": "고독 장치로 중독시킨 적",
    "ELA": "격발한 GRZMOT 지뢰",
    "VIGIL": "드론 기만",
    "MAESTRO": "악의 눈으로 처치한 수",
    "ALIBI": "프리즈마에 속은 적",
    "CLASH": "둔화 적용 중 처치한 적",
    "KAID": "전기집게발 설치 완료",
    "MOZZIE": "해킹한 드론",
    "WARDEN": "응시 사용 중 사살",
    "GOYO": "아군이 폭발시킨 VOLCÁN",
    "WAMAI": "포획한 투사체",
    "ORYX": "라마 질주 후에 처치"
}

ALL = ["sledge", "thatcher", "ash", "thermite", "twitch", "montagne", "glaz", "fuze", "blitz", "iq", "buck",
       "blackbeard", "capitao", "hibana", "jackal", "ying", "zofia", "dokkaebi", "lion", "finka", "maverick",
       "nomad", "gridlock", "nokk", "amaru", "kali", "iana", "smoke", "mute", "castle", "pulse", "rook", "doc",
       "kapkan", "tachanka", "jager", "bandit", "frost", "valkyrie", "caveira", "echo", "mira", "lesion", "ela",
       "vigil", "maestro", "alibi", "clash", "kaid", "mozzie", "warden", "goyo", "wamai", "oryx"]
ATT = ["sledge", "thatcher", "ash", "thermite", "twitch", "montagne", "glaz", "fuze", "blitz", "iq", "buck",
       "blackbeard", "capitao", "hibana", "jackal", "ying", "zofia", "dokkaebi", "lion", "finka", "maverick",
       "nomad", "gridlock", "nokk", "amaru", "kali", "iana"]
DEF = ["smoke", "mute", "castle", "pulse", "rook", "doc", "kapkan", "tachanka", "jager", "bandit", "frost", "valkyrie",
       "caveira", "echo", "mira", "lesion", "ela", "vigil", "maestro", "alibi", "clash", "kaid", "mozzie", "warden",
       "goyo", "wamai", "oryx"]


def get_Auth():
    auth = api.Auth("hoo412298@gmail.com", "sinhoo5258")
    return auth


def get_Plat(platform):
    if platform == "UPLAY":
        return api.Platforms.UPLAY
    elif platform == "XBOX":
        return api.Platforms.XBOX
    else:
        return api.Platforms.PLAYSTATION

def get_Region(region):
    if region == "ASIA":
        return api.RankedRegions.ASIA
    elif region == "EU":
        return api.RankedRegions.EU
    else:
        return api.RankedRegions.NA


async def get_info(name, plat="UPLAY"):
    auth = get_Auth()
    platform = get_Plat(plat)
    player = await auth.get_player(name, platform)
    await player.load_general()
    return player


async def get_playtime(name, plat="UPLAY"):
    auth = get_Auth()
    platform = get_Plat(plat)
    player = await auth.get_player(name, platform)
    await player.load_general()
    return player.time_played


async def get_level(name, plat="UPLAY"):
    auth = get_Auth()
    platform = get_Plat(plat)
    player = await auth.get_player(name, platform)
    await player.load_level()
    return player.level


async def get_kd(name, plat="UPLAY"):
    auth = get_Auth()
    platform = get_Plat(plat)
    player = await auth.get_player(name, platform)
    await player.load_general()
    return round(player.kills / player.deaths, 2)


async def get_operKill(name, oper, plat="UPLAY"):
    auth = get_Auth()
    platform = get_Plat(plat)
    player = await auth.get_player(name, platform)
    operator = await player.get_operator(oper)
    return operator.kills


async def get_operKD(name, oper, plat="UPLAY"):
    auth = get_Auth()
    platform = get_Plat(plat)
    player = await auth.get_player(name, platform)
    operator = await player.get_operator(oper)
    return round(operator.kills / operator.deaths, 2)


def get_time_str(time):
    time_str = ""
    if (time / 3600 / 24) > 1:
        time_str += str(int(time / 3600 / 24)) + "일 "
    if (time / 3600 % 24) > 1:
        time_str += str(int(time / 3600 % 24)) + "시간 "
    if (time % 3600 / 60) > 1:
        time_str += str(int(time % 3600 / 60)) + "분"
    time_str += "(" + str(round(time / 3600, 2)) + "시간)"
    return time_str


def get_topOperKD(operators, num=2):
    kd = {}
    for oper in operators:
        if operators[oper].deaths != 0:
            kd[oper] = round(operators[oper].kills / operators[oper].deaths, 2)
        else:
            kd[oper] = 0
    sorted_kd = sorted(kd.items(), key=lambda kd: kd[1], reverse=True)
    return sorted_kd[0:num]


def get_topAttKD(operators, num=2):
    kd = {}
    for oper in operators:
        if operators[oper].deaths != 0 and oper in ATT:
            kd[oper] = round(operators[oper].kills / operators[oper].deaths, 2)
        elif operators[oper].deaths == 0 and oper in ATT:
            kd[oper] = 0
    sorted_kd = sorted(kd.items(), key=lambda kd: kd[1], reverse=True)
    return sorted_kd[0:num]


def get_topDefKD(operators, num=2):
    kd = {}
    for oper in operators:
        if operators[oper].deaths != 0 and oper in DEF:
            kd[oper] = round(operators[oper].kills / operators[oper].deaths, 2)
        elif operators[oper].deaths == 0 and oper in DEF:
            kd[oper] = 0
    sorted_kd = sorted(kd.items(), key=lambda kd: kd[1], reverse=True)
    return sorted_kd[0:num]


async def get_operTime(name, oper, plat="UPLAY"):
    auth = get_Auth()
    platform = get_Plat(plat)
    player = await auth.get_player(name, platform)
    operator = await player.get_operator(oper)
    return operator.time_played


def get_topOperTime(operators, num=2):
    time = {}
    for oper in operators:
        time[oper] = operators[oper].time_played
    sorted_time = sorted(time.items(), key=lambda time: time[1], reverse=True)
    return sorted_time[0:num]


def get_topAttTime(operators, num=2):
    time = {}
    for oper in operators:
        if oper in ATT:
            time[oper] = operators[oper].time_played
    sorted_time = sorted(time.items(), key=lambda time: time[1], reverse=True)
    return sorted_time[0:num]


def get_topDefTime(operators, num=2):
    time = {}
    for oper in operators:
        if oper in DEF:
            time[oper] = operators[oper].time_played
    sorted_time = sorted(time.items(), key=lambda time: time[1], reverse=True)
    return sorted_time[0:num]


async def get_team(names, plat):
    auth = get_Auth()
    platform = get_Plat(plat)
    players = names
    players_batch = await auth.get_player_batch(names=players, platform=platform)
    ranks = await players_batch.get_rank(api.RankedRegions.ASIA)
    mmr_list = []
    kd_list = []
    pt_list = []
    score_list = []
    await players_batch.load_general()
    for player in players_batch:
        mmr_list.append(int(ranks[player.id].mmr))
        kd_list.append(round(player.kills / player.deaths, 2))
        pt_list.append(player.time_played)
    for i in range(len(names)):
        score_list.append(round(0.25 * mmr_list[i] + 0.55 * kd_list[i] + 0.2 * pt_list[i], 2))
    score_dict = {}
    for i in range(len(names)):
        score_dict[players[i]] = score_list[i]
    sorted_res = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_res


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    val = loop.run_until_complete(get_team("nra_viscabarsha", "nra_lynelk", "up_grade_", "middle_grade_", "my_muse0105",
                                           "kor_mk545", "down_grade_", "nra_nixtan", "nra_make_way-in", "side_grade_"))
    print(val)
