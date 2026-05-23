"""
Adds 'effect_en' and 'effect_ta' fields to each entry in interpretations.json.
These are short, planet-free effect descriptions used to compose the narrative.
"""
import json

effects = {
    "Sun": {
        "1": {"effect_en": "Health may need extra attention today, with possible fatigue and restlessness.", "effect_ta": "இன்று உடல் ஆரோக்கியத்தில் கூடுதல் கவனம் தேவை, சோர்வும் அமைதியின்மையும் ஏற்படலாம்."},
        "2": {"effect_en": "Financial caution is advised as unexpected expenses and family disagreements may surface.", "effect_ta": "எதிர்பாராத செலவுகளும் குடும்பத்தில் கருத்து வேறுபாடுகளும் வரலாம், நிதி விஷயங்களில் கவனம் தேவை."},
        "3": {"effect_en": "Courage and confidence are heightened, bringing victory in competitive situations.", "effect_ta": "தைரியமும் நம்பிக்கையும் அதிகரித்து, போட்டிகளில் வெற்றி கிடைக்கும்."},
        "4": {"effect_en": "Domestic peace may feel strained, with some mental unrest at home.", "effect_ta": "வீட்டில் அமைதி குறையலாம், மன அழுத்தம் ஏற்படலாம்."},
        "5": {"effect_en": "Creative projects may face delays, and decisions could feel harder than usual.", "effect_ta": "படைப்புத் திட்டங்களில் தாமதம் ஏற்படலாம், முடிவெடுப்பது சிரமமாக இருக்கலாம்."},
        "6": {"effect_en": "A strong day for overcoming obstacles and emerging victorious from challenges.", "effect_ta": "தடைகளை கடந்து சவால்களில் வெற்றி பெற சிறந்த நாள்."},
        "7": {"effect_en": "Partnerships and close relationships may need gentle handling today.", "effect_ta": "கூட்டாண்மை மற்றும் நெருக்கமான உறவுகளில் மென்மையான அணுகுமுறை தேவை."},
        "8": {"effect_en": "Patience is needed as obstacles and minor health issues may arise.", "effect_ta": "தடைகளும் சிறிய உடல் பிரச்சனைகளும் வரலாம், பொறுமை அவசியம்."},
        "9": {"effect_en": "Spiritual efforts may feel strained, and guidance from elders may be harder to receive.", "effect_ta": "ஆன்மீக முயற்சிகளில் சிரமம் ஏற்படலாம், பெரியவர்களின் வழிகாட்டுதல் தடைப்படலாம்."},
        "10": {"effect_en": "Professional ambitions receive a strong boost, with recognition from superiors.", "effect_ta": "தொழில் லட்சியங்களுக்கு வலுவான ஊக்கம் கிடைக்கும், மேலதிகாரிகளிடம் அங்கீகாரம் கிடைக்கும்."},
        "11": {"effect_en": "Financial gains and social connections flourish, bringing happiness and new opportunities.", "effect_ta": "பண வரவு அதிகரிக்கும், சமூக உறவுகள் வலுப்பெற்று மகிழ்ச்சியும் புதிய வாய்ப்புகளும் கிடைக்கும்."},
        "12": {"effect_en": "Expenditure may increase, and rest is more important than pushing forward.", "effect_ta": "செலவுகள் அதிகரிக்கலாம், முன்னேறுவதை விட ஓய்வு எடுப்பது நல்லது."}
    },
    "Moon": {
        "1": {"effect_en": "A pleasant day with comfort, good food, and a calm state of mind.", "effect_ta": "சுகமான நாள், நல்ல உணவு, அமைதியான மன நிலை கிடைக்கும்."},
        "2": {"effect_en": "A sense of dissatisfaction may linger — be mindful in conversations.", "effect_ta": "மனநிறைவின்மை உணர்வு இருக்கலாம், உரையாடல்களில் கவனமாக இருங்கள்."},
        "3": {"effect_en": "Efforts yield success, and communications go smoothly today.", "effect_ta": "முயற்சிகள் வெற்றி தரும், தகவல் பரிமாற்றங்கள் சிறப்பாக அமையும்."},
        "4": {"effect_en": "Anxiety and domestic worries may cloud the mind — avoid major decisions today.", "effect_ta": "கவலையும் வீட்டுக் கவலைகளும் மனதை மறைக்கலாம், இன்று பெரிய முடிவுகளைத் தவிர்க்கவும்."},
        "5": {"effect_en": "Plans may not unfold as expected, and stomach discomfort is possible.", "effect_ta": "திட்டங்கள் எதிர்பார்த்தபடி நடக்காமல் போகலாம், வயிற்று உபாதை வரலாம்."},
        "6": {"effect_en": "Good health and a strong sense of well-being prevail — tackle problems with confidence.", "effect_ta": "நல்ல ஆரோக்கியமும் நல்வாழ்வு உணர்வும் நிலவும், நம்பிக்கையுடன் பிரச்சனைகளை எதிர்கொள்ளுங்கள்."},
        "7": {"effect_en": "Relationships bring joy, and social interactions are warm and fulfilling.", "effect_ta": "உறவுகள் மகிழ்ச்சி தரும், சமூக தொடர்புகள் இனிமையாகவும் நிறைவாகவும் இருக்கும்."},
        "8": {"effect_en": "Emotional turbulence is possible — practice self-care and patience.", "effect_ta": "உணர்ச்சி கொந்தளிப்பு ஏற்படலாம், சுய பராமரிப்பும் பொறுமையும் கடைப்பிடியுங்கள்."},
        "9": {"effect_en": "The mind feels unsettled, and minor health niggles may distract you.", "effect_ta": "மனம் அமைதியின்றி இருக்கும், சிறிய உடல் பிரச்சனைகள் கவனத்தை சிதறடிக்கலாம்."},
        "10": {"effect_en": "A productive day with a sense of achievement and professional satisfaction.", "effect_ta": "சாதனை உணர்வும் தொழில்முறை திருப்தியும் கிடைக்கும், பயனுள்ள நாள்."},
        "11": {"effect_en": "Happiness flows naturally today — desires are fulfilled and friendships thrive.", "effect_ta": "இன்று இயல்பாகவே மகிழ்ச்சி வரும், ஆசைகள் நிறைவேறும், நட்புகள் செழிக்கும்."},
        "12": {"effect_en": "Spending may increase and sleep could be disrupted — a day for rest, not action.", "effect_ta": "செலவுகள் அதிகரிக்கலாம், தூக்கம் பாதிக்கப்படலாம், செயலுக்கு அல்ல ஓய்வுக்கான நாள்."}
    },
    "Mars": {
        "1": {"effect_en": "Temper may flare easily — channel your energy into physical exercise rather than confrontations.", "effect_ta": "கோபம் எளிதில் வரலாம், மோதல்களை விட உடற்பயிற்சியில் சக்தியைச் செலுத்துங்கள்."},
        "2": {"effect_en": "Guard your finances carefully and choose your words wisely in family matters.", "effect_ta": "நிதியைக் கவனமாகப் பாதுகாத்து, குடும்ப விஷயங்களில் வார்த்தைகளை கவனமாகத் தேர்ந்தெடுங்கள்."},
        "3": {"effect_en": "Bold action pays off today — courage is rewarded and competitors fall behind.", "effect_ta": "இன்று துணிச்சலான செயல்கள் பலன் தரும், தைரியத்திற்கு வெகுமதி கிடைக்கும்."},
        "4": {"effect_en": "Domestic harmony needs attention, and property matters may face complications.", "effect_ta": "வீட்டு அமைதியில் கவனம் தேவை, சொத்து விஷயங்களில் சிக்கல் வரலாம்."},
        "5": {"effect_en": "Avoid impulsive decisions, especially regarding investments or speculative ventures.", "effect_ta": "அவசர முடிவுகளைத் தவிர்க்கவும், குறிப்பாக முதலீடுகள் அல்லது ஊக வணிகங்களில்."},
        "6": {"effect_en": "Enemies and obstacles are overcome with commanding strength and determination.", "effect_ta": "ஆதிக்கமான வலிமையுடனும் உறுதியுடனும் எதிரிகளையும் தடைகளையும் வெல்லலாம்."},
        "7": {"effect_en": "Relationships with partners need patience — avoid unnecessary arguments.", "effect_ta": "கூட்டாளிகளுடன் உறவுகளில் பொறுமை தேவை, தேவையற்ற வாக்குவாதங்களைத் தவிர்க்கவும்."},
        "8": {"effect_en": "Exercise caution in travel and physical activities — accidents are more likely now.", "effect_ta": "பயணம் மற்றும் உடல் செயல்பாடுகளில் கவனம் தேவை, விபத்துகள் ஏற்படும் வாய்ப்பு அதிகம்."},
        "9": {"effect_en": "Legal matters and dealings with elders require extra care and diplomacy.", "effect_ta": "சட்ட விஷயங்களிலும் பெரியவர்களுடனான தொடர்புகளிலும் கூடுதல் கவனமும் இராஜதந்திரமும் தேவை."},
        "10": {"effect_en": "Career progress may face friction — protect your professional reputation carefully.", "effect_ta": "தொழில் முன்னேற்றத்தில் உராய்வு ஏற்படலாம், தொழில் நற்பெயரை கவனமாகக் காக்கவும்."},
        "11": {"effect_en": "Financial gains and property matters progress well — a rewarding period for bold ventures.", "effect_ta": "பண வரவும் சொத்து விஷயங்களும் நன்றாக முன்னேறும், துணிச்சலான முயற்சிகளுக்கு பலன் தரும் காலம்."},
        "12": {"effect_en": "Energy levels may dip — conserve your strength and avoid overexertion.", "effect_ta": "சக்தி குறையலாம், உங்கள் பலத்தைச் சேமித்து அதிக உழைப்பைத் தவிர்க்கவும்."}
    },
    "Mercury": {
        "1": {"effect_en": "Routine may feel disrupted, and new ventures are best postponed.", "effect_ta": "வழக்கமான பணிகளில் இடையூறு ஏற்படலாம், புதிய முயற்சிகளை தள்ளி வைப்பது நல்லது."},
        "2": {"effect_en": "Communication skills shine, bringing financial gains and success in learning.", "effect_ta": "தகவல் பரிமாற்றத் திறன் மிளிரும், பண வரவும் கல்வியில் வெற்றியும் கிடைக்கும்."},
        "3": {"effect_en": "Double-check important messages — miscommunications are likely today.", "effect_ta": "முக்கிய செய்திகளை இருமுறை சரிபார்க்கவும், தவறான தொடர்புகள் வர வாய்ப்புள்ளது."},
        "4": {"effect_en": "Intellectual pursuits and education bring rewards — a good day for focused study.", "effect_ta": "அறிவுசார் முயற்சிகளும் கல்வியும் பலன் தரும், கவனமான படிப்புக்கு நல்ல நாள்."},
        "5": {"effect_en": "Family tensions may arise — stay calm and avoid heated discussions.", "effect_ta": "குடும்ப பதற்றம் ஏற்படலாம், அமைதியாக இருந்து வாதங்களைத் தவிர்க்கவும்."},
        "6": {"effect_en": "Problems find clever solutions today — competitive situations favour the well-prepared.", "effect_ta": "இன்று பிரச்சனைகளுக்கு புத்திசாலித்தனமான தீர்வுகள் கிடைக்கும், நன்கு தயாரானவர்களுக்கு போட்டிகள் சாதகமாக அமையும்."},
        "7": {"effect_en": "Be precise in agreements and contracts — misunderstandings can be costly.", "effect_ta": "ஒப்பந்தங்களிலும் உடன்படிக்கைகளிலும் துல்லியமாக இருங்கள், தவறான புரிதல்கள் விலை கொடுக்கலாம்."},
        "8": {"effect_en": "Research and investigation yield hidden gains — dig deeper for answers.", "effect_ta": "ஆராய்ச்சியும் விசாரணையும் மறைந்திருக்கும் லாபங்களைத் தரும், பதில்களுக்கு ஆழமாகத் தேடுங்கள்."},
        "9": {"effect_en": "Long-distance plans may face delays — patience with travel arrangements is needed.", "effect_ta": "நீண்ட தூர திட்டங்கள் தாமதமாகலாம், பயண ஏற்பாடுகளில் பொறுமை தேவை."},
        "10": {"effect_en": "Professional networking thrives — career gains come through smart communication.", "effect_ta": "தொழில்முறை நெட்வொர்க்கிங் சிறக்கும், புத்திசாலித்தனமான தொடர்பு மூலம் தொழில் முன்னேற்றம் கிடைக்கும்."},
        "11": {"effect_en": "All endeavors succeed, friendships flourish, and happiness comes easily.", "effect_ta": "எல்லா முயற்சிகளும் வெற்றி பெறும், நட்புகள் செழிக்கும், மகிழ்ச்சி எளிதில் வரும்."},
        "12": {"effect_en": "Guard against signing errors and misunderstandings in written communication.", "effect_ta": "கையொப்ப பிழைகளிலிருந்தும் எழுத்துத் தொடர்பில் தவறான புரிதல்களிலிருந்தும் எச்சரிக்கையாக இருங்கள்."}
    },
    "Jupiter": {
        "1": {"effect_en": "Unexpected changes may disrupt plans — careful planning before action is wise.", "effect_ta": "எதிர்பாராத மாற்றங்கள் திட்டங்களை குழப்பலாம், செயலுக்கு முன் கவனமான திட்டமிடல் புத்திசாலித்தனம்."},
        "2": {"effect_en": "Family life is harmonious and finances prosper — a blessed period for domestic matters.", "effect_ta": "குடும்ப வாழ்க்கை இணக்கமாகவும் நிதி செழிப்பாகவும் இருக்கும், குடும்ப விஷயங்களுக்கு ஆசீர்வாதமான காலம்."},
        "3": {"effect_en": "Be cautious about committing to new responsibilities — overextension is likely.", "effect_ta": "புதிய பொறுப்புகளை ஏற்பதில் கவனமாக இருங்கள், அதிக சுமை ஏற்படலாம்."},
        "4": {"effect_en": "Close relationships may feel strained — nurture them with extra care.", "effect_ta": "நெருக்கமான உறவுகளில் அழுத்தம் உணரலாம், கூடுதல் கவனத்துடன் பேணுங்கள்."},
        "5": {"effect_en": "Wisdom deepens and creative fulfillment arrives — a spiritually enriching period.", "effect_ta": "ஞானம் ஆழமாகும், படைப்பு நிறைவு கிடைக்கும், ஆன்மீகமாக வளமான காலம்."},
        "6": {"effect_en": "Hidden opposition may surface — stay vigilant and trust your instincts.", "effect_ta": "மறைமுக எதிர்ப்பு வெளிப்படலாம், விழிப்புடன் இருந்து உங்கள் உள்ளுணர்வை நம்புங்கள்."},
        "7": {"effect_en": "Partnerships deepen with mutual respect, and beneficial travels are indicated.", "effect_ta": "பரஸ்பர மரியாதையுடன் கூட்டாண்மை ஆழமாகும், பயனுள்ள பயணங்கள் அமையும்."},
        "8": {"effect_en": "Risky financial commitments should be avoided — protect your resources.", "effect_ta": "ஆபத்தான நிதி முடிவுகளைத் தவிர்க்கவும், உங்கள் வளங்களைப் பாதுகாருங்கள்."},
        "9": {"effect_en": "Fortune smiles brightly — higher learning, dharma, and spiritual growth are all favoured.", "effect_ta": "அதிர்ஷ்டம் பிரகாசமாக புன்னகைக்கும், உயர் கல்வி, தர்மம், ஆன்மீக வளர்ச்சி அனைத்தும் சாதகமாக இருக்கும்."},
        "10": {"effect_en": "Maintain humility at work — career progress may temporarily slow.", "effect_ta": "பணியிடத்தில் பணிவுடன் இருங்கள், தொழில் முன்னேற்றம் தற்காலிகமாக குறையலாம்."},
        "11": {"effect_en": "One of the most auspicious periods — abundant gains, honors, and deep happiness arrive.", "effect_ta": "மிகவும் சுபமான காலம், ஏராளமான லாபம், மரியாதை, ஆழமான மகிழ்ச்சி கிடைக்கும்."},
        "12": {"effect_en": "Financial discipline is essential as expenditure tends to rise unexpectedly.", "effect_ta": "செலவுகள் எதிர்பாராமல் அதிகரிக்கும் என்பதால் நிதி ஒழுக்கம் அவசியம்."}
    },
    "Venus": {
        "1": {"effect_en": "Charm and attractiveness are enhanced — a delightful day for enjoyment and self-expression.", "effect_ta": "வசீகரமும் அழகும் மேம்படும், இன்பம் மற்றும் சுய வெளிப்பாட்டிற்கு மகிழ்ச்சியான நாள்."},
        "2": {"effect_en": "Sweet speech wins hearts, and artistic or social gatherings bring joy.", "effect_ta": "இனிமையான பேச்சு இதயங்களை வெல்லும், கலை அல்லது சமூக கூட்டங்கள் மகிழ்ச்சி தரும்."},
        "3": {"effect_en": "Influence grows through communication, and short journeys are productive.", "effect_ta": "தகவல் பரிமாற்றம் மூலம் செல்வாக்கு வளரும், குறுகிய பயணங்கள் பயனுள்ளதாக இருக்கும்."},
        "4": {"effect_en": "Home life is comfortable and friendships are warm — a nurturing day.", "effect_ta": "வீட்டு வாழ்க்கை சுகமாகவும் நட்புகள் அன்பாகவும் இருக்கும், அரவணைக்கும் நாள்."},
        "5": {"effect_en": "Romance, creativity, and respect from others all flow beautifully today.", "effect_ta": "காதல், படைப்பாற்றல், மற்றவர்களிடம் மரியாதை அனைத்தும் இன்று அழகாக வரும்."},
        "6": {"effect_en": "Overindulgence should be avoided — rivals may try to undermine your position.", "effect_ta": "அதிக ஈடுபாட்டைத் தவிர்க்கவும், போட்டியாளர்கள் உங்கள் நிலையை குலைக்க முயற்சிக்கலாம்."},
        "7": {"effect_en": "Diplomacy is essential in close relationships — handle disagreements gently.", "effect_ta": "நெருக்கமான உறவுகளில் இராஜதந்திரம் அவசியம், கருத்து வேறுபாடுகளை மென்மையாக கையாளுங்கள்."},
        "8": {"effect_en": "Hidden opportunities reveal themselves — unexpected gains from surprising sources.", "effect_ta": "மறைந்திருக்கும் வாய்ப்புகள் வெளிப்படும், ஆச்சரியமான மூலங்களிலிருந்து எதிர்பாராத லாபம் கிடைக்கும்."},
        "9": {"effect_en": "Cultural pursuits and long journeys are deeply rewarding and spiritually fulfilling.", "effect_ta": "கலாச்சார முயற்சிகளும் நீண்ட பயணங்களும் ஆழமான பலனையும் ஆன்மீக நிறைவையும் தரும்."},
        "10": {"effect_en": "Workplace dynamics require professionalism — avoid mixing personal and work matters.", "effect_ta": "பணியிட நிலைகளுக்கு தொழில்முறை தேவை, தனிப்பட்ட மற்றும் பணி விஷயங்களை கலக்க வேண்டாம்."},
        "11": {"effect_en": "Pleasures, gains, and social life all flourish — desires find their fulfillment.", "effect_ta": "இன்பங்கள், லாபம், சமூக வாழ்க்கை அனைத்தும் செழிக்கும், ஆசைகள் நிறைவேறும்."},
        "12": {"effect_en": "Rest and rejuvenation are deeply satisfying — a good day for quiet pleasures.", "effect_ta": "ஓய்வும் புத்துணர்ச்சியும் ஆழமான திருப்தி தரும், அமைதியான இன்பங்களுக்கு நல்ல நாள்."}
    },
    "Saturn": {
        "1": {"effect_en": "A demanding period requiring perseverance — health and spirits may feel low, but inner strength grows.", "effect_ta": "விடாமுயற்சி தேவைப்படும் காலம், உடல்நலமும் மனவலிமையும் குறையலாம், ஆனால் உள்ளார்ந்த வலிமை வளரும்."},
        "2": {"effect_en": "Financial pressure and family tensions ease gradually — the worst is behind you.", "effect_ta": "நிதி அழுத்தமும் குடும்ப பதற்றமும் படிப்படியாகக் குறையும், மோசமான காலம் கடந்து விட்டது."},
        "3": {"effect_en": "Hard work bears fruit — success, gains, and improved health reward your persistence.", "effect_ta": "கடின உழைப்பு பலன் தரும், வெற்றி, லாபம், மேம்பட்ட ஆரோக்கியம் உங்கள் விடாமுயற்சிக்கு வெகுமதி."},
        "4": {"effect_en": "Domestic challenges test your patience, but growth comes through enduring them.", "effect_ta": "வீட்டுச் சவால்கள் உங்கள் பொறுமையை சோதிக்கும், ஆனால் அவற்றை தாங்குவதன் மூலம் வளர்ச்சி வரும்."},
        "5": {"effect_en": "Speculative ventures carry high risk — conservative choices protect what you have.", "effect_ta": "ஊக வணிகங்கள் அதிக ஆபத்து கொண்டவை, பழமையான தேர்வுகள் உங்களிடம் உள்ளதைப் பாதுகாக்கும்."},
        "6": {"effect_en": "Long-standing problems finally yield — perseverance in legal and health matters pays off.", "effect_ta": "நீண்டகால பிரச்சனைகள் இறுதியாக விடுபடும், சட்ட மற்றும் சுகாதார விஷயங்களில் விடாமுயற்சி பலன் தரும்."},
        "7": {"effect_en": "Travel may be tiring, and patience with your partner is especially important now.", "effect_ta": "பயணம் சோர்வாக இருக்கலாம், இப்போது உங்கள் துணையிடம் பொறுமை மிக முக்கியம்."},
        "8": {"effect_en": "One of the most challenging periods — focus on preventive health and spiritual strength.", "effect_ta": "மிகவும் சவாலான காலம், தடுப்பு சுகாதாரம் மற்றும் ஆன்மீக வலிமையில் கவனம் செலுத்துங்கள்."},
        "9": {"effect_en": "Fortune feels elusive, and relationships with mentors may be strained.", "effect_ta": "அதிர்ஷ்டம் பிடிபடாமல் இருக்கும், குருவுடனான உறவுகளில் அழுத்தம் இருக்கலாம்."},
        "10": {"effect_en": "Career requires discipline and a low profile — avoid conflicts with authority.", "effect_ta": "தொழிலுக்கு ஒழுக்கமும் அடக்கமும் தேவை, அதிகாரிகளுடன் மோதல்களைத் தவிர்க்கவும்."},
        "11": {"effect_en": "Well-deserved rewards arrive — financial gains and positions of honour come to the disciplined.", "effect_ta": "தகுதியான வெகுமதிகள் வரும், ஒழுக்கமானவர்களுக்கு பண வரவும் மரியாதையான பதவிகளும் கிடைக்கும்."},
        "12": {"effect_en": "A testing period begins — increased expenses and health vigilance are needed.", "effect_ta": "சோதனைக் காலம் தொடங்குகிறது, அதிகரிக்கும் செலவுகளும் ஆரோக்கிய விழிப்பும் தேவை."}
    },
    "Rahu": {
        "1": {"effect_en": "Confusion and restlessness may cloud judgment — be wary of misleading influences.", "effect_ta": "குழப்பமும் அமைதியின்மையும் தீர்ப்பை மறைக்கலாம், தவறான செல்வாக்குகளிடம் எச்சரிக்கையாக இருங்கள்."},
        "2": {"effect_en": "Watch for financial deception and guard your resources carefully.", "effect_ta": "நிதி ஏமாற்றத்தைக் கவனியுங்கள், உங்கள் வளங்களை கவனமாகப் பாதுகாருங்கள்."},
        "3": {"effect_en": "Communication skills are amplified — use them boldly for impressive results.", "effect_ta": "தகவல் பரிமாற்ற திறன் அதிகரிக்கும், அசத்தலான முடிவுகளுக்கு அவற்றை துணிச்சலாகப் பயன்படுத்துங்கள்."},
        "4": {"effect_en": "Inner peace may feel elusive as anxieties about home and property surface.", "effect_ta": "வீடு மற்றும் சொத்து பற்றிய கவலைகள் வெளிப்படுவதால் உள் அமைதி கிடைப்பது கடினமாக இருக்கலாம்."},
        "5": {"effect_en": "Avoid gambling and risky investments — losses in speculation are likely.", "effect_ta": "சூதாட்டம் மற்றும் ஆபத்தான முதலீடுகளைத் தவிர்க்கவும், ஊகத்தில் நஷ்டம் வரலாம்."},
        "6": {"effect_en": "A powerful period for overcoming adversaries — obstacles crumble before your resolve.", "effect_ta": "எதிரிகளை வெல்ல சக்திவாய்ந்த காலம், உங்கள் உறுதியின் முன் தடைகள் உடையும்."},
        "7": {"effect_en": "Verify claims from business associates — not everything presented is genuine.", "effect_ta": "வணிகக் கூட்டாளிகளின் கூற்றுகளை சரிபார்க்கவும், முன்வைக்கப்படுவது அனைத்தும் உண்மையல்ல."},
        "8": {"effect_en": "Extra caution with health and safety is non-negotiable during this period.", "effect_ta": "இந்தக் காலத்தில் ஆரோக்கியம் மற்றும் பாதுகாப்பில் கூடுதல் கவனம் விட்டுக்கொடுக்க முடியாதது."},
        "9": {"effect_en": "Be cautious of false guidance — not all advice you receive is trustworthy.", "effect_ta": "தவறான வழிகாட்டுதலில் எச்சரிக்கையாக இருங்கள், நீங்கள் பெறும் அனைத்து ஆலோசனைகளும் நம்பகமானவை அல்ல."},
        "10": {"effect_en": "Unconventional approaches to career bring surprising success and recognition.", "effect_ta": "தொழிலில் வழக்கத்திற்கு மாறான அணுகுமுறைகள் ஆச்சரியமான வெற்றியையும் அங்கீகாரத்தையும் தரும்."},
        "11": {"effect_en": "Prosperity flows from unexpected and unconventional sources — an auspicious period.", "effect_ta": "எதிர்பாராத மற்றும் வழக்கத்திற்கு மாறான மூலங்களிலிருந்து வளம் வரும், சுபமான காலம்."},
        "12": {"effect_en": "Anxiety and sleep disturbances may increase — calming routines are essential.", "effect_ta": "கவலையும் தூக்கமின்மையும் அதிகரிக்கலாம், அமைதியான வழக்கங்கள் அவசியம்."}
    },
    "Ketu": {
        "1": {"effect_en": "A sense of detachment pervades — channel it towards spiritual growth rather than withdrawal.", "effect_ta": "பற்றின்மை உணர்வு நிலவும், விலகுவதை விட ஆன்மீக வளர்ச்சிக்கு அதை வழிநடத்துங்கள்."},
        "2": {"effect_en": "Be mindful of your words and finances — both need careful handling today.", "effect_ta": "உங்கள் வார்த்தைகளிலும் நிதியிலும் கவனமாக இருங்கள், இரண்டும் இன்று கவனமான கையாளுதல் தேவை."},
        "3": {"effect_en": "Spiritual insights translate into practical breakthroughs — trust your intuition.", "effect_ta": "ஆன்மீக உள்ளுணர்வுகள் நடைமுறை முன்னேற்றங்களாக மாறும், உங்கள் உள்ளுணர்வை நம்புங்கள்."},
        "4": {"effect_en": "Inner peace feels distant as domestic worries and unnamed fears arise.", "effect_ta": "வீட்டுக் கவலைகளும் பெயரிடப்படாத பயங்களும் எழுவதால் உள் அமைதி தூரமாக இருக்கும்."},
        "5": {"effect_en": "Stomach health needs attention, and investments should be approached conservatively.", "effect_ta": "வயிற்று ஆரோக்கியத்தில் கவனம் தேவை, முதலீடுகளை பழமையான முறையில் அணுகவும்."},
        "6": {"effect_en": "Healing and victory over old enemies come naturally — a protective and empowering time.", "effect_ta": "பழைய எதிரிகளை வெல்வதும் குணமடைவதும் இயல்பாக வரும், பாதுகாப்பான மற்றும் சக்தி தரும் நேரம்."},
        "7": {"effect_en": "Relationships need extra understanding — avoid taking your partner for granted.", "effect_ta": "உறவுகளுக்கு கூடுதல் புரிதல் தேவை, உங்கள் துணையை சாதாரணமாக எடுப்பதைத் தவிர்க்கவும்."},
        "8": {"effect_en": "Sudden setbacks are possible — spiritual practices offer the best shield.", "effect_ta": "திடீர் பின்னடைவுகள் வரலாம், ஆன்மீக பயிற்சிகள் சிறந்த கவசத்தை அளிக்கும்."},
        "9": {"effect_en": "Stay grounded in your principles — conflicting advice may cause confusion.", "effect_ta": "உங்கள் கொள்கைகளில் உறுதியாக இருங்கள், முரண்பட்ட ஆலோசனைகள் குழப்பத்தை ஏற்படுத்தலாம்."},
        "10": {"effect_en": "Avoid impulsive career changes — clarity will come with time, not haste.", "effect_ta": "அவசர தொழில் மாற்றங்களைத் தவிர்க்கவும், தெளிவு அவசரத்தால் அல்ல, நேரத்தால் வரும்."},
        "11": {"effect_en": "Spiritual wisdom translates into material benefits — a quietly rewarding period.", "effect_ta": "ஆன்மீக ஞானம் பொருள் நலன்களாக மாறும், அமைதியாக பலன் தரும் காலம்."},
        "12": {"effect_en": "Though expenses rise, meditation and inner work can be deeply transformative now.", "effect_ta": "செலவுகள் அதிகரித்தாலும், தியானமும் உள்வேலையும் இப்போது ஆழமான மாற்றத்தை அளிக்கும்."}
    }
}

# Load existing interpretations and merge
with open("/Users/shankarnarayanan/ASTRO/backend/interpretations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for planet, houses in effects.items():
    for house, eff in houses.items():
        if planet in data and house in data[planet]:
            data[planet][house]["effect_en"] = eff["effect_en"]
            data[planet][house]["effect_ta"] = eff["effect_ta"]

with open("/Users/shankarnarayanan/ASTRO/backend/interpretations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

count = sum(1 for p in effects for h in effects[p])
print(f"Added {count} effect entries to interpretations.json")
