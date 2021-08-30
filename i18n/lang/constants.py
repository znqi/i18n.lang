#   Copyright (c) 2021, Zenqi

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

try:
  import googletrans
  TRANSLATOR = googletrans.Translator()
  
except ModuleNotFoundError:
  TRANSLATOR = None

import pathlib

BASE_DIR: pathlib.Path = pathlib.Path().resolve()
COUNTRIES_TO_LANG = {
    
  "afrikaans": "af",
  "afrikaans (south africa)": "af_ZA",
  "arabic": "ar",
  "arabic (u.a.e.)": "ar_AE",
  "arabic (bahrain)": "ar_BH",
  "arabic (algeria)": "ar_DZ",
  "arabic (egypt)": "ar_EG",
  "arabic (iraq)": "ar_IQ",
  "arabic (jordan)": "ar_JO",
  "arabic (kuwait)": "ar_KW",
  "arabic (lebanon)": "ar_LB",
  "arabic (libya)": "ar_LY",
  "arabic (morocco)": "ar_MA",
  "arabic (oman)": "ar_OM",
  "arabic (qatar)": "ar_QA",
  "arabic (saudi arabia)": "ar_SA",
  "arabic (syria)": "ar_SY",
  "arabic (tunisia)": "ar_TN",
  "arabic (yemen)": "ar_YE",
  "azeri (latin)": "az",
  "azeri (latin) (azerbaijan)": "az_AZ",
  "azeri (cyrillic) (azerbaijan)": "az_AZ",
  "belarusian": "be",
  "belarusian (belarus)": "be_BY",
  "bulgarian": "bg",
  "bulgarian (bulgaria)": "bg_BG",
  "bosnian (bosnia and herzegovina)": "bs_BA",
  "catalan": "ca",
  "catalan (spain)": "ca_ES",
  "czech": "cs",
  "czech (czech republic)": "cs_CZ",
  "welsh": "cy",
  "welsh (united kingdom)": "cy_GB",
  "danish": "da",
  "danish (denmark)": "da_DK",
  "german": "de",
  "german (austria)": "de_AT",
  "german (switzerland)": "de_CH",
  "german (germany)": "de_DE",
  "german (liechtenstein)": "de_LI",
  "german (luxembourg)": "de_LU",
  "divehi": "dv",
  "divehi (maldives)": "dv_MV",
  "greek": "el",
  "greek (greece)": "el_GR",
  "english": "en",
  "english (australia)": "en_AU",
  "english (belize)": "en_BZ",
  "english (canada)": "en_CA",
  "english (caribbean)": "en_CB",
  "english (united kingdom)": "en_GB",
  "english (ireland)": "en_IE",
  "english (jamaica)": "en_JM",
  "english (new zealand)": "en_NZ",
  "english (republic of the philippines)": "en_PH",
  "english (trinidad and tobago)": "en_TT",
  "english (united states)": "en_US",
  "english (south africa)": "en_ZA",
  "english (zimbabwe)": "en_ZW",
  "esperanto": "eo",
  "spanish": "es",
  "spanish (argentina)": "es_AR",
  "spanish (bolivia)": "es_BO",
  "spanish (chile)": "es_CL",
  "spanish (colombia)": "es_CO",
  "spanish (costa rica)": "es_CR",
  "spanish (dominican republic)": "es_DO",
  "spanish (ecuador)": "es_EC",
  "spanish (castilian)": "es_ES",
  "spanish (spain)": "es_ES",
  "spanish (guatemala)": "es_GT",
  "spanish (honduras)": "es_HN",
  "spanish (mexico)": "es_MX",
  "spanish (nicaragua)": "es_NI",
  "spanish (panama)": "es_PA",
  "spanish (peru)": "es_PE",
  "spanish (puerto rico)": "es_PR",
  "spanish (paraguay)": "es_PY",
  "spanish (el salvador)": "es_SV",
  "spanish (uruguay)": "es_UY",
  "spanish (venezuela)": "es_VE",
  "estonian": "et",
  "estonian (estonia)": "et_EE",
  "basque": "eu",
  "basque (spain)": "eu_ES",
  "farsi": "fa",
  "farsi (iran)": "fa_IR",
  "finnish": "fi",
  "finnish (finland)": "fi_FI",
  "faroese": "fo",
  "faroese (faroe islands)": "fo_FO",
  "french": "fr",
  "french (belgium)": "fr_BE",
  "french (canada)": "fr_CA",
  "french (switzerland)": "fr_CH",
  "french (france)": "fr_FR",
  "french (luxembourg)": "fr_LU",
  "french (principality of monaco)": "fr_MC",
  "galician": "gl",
  "galician (spain)": "gl_ES",
  "gujarati": "gu",
  "gujarati (india)": "gu_IN",
  "hebrew": "he",
  "hebrew (israel)": "he_IL",
  "hindi": "hi",
  "hindi (india)": "hi_IN",
  "croatian": "hr",
  "croatian (bosnia and herzegovina)": "hr_BA",
  "croatian (croatia)": "hr_HR",
  "hungarian": "hu",
  "hungarian (hungary)": "hu_HU",
  "armenian": "hy",
  "armenian (armenia)": "hy_AM",
  "indonesian": "id",
  "indonesian (indonesia)": "id_ID",
  "icelandic": "is",
  "icelandic (iceland)": "is_IS",
  "italian": "it",
  "italian (switzerland)": "it_CH",
  "italian (italy)": "it_IT",
  "japanese": "ja",
  "japanese (japan)": "ja_JP",
  "georgian": "ka",
  "georgian (georgia)": "ka_GE",
  "kazakh": "kk",
  "kazakh (kazakhstan)": "kk_KZ",
  "kannada": "kn",
  "kannada (india)": "kn_IN",
  "korean": "ko",
  "korean (korea)": "ko_KR",
  "konkani": "kok",
  "konkani (india)": "kok_IN",
  "kyrgyz": "ky",
  "kyrgyz (kyrgyzstan)": "ky_KG",
  "lithuanian": "lt",
  "lithuanian (lithuania)": "lt_LT",
  "latvian": "lv",
  "latvian (latvia)": "lv_LV",
  "maori": "mi",
  "maori (new zealand)": "mi_NZ",
  "fyro macedonian": "mk",
  "fyro macedonian (former yugoslav republic of macedonia)": "mk_MK",
  "mongolian": "mn",
  "mongolian (mongolia)": "mn_MN",
  "marathi": "mr",
  "marathi (india)": "mr_IN",
  "malay": "ms",
  "malay (brunei darussalam)": "ms_BN",
  "malay (malaysia)": "ms_MY",
  "maltese": "mt",
  "maltese (malta)": "mt_MT",
  "norwegian (bokm?l)": "nb",
  "norwegian (bokm?l) (norway)": "nb_NO",
  "dutch": "nl",
  "dutch (belgium)": "nl_BE",
  "dutch (netherlands)": "nl_NL",
  "norwegian (nynorsk) (norway)": "nn_NO",
  "northern sotho": "ns",
  "northern sotho (south africa)": "ns_ZA",
  "punjabi": "pa",
  "punjabi (india)": "pa_IN",
  "polish": "pl",
  "polish (poland)": "pl_PL",
  "pashto": "ps",
  "pashto (afghanistan)": "ps_AR",
  "portuguese": "pt",
  "portuguese (brazil)": "pt_BR",
  "portuguese (portugal)": "pt_PT",
  "quechua": "qu",
  "quechua (bolivia)": "qu_BO",
  "quechua (ecuador)": "qu_EC",
  "quechua (peru)": "qu_PE",
  "romanian": "ro",
  "romanian (romania)": "ro_RO",
  "russian": "ru",
  "russian (russia)": "ru_RU",
  "sanskrit": "sa",
  "sanskrit (india)": "sa_IN",
  "sami (northern)": "se",
  "sami (northern) (finland)": "se_FI",
  "sami (skolt) (finland)": "se_FI",
  "sami (inari) (finland)": "se_FI",
  "sami (northern) (norway)": "se_NO",
  "sami (lule) (norway)": "se_NO",
  "sami (southern) (norway)": "se_NO",
  "sami (northern) (sweden)": "se_SE",
  "sami (lule) (sweden)": "se_SE",
  "sami (southern) (sweden)": "se_SE",
  "slovak": "sk",
  "slovak (slovakia)": "sk_SK",
  "slovenian": "sl",
  "slovenian (slovenia)": "sl_SI",
  "albanian": "sq",
  "albanian (albania)": "sq_AL",
  "serbian (latin) (bosnia and herzegovina)": "sr_BA",
  "serbian (cyrillic) (bosnia and herzegovina)": "sr_BA",
  "serbian (latin) (serbia and montenegro)": "sr_SP",
  "serbian (cyrillic) (serbia and montenegro)": "sr_SP",
  "swedish": "sv",
  "swedish (finland)": "sv_FI",
  "swedish (sweden)": "sv_SE",
  "swahili": "sw",
  "swahili (kenya)": "sw_KE",
  "syriac": "syr",
  "syriac (syria)": "syr_SY",
  "tamil": "ta",
  "tamil (india)": "ta_IN",
  "telugu": "te",
  "telugu (india)": "te_IN",
  "thai": "th",
  "thai (thailand)": "th_TH",
  "tagalog": "tl",
  "tagalog (philippines)": "tl_PH",
  "tswana": "tn",
  "tswana (south africa)": "tn_ZA",
  "turkish": "tr",
  "turkish (turkey)": "tr_TR",
  "tatar": "tt",
  "tatar (russia)": "tt_RU",
  "tsonga": "ts",
  "ukrainian": "uk",
  "ukrainian (ukraine)": "uk_UA",
  "urdu": "ur",
  "urdu (islamic republic of pakistan)": "ur_PK",
  "uzbek (latin)": "uz",
  "uzbek (latin) (uzbekistan)": "uz_UZ",
  "uzbek (cyrillic) (uzbekistan)": "uz_UZ",
  "vietnamese": "vi",
  "vietnamese (viet nam)": "vi_VN",
  "xhosa": "xh",
  "xhosa (south africa)": "xh_ZA",
  "chinese": "zh_CN",
  "chinese (traditional)": "zh_TW",
  "zulu": "zu",
  "zulu (south africa)": "zu_ZA"
}

COUNTRIES_TO_CODE = {
    "aruba": "aw",
    "afghanistan": "af",
    "angola": "ao",
    "anguilla": "ai",
    "\u00e5land islands": "ax",
    "albania": "al",
    "andorra": "ad",
    "united arab emirates": "ae",
    "argentina": "ar",
    "armenia": "am",
    "american samoa": "as",
    "antarctica": "aq",
    "french southern territories": "tf",
    "antigua and barbuda": "ag",
    "australia": "au",
    "austria": "at",
    "azerbaijan": "az",
    "burundi": "bi",
    "belgium": "be",
    "benin": "bj",
    "bonaire, sint eustatius and saba": "bq",
    "burkina faso": "bf",
    "bangladesh": "bd",
    "bulgaria": "bg",
    "bahrain": "bh",
    "bahamas": "bs",
    "bosnia and herzegovina": "ba",
    "saint barth\u00e9lemy": "bl",
    "belarus": "by",
    "belize": "bz",
    "bermuda": "bm",
    "bolivia, plurinational state of": "bo",
    "brazil": "br",
    "barbados": "bb",
    "brunei darussalam": "bn",
    "bhutan": "bt",
    "bouvet island": "bv",
    "botswana": "bw",
    "central african republic": "cf",
    "canada": "ca",
    "cocos (keeling) islands": "cc",
    "switzerland": "ch",
    "chile": "cl",
    "china": "cn",
    "c\u00f4te d'ivoire": "ci",
    "cameroon": "cm",
    "congo, the democratic republic of the": "cd",
    "congo": "cg",
    "cook islands": "ck",
    "colombia": "co",
    "comoros": "km",
    "cabo verde": "cv",
    "costa rica": "cr",
    "cuba": "cu",
    "cura\u00e7ao": "cw",
    "christmas island": "cx",
    "cayman islands": "ky",
    "cyprus": "cy",
    "czechia": "cz",
    "germany": "de",
    "djibouti": "dj",
    "dominica": "dm",
    "denmark": "dk",
    "dominican republic": "do",
    "algeria": "dz",
    "ecuador": "ec",
    "egypt": "eg",
    "eritrea": "er",
    "western sahara": "eh",
    "spain": "es",
    "estonia": "ee",
    "ethiopia": "et",
    "finland": "fi",
    "fiji": "fj",
    "falkland islands (malvinas)": "fk",
    "france": "fr",
    "faroe islands": "fo",
    "micronesia, federated states of": "fm",
    "gabon": "ga",
    "united kingdom": "gb",
    "georgia": "ge",
    "guernsey": "gg",
    "ghana": "gh",
    "gibraltar": "gi",
    "guinea": "gn",
    "guadeloupe": "gp",
    "gambia": "gm",
    "guinea_bissau": "gw",
    "equatorial guinea": "gq",
    "greece": "gr",
    "grenada": "gd",
    "greenland": "gl",
    "guatemala": "gt",
    "french guiana": "gf",
    "guam": "gu",
    "guyana": "gy",
    "hong kong": "hk",
    "heard island and mcdonald islands": "hm",
    "honduras": "hn",
    "croatia": "hr",
    "haiti": "ht",
    "hungary": "hu",
    "indonesia": "id",
    "isle of man": "im",
    "india": "in",
    "british indian ocean territory": "io",
    "ireland": "ie",
    "iran, islamic republic of": "ir",
    "iraq": "iq",
    "iceland": "is",
    "israel": "il",
    "italy": "it",
    "jamaica": "jm",
    "jersey": "je",
    "jordan": "jo",
    "japan": "jp",
    "kazakhstan": "kz",
    "kenya": "ke",
    "kyrgyzstan": "kg",
    "cambodia": "kh",
    "kiribati": "ki",
    "saint kitts and nevis": "kn",
    "korea, republic of": "kr",
    "kuwait": "kw",
    "lao people's democratic republic": "la",
    "lebanon": "lb",
    "liberia": "lr",
    "libya": "ly",
    "saint lucia": "lc",
    "liechtenstein": "li",
    "sri lanka": "lk",
    "lesotho": "ls",
    "lithuania": "lt",
    "luxembourg": "lu",
    "latvia": "lv",
    "macao": "mo",
    "saint martin (french part)": "mf",
    "morocco": "ma",
    "monaco": "mc",
    "moldova, republic of": "md",
    "madagascar": "mg",
    "maldives": "mv",
    "mexico": "mx",
    "marshall islands": "mh",
    "north macedonia": "mk",
    "mali": "ml",
    "malta": "mt",
    "myanmar": "mm",
    "montenegro": "me",
    "mongolia": "mn",
    "northern mariana islands": "mp",
    "mozambique": "mz",
    "mauritania": "mr",
    "montserrat": "ms",
    "martinique": "mq",
    "mauritius": "mu",
    "malawi": "mw",
    "malaysia": "my",
    "mayotte": "yt",
    "namibia": "na",
    "new caledonia": "nc",
    "niger": "ne",
    "norfolk island": "nf",
    "nigeria": "ng",
    "nicaragua": "ni",
    "niue": "nu",
    "netherlands": "nl",
    "norway": "no",
    "nepal": "np",
    "nauru": "nr",
    "new zealand": "nz",
    "oman": "om",
    "pakistan": "pk",
    "panama": "pa",
    "pitcairn": "pn",
    "peru": "pe",
    "philippines": "ph",
    "palau": "pw",
    "papua new guinea": "pg",
    "poland": "pl",
    "puerto rico": "pr",
    "korea, democratic people's republic of": "kp",
    "portugal": "pt",
    "paraguay": "py",
    "palestine, state of": "ps",
    "french polynesia": "pf",
    "qatar": "qa",
    "r\u00e9union": "re",
    "romania": "ro",
    "russian federation": "ru",
    "rwanda": "rw",
    "saudi arabia": "sa",
    "sudan": "sd",
    "senegal": "sn",
    "singapore": "sg",
    "south georgia and the south sandwich islands": "gs",
    "saint helena, ascension and tristan da cunha": "sh",
    "svalbard and jan mayen": "sj",
    "solomon islands": "sb",
    "sierra leone": "sl",
    "el salvador": "sv",
    "san marino": "sm",
    "somalia": "so",
    "saint pierre and miquelon": "pm",
    "serbia": "rs",
    "south sudan": "ss",
    "sao tome and principe": "st",
    "suriname": "sr",
    "slovakia": "sk",
    "slovenia": "si",
    "sweden": "se",
    "eswatini": "sz",
    "sint maarten (dutch part)": "sx",
    "seychelles": "sc",
    "syrian arab republic": "sy",
    "turks and caicos islands": "tc",
    "chad": "td",
    "togo": "tg",
    "thailand": "th",
    "tajikistan": "tj",
    "tokelau": "tk",
    "turkmenistan": "tm",
    "timor_leste": "tl",
    "tonga": "to",
    "trinidad and tobago": "tt",
    "tunisia": "tn",
    "turkey": "tr",
    "tuvalu": "tv",
    "taiwan, province of china": "tw",
    "tanzania, united republic of": "tz",
    "uganda": "ug",
    "ukraine": "ua",
    "united states minor outlying islands": "um",
    "uruguay": "uy",
    "united states": "us",
    "uzbekistan": "uz",
    "holy see (vatican city state)": "va",
    "saint vincent and the grenadines": "vc",
    "venezuela, bolivarian republic of": "ve",
    "virgin islands, british": "vg",
    "virgin islands, u.s.": "vi",
    "viet nam": "vn",
    "vanuatu": "vu",
    "wallis and futuna": "wf",
    "samoa": "ws",
    "yemen": "ye",
    "south africa": "za",
    "zambia": "zm",
    "zimbabwe": "zw"
}