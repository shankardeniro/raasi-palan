"""
One-time script to generate the interpretations.json file with
traditional Gochara effect placeholders for all 9 planets x 12 houses.
"""

import json

interpretations = {
    "_meta": {
        "description": "Gochara (transit) interpretation texts for each planet-in-house combination",
        "how_to_edit": "Each planet has entries for houses 1-12. Each entry has 'en' (English) and 'ta' (Tamil) text, plus 'tendency' (favourable/unfavourable/mixed). Replace the text with content from your Vedic astrology books.",
        "total_entries": 108
    },
    "Sun": {
        "1": {
            "tendency": "unfavourable",
            "en": "Sun transiting your 1st house may bring health concerns, fatigue, and a restless mind. Ego clashes with authority figures are possible. Take care of your physical well-being.",
            "ta": "சூரியன் உங்கள் லக்னத்தில் சஞ்சரிப்பதால் உடல் நலக்குறைவு, சோர்வு மற்றும் மன அமைதியின்மை ஏற்படலாம். உயர் அதிகாரிகளுடன் கருத்து வேறுபாடுகள் வரலாம். உடல் ஆரோக்கியத்தில் கவனம் தேவை."
        },
        "2": {
            "tendency": "unfavourable",
            "en": "Sun in your 2nd house may cause financial setbacks and family disagreements. Be cautious with spending. Eye-related health issues are possible.",
            "ta": "சூரியன் 2-ம் இடத்தில் சஞ்சரிப்பதால் பணவரவில் தடை, குடும்பத்தில் கருத்து வேறுபாடுகள் ஏற்படலாம். செலவுகளில் கவனம் தேவை. கண் தொடர்பான பிரச்சனைகள் வரலாம்."
        },
        "3": {
            "tendency": "favourable",
            "en": "Sun in your 3rd house brings courage, victory over rivals, and improved health. A good period for taking bold initiatives and short travels.",
            "ta": "சூரியன் 3-ம் இடத்தில் சஞ்சரிப்பதால் தைரியம் அதிகரிக்கும், எதிரிகளை வெல்லலாம், உடல் ஆரோக்கியம் மேம்படும். துணிச்சலான முடிவுகளுக்கும் குறுகிய பயணங்களுக்கும் நல்ல நேரம்."
        },
        "4": {
            "tendency": "unfavourable",
            "en": "Sun in your 4th house may bring domestic unrest and mental anxiety. Relationship with mother or elders at home may be strained. Vehicle-related caution advised.",
            "ta": "சூரியன் 4-ம் இடத்தில் சஞ்சரிப்பதால் வீட்டில் அமைதியின்மை, மன உளைச்சல் ஏற்படலாம். தாய் அல்லது பெரியவர்களுடன் உறவில் சிக்கல் வரலாம். வாகனப் பயணத்தில் கவனம் தேவை."
        },
        "5": {
            "tendency": "unfavourable",
            "en": "Sun in your 5th house may cause worry related to children or creative projects. Mental restlessness and difficulty in decision-making are possible.",
            "ta": "சூரியன் 5-ம் இடத்தில் சஞ்சரிப்பதால் குழந்தைகள் தொடர்பான கவலை அல்லது படைப்புத் திட்டங்களில் தடை ஏற்படலாம். மன அமைதியின்மையும் முடிவெடுப்பதில் சிரமமும் வரலாம்."
        },
        "6": {
            "tendency": "favourable",
            "en": "Sun in your 6th house brings victory over enemies, relief from illness, and success in competitive situations. A strong period for overcoming obstacles.",
            "ta": "சூரியன் 6-ம் இடத்தில் சஞ்சரிப்பதால் எதிரிகளை வெல்லலாம், நோய்களிலிருந்து நிவாரணம் கிடைக்கும், போட்டிகளில் வெற்றி கிடைக்கும். தடைகளை கடக்க நல்ல காலம்."
        },
        "7": {
            "tendency": "unfavourable",
            "en": "Sun in your 7th house may bring travel fatigue and tension in partnerships or marriage. Avoid unnecessary confrontations with spouse or business partners.",
            "ta": "சூரியன் 7-ம் இடத்தில் சஞ்சரிப்பதால் பயணச் சோர்வு, வாழ்க்கைத் துணை அல்லது வியாபாரக் கூட்டாளிகளுடன் பிரச்சனை ஏற்படலாம். தேவையற்ற மோதல்களைத் தவிர்க்கவும்."
        },
        "8": {
            "tendency": "unfavourable",
            "en": "Sun in your 8th house may bring health troubles, obstacles in work, and quarrels. Be cautious with risky ventures. A period requiring patience.",
            "ta": "சூரியன் 8-ம் இடத்தில் சஞ்சரிப்பதால் உடல் நலக்குறைவு, வேலையில் தடைகள், சச்சரவுகள் ஏற்படலாம். ஆபத்தான முயற்சிகளில் கவனம் தேவை. பொறுமை அவசியம்."
        },
        "9": {
            "tendency": "unfavourable",
            "en": "Sun in your 9th house may cause obstacles in fortune, conflicts with father or mentors, and physical weakness. Spiritual practices may feel strained.",
            "ta": "சூரியன் 9-ம் இடத்தில் சஞ்சரிப்பதால் பாக்கியத்தில் தடை, தந்தை அல்லது குருவுடன் கருத்து வேறுபாடு, உடல் பலவீனம் ஏற்படலாம். ஆன்மீக முயற்சிகளில் சிரமம் வரலாம்."
        },
        "10": {
            "tendency": "favourable",
            "en": "Sun in your 10th house brings career success, recognition from superiors, and fulfillment of professional goals. A powerful period for ambition.",
            "ta": "சூரியன் 10-ம் இடத்தில் சஞ்சரிப்பதால் தொழிலில் வெற்றி, மேலதிகாரிகளிடம் அங்கீகாரம், தொழில் இலக்குகள் நிறைவேறும். லட்சியங்களுக்கு சக்திவாய்ந்த காலம்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Sun in your 11th house brings financial gains, happiness, and fulfillment of desires. Social connections strengthen and new opportunities arise.",
            "ta": "சூரியன் 11-ம் இடத்தில் சஞ்சரிப்பதால் பண வரவு அதிகரிக்கும், மகிழ்ச்சி, ஆசைகள் நிறைவேறும். சமூக உறவுகள் வலுப்பெறும், புதிய வாய்ப்புகள் உருவாகும்."
        },
        "12": {
            "tendency": "unfavourable",
            "en": "Sun in your 12th house may increase expenditure, cause eye-related issues, and bring a sense of loss. Rest and recuperation are important.",
            "ta": "சூரியன் 12-ம் இடத்தில் சஞ்சரிப்பதால் செலவுகள் அதிகரிக்கும், கண் தொடர்பான பிரச்சனைகள், இழப்பு உணர்வு ஏற்படலாம். ஓய்வும் உடல் பராமரிப்பும் முக்கியம்."
        }
    },
    "Moon": {
        "1": {
            "tendency": "favourable",
            "en": "Moon in your 1st house brings comfort, good food, and a pleasant state of mind. A good day for self-care and enjoying life's pleasures.",
            "ta": "சந்திரன் உங்கள் லக்னத்தில் சஞ்சரிப்பதால் உடல் சுகம், நல்ல உணவு, மன நிம்மதி கிடைக்கும். சுய பராமரிப்புக்கும் இன்பங்களை அனுபவிக்கவும் நல்ல நாள்."
        },
        "2": {
            "tendency": "unfavourable",
            "en": "Moon in your 2nd house may bring financial obstacles and a sense of dissatisfaction. Watch your words in family conversations.",
            "ta": "சந்திரன் 2-ம் இடத்தில் சஞ்சரிப்பதால் பண வரவில் தடை, மனநிறைவின்மை ஏற்படலாம். குடும்ப உரையாடல்களில் வார்த்தைகளில் கவனம் தேவை."
        },
        "3": {
            "tendency": "favourable",
            "en": "Moon in your 3rd house brings success, gains from efforts, and happiness. Courage increases and communications go well.",
            "ta": "சந்திரன் 3-ம் இடத்தில் சஞ்சரிப்பதால் வெற்றி, முயற்சிகளில் லாபம், மகிழ்ச்சி கிடைக்கும். தைரியம் அதிகரிக்கும், தகவல் பரிமாற்றங்கள் சிறப்பாக அமையும்."
        },
        "4": {
            "tendency": "unfavourable",
            "en": "Moon in your 4th house may bring fear, mental anxiety, and domestic concerns. Avoid major decisions today and seek calm.",
            "ta": "சந்திரன் 4-ம் இடத்தில் சஞ்சரிப்பதால் பயம், மன கவலை, வீட்டு விஷயங்களில் கவலை ஏற்படலாம். இன்று பெரிய முடிவுகளைத் தவிர்த்து, அமைதியைத் தேடுங்கள்."
        },
        "5": {
            "tendency": "unfavourable",
            "en": "Moon in your 5th house may cause disappointment in plans, stomach discomfort, and worry about children or creative work.",
            "ta": "சந்திரன் 5-ம் இடத்தில் சஞ்சரிப்பதால் திட்டங்களில் ஏமாற்றம், வயிற்று உபாதை, குழந்தைகள் அல்லது படைப்புப் பணிகள் பற்றிய கவலை ஏற்படலாம்."
        },
        "6": {
            "tendency": "favourable",
            "en": "Moon in your 6th house brings good health, comfort, and victory over adversaries. A strong day for tackling problems head-on.",
            "ta": "சந்திரன் 6-ம் இடத்தில் சஞ்சரிப்பதால் நல்ல ஆரோக்கியம், சுகம், எதிரிகளை வெல்லும் ஆற்றல் கிடைக்கும். பிரச்சனைகளை நேரடியாக எதிர்கொள்ள நல்ல நாள்."
        },
        "7": {
            "tendency": "favourable",
            "en": "Moon in your 7th house brings happiness in relationships, good food, and social enjoyment. A pleasant day for partnerships.",
            "ta": "சந்திரன் 7-ம் இடத்தில் சஞ்சரிப்பதால் உறவுகளில் மகிழ்ச்சி, நல்ல உணவு, சமூக இன்பம் கிடைக்கும். கூட்டாண்மைக்கு இனிய நாள்."
        },
        "8": {
            "tendency": "unfavourable",
            "en": "Moon in your 8th house may bring health anxiety, emotional turbulence, and unexpected troubles. Practice patience and self-care.",
            "ta": "சந்திரன் 8-ம் இடத்தில் சஞ்சரிப்பதால் உடல் கவலை, உணர்ச்சி கொந்தளிப்பு, எதிர்பாராத பிரச்சனைகள் ஏற்படலாம். பொறுமையும் சுய பராமரிப்பும் அவசியம்."
        },
        "9": {
            "tendency": "unfavourable",
            "en": "Moon in your 9th house may bring mental distress and minor health issues. Spiritual efforts may not yield expected results today.",
            "ta": "சந்திரன் 9-ம் இடத்தில் சஞ்சரிப்பதால் மன உளைச்சல், சிறிய உடல் பிரச்சனைகள் ஏற்படலாம். ஆன்மீக முயற்சிகள் எதிர்பார்த்த பலனைத் தராமல் போகலாம்."
        },
        "10": {
            "tendency": "favourable",
            "en": "Moon in your 10th house brings success in professional matters, recognition, and a sense of achievement. A productive and rewarding day.",
            "ta": "சந்திரன் 10-ம் இடத்தில் சஞ்சரிப்பதால் தொழில் விஷயங்களில் வெற்றி, அங்கீகாரம், சாதனை உணர்வு கிடைக்கும். பயனுள்ள மற்றும் பலன் தரும் நாள்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Moon in your 11th house brings happiness, financial gains, and good food. Desires are fulfilled and social life is enjoyable.",
            "ta": "சந்திரன் 11-ம் இடத்தில் சஞ்சரிப்பதால் மகிழ்ச்சி, பண வரவு, நல்ல உணவு கிடைக்கும். ஆசைகள் நிறைவேறும், சமூக வாழ்க்கை இனிமையாக இருக்கும்."
        },
        "12": {
            "tendency": "unfavourable",
            "en": "Moon in your 12th house may increase spending and bring worry. Sleep may be disturbed. A day for rest rather than new ventures.",
            "ta": "சந்திரன் 12-ம் இடத்தில் சஞ்சரிப்பதால் செலவுகள் அதிகரிக்கும், கவலை ஏற்படலாம். தூக்கம் பாதிக்கப்படலாம். புதிய முயற்சிகளை விட ஓய்வுக்கு ஏற்ற நாள்."
        }
    },
    "Mars": {
        "1": {
            "tendency": "unfavourable",
            "en": "Mars in your 1st house may bring conflicts, fever, and blood-related health issues. Control your temper and avoid risky physical activities.",
            "ta": "செவ்வாய் உங்கள் லக்னத்தில் சஞ்சரிப்பதால் மோதல்கள், காய்ச்சல், இரத்தம் தொடர்பான உடல் பிரச்சனைகள் ஏற்படலாம். கோபத்தைக் கட்டுப்படுத்துங்கள், ஆபத்தான செயல்களைத் தவிர்க்கவும்."
        },
        "2": {
            "tendency": "unfavourable",
            "en": "Mars in your 2nd house may cause financial loss, harsh speech, and eye-related problems. Guard your finances and speak with care.",
            "ta": "செவ்வாய் 2-ம் இடத்தில் சஞ்சரிப்பதால் பண இழப்பு, கடுமையான பேச்சு, கண் தொடர்பான பிரச்சனைகள் ஏற்படலாம். நிதியைப் பாதுகாத்து, கவனமாகப் பேசுங்கள்."
        },
        "3": {
            "tendency": "favourable",
            "en": "Mars in your 3rd house brings courage, financial gains, and victory over competitors. A powerful time for bold action and leadership.",
            "ta": "செவ்வாய் 3-ம் இடத்தில் சஞ்சரிப்பதால் தைரியம், பண வரவு, போட்டியாளர்களை வெல்லும் ஆற்றல் கிடைக்கும். துணிச்சலான செயல்களுக்கும் தலைமைக்கும் சிறந்த நேரம்."
        },
        "4": {
            "tendency": "unfavourable",
            "en": "Mars in your 4th house may bring stomach troubles, domestic conflicts, and mental unrest. Property matters may face complications.",
            "ta": "செவ்வாய் 4-ம் இடத்தில் சஞ்சரிப்பதால் வயிற்றுப் பிரச்சனை, வீட்டில் சண்டை, மன அமைதியின்மை ஏற்படலாம். சொத்து விஷயங்களில் சிக்கல் வரலாம்."
        },
        "5": {
            "tendency": "unfavourable",
            "en": "Mars in your 5th house may cause conflicts, loss in speculative ventures, and worry about children. Avoid impulsive decisions.",
            "ta": "செவ்வாய் 5-ம் இடத்தில் சஞ்சரிப்பதால் மோதல்கள், ஊக வணிகத்தில் நஷ்டம், குழந்தைகள் பற்றிய கவலை ஏற்படலாம். அவசர முடிவுகளைத் தவிர்க்கவும்."
        },
        "6": {
            "tendency": "favourable",
            "en": "Mars in your 6th house brings victory over enemies, success in legal matters, and relief from ongoing troubles. A commanding period.",
            "ta": "செவ்வாய் 6-ம் இடத்தில் சஞ்சரிப்பதால் எதிரிகளை வெல்லலாம், சட்ட விஷயங்களில் வெற்றி, நிலவும் பிரச்சனைகளிலிருந்து நிவாரணம் கிடைக்கும். ஆதிக்கமான காலம்."
        },
        "7": {
            "tendency": "unfavourable",
            "en": "Mars in your 7th house may cause marital disagreements, eye problems, and disputes with partners. Practice patience in relationships.",
            "ta": "செவ்வாய் 7-ம் இடத்தில் சஞ்சரிப்பதால் திருமண உறவில் கருத்து வேறுபாடு, கண் பிரச்சனை, கூட்டாளிகளுடன் சச்சரவு ஏற்படலாம். உறவுகளில் பொறுமை காக்கவும்."
        },
        "8": {
            "tendency": "unfavourable",
            "en": "Mars in your 8th house may bring accidents, health risks, and unexpected obstacles. Exercise extreme caution in travel and physical activities.",
            "ta": "செவ்வாய் 8-ம் இடத்தில் சஞ்சரிப்பதால் விபத்துகள், உடல்நல ஆபத்துகள், எதிர்பாராத தடைகள் ஏற்படலாம். பயணம் மற்றும் உடல் செயல்பாடுகளில் மிகுந்த கவனம் தேவை."
        },
        "9": {
            "tendency": "unfavourable",
            "en": "Mars in your 9th house may cause losses, legal complications, and reduced fortune. Avoid unnecessary arguments with elders.",
            "ta": "செவ்வாய் 9-ம் இடத்தில் சஞ்சரிப்பதால் நஷ்டங்கள், சட்ட சிக்கல்கள், பாக்கியம் குறையலாம். பெரியவர்களுடன் தேவையற்ற வாக்குவாதங்களைத் தவிர்க்கவும்."
        },
        "10": {
            "tendency": "unfavourable",
            "en": "Mars in your 10th house may bring career obstacles and conflicts with superiors. Professional reputation needs careful guarding.",
            "ta": "செவ்வாய் 10-ம் இடத்தில் சஞ்சரிப்பதால் தொழிலில் தடைகள், மேலதிகாரிகளுடன் மோதல் ஏற்படலாம். தொழில் நற்பெயரைக் கவனமாகக் காக்க வேண்டும்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Mars in your 11th house brings financial gains, property acquisition, and happiness. A rewarding period for investments and bold ventures.",
            "ta": "செவ்வாய் 11-ம் இடத்தில் சஞ்சரிப்பதால் பண வரவு, சொத்து வாங்குதல், மகிழ்ச்சி கிடைக்கும். முதலீடுகள் மற்றும் துணிச்சலான முயற்சிகளுக்கு பலன் தரும் காலம்."
        },
        "12": {
            "tendency": "unfavourable",
            "en": "Mars in your 12th house may increase expenditure, cause health issues, and bring eye-related troubles. Conserve energy and finances.",
            "ta": "செவ்வாய் 12-ம் இடத்தில் சஞ்சரிப்பதால் செலவுகள் அதிகரிக்கும், உடல் பிரச்சனைகள், கண் தொடர்பான சிக்கல்கள் ஏற்படலாம். சக்தியையும் நிதியையும் சேமியுங்கள்."
        }
    },
    "Mercury": {
        "1": {
            "tendency": "unfavourable",
            "en": "Mercury in your 1st house may cause displacement from routine, anxiety, and loss. Avoid starting major new ventures today.",
            "ta": "புதன் உங்கள் லக்னத்தில் சஞ்சரிப்பதால் வழக்கமான பணிகளில் இடையூறு, கவலை, நஷ்டம் ஏற்படலாம். இன்று பெரிய புதிய முயற்சிகளைத் தொடங்குவதைத் தவிர்க்கவும்."
        },
        "2": {
            "tendency": "favourable",
            "en": "Mercury in your 2nd house brings financial gains, eloquent speech, and success in learning. Business communications yield positive results.",
            "ta": "புதன் 2-ம் இடத்தில் சஞ்சரிப்பதால் பண வரவு, சிறந்த பேச்சுத் திறன், கல்வியில் வெற்றி கிடைக்கும். வணிகத் தொடர்புகள் நல்ல பலன் தரும்."
        },
        "3": {
            "tendency": "unfavourable",
            "en": "Mercury in your 3rd house may bring conflicts with siblings, fear of adversaries, and communication mishaps. Double-check important messages.",
            "ta": "புதன் 3-ம் இடத்தில் சஞ்சரிப்பதால் உடன்பிறந்தவர்களுடன் மோதல், எதிரிகள் பற்றிய பயம், தகவல் பரிமாற்றத்தில் தவறுகள் ஏற்படலாம். முக்கிய செய்திகளை இருமுறை சரிபார்க்கவும்."
        },
        "4": {
            "tendency": "favourable",
            "en": "Mercury in your 4th house brings gains in property, educational success, and domestic harmony. Intellectual pursuits are rewarded.",
            "ta": "புதன் 4-ம் இடத்தில் சஞ்சரிப்பதால் சொத்தில் லாபம், கல்வியில் வெற்றி, வீட்டில் அமைதி கிடைக்கும். அறிவுசார் முயற்சிகளுக்கு பலன் கிடைக்கும்."
        },
        "5": {
            "tendency": "unfavourable",
            "en": "Mercury in your 5th house may cause quarrels with family members and mental tension. Creative projects may face unexpected delays.",
            "ta": "புதன் 5-ம் இடத்தில் சஞ்சரிப்பதால் குடும்ப உறுப்பினர்களுடன் சண்டை, மன அழுத்தம் ஏற்படலாம். படைப்புத் திட்டங்கள் எதிர்பாராத தாமதத்தை சந்திக்கலாம்."
        },
        "6": {
            "tendency": "favourable",
            "en": "Mercury in your 6th house brings victory in disputes, gains, and success in competitive exams. Problems find clever solutions.",
            "ta": "புதன் 6-ம் இடத்தில் சஞ்சரிப்பதால் தகராறுகளில் வெற்றி, லாபம், போட்டித் தேர்வுகளில் வெற்றி கிடைக்கும். பிரச்சனைகளுக்கு புத்திசாலித்தனமான தீர்வுகள் கிடைக்கும்."
        },
        "7": {
            "tendency": "unfavourable",
            "en": "Mercury in your 7th house may cause disputes with spouse or business partners and miscommunication. Be precise in agreements.",
            "ta": "புதன் 7-ம் இடத்தில் சஞ்சரிப்பதால் வாழ்க்கைத் துணை அல்லது வணிகக் கூட்டாளிகளுடன் சண்டை, தவறான புரிதல் ஏற்படலாம். ஒப்பந்தங்களில் துல்லியமாக இருங்கள்."
        },
        "8": {
            "tendency": "favourable",
            "en": "Mercury in your 8th house brings gains through research, investigations, and hidden sources. Good for studying or solving mysteries.",
            "ta": "புதன் 8-ம் இடத்தில் சஞ்சரிப்பதால் ஆராய்ச்சி, விசாரணைகள், மறைந்திருக்கும் மூலங்கள் மூலம் லாபம் கிடைக்கும். படிப்பு அல்லது புதிர்களை தீர்ப்பதற்கு நல்ல நேரம்."
        },
        "9": {
            "tendency": "unfavourable",
            "en": "Mercury in your 9th house may cause mental distress and obstacles in long-distance travel or higher education. Plans may face delays.",
            "ta": "புதன் 9-ம் இடத்தில் சஞ்சரிப்பதால் மன உளைச்சல், நீண்ட தூர பயணம் அல்லது உயர் கல்வியில் தடைகள் ஏற்படலாம். திட்டங்கள் தாமதமாகலாம்."
        },
        "10": {
            "tendency": "favourable",
            "en": "Mercury in your 10th house brings career success, intellectual recognition, and gains through communication. Professional networking thrives.",
            "ta": "புதன் 10-ம் இடத்தில் சஞ்சரிப்பதால் தொழில் வெற்றி, அறிவுசார் அங்கீகாரம், தகவல் பரிமாற்றம் மூலம் லாபம் கிடைக்கும். தொழில்முறை நெட்வொர்க்கிங் சிறக்கும்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Mercury in your 11th house brings financial gains, happiness, and success in all endeavors. Friendships and social connections are fruitful.",
            "ta": "புதன் 11-ம் இடத்தில் சஞ்சரிப்பதால் பண வரவு, மகிழ்ச்சி, எல்லா முயற்சிகளிலும் வெற்றி கிடைக்கும். நட்புகள் மற்றும் சமூக உறவுகள் பலன் தரும்."
        },
        "12": {
            "tendency": "unfavourable",
            "en": "Mercury in your 12th house may bring fear, financial loss, and communication obstacles. Guard against misunderstandings and signing errors.",
            "ta": "புதன் 12-ம் இடத்தில் சஞ்சரிப்பதால் பயம், பண இழப்பு, தகவல் பரிமாற்றத்தில் தடைகள் ஏற்படலாம். தவறான புரிதல்கள் மற்றும் கையொப்ப பிழைகளிலிருந்து எச்சரிக்கையாக இருங்கள்."
        }
    },
    "Jupiter": {
        "1": {
            "tendency": "unfavourable",
            "en": "Jupiter in your 1st house may cause displacement, unexpected expenses, and obstacles. A period requiring careful planning before action.",
            "ta": "குரு உங்கள் லக்னத்தில் சஞ்சரிப்பதால் இடப்பெயர்வு, எதிர்பாராத செலவுகள், தடைகள் ஏற்படலாம். செயலுக்கு முன் கவனமான திட்டமிடல் தேவைப்படும் காலம்."
        },
        "2": {
            "tendency": "favourable",
            "en": "Jupiter in your 2nd house brings wealth, family happiness, and eloquent speech. Financial matters prosper and domestic life is harmonious.",
            "ta": "குரு 2-ம் இடத்தில் சஞ்சரிப்பதால் செல்வம், குடும்ப மகிழ்ச்சி, சிறந்த பேச்சுத் திறன் கிடைக்கும். நிதி விஷயங்கள் செழிக்கும், குடும்ப வாழ்க்கை இணக்கமாக இருக்கும்."
        },
        "3": {
            "tendency": "unfavourable",
            "en": "Jupiter in your 3rd house may cause loss of position and obstacles in endeavors. Be cautious about committing to new responsibilities.",
            "ta": "குரு 3-ம் இடத்தில் சஞ்சரிப்பதால் பதவி இழப்பு, முயற்சிகளில் தடைகள் ஏற்படலாம். புதிய பொறுப்புகளை ஏற்றுக்கொள்வதில் கவனமாக இருங்கள்."
        },
        "4": {
            "tendency": "unfavourable",
            "en": "Jupiter in your 4th house may bring troubles in domestic life and loss of comfort. Relationships with close ones may feel strained.",
            "ta": "குரு 4-ம் இடத்தில் சஞ்சரிப்பதால் குடும்ப வாழ்க்கையில் சிக்கல்கள், சுகம் குறையலாம். நெருக்கமானவர்களுடனான உறவுகளில் அழுத்தம் உணரலாம்."
        },
        "5": {
            "tendency": "favourable",
            "en": "Jupiter in your 5th house brings blessings of children, wisdom, and success. Spiritual growth, creative fulfillment, and good fortune prevail.",
            "ta": "குரு 5-ம் இடத்தில் சஞ்சரிப்பதால் புத்திர பாக்கியம், ஞானம், வெற்றி கிடைக்கும். ஆன்மீக வளர்ச்சி, படைப்பு நிறைவு, நல்ல அதிர்ஷ்டம் நிலவும்."
        },
        "6": {
            "tendency": "unfavourable",
            "en": "Jupiter in your 6th house may increase enemies, cause health concerns, and bring obstacles. Stay vigilant against hidden opposition.",
            "ta": "குரு 6-ம் இடத்தில் சஞ்சரிப்பதால் எதிரிகள் அதிகரிக்கலாம், உடல்நலக் கவலை, தடைகள் ஏற்படலாம். மறைமுக எதிர்ப்பிலிருந்து விழிப்புடன் இருங்கள்."
        },
        "7": {
            "tendency": "favourable",
            "en": "Jupiter in your 7th house brings happiness in marriage, beneficial travels, and gains through partnerships. Relationships deepen with mutual respect.",
            "ta": "குரு 7-ம் இடத்தில் சஞ்சரிப்பதால் திருமண வாழ்க்கையில் மகிழ்ச்சி, பயனுள்ள பயணங்கள், கூட்டாண்மை மூலம் லாபம் கிடைக்கும். பரஸ்பர மரியாதையுடன் உறவுகள் ஆழமாகும்."
        },
        "8": {
            "tendency": "unfavourable",
            "en": "Jupiter in your 8th house may bring health issues, obstacles, and loss of resources. Avoid risky financial commitments during this period.",
            "ta": "குரு 8-ம் இடத்தில் சஞ்சரிப்பதால் உடல் பிரச்சனைகள், தடைகள், வளங்கள் குறையலாம். இந்தக் காலத்தில் ஆபத்தான நிதி முடிவுகளைத் தவிர்க்கவும்."
        },
        "9": {
            "tendency": "favourable",
            "en": "Jupiter in your 9th house brings great fortune, spiritual growth, and success in higher pursuits. A blessed period for dharma and learning.",
            "ta": "குரு 9-ம் இடத்தில் சஞ்சரிப்பதால் பெரும் பாக்கியம், ஆன்மீக வளர்ச்சி, உயர் முயற்சிகளில் வெற்றி கிடைக்கும். தர்மம் மற்றும் கல்விக்கு ஆசீர்வாதமான காலம்."
        },
        "10": {
            "tendency": "unfavourable",
            "en": "Jupiter in your 10th house may cause loss of professional status and obstacles in career. Maintain humility and avoid overcommitting.",
            "ta": "குரு 10-ம் இடத்தில் சஞ்சரிப்பதால் தொழில் நிலையில் இழப்பு, வேலையில் தடைகள் ஏற்படலாம். பணிவுடன் இருங்கள், அதிகமாக உறுதியளிப்பதைத் தவிர்க்கவும்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Jupiter in your 11th house brings abundant gains, vehicles, positions of honor, and happiness. One of the most auspicious transit positions.",
            "ta": "குரு 11-ம் இடத்தில் சஞ்சரிப்பதால் ஏராளமான லாபம், வாகனம், மரியாதையான பதவிகள், மகிழ்ச்சி கிடைக்கும். மிகவும் சுப நிலைகளில் ஒன்று."
        },
        "12": {
            "tendency": "unfavourable",
            "en": "Jupiter in your 12th house may bring increased expenditure, obstacles, and a sense of loss. Practice financial discipline and patience.",
            "ta": "குரு 12-ம் இடத்தில் சஞ்சரிப்பதால் செலவுகள் அதிகரிக்கும், தடைகள், இழப்பு உணர்வு ஏற்படலாம். நிதி ஒழுக்கமும் பொறுமையும் கடைப்பிடியுங்கள்."
        }
    },
    "Venus": {
        "1": {
            "tendency": "favourable",
            "en": "Venus in your 1st house brings luxuries, physical comforts, and pleasures. Appearance and charm are enhanced. A delightful period.",
            "ta": "சுக்கிரன் உங்கள் லக்னத்தில் சஞ்சரிப்பதால் ஆடம்பரங்கள், உடல் சுகங்கள், இன்பங்கள் கிடைக்கும். தோற்றமும் வசீகரமும் மேம்படும். மகிழ்ச்சியான காலம்."
        },
        "2": {
            "tendency": "favourable",
            "en": "Venus in your 2nd house brings financial gains, family happiness, and sweet speech. Artistic pursuits and social gatherings are rewarding.",
            "ta": "சுக்கிரன் 2-ம் இடத்தில் சஞ்சரிப்பதால் பண வரவு, குடும்ப மகிழ்ச்சி, இனிமையான பேச்சு கிடைக்கும். கலை முயற்சிகள் மற்றும் சமூக கூட்டங்கள் பலன் தரும்."
        },
        "3": {
            "tendency": "favourable",
            "en": "Venus in your 3rd house brings gains through communication, success, and positions of influence. Short travels are enjoyable and productive.",
            "ta": "சுக்கிரன் 3-ம் இடத்தில் சஞ்சரிப்பதால் தகவல் பரிமாற்றம் மூலம் லாபம், வெற்றி, செல்வாக்கு கிடைக்கும். குறுகிய பயணங்கள் மகிழ்ச்சியாகவும் பயனுள்ளதாகவும் இருக்கும்."
        },
        "4": {
            "tendency": "favourable",
            "en": "Venus in your 4th house brings domestic comfort, good friends, and happiness at home. Property-related matters are favourable.",
            "ta": "சுக்கிரன் 4-ம் இடத்தில் சஞ்சரிப்பதால் வீட்டு சுகம், நல்ல நண்பர்கள், இல்லத்தில் மகிழ்ச்சி கிடைக்கும். சொத்து தொடர்பான விஷயங்கள் சாதகமாக இருக்கும்."
        },
        "5": {
            "tendency": "favourable",
            "en": "Venus in your 5th house brings success in creative and romantic matters, respect from others, and joy from children.",
            "ta": "சுக்கிரன் 5-ம் இடத்தில் சஞ்சரிப்பதால் படைப்பு மற்றும் காதல் விஷயங்களில் வெற்றி, மற்றவர்களிடம் மரியாதை, குழந்தைகளால் மகிழ்ச்சி கிடைக்கும்."
        },
        "6": {
            "tendency": "unfavourable",
            "en": "Venus in your 6th house may bring obstacles from enemies, health concerns, and humiliation. Avoid overindulgence in pleasures.",
            "ta": "சுக்கிரன் 6-ம் இடத்தில் சஞ்சரிப்பதால் எதிரிகளால் தடைகள், உடல் நலக் கவலை, அவமானம் ஏற்படலாம். இன்பங்களில் அதிக ஈடுபாட்டைத் தவிர்க்கவும்."
        },
        "7": {
            "tendency": "unfavourable",
            "en": "Venus in your 7th house may cause quarrels with spouse, partnership troubles, and social embarrassment. Handle relationships diplomatically.",
            "ta": "சுக்கிரன் 7-ம் இடத்தில் சஞ்சரிப்பதால் வாழ்க்கைத் துணையுடன் சண்டை, கூட்டாண்மையில் சிக்கல், சமூக அவமானம் ஏற்படலாம். உறவுகளை இராஜதந்திரமாக கையாளுங்கள்."
        },
        "8": {
            "tendency": "favourable",
            "en": "Venus in your 8th house brings gains from unexpected sources, vehicles, and material comforts. Hidden opportunities reveal themselves.",
            "ta": "சுக்கிரன் 8-ம் இடத்தில் சஞ்சரிப்பதால் எதிர்பாராத மூலங்களிலிருந்து லாபம், வாகனம், பொருள் சுகங்கள் கிடைக்கும். மறைந்திருக்கும் வாய்ப்புகள் வெளிப்படும்."
        },
        "9": {
            "tendency": "favourable",
            "en": "Venus in your 9th house brings comforts, fortune, and spiritual fulfillment. Long-distance travel and cultural pursuits are highly rewarding.",
            "ta": "சுக்கிரன் 9-ம் இடத்தில் சஞ்சரிப்பதால் சுகங்கள், பாக்கியம், ஆன்மீக நிறைவு கிடைக்கும். நீண்ட தூர பயணம் மற்றும் கலாச்சார முயற்சிகள் மிகவும் பலன் தரும்."
        },
        "10": {
            "tendency": "unfavourable",
            "en": "Venus in your 10th house may cause quarrels at the workplace and obstacles in career progress. Maintain professionalism in all dealings.",
            "ta": "சுக்கிரன் 10-ம் இடத்தில் சஞ்சரிப்பதால் பணியிடத்தில் சண்டைகள், தொழில் முன்னேற்றத்தில் தடைகள் ஏற்படலாம். எல்லா விடயங்களிலும் தொழில்முறையைக் கடைப்பிடியுங்கள்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Venus in your 11th house brings gains, pleasures, and fulfillment of desires. Social life flourishes and financial prospects brighten.",
            "ta": "சுக்கிரன் 11-ம் இடத்தில் சஞ்சரிப்பதால் லாபம், இன்பங்கள், ஆசைகள் நிறைவேறும். சமூக வாழ்க்கை செழிக்கும், நிதி வாய்ப்புகள் பிரகாசமாகும்."
        },
        "12": {
            "tendency": "favourable",
            "en": "Venus in your 12th house brings comforts, luxuries, and pleasures of the bed. A good period for rest, rejuvenation, and spiritual pursuits.",
            "ta": "சுக்கிரன் 12-ம் இடத்தில் சஞ்சரிப்பதால் சுகங்கள், ஆடம்பரங்கள், படுக்கை இன்பங்கள் கிடைக்கும். ஓய்வு, புத்துணர்ச்சி, ஆன்மீக முயற்சிகளுக்கு நல்ல காலம்."
        }
    },
    "Saturn": {
        "1": {
            "tendency": "unfavourable",
            "en": "Saturn in your 1st house (Sade Sati peak phase) brings health challenges, loss, and displacement. Patience and perseverance are essential. Seek solace in spiritual practices.",
            "ta": "சனி உங்கள் லக்னத்தில் சஞ்சரிப்பதால் (சனிப்பெயர்ச்சி உச்சக்கட்டம்) உடல் நல சவால்கள், இழப்பு, இடப்பெயர்வு ஏற்படலாம். பொறுமையும் விடாமுயற்சியும் அவசியம். ஆன்மீகத்தில் ஆறுதல் தேடுங்கள்."
        },
        "2": {
            "tendency": "unfavourable",
            "en": "Saturn in your 2nd house (Sade Sati departing phase) may cause financial strain, family tensions, and speech-related issues. The difficult period is gradually easing.",
            "ta": "சனி 2-ம் இடத்தில் சஞ்சரிப்பதால் (சனிப்பெயர்ச்சி விடை பெறும் நிலை) நிதி நெருக்கடி, குடும்ப பதற்றம், பேச்சு தொடர்பான பிரச்சனைகள் ஏற்படலாம். கடினமான காலம் படிப்படியாக குறையும்."
        },
        "3": {
            "tendency": "favourable",
            "en": "Saturn in your 3rd house brings success, gains, victory over enemies, and improved health. One of Saturn's best transit positions — make the most of it.",
            "ta": "சனி 3-ம் இடத்தில் சஞ்சரிப்பதால் வெற்றி, லாபம், எதிரிகளை வெல்லும் ஆற்றல், உடல் ஆரோக்கியம் மேம்படும். சனியின் சிறந்த நிலைகளில் ஒன்று — இதை நன்றாகப் பயன்படுத்துங்கள்."
        },
        "4": {
            "tendency": "unfavourable",
            "en": "Saturn in your 4th house (Kantaka Sani) brings domestic troubles, mental unrest, and obstacles in property matters. A challenging but growth-building period.",
            "ta": "சனி 4-ம் இடத்தில் சஞ்சரிப்பதால் (கண்டக சனி) வீட்டில் சிக்கல்கள், மன அமைதியின்மை, சொத்து விஷயங்களில் தடைகள் ஏற்படலாம். சவாலான ஆனால் வளர்ச்சி தரும் காலம்."
        },
        "5": {
            "tendency": "unfavourable",
            "en": "Saturn in your 5th house may bring obstacles, losses, and worry about children. Speculative ventures should be strictly avoided.",
            "ta": "சனி 5-ம் இடத்தில் சஞ்சரிப்பதால் தடைகள், நஷ்டங்கள், குழந்தைகள் பற்றிய கவலை ஏற்படலாம். ஊக வணிகங்களை கண்டிப்பாகத் தவிர்க்கவும்."
        },
        "6": {
            "tendency": "favourable",
            "en": "Saturn in your 6th house brings victory over enemies, good health, and success in legal matters. A strong period for overcoming long-standing problems.",
            "ta": "சனி 6-ம் இடத்தில் சஞ்சரிப்பதால் எதிரிகளை வெல்லலாம், நல்ல ஆரோக்கியம், சட்ட விஷயங்களில் வெற்றி கிடைக்கும். நீண்டகால பிரச்சனைகளை கடக்க வலிமையான காலம்."
        },
        "7": {
            "tendency": "unfavourable",
            "en": "Saturn in your 7th house may bring travel fatigue, marital tensions, and difficulties in partnerships. Patience with your spouse and partners is key.",
            "ta": "சனி 7-ம் இடத்தில் சஞ்சரிப்பதால் பயணச் சோர்வு, திருமண உறவில் பதற்றம், கூட்டாண்மையில் சிரமங்கள் ஏற்படலாம். வாழ்க்கைத் துணை மற்றும் கூட்டாளிகளிடம் பொறுமை முக்கியம்."
        },
        "8": {
            "tendency": "unfavourable",
            "en": "Saturn in your 8th house (Ashtama Sani) is one of the most challenging transits — health issues, obstacles, and setbacks are likely. Focus on spiritual strength and preventive health care.",
            "ta": "சனி 8-ம் இடத்தில் சஞ்சரிப்பதால் (அஷ்டம சனி) மிகவும் சவாலான காலம் — உடல் நலப் பிரச்சனைகள், தடைகள், பின்னடைவுகள் ஏற்படலாம். ஆன்மீக பலத்திலும் தடுப்பு சுகாதாரத்திலும் கவனம் செலுத்துங்கள்."
        },
        "9": {
            "tendency": "unfavourable",
            "en": "Saturn in your 9th house may cause loss, obstacles in fortune, and displacement. Relationship with father or guru may be strained.",
            "ta": "சனி 9-ம் இடத்தில் சஞ்சரிப்பதால் நஷ்டம், பாக்கியத்தில் தடை, இடப்பெயர்வு ஏற்படலாம். தந்தை அல்லது குருவுடனான உறவில் பிரச்சனை வரலாம்."
        },
        "10": {
            "tendency": "unfavourable",
            "en": "Saturn in your 10th house may cause career obstacles, loss of professional status, and conflicts with authority. Maintain discipline and a low profile.",
            "ta": "சனி 10-ம் இடத்தில் சஞ்சரிப்பதால் தொழிலில் தடைகள், தொழில் நிலை இழப்பு, அதிகாரிகளுடன் மோதல் ஏற்படலாம். ஒழுக்கத்தையும் அடக்கத்தையும் கடைப்பிடியுங்கள்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Saturn in your 11th house brings financial gains, positions of honor, and success. One of Saturn's best transits — a period of well-deserved rewards.",
            "ta": "சனி 11-ம் இடத்தில் சஞ்சரிப்பதால் பண வரவு, மரியாதையான பதவிகள், வெற்றி கிடைக்கும். சனியின் சிறந்த நிலைகளில் ஒன்று — தகுதியான வெகுமதிகளின் காலம்."
        },
        "12": {
            "tendency": "unfavourable",
            "en": "Saturn in your 12th house (Sade Sati entering phase) brings increased expenditure, health concerns, and the beginning of a challenging period. Spiritual practices and financial caution are recommended.",
            "ta": "சனி 12-ம் இடத்தில் சஞ்சரிப்பதால் (சனிப்பெயர்ச்சி ஆரம்பம்) செலவுகள் அதிகரிக்கும், உடல் நலக் கவலை, சவாலான காலத்தின் தொடக்கம். ஆன்மீக பயிற்சிகள் மற்றும் நிதி கவனம் பரிந்துரைக்கப்படுகிறது."
        }
    },
    "Rahu": {
        "1": {
            "tendency": "unfavourable",
            "en": "Rahu in your 1st house may bring health anxiety, confusion, and a restless mind. Avoid deception and be wary of misleading people.",
            "ta": "ராகு உங்கள் லக்னத்தில் சஞ்சரிப்பதால் உடல் நலக் கவலை, குழப்பம், அமைதியற்ற மனம் ஏற்படலாம். ஏமாற்றங்களைத் தவிர்த்து, தவறான வழிகாட்டுபவர்களிடம் எச்சரிக்கையாக இருங்கள்."
        },
        "2": {
            "tendency": "unfavourable",
            "en": "Rahu in your 2nd house may cause financial loss, harsh or deceptive speech, and family discord. Guard your finances and relationships.",
            "ta": "ராகு 2-ம் இடத்தில் சஞ்சரிப்பதால் பண இழப்பு, கடுமையான அல்லது ஏமாற்றும் பேச்சு, குடும்ப முரண்பாடு ஏற்படலாம். உங்கள் நிதி மற்றும் உறவுகளைப் பாதுகாருங்கள்."
        },
        "3": {
            "tendency": "favourable",
            "en": "Rahu in your 3rd house brings gains, victory over adversaries, and increased courage. Communication skills are amplified to great effect.",
            "ta": "ராகு 3-ம் இடத்தில் சஞ்சரிப்பதால் லாபம், எதிரிகளை வெல்லும் ஆற்றல், தைரியம் அதிகரிக்கும். தகவல் பரிமாற்ற திறன் பெரிய அளவில் மேம்படும்."
        },
        "4": {
            "tendency": "unfavourable",
            "en": "Rahu in your 4th house may bring stomach troubles, mental unrest, and property-related anxieties. Domestic peace may be disturbed.",
            "ta": "ராகு 4-ம் இடத்தில் சஞ்சரிப்பதால் வயிற்றுப் பிரச்சனைகள், மன அமைதியின்மை, சொத்து தொடர்பான கவலைகள் ஏற்படலாம். வீட்டு அமைதி பாதிக்கப்படலாம்."
        },
        "5": {
            "tendency": "unfavourable",
            "en": "Rahu in your 5th house may cause losses in speculation, worry about children, and mental disturbance. Avoid gambling and risky investments.",
            "ta": "ராகு 5-ம் இடத்தில் சஞ்சரிப்பதால் ஊக வணிகத்தில் நஷ்டம், குழந்தைகள் பற்றிய கவலை, மன இடையூறு ஏற்படலாம். சூதாட்டம் மற்றும் ஆபத்தான முதலீடுகளைத் தவிர்க்கவும்."
        },
        "6": {
            "tendency": "favourable",
            "en": "Rahu in your 6th house brings victory over enemies, relief from illness, and success in competitive situations. A powerful period for overcoming adversity.",
            "ta": "ராகு 6-ம் இடத்தில் சஞ்சரிப்பதால் எதிரிகளை வெல்லலாம், நோய்களிலிருந்து நிவாரணம், போட்டிகளில் வெற்றி கிடைக்கும். எதிர்மறைகளை கடக்க சக்திவாய்ந்த காலம்."
        },
        "7": {
            "tendency": "unfavourable",
            "en": "Rahu in your 7th house may cause financial loss, marital issues, and deceptive partnerships. Verify claims from business associates carefully.",
            "ta": "ராகு 7-ம் இடத்தில் சஞ்சரிப்பதால் பண இழப்பு, திருமண பிரச்சனைகள், ஏமாற்றும் கூட்டாண்மை ஏற்படலாம். வணிகக் கூட்டாளிகளின் கூற்றுகளை கவனமாக சரிபார்க்கவும்."
        },
        "8": {
            "tendency": "unfavourable",
            "en": "Rahu in your 8th house may bring health risks, unexpected crises, and obstacles. Be extra cautious with health and safety measures.",
            "ta": "ராகு 8-ம் இடத்தில் சஞ்சரிப்பதால் உடல் நல ஆபத்துகள், எதிர்பாராத நெருக்கடிகள், தடைகள் ஏற்படலாம். ஆரோக்கியம் மற்றும் பாதுகாப்பு நடவடிக்கைகளில் மிகுந்த கவனம் தேவை."
        },
        "9": {
            "tendency": "unfavourable",
            "en": "Rahu in your 9th house may cause loss of fortune, mental distress, and obstacles in spiritual pursuits. Be cautious of false gurus or misleading advice.",
            "ta": "ராகு 9-ம் இடத்தில் சஞ்சரிப்பதால் பாக்கிய இழப்பு, மன உளைச்சல், ஆன்மீக முயற்சிகளில் தடைகள் ஏற்படலாம். போலி குருக்கள் அல்லது தவறான ஆலோசனைகளிடம் எச்சரிக்கையாக இருங்கள்."
        },
        "10": {
            "tendency": "favourable",
            "en": "Rahu in your 10th house brings career success, gains in profession, and recognition through unconventional means. A dynamic period for ambitious goals.",
            "ta": "ராகு 10-ம் இடத்தில் சஞ்சரிப்பதால் தொழில் வெற்றி, தொழிலில் லாபம், வழக்கத்திற்கு மாறான வழிகளில் அங்கீகாரம் கிடைக்கும். லட்சிய இலக்குகளுக்கு சக்திவாய்ந்த காலம்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Rahu in your 11th house brings financial prosperity, fulfillment of desires, and gains from foreign or unconventional sources. An auspicious transit.",
            "ta": "ராகு 11-ம் இடத்தில் சஞ்சரிப்பதால் நிதி வளம், ஆசைகள் நிறைவேறுதல், வெளிநாடு அல்லது வழக்கத்திற்கு மாறான மூலங்களிலிருந்து லாபம் கிடைக்கும். சுபமான நிலை."
        },
        "12": {
            "tendency": "unfavourable",
            "en": "Rahu in your 12th house may increase expenditure, cause anxiety and sleep disturbances. Foreign connections may bring mixed results.",
            "ta": "ராகு 12-ம் இடத்தில் சஞ்சரிப்பதால் செலவுகள் அதிகரிக்கும், கவலை மற்றும் தூக்கமின்மை ஏற்படலாம். வெளிநாட்டு தொடர்புகள் கலவையான முடிவுகளைத் தரலாம்."
        }
    },
    "Ketu": {
        "1": {
            "tendency": "unfavourable",
            "en": "Ketu in your 1st house may bring mental distress, health issues, and a feeling of detachment. Focus on spiritual growth to channel this energy positively.",
            "ta": "கேது உங்கள் லக்னத்தில் சஞ்சரிப்பதால் மன உளைச்சல், உடல் பிரச்சனைகள், பற்றின்மை உணர்வு ஏற்படலாம். இந்த சக்தியை நேர்மறையாக வழிநடத்த ஆன்மீக வளர்ச்சியில் கவனம் செலுத்துங்கள்."
        },
        "2": {
            "tendency": "unfavourable",
            "en": "Ketu in your 2nd house may cause financial loss, speech difficulties, and family misunderstandings. Be mindful of your words and finances.",
            "ta": "கேது 2-ம் இடத்தில் சஞ்சரிப்பதால் பண இழப்பு, பேச்சு சிரமங்கள், குடும்ப தவறான புரிதல்கள் ஏற்படலாம். உங்கள் வார்த்தைகளிலும் நிதியிலும் கவனமாக இருங்கள்."
        },
        "3": {
            "tendency": "favourable",
            "en": "Ketu in your 3rd house brings success, courage, and gains. Spiritual insights may lead to practical breakthroughs. A favourable transit.",
            "ta": "கேது 3-ம் இடத்தில் சஞ்சரிப்பதால் வெற்றி, தைரியம், லாபம் கிடைக்கும். ஆன்மீக உள்ளுணர்வுகள் நடைமுறை முன்னேற்றங்களுக்கு வழிவகுக்கும். சாதகமான நிலை."
        },
        "4": {
            "tendency": "unfavourable",
            "en": "Ketu in your 4th house may bring domestic disturbances, fears, and property-related worries. Inner peace may feel elusive.",
            "ta": "கேது 4-ம் இடத்தில் சஞ்சரிப்பதால் வீட்டில் இடையூறுகள், பயங்கள், சொத்து தொடர்பான கவலைகள் ஏற்படலாம். உள் அமைதி கிடைப்பது கடினமாக இருக்கலாம்."
        },
        "5": {
            "tendency": "unfavourable",
            "en": "Ketu in your 5th house may cause stomach issues, loss in investments, and worry about children. Avoid speculative activities.",
            "ta": "கேது 5-ம் இடத்தில் சஞ்சரிப்பதால் வயிற்றுப் பிரச்சனைகள், முதலீடுகளில் நஷ்டம், குழந்தைகள் பற்றிய கவலை ஏற்படலாம். ஊக செயல்பாடுகளைத் தவிர்க்கவும்."
        },
        "6": {
            "tendency": "favourable",
            "en": "Ketu in your 6th house brings victory over enemies, healing from illness, and success in spiritual practices. A protective and empowering transit.",
            "ta": "கேது 6-ம் இடத்தில் சஞ்சரிப்பதால் எதிரிகளை வெல்லலாம், நோய்களிலிருந்து குணமடையலாம், ஆன்மீக பயிற்சிகளில் வெற்றி கிடைக்கும். பாதுகாப்பான மற்றும் சக்தி தரும் நிலை."
        },
        "7": {
            "tendency": "unfavourable",
            "en": "Ketu in your 7th house may cause marital difficulties, humiliation, and fatigue. Relationships need extra care and understanding.",
            "ta": "கேது 7-ம் இடத்தில் சஞ்சரிப்பதால் திருமண சிரமங்கள், அவமானம், சோர்வு ஏற்படலாம். உறவுகளுக்கு கூடுதல் கவனமும் புரிதலும் தேவை."
        },
        "8": {
            "tendency": "unfavourable",
            "en": "Ketu in your 8th house may bring health risks, obstacles, and sudden setbacks. Spiritual practices offer the best protection during this transit.",
            "ta": "கேது 8-ம் இடத்தில் சஞ்சரிப்பதால் உடல்நல ஆபத்துகள், தடைகள், திடீர் பின்னடைவுகள் ஏற்படலாம். இந்த நிலையில் ஆன்மீக பயிற்சிகள் சிறந்த பாதுகாப்பை அளிக்கும்."
        },
        "9": {
            "tendency": "unfavourable",
            "en": "Ketu in your 9th house may obstruct fortune, cause conflicts with father or mentors, and disrupt spiritual progress. Stay grounded in your practices.",
            "ta": "கேது 9-ம் இடத்தில் சஞ்சரிப்பதால் பாக்கியத்தில் தடை, தந்தை அல்லது குருவுடன் மோதல், ஆன்மீக முன்னேற்றத்தில் இடையூறு ஏற்படலாம். உங்கள் பயிற்சிகளில் உறுதியாக இருங்கள்."
        },
        "10": {
            "tendency": "unfavourable",
            "en": "Ketu in your 10th house may cause obstacles in career, loss of status, and professional confusion. Avoid making major career changes impulsively.",
            "ta": "கேது 10-ம் இடத்தில் சஞ்சரிப்பதால் தொழிலில் தடைகள், நிலை இழப்பு, தொழில்முறை குழப்பம் ஏற்படலாம். பெரிய தொழில் மாற்றங்களை அவசரமாக எடுப்பதைத் தவிர்க்கவும்."
        },
        "11": {
            "tendency": "favourable",
            "en": "Ketu in your 11th house brings gains, success, and fulfillment. Spiritual wisdom translates into material benefits. A rewarding transit.",
            "ta": "கேது 11-ம் இடத்தில் சஞ்சரிப்பதால் லாபம், வெற்றி, நிறைவு கிடைக்கும். ஆன்மீக ஞானம் பொருள் நலன்களாக மாறும். பலன் தரும் நிலை."
        },
        "12": {
            "tendency": "unfavourable",
            "en": "Ketu in your 12th house may increase expenditure and cause losses. However, spiritual liberation and meditation practices can be deeply transformative.",
            "ta": "கேது 12-ம் இடத்தில் சஞ்சரிப்பதால் செலவுகள் அதிகரிக்கும், நஷ்டங்கள் ஏற்படலாம். ஆயினும், ஆன்மீக விடுதலை மற்றும் தியான பயிற்சிகள் ஆழமான மாற்றத்தை அளிக்கும்."
        }
    }
}

with open("/Users/shankarnarayanan/ASTRO/backend/interpretations.json", "w", encoding="utf-8") as f:
    json.dump(interpretations, f, indent=2, ensure_ascii=False)

total = sum(1 for planet in interpretations if planet != "_meta" for _ in interpretations[planet])
print(f"Generated {total} interpretation entries for {len([p for p in interpretations if p != '_meta'])} planets")
print("Saved to backend/interpretations.json")
