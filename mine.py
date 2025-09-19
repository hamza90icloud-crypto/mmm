# -*- coding: utf-8 -*-
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
import json
import os
import random
from datetime import datetime

# بيانات الأسئلة القرآنية مع الفئات
categories = {
    1: {
        "name": "حزب الأعلى",
        "questions": [
            "سَبِّحِ اسْمَ رَبِّكَ الْأَعْلَى",
            "أَفَلَا يَنظُرُونَ إِلَى الْإِبِلِ كَيْفَ خُلِقَتْ", 
            "لَا أُقْسِمُ بِهَٰذَا الْبَلَدِ",
            "وَاللَّيْلِ إِذَا يَغْشَىٰ", 
            "أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ",
            "إِنَّا أَنزَلْنَاهُ فِي لَيْلَةِ الْقَدْرِ", 
            "يَوْمَئِذٍ يَصْدُرُ النَّاسُ أَشْتَاتًا",
            "أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَابِ الْفِيلِ"
        ]
    },
    2: {
        "name": "حزب النبأ",
        "questions": [
            "إِنَّ بَطْشَ رَبِّكَ لَشَدِيدٌ",
            "فَلَا أُقْسِمُ بِالشَّفَقِ", 
            "كَلَّا إِنَّ كِتَابَ الْفُجَّارِ",
            "فَلَا أُقْسِمُ بِالْخُنَّسِ",
            "فَإِذَا جَاءَتِ الصَّاخَّةُ", 
            "يَسْأَلُونَكَ عَنِ السَّاعَةِ",
            "وَالنَّازِعَاتِ غَرْقًا", 
            "عَمَّ يَتَسَاءَلُونَ"
        ]
    },
    3: {
        "name": "حزب الجن",
        "questions": [
            "بداية سورة الجن",
            "وأن المسـٰجد لله", 
            "إن ربك يعلم انك",
            "وما جعلنا أصحـٰب النار",
            "بداية سورة القيـٰمة",
            "بداية سورة الإنسان",
            "ويطوف عليهم ولدان مخلدون",
            " ألم نهلك الاولين"
        ]
    },
    4: {
        "name": "حزب الملك",
        "questions": [
            "بداية سورة الملك",
            "أولم يرواْ إلى الطير فوقهم", 
            "فطاف عليها طآئف من ربك",
            "بداية سورة الحآقة",
            "فلا أُقسم بما تبصرون", 
            "إن الإنسان خلق هلوعاً",
            "فلا أُقسم برب المشارق والمغارب", 
            "ألم ترواْ كيف خلق الله سبع"
        ]
    },
    5: {
        "name": "حزب الجمعة",
        "questions": [
            "بداية سورة الجمعة",
            "يـٰأيها الذين ءامنوا إذا نودىَ", 
            "يـٰأيها الذين ءامنوا لا تلهكم",
            "زعم الذين كفروا ان لن يبعثوا",
            "يـٰأيها الذين ءامنوا إن من ازواجكم", 
            "أسكنوهن من حيث سكنتم",
            "الله الذي خلق سبع سمـٰوٰت", 
            "يـٰأيها الذين ءامنوا توبوا إلى الله"
        ]
    },
    6: {
        "name":"حزب المجادلة",
        "questions": [
            "بداية سورة المجادلة",
            "ألم تر إلى الذين نهوا عن النجوىٰ", 
            "ألم تر إلى الذين تولوا",
            "بداية سورة الحشر",
            "ألم تر إلى الذين نافقوا", 
            "بداية سورة الممتحنة",
            "عسى الله ان يجعل بينكم", 
            "بداية سورة الصف"
        ]
    },
    7: {
        "name":"حزب الرحمـٰن",
        "questions": [
            "بداية سورة الرحمـٰن",
            "يٰمعشر الجن والإنس ", 
            "هل جزآء الإحسان إلا الإحسان",
            "وأصحـٰب اليمين ما أصحٰب اليمين",
            "فلا أُقسم بمواقع النجوم", 
            "ءامنوا بالله ورسوله",
            "ألم يأْن للذين ءامنوا", 
            "ما أصاب من مصيبة في الأرض"
        ]
    },
    8:{
        "name":"حزب قال فما خطبكم",
        "questions": [
            "قال فما خطبكم ايهاالمرسلون",
            "وما خلقت الجن والإنس ", 
            "ويطوف عليهم غلمان لهم"
            "وإن يرواْ كسفا من السمآء ساقطاً",
            "وكم من ملك في السمـٰوٰت", 
            "هٰذا نذير من النذر الأُولى",
            "كذبت عاد فكيف كان عذابي ونذر", 
            "ولقد جا ءال فرعون النذر"
        ]
    },
    9: {
        "name":"حزب لقد رضىَ الله",
        "questions": [
            "لقد رضىَ الله عن المؤمنين",
            "لقد صدق الله رسوله الرءيا ", 
            "بداية سورة الحجرٰت",
            "وإن طآئفتان من المؤمنين اقتتلوا",
            "قالت الأعراب ءامنا", 
            "أفلم ينظروا إلى السمآء فوقهم",
            "أقال قرينه ربنا ما أطغيته", 
            "بداية سورة الذٰريـٰت"
        ]
    }, 
    
    10:{
        "name":"حزب الأحقاف",
        "questions": [
            "بداية سورة الأحقاف",
            "ووصينا الإنسان بوالديه حسناً ", 
            "واذكر أخا عاد اذ أنذر قومه"
            "أولم يرواْ أن الله الذي خلق السمـٰوٰت والأرض",
            "أفلم يسيرو في الأرض فينظروا كيف كان", 
            "ويقول الذين ءامنوا لولا نزلت سورة",
            "يـٰأيها الذين ءامنوا اطيعوا الله ", 
            "إناأرسلنـٰك شاهداً ومبشراً ونذيراً"
        ]
    }, 
   
    11:{
        "name":"حزب قل أولوْ جئتكم",
        "questions": [
            "قل أولوْ جئتكم بأهدىٰ",
            "فاستمسك بالذي أُوحىَ إليك ", 
            "ولما جآء عيسى بالبينـٰت"
            "وهو الذي في السمآ• إلٰه",
            "كم تركوا من جنـٰت وعيون", 
            "إن المتقين في مقام أمين",
            "هـٰذا هدىً ", 
            "أفرايت من اتخذ إلٰهه هواه"
        ]
    }, 
    
    12:{
        "name":"حزب إليه يرد",
        "questions": [
            "إليه يرد علم الساعة",
            "بداية سورة الشورىٰ ", 
            "شرع لكم من الدين "
            "أم لهم شركـٰٓؤا شرعوا لهم من الدين",
            "أو يوبقهمن بما كسبوا", 
            "ولمن صبر وغفر",
            "وما كان لبشر أن يكلمه الله ", 
            "والذي خلق الأزواج كلها"
        ]
    }, 
    
    13:{
        "name":"حزب ويـٰقوم مالىَ أدعولكم",
        "questions": [
            "ويـٰقوم مالىَ أدعوكم إلى الى النجوٰة",
            "ولقد ءاتينا موسى الهدى ", 
            "قل إني نهيت أن أعبد"
            "الله الذي جعل لكم الأنعام ",
            "قل أٰىنكم لتكفرون بالذي خلق الأرض", 
            "وأما ثمود فهدينـٰهم",
            "وقال الذين كفرو لا تسمعوا لهٰذا القرءان ", 
            "فإن استكبروا فالذين عند ربك"
        ]
    }, 
    
    14:{
        "name":"حزب فمن أظلم ",
        "questions": [
            "فمن أظلم ممن كذب على الله",
            "أم اتخذوا من دون الله شفعآء ", 
            "قل يـٰعبادىَ الذين أسرفوا "
            "وما قدروا الله حق قدره",
            "بداية سورة غافر", 
            "إن الذين كفروا ينادون",
            "أولم يسيروا في الأرض فينظروا", 
            "وقال الذي ءامن يـٰقوم إنى "
        ]
    }, 
    
    15:{
        "name":"حزب فنبذنٰه بالعرآء",
        "questions": [
            "فنبذنٰه بالعرآء وهو سقيم",
            "بداية سورة صٓ ", 
            "وهل أتىٰك نبؤا الخصم"
            "ووهبنا لداوود سليمـٰن",
            "وعندهم قـٰصرٰت الطرف أتراب", 
            "قال فالحق والحق أقول",
            "وإذا مس الإنسان ضر دعا ربه ", 
            "أفمن حق عليه كلمة العذاب"
        ]
    }, 
   
    16:{
        "name":"حزب وما أنزلنا على قومه",
        "questions": [
            "وما أنزلنا على قومه من بعده*",
            "وإذا قيل لهم اتقوا ما بين أيديكم ", 
            "ألم أعهد إليكم يٰبني ءادم"
            "أولم ير الإنسان أنى خلقنـٰه",
            "أُحشروا الذين ظلموا وأزواجهم", 
            "قال قآئل منهم إني كان لي قرين",
            "وإن من شيعته لإبرٰهيم ", 
            "ولقد مننا علىٰ موسىٰ وهـٰرون"
        ]
    },  
    
    17:{
        "name":"حزب قل من يرزقكم من",
        "questions": [
            "قل من يرزقم من السمـٰوٰت والأرض قل الله",
            "وما أرسلنا في قرية من نذير ", 
            "قل إنما أعظكم بواحدة"
            "يـٰأيها الناس إن وعد الله حق",
            "يـٰأيها الناس أنتم الفقرآء", 
            "والذي أوحينا إليك من الكتـٰب هو الحق",
            "قل أرايتم شركآءكم الذين تدعون من ", 
            "بداية سورة يسٓ"
        ]
    }, 
    
    18:{
        "name":"حزب إن المسلمين والمسلمٰت",
        "questions": [
            "إن المسلمين والمسلمٰت",
            "ما كان محمد أبا أحد من رجالكم ", 
            "ترجي من تشآء منهن"
            "لا جناح عليهن في ءابآئهن",
            "لئن لم ينته المنـٰفقون", 
            "إنا عرضنا الأمانة على السمـٰوٰت ",
            "وقال الذين كفروا هل ندلكم ", 
            "لقد كان لسبإ في مساكنهم ءاية"
        ]
    }, 
    
    19:{
        "name":"حزب ومن يسلم وجهه",
        "questions": [
            "ومن يسلم وجهه إلى الله",
            "وإذا غشيهم موج كالظلل ", 
            " قل يتوفىٰكم ملك الموت "
            "ولقد ءاتينا موسى الكتٰب فلا تكن",
            "النبىٓء اَولى بالمؤمنين من أنفسهم", 
            "وإذ قالت طآئفة منهم يـٰأهل يثرب ",
            "يحسبون الأحزاب لم يذهبوا ", 
            "يـٰأيها النبىٓء قل لأزواج إن كنتن"
        ]
    },
    
    20:{
        "name":"حزب ولا تجادلوا أهل الكتٰب",
        "questions": [
            "ولا تجادلوا أهل الكتٰب",
            "وكأين من دآبة لا تحمل رزقها ", 
            " أولم يسيرو في الأرض فينظروا "
            "ومن ءايٰته خلق السمـٰوٰت والأرض واختلاف",
            "منيبين إليه واتقوه", 
            "ظهر الفساد في البر والبحر  ",
            "الله الذي خلقكم من ضعف ", 
            "ولقد ءاتينا لقمـٰن الحكمة"
        ]
    },
    
    21:{
        "name":"حزب ولقد وصلنا",
        "questions": [
            "ولقد وصلنا لهم القول",
            "أفن وعدنٰه وعداً حسناً ", 
            " إن قارون كان من قوم موسىٰ "
            "تلك الدارة اءلاخرة نجعلها",
            "ووصينا الإنسان بوالديه حسناً", 
            "وإبرٰهيم إذ قال لقومه اعبدوا الله ",
            "فئـامن له لوط ", 
            "وإلى مدين أخاهم شعيباً فقال"
        ]
    },
    
    22:{
        "name":"حزب قل الحمد لله وسلام",
        "questions": [
            "قل الحمد لله وسلام على عباده",
            "وقال الذين كفروا إذا كنا تراباً ", 
            " وإذا وقع القول عليهم اخرجنا لهم "
            "بداية سورة القصص",
            "وحرمنا عليه المراضع من قبل", 
            "وجآء وجل من أقصى المدينة ",
            "فلما قضى موسى الأجل  ", 
            "وقال فرعون يـٰأيها الملأ"
        ]
    },
    
    23:{
        "name":"حزب قالوا أنؤمن لك",
        "questions": [
            "قالو أنؤمن لك واتبعك الارذلون ",
            "أتتركون فيما هـٰهنا ءامنين ", 
            " أوفوا الكيل ولا تكونوا "
            "وما أهلكنا من قرية",
            "وإنك لتلقى القرءان ", 
            "حتىٰ إذا أتواْ على واد النمل ",
            "قال سننظر أصدقت  ", 
            "قال نكروا لها عرشها ننظر أتهتدي"
        ]
    },
    24:{
        "name":"حزب وقال الذين لا يرجون لقآءنا",
        "questions": [
            "وقال الذين لا يرجون لقآءنا",
            "وقال الذين كفروا لولا نزل ", 
            " ألم تر إلىٰ ربك كيف مد الظل "
            "تبـٰرك الذي جعل في السمآء بروجاً",
            "بداية سورة الشعرآء", 
            "قال فرعون وما رب العـٰلمين ",
            "قالوا لا ضير ", 
            "الذي خلقني فهو يهدين"
        ]
    },  
    
    25:{
        "name":"حزب يٰأها الذين ءامنوا لا تتبعوا",
        "questions": [
            "يٰأيها الذين ءامنوا لا تتبعوا",
            "قل للمؤمنين يغضوا من أبصارهم ", 
            " الله نور السمـٰوٰت والأرض "
            "ألم تر أن الله يزجي سحاباً",
            "وأقسموا بالله جهد أيمانهم لئن", 
            "والقواعد من النسآء ",
            "لا تجعلوا دعآء الرسول بينكم ", 
            "تبـٰرك الذي إن شآء"
        ]
    },
    
    26:{
        "name":"حزب المؤمنون",
        "questions": [
            "بداية سورة المؤمنون",
            "وإن لكم في الأنعام لعبرة ", 
            " هيهات هيهات لما توعدون "
            "إن الذين هم من خشية ربهم",
            "ولو رحمنـٰهم", 
            "وقل رب أعوذ بك من همزات ",
            "أفحسبتم أنا خلقنـٰكم عبثاً ", 
            "الذي خلقني فهو يهدين"
        ]
    },
    
    27:{
        "name":"حزب الحج",
        "questions": [
            "بداية سورة الحج",
            "ومن الناس من يعبد الله على حرف ", 
            " هٰذٰن خصمان اختصموا في ربهم "
            "ذٰلك ومن يعظم حرمـٰت الله",
            "إن الله يدافع عن الذين ءامنوا", 
            "قل يٰأيها الناس إنما أناْ لكم نذير ",
            "ذٰلك ومن عاقب بمثل ما عوقب به ", 
            "ألم تعلم أن الله يعلم ما في السمآء"
        ]
    },
    
    28:{
        "name":"حزب الأنبياء",
        "questions": [
            "بداية سورة الأنبياء",
            "وما خلقنا السمآء والأرض وما بينهما ", 
            " أولم الذين كفروا أن السمـٰوٰت والأرض "
            "قل من يكلؤكم باليل والنهارمن الرحمٰن",
            "ولقد ءاتينا إبرٰهيم رشده", 
            "ولوطاً ءاتينٰه حكماً وعلماً ",
            "وذا النون إذ ذهب مغاضباً ", 
            "إن الذين سبقت لهم منا الحسنىٰ"
        ]
    },
    
    29:{
        "name":"حزب طه",
        "questions": [
            "بداية سورة طه",
            "قال رب اشرح لي صدري ", 
            " منها خلقنـٰكم وفيها نعيدكم "
            "قالوا لن نؤثرك على ما جآءنا",
            "وما أعجلك عن قومك يٰموسىٰ", 
            "قال فما خطبك يٰسامرىّ ",
            "وعنت الجوه للحىّ القيوم ", 
            "أفلم يهد لهم كم أهلكنا قبلهم من القرون"
        ]
    },
    
    30:{
        "name":"حزب قال أقل لك إنك",
        "questions": [
            "قال ألم أقل لك إنك لن تستطيع",
            "ويسئلونك عن ذي القرنين ", 
            " وتركنا بعضهم يومئذ يموج في بعض "
            "بداية سورة مريم",
            "فحملته فانتبذت به مكاناً قصياً", 
            "واذكر في الكتٰب إبرٰهيم ",
            "فخلف من بعدهم خلف اضاعوا الصلوٰة ", 
            "أفراَيت الذي كفر بئايـٰتنا"
        ]
    },
    
    31:{
        "name":"حزب أولم يروا أن الله الذي خلق السمٰوٰت",
        "questions": [
            "أولم يروا أن الله الذي خلق السمٰوٰت والأرض"
            "بداية سورة الكهف ", 
            " وترى الشمس إذا طلعت تزاور "
            "فلا تمار فيهم إلا مرآءً ظاهراً",
            "واضرب لهم مثلا رجلين جعلنالأحدهما", 
            "واضرب لهم مثل الحيوٰة الدنيا ",
            "ولقد صرفنا في هٰذا القرءان للناس ", 
            "قال ذٰلك ما كنا نبغ"
        ]
    },
   
    32:{
        "name":"حزب الإسراء",
        "questions": [
            "بداية سورة الإسراء"
            "ويدع الإنسان بالشر دعآءه بالخير ", 
            " وقضىٰ ربك أن لا تعبدوا إلا إياه "
            "ولا تقف ما ليس لك به علم",
            "قل كونوا حجارة أو حديداً", 
            "وإذ قلنا للملآئكة اسجدوا ءلادم ",
            "ولقد كرمنا بني ءادم ", 
            "ويسئلونك عن الروح"
        ]
    }, 
    
    33:{
        "name":"حزب وقال الله لا تتخذو إلاهين اثنين",
        "questions": [
            "وقال الله لا تتخذوا إلاهين اثنين"
            "تالله لقد أرسلنا إلىٰ أُمم من قبلك ", 
            " والله فضل بعضكم علىٰ بعض في الرزق "
            "ألم يرواْ إلىٰ الطير مسخرٰت",
            "إن الله يأمركم بالعدل والإحسان", 
            "فإذا قرأت القرءان فاستعذ بالله  ",
            "يوم تأتي كل نفس تجادل عن نفسها ", 
            "إن إبرٰهيم كان أُمة قانتاً لله حنيفاً"
        ]
    },
    
    34:{
        "name":"حزب الحجر",
        "questions": [
            "بداية سورة الحجر"
            "ولقد خلقنا الإنسان من صلصال ", 
            " نبئْ عبادىَ أنىَ أناْ الغفور الرحيم "
            "ولقد كذب أصحٰب الحجر المرسلين",
            "بداية سورة النحل", 
            "وألقىٰ في الأرض رواسى ",
            "وقيل للذين اتقواْ ماذا أنزل ربكم ", 
            "وأقسموا بالله جهد أيمانهم لا يبعث "
        ]
    },
    
    35:{
        "name":"حزب أفمن يعلم أنما أُنزل",
        "questions": [
            "أفمن يعلم أنما أنزل إليك من ربك"
            "كذٰلك أرسلنٰك في أُمة ", 
            " مثل الجنة التي وعد المتقون "
            "بداية سورة إبرٰهيم",
            "قالت رسلهم أفي الله شك", 
            "ألم تر أن الله خلق السمٰوٰت والأرض بالحق ",
            "ألم تر إلى الذين بدلوا نعمت الله كفراً ", 
            "الحمد لله الذي وهب لي على الكبرإسمٰعيل"
        ]
    },
    
    36:{
        "name":"حزب وما أُبرئ نفسىَ",
        "questions": [
            "وما أُبرئ نفسىَ"
            "وقال يٰبني لا تدخلوا من باب واحد ", 
            " قالوا إن يسرق فقد سرق أخ له "
            "فلما دخلوا عليه قالوا يٰأيها العزيز",
            "رب قد ءاتيتني من الملك", 
            "حتىٰ إذا استيئس الرسل ",
            "وإن تعجب فعجب قولهم ", 
            "قل من رب السمٰوٰت والأرض قل الله"
        ]
    },
 
    37:{
        "name":"حزب وإلى مدين أخاهم شعيباً",
        "questions": [
            "وإلى مدين أخاهم شعباً"
            "ولما جا أمرنا نجينا شعيباً ", 
            " يوم يأْتي لا تكلم نفس إلا بإذنه "
            "وكلا نقص عليك من أنبآء الرسل",
            "قال قآئل منهم لا تقتلوا يوسف", 
            "ولما بلغ أشده ءاتينٰه حكماً وعلماً ",
            "قال رب السجن أحب إلي ", 
            "وقال الملك إنىَ أرىٰ سبع بقرٰت سمان"
        ]
    },   
    
    38:{
        "name":"حزب وما من دآبة في الأرض",
        "questions": [
            "وما من دآبة في الأرض إلا على الله"
            "من كان يريد الحيوٰة الدنيا وزينتها ", 
            " مثل الفريقين كالأعمىٰ والأصم "
            "قالوا يٰنوح قد جادلتنا ",
            "وقال اركبوا فيها بسم الله مجراها", 
            "وإلى عاد أخاهم هوداً ",
            "قالوا يٰصالح قد كنت فينا مروجواً ", 
            "فلما ذهب عن إبرٰهيم الروع"
        ]
    },
    39:{
        "name":"حزب للذين أحسنوا الحسنىٰ",
        "questions": [
            "للذين أحسنوا الحسنى وزيادة"
            "وما كان هٰذا القرءان أن يفترى ", 
            " قل لاأملك لنفسي ضراً ولا نفعاً "
            "وما تكون في شأن",
            "واتل عليهم نبأ نوح ", 
            "فما ءامن لموسى  ",
            "ولقد بوأنا بني إسرآئيل  ", 
            "قل يٰأيها الناس إن كنتم في شك"
        ]
    },
    40:{
        "name":"حزب إنما السبيل على الذين",
        "questions": [
            "إنما السبيل على الذين يستأذنونك"
            "وممن حولكم من الأعراب منٰفقون ", 
            " إن الله اشترىٰ من المؤمنين أنفسهم "
            "لقد تاب الله على النبىٓء والمهٰجرين",
            "يـٰأيها الذين ءامنوا قاتلوا الذين يلونكم ", 
            "إن ربكم الله الذي خلق السمٰوٰت   ",
            "ولو يعجل الله للناس الشر  ", 
            "وما كان الناس إلا أُمة واحدة فاختلفوا"
        ]
    },
    41:{
        "name":"حزب يـٰأيها الذين ءامنوا إن كثيراً",
        "questions": [
            "يٰأيها الذين ءامنوا إن كثيراً من الأحبار"
            "إلا تنصروه فقد نصره الله ", 
            " ولو أرادوا الخروج لأعدوا له عدة "
            "وما منعهم أن تقبل منهم نفقاتهم",
            "ومنهم الذين يؤذون النبىٓء ", 
            "ألم يأتهم نبأُ الذين من قبلهم  ",
            "ومنهم من عاهد الله لئن ءاتىٰنا  ", 
            "ولا تصل علىٰ أحد منهم مات أبداً"
        ]
    },  
    42:{
        "name":"حزب واعلموا أنما غنمتم من شيء",
        "questions": [
            "واعلموا أنما غنمتم من شيْء"
            "إذ يقول المنٰفقون والذين في قلوبهم  ", 
            " وأعدوا لهم ما استطعتم من قوة "
            "إن الذين ءامنوا وهاجروا وجاهدوا",
            "فإذا انسلخ الأشهر الحرم فاقتلوا ", 
            "وإن نكثوا أيمانهم من بعد عهدهم  ",
            "أجعلتم سقاية  الحآج وعمارة   ", 
            "لقد نصركم الله في مواطن كثيرة"
        ]
    },
    43:{
        "name":"حزب وإذ نتقنا الجبل فوقهم",
        "questions": [
            "وإذ نتقنا الجبل فوقهم كأنه ظلة"
            "ولله الأسمآء الحسنىٰ فادعوه بها ", 
            " قل لا أملك لنفسي نفعاً ولا ضراً "
            "خذ العفو وأمر بالعرف وأعرض",
            "كما أخرجك ربك من بيتك بالحق", 
            "إذ يوحي ربك إلى الملآئكة   ",
            "إن شر الدوآب عند الله الصم  ", 
            "وإذ قالوا اللهم إن كان هٰذا"
        ]
    },
    44:{
        "name":"حزب قال الملأُ الذين استكبروا ",
        "questions": [
            "قال الملأُ الذين استكبروا من قومه"
            "أولم يهد للذين يرثون الأرض ", 
            " وأوحينا إلىٰ موسىٰ أن ألق عصاك "
            "وقالوا مهما تأْتنا به من ءاية",
            "وواعدنا موسىٰ ثلاثين ليلة ", 
            "واتخذ قوم موسىٰ من بعده من حليهم  ",
            "واكتب لنا في هٰذه الدنيا حسنة  ", 
            "وسئلهم عن القرية التي كانت حاضرة"
        ]
    },
    45:{
        "name":"حزب الأعراف",
        "questions": [
            "بداية سورة الأعراف"
            "ويـٰئادم اسكن أنت وزوجك الجنة ", 
            " قل أمر ربي بالقسط "
            "قال ادخلوا في أمم قد خلت",
            "وإذا صرفت أبصارهم تلقا أصحٰب ", 
            "ادعو ربكم تضرعاً وخفية  ",
            "وإلى عاد أخاهم هوداً قال يٰقوم  ", 
            "قال الملأُ الذين استكبروا من قومه للذين"
        ]
    },
    46:{
        "name":"حزب ولو أننا نزلنا إليهم الملآئكة",
        "questions": [
            "ولو أننا نزلنا إليهم الملآئكة"
            "وذروا ظاهر الإثم وباطنه ", 
            " لهم دار السلام عند ربهم "
            "وجلعلوا لله مما ذرأ من الحرث",
            "وهو الذي أنشأ جنٰت معروشـٰت ", 
            "قل لا أجد في ما أُوحىَ إلىّ  ",
            "قل تعالواْ أتل ما حرم ربكم عليكم", 
            "هل ينظرون إلا أن تأتيهم الملآئة"
        ]
    },
    47:{
        "name":"حزب إنما يستجيب الذين يسمعون",
        "questions": [
            "إنما يستجيب الذين يسمعون"
            "قل لا أقول لكم عندي خزآئن الله ", 
            " وعنده مفاتح الغيب  "
            "وذر الذين اتخذوا دينهم لعباً ولهواً",
            "وحـآجه قومه ", 
            "وما قدروا الله حق قدره  ",
            "وجعلوا لله شركآء الجن وخلقهم", 
            "ولو أننا نزلنا إليهم الملآئكة"
        ]
    }, 
    48:{
        "name":"حزب لتجدن أشد الناس عداوة ",
        "questions": [
            "لتجدن أشد الناس عداوة "
            "يٰأيها الذين ءامنوا إنما الخمر ", 
            " جعل الله الكعبة البيت الحرام "
            "يٰأيها الذين ءامنوا شهادة بينكم",
            "وإذ أوحيت إلى الحواريين  ", 
            "بداية سورة الأنعام  ",
            "وله ما سكن في اليل والنهار", 
            "ومنهم من يستمع إليك"
        ]
    },
    49:{
        "name":"حزب قال رجلان ",
        "questions": [
            "قال رجلان "
            "من أجل ذٰلك كتبنا ", 
            " يـٰأيها الرسول لا يحزنك "
            "وكتبنا عليهم فيها أن النفس",
            "وأن احكم بينهم بما أنزل الله  ", 
            "قل يٰأهل الكتٰب هل تنقمون منا  ",
            "يٰأيها الرسول بلغ ما أنزل إليك", 
            "(ما المسيح ابن مريم إلا رسول (وأمه صديقة"
        ]
    },
    50:{
        "name":"حزب لا يحب الله الجهر ",
        "questions": [
            "لا يحب الله الجهر بالسوٓء من القول "
            "وإن مِّن أهل الكتٰب إلا ليؤمنن به ", 
            " لٰكن الله يشهد بما أنزل إليك "
            "لن يستنكف المسيح أن يكون عبداً",
            "حرمت عليكم الميتة والدم  ", 
            "يٰأيها الذين ءامنوا إذا قمتم إلى الصلوٰة  ",
            "ولقد أخذ الله ميثاق بني إسرآئيل وبعثنا", 
            "لقد كفر الذين قالوا إن الله هو المسيح"
        ]
    },
    51:{
        "name":"حزب الله لا إلٰه إلا هو ",
        "questions": [
            "الله لا إلٰ إلا هو ليجمعنكم "
            "ومن يقتل مؤمناً متعمداً ", 
            " ومن يهاجر في سبيل الله  "
            "إنا أنزلنا إليك الكتٰب بالحق",
            "لا خير في كثير من نجوىٰهم  ", 
            "ليس بأمانيكم ولا أماني أهل الكتٰب  ",
            "وإن يتفرقا يغن الله كلا من سعته", 
            "بشر المنٰفقين بأن لهم عذاباً أليماً"
        ]
    },
    52:{
        "name":"حزب والمحصنـٰت من النسآء ",
        "questions": [
            "والمحصنـٰت من النسآء "
            "إن تجتنبوا كبآئر ما تنهَوْنَ عنه ", 
            " واعبدوا الله ولا تشركوا به شيئاً "
            "يٰأيها الذين أُوتوا الكتٰب ءامنوا بما نزلنا",
            "إن الله يأمركم أن تؤدوا الأمانٰت إلىٰ أهلها  ", 
            "وما أرسلنا من رسول إلا ليطاع بإذن الله  ",
            "فليقاتل في سبيل الله", 
            "أين ما تكونوا يدرككّم الموت"
        ]
    },
    53:{
        "name":"حزب يستبشرون بنعمة من الله ",
        "questions": [
            "يستبشرون بنعمة من الله وفضل "
            "ما كان الله ليذر المؤمنين ", 
            " لتبلوُنّ في أموالكم وأنفسكم "
            "فاستجاب لهم ربهم أني لا أضيع",
            "وابتلوا اليتـٰمىٰ  ", 
            "يوصيكم الله في أولادكم  ",
            "تلك حدود الله ومن يطع الله ورسوله",
            "يـٰأيها الذين ءامنوا لا يحل لكم أن ترثوا "
        ]
    },
    54:{
        "name":"حزب لن تنالوا البر ",
        "questions": [
            "لن تنالو البر حتىٰ تنفقوا "
            "ولتكن منكم أمة ", 
            " ليسوا سوآءً "
            "وإذ غدوت من أهلك",
            "سارعوا إلى مغفرة من ربكم  ", 
            "(وما محمد إلا رسول (أفإن مات",
            "إذ تصعدون ولا تلوون علىٰ أحد",
            "إن ينصركم الله فلا غالب لكم "
       ]
   },
    55:{
        "name":"حزب قل أٰؤُنبؤكم ",
        "questions": [
            "قل أٰؤُنبؤكم بخبر من ذٰلكم "
            "قل اللهم مالك الملك ", 
            " إن الله اصطفىٰ ءادم ونوحاً "
            "وإذ قالت الملآئكة يٰمريم ",
            "فلما أحس عيسىٰ منهم الكفر  ", 
            "قل يٰأهل الكتٰب تعالواْ إلىٰ كلمة  ",
            "ومن أهل الكتٰب من إن تأمنه",
            "أفغير دين الله تبغون "
        ] 
    },
    56:{
        "name":"حزب تلك الرسل ",
        "questions": [
            "تلك الرسل فضلنا بعضهم على بعض "
            "ألم تر إلى الذي حآج إبرٰهيم ", 
            " قول معروف ومغفرة خير "
            "يٰأيها الذين ءامنوا أنفقوا من طيبٰت ",
            "ليس عليك هدىٰهم  ",
            "يٰأيها الذين ءامنوا إذا تداينتم ",
            "وإن كنتم على سفر"
            "إن الله لا يخفىٰ عليه شيْء"
        ]
    }, 
    
    57:{
        "name":"حزب واذكرو الله في أيام  ",
        "questions": [
            "واذكروا الله في أيام معدودٰت "
            "كان الناس أمةً واحدةً فبعث الله ", 
            " يسئلونك عن الخمر والميسر "
            "والمطلقٰت يتربصن بأنفسهن ",
            "والوالدٰت يرضعن أولادهن حولين  ", 
            "لا جناح عليكم إن طلقتم النسآء  ",
            "ألم تر إلى الذين خرجوا من ديارهم",
            "وقال لهم نبيٓئهم إن ءاية ملكه "
        ] 
    },
    
    58:{
        "name":"حزب سيقول السفهآء ",
        "questions": [
            "سيقول السفهآء من الناس "
            "ولكل وجهة هو موليها ", 
            "إن الصفا والمروة  "
            "يٰأيها الناس كلوا مما في الأرض ",
            "ليس البر أن تولوا وجوهكم  ", 
            "شهر رمضان الذي أنزل فيه القرءان  ",
            "يسئلونك عن الأهلة",
            "الحج أشهر معلومات "
        ] 
    }, 
    59:{
        "name":"حزب وإذا لقوا الذين ءامنوا ",
        "questions": [
            "وإذا لقوا الذين ءامنوا "
            "وإن يأتوكم أسارىٰ تفادوهم ", 
            " ولقد جآءكم موسىٰ بالبينٰت "
            "واتبعوا ما تتلوا الشيٰطين على ملك سليمٰن ",
            "ما ننسخ من ءاية أو ننسها  ", 
            "ولله المشرق والمغرب  ",
            "وإذ ابتلىٰ إبرٰهيم  ربُّه",
            "أم كنتم شهدآء اِذ حضر يعقوب الموت "
        ] 
    }, 
    60:{
        "name":"حزب الفاتحة ",
        "questions": [
            "بداية سورة البقرة "
            "وإذا لقوا الذين ءامنوا ", 
            " إن الله لا يستحيِى "
            "وإذ قلنا للملآئكة اسجدوا ءلادم ",
            "أتأمرون الناس بالبر  ", 
            "وإذ قال موسى لقومه يٰقوم إنكم ظلمتم  ",
            "وإذ استسقى موسى لقومه",
            "وإذ قال موسىٰ لقومه إن الله يأمركم "
        ] 
    },
}

# ملف لتخزين النتائج
RESULTS_FILE = "students_results.json"

# تطبيق الأنماط الإسلامية المحدثة
display(HTML("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Scheherazade+New:wght@400;700&display=swap');
    
    * {
        font-family: 'Scheherazade New', Arial, sans-serif !important;
    }
    
    .islamic-bg {
        background: linear-gradient(135deg, #1a472a 0%, #2e593c 100%);
        color: white;
        padding: 8px;
        border-radius: 12px;
        text-align: center;
        margin: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        border: 1px solid #3a6b47;
        position: relative;
        overflow: hidden;
    }
    
    .islamic-bg::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 80 80"><text x="50%" y="50%" font-size="22" text-anchor="middle" fill="rgba(255,255,255,0.03)" dominant-baseline="middle">﷽</text></svg>');
        background-repeat: repeat;
        z-index: 0;
    }
    
    .islamic-bg > * {
        position: relative;
        z-index: 1;
    }
    
    .islamic-button {
        background: linear-gradient(135deg, #3a6b47 0%, #2e593c 100%) !important;
        color: white !important;
        border-radius: 40px !important;
        border: none !important;
        font-weight: bold !important;
        margin: 8px !important;
        box-shadow: 0 3px 8px rgba(0,0,0,0.15) !important;
        padding: 10px 20px !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
        transform: translateY(0);
        min-width: 120px;
        height: 45px;
    }
    
    .islamic-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 12px rgba(0,0,0,0.2) !important;
        background: linear-gradient(135deg, #2e593c 0%, #3a6b47 100%) !important;
    }
    
    .islamic-button:active {
        transform: translateY(1px);
    }
    
    .islamic-text {
        color: #f8f9f0 !important;
    }
    
    .question-box {
        background: linear-gradient(135deg, #f8f9f0 0%, #e9f5e9 100%) !important;
        color: #1e2e1e !important;
        padding: 15px;
        border-radius: 10px;
        margin: 12px 0;
        text-align: center;
        font-size: 16px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.08);
        border: 1px solid #d0e0d0;
        position: relative;
        overflow: hidden;
        line-height: 1.4;
    }
    
    .question-box::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3a6b47, #2e593c);
    }
    
    .exam-details {
        background: linear-gradient(135deg, #e8f5e9 0%, #d0e8d0 100%) !important;
        padding: 15px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 4px solid #3a6b47;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        font-size: 14px;
    }
    
    .score-input {
        background-color: white !important;
        border: 2px solid #3a6b47 !important;
        border-radius: 8px !important;
        padding: 8px !important;
        margin: 8px !important;
        font-size: 14px !important;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.08);
        height: 40px;
        width: 130px !important;
    }
    
    .input-container {
        background: rgba(255, 255, 255, 0.15);
        padding: 15px;
        border-radius: 10px;
        margin: 12px 0;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .category-info {
        background: rgba(255, 255, 255, 0.2);
        padding: 10px;
        border-radius: 8px;
        margin: 6px 0;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255,255,255,0.1);
        font-size: 14px;
    }
    
    .question-list {
        background: linear-gradient(135deg, #f0f8ff 0%, #e0f0e0 100%);
        padding: 10px;
        border-radius: 6px;
        margin: 6px 0;
        border-left: 3px solid #3a6b47;
        font-size: 13px;
    }
    
    .header-title {
        font-size: 1.2em;
        margin-bottom: 5px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        background: linear-gradient(45deg, #f8f9f0, #c9e0c9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        padding: 3px;
    }
    
    .subtitle {
        font-size: 0.8em;
        margin-bottom: 8px;
        opacity: 0.9;
    }
    
    .quran-verse {
        font-size: 1.0em;
        margin: 8px 0;
        line-height: 1.4;
    }
    
    .category-checkbox {
        margin: 6px !important;
        transform: scale(1.1);
    }
    
    .category-checkbox label {
        font-size: 14px !important;
        font-weight: bold !important;
    }
    
    .progress-bar {
        height: 8px;
        background: rgba(255,255,255,0.2);
        border-radius: 4px;
        overflow: hidden;
        margin: 10px 0;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #3a6b47, #2e593c);
        border-radius: 4px;
        transition: width 0.5s ease;
    }
    
    .floating-icon {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0px); }
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }
    
    .fade-in {
        animation: fadeIn 0.8s;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .stats-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 8px;
        margin: 5px;
        text-align: center;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255,255,255,0.15);
        transition: all 0.3s ease;
        min-width: 80px;
        max-width: 100px;
    }
    
    .stats-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 12px rgba(0,0,0,0.15);
    }
    
    .stats-number {
        font-size: 1.2em;
        font-weight: bold;
        margin: 3px 0;
        background: linear-gradient(45deg, #f8f9f0, #c9e0c9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stats-label {
        font-size: 0.7em;
        opacity: 0.8;
    }
    
    .scrollable-container {
        max-height: 300px;
        overflow-y: auto;
        margin: 10px 0;
        padding: 5px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .scrollable-container::-webkit-scrollbar {
        width: 8px;
    }
    
    .scrollable-container::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    
    .scrollable-container::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.3);
        border-radius: 4px;
    }
    
    .scrollable-container::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.5);
    }
    
    .stats-triangle {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 5px 0;
    }
    
    .stats-top-row {
        display: flex;
        justify-content: center;
        margin-bottom: 5px;
    }
    
    .stats-bottom-row {
        display: flex;
        justify-content: center;
    }
    
    /* تحسينات للهواتف */
    .mobile-optimized {
        max-height: 60vh;
        overflow-y: auto;
        padding: 10px;
        margin-bottom: 70px; /* مساحة للأزرار الثابتة */
    }
    
    .fixed-buttons {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(135deg, #1a472a 0%, #2e593c 100%);
        padding: 10px;
        z-index: 1000;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.2);
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .medium-button {
        min-width: 110px !important;
        height: 42px !important;
        font-size: 13px !important;
        padding: 8px 15px !important;
        margin: 5px !important;
    }
    
    .student-card {
        background: linear-gradient(135deg, #f8f9f0 0%, #e9f5e9 100%);
        padding: 12px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 3px 8px rgba(0,0,0,0.08);
        border: 1px solid #d0e0d0;
    }
    
    @media (max-width: 600px) {
        .islamic-button {
            min-width: 110px;
            height: 42px;
            font-size: 13px;
            padding: 8px 15px;
            margin: 5px;
        }
        
        .header-title {
            font-size: 1.1em;
        }
        
        .subtitle {
            font-size: 0.75em;
        }
        
        .question-box {
            padding: 12px;
            font-size: 14px;
        }
        
        .stats-card {
            min-width: 70px;
            padding: 6px;
        }
        
        .stats-number {
            font-size: 1.1em;
        }
        
        .stats-label {
            font-size: 0.65em;
        }
        
        .mobile-optimized {
            max-height: 65vh;
            margin-bottom: 75px;
        }
        
        .fixed-buttons {
            padding: 8px;
        }
    }
</style>
"""))

# إنشاء عناصر واجهة المستخدم الرئيسية
output = widgets.Output()

# عناصر شاشة إعداد الامتحان
student_name_input = widgets.Text(
    value='', 
    placeholder='أدخل اسم الطالب هنا', 
    layout=widgets.Layout(width='280px', height='40px'),
    style={'font_size': '14px'}
)

questions_count_input = widgets.IntText(
    value=5, 
    min=1, 
    max=20, 
    layout=widgets.Layout(width='80px', height='40px'),
    style={'font_size': '14px'}
)

# صناديق اختيار الأحزاب - فارغة افتراضياً
category_checks = {}
category_container = widgets.VBox([], layout=widgets.Layout(margin='10px 0'))

for cat_id in categories.keys():
    category_checks[cat_id] = widgets.Checkbox(
        value=False,  # فارغة افتراضياً
        description=f'{categories[cat_id]["name"]}',
        layout=widgets.Layout(width='200px', margin='5px'),
        style={'font_size': '14px'}
    )
    category_container.children += (category_checks[cat_id],)

# الأزرار الرئيسية - تم تكبيرها قليلاً
start_exam_setup_btn = widgets.Button(
    description='بدء الامتحان ', 
    button_style='success', 
    layout=widgets.Layout(width='220px', height='45px')
)
start_exam_setup_btn.add_class("islamic-button")
start_exam_setup_btn.add_class("medium-button")

view_progress_btn = widgets.Button(
    description='عرض التقدم ', 
    button_style='info', 
    layout=widgets.Layout(width='220px', height='45px')
)
view_progress_btn.add_class("islamic-button")
view_progress_btn.add_class("medium-button")

exit_btn = widgets.Button(
    description='خروج ', 
    button_style='danger', 
    layout=widgets.Layout(width='220px', height='45px')
)
exit_btn.add_class("islamic-button")
exit_btn.add_class("medium-button")

# زر بدء الامتحان في شاشة الإعداد
start_exam_confirm_btn = widgets.Button(
    description='بدء الامتحان ', 
    button_style='success', 
    layout=widgets.Layout(width='180px', height='45px')
)
start_exam_confirm_btn.add_class("islamic-button")
start_exam_confirm_btn.add_class("medium-button")

# عناصر إدخال النتيجة
score_input = widgets.IntText(
    value=0, 
    min=0, 
    max=100, 
    description='الدرجة:', 
    layout=widgets.Layout(width='130px', height='40px'),
    style={'font_size': '14px'}
)

total_input = widgets.IntText(
    value=10, 
    min=1, 
    max=100, 
    description='من:', 
    layout=widgets.Layout(width='130px', height='40px'),
    style={'font_size': '14px'}
)

save_score_btn = widgets.Button(
    description='حفظ النتيجة ', 
    button_style='success', 
    layout=widgets.Layout(width='150px', height='45px')
)
save_score_btn.add_class("islamic-button")
save_score_btn.add_class("medium-button")

back_btn = widgets.Button(
    description='رجوع ', 
    button_style='warning', 
    layout=widgets.Layout(width='150px', height='45px')
)
back_btn.add_class("islamic-button")
back_btn.add_class("medium-button")

# متغيرات حالة التطبيق
current_screen = "welcome"
exam_questions = []
current_question_index = 0
exam_student = ""
results = {}
selected_student_details = ""
current_score = 0
current_total = 0
manual_scores = []
selected_categories = []
selected_questions_count = 0

def load_results():
    global results
    try:
        if os.path.exists(RESULTS_FILE):
            with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        return {}
    return {}

def save_results():
    try:
        with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False

def show_welcome_screen():
    global current_screen
    current_screen = "welcome"
    
    # مسح مدخلات اسم الطالب عند الرجوع للصفحة الرئيسية
    student_name_input.value = ''
    
    with output:
        clear_output()
        display(HTML(
            '''
            <div class="islamic-bg fade-in">
                <div class="header-title">🌙 مركز بن عطية لتحفيظ القرآن الكريم 🌙</div>
                <div class="subtitle">نظام متكامل لتقييم حفظ القرآن الكريم</div>
                <div class="quran-verse">( وَرَتِّلِ الْقُرْآنَ تَرْتِيلًا )</div>
                
                <div class="stats-triangle">
                    <div class="stats-top-row">
                        <div class="stats-card">
                            <div class="stats-number">''' + str(len(load_results())) + '''</div>
                            <div class="stats-label">طالب مسجل</div>
                        </div>
                        <div class="stats-card">
                            <div class="stats-number">''' + str(sum([data.get("exam_count", 0) for data in load_results().values()])) + '''</div>
                            <div class="stats-label">امتحان منجز</div>
                        </div>
                    </div>
                    <div class="stats-bottom-row">
                        <div class="stats-card">
                            <div class="stats-number">''' + str(len(categories)) + '''</div>
                            <div class="stats-label">حزب متاح</div>
                        </div>
                    </div>
                </div>
            </div>
            '''
        ))
        
        # عرض الأزرار الرئيسية
        buttons_container = widgets.VBox([
            start_exam_setup_btn, 
            view_progress_btn, 
            exit_btn
        ], layout=widgets.Layout(align_items='center', margin='20px 0'))
        
        display(buttons_container)
        
        # إضافة الأزرار الثابتة في الأسفل للهواتف
        display(HTML(
            '''
            <div class="fixed-buttons">
                <div id="fixed-buttons-container"></div>
            </div>
            <script>
                function updateFixedButtons() {
                    var fixedContainer = document.getElementById('fixed-buttons-container');
                    var buttons = document.querySelectorAll('.islamic-button');
                    
                    // مسح المحتوى الحالي
                    fixedContainer.innerHTML = '';
                    
                    // إضافة الأزرار إلى الحاوية الثابتة
                    buttons.forEach(function(button) {
                        if (button.offsetParent !== null) { // إذا كان الزر مرئياً
                            var clone = button.cloneNode(true);
                            clone.style.margin = '5px';
                            fixedContainer.appendChild(clone);
                            
                            // إضافة حدث النقر للزر المستنسخ
                            clone.addEventListener('click', function() {
                                button.click();
                            });
                        }
                    });
                }
                
                // تحديث الأزرار الثابتة عند التمرير وعند تغيير الحجم
                window.addEventListener('scroll', updateFixedButtons);
                window.addEventListener('resize', updateFixedButtons);
                
                // تحديث أولي للأزرار الثابتة
                setTimeout(updateFixedButtons, 100);
            </script>
            '''
        ))

def show_exam_setup():
    global current_screen
    current_screen = "exam_setup"
    
    with output:
        clear_output()
        display(HTML(
            '''
            <div class="islamic-bg fade-in">
                <div class="header-title">📝 إعداد الامتحان</div>
                <div class="subtitle">أدخل معلومات الطالب واختر الأحزاب</div>
            </div>
            '''
        ))
        
        # حاوية لحقل اسم الطالب
        name_container = widgets.VBox([
            widgets.HTML(value='<p style="color: #f8f9f0; font-size: 16px; margin: 10px 0;">اسم الطالب:</p>'),
            student_name_input
        ], layout=widgets.Layout(margin='10px 0'))
        
        display(name_container)
        
        # حاوية لاختيار الأحزاب - قابلة للتمرير
        display(widgets.HTML(value='<p style="color: #f8f9f0; font-size: 16px; margin: 10px 0;">اختر الأحزاب:</p>'))
        
        # استخدام الحاوية القابلة للتمرير
        scroll_box = widgets.Box([category_container], layout=widgets.Layout(
            height='300px', 
            overflow_y='auto',
            padding='5px',
            border='1px solid rgba(255,255,255,0.2)',
            border_radius='8px',
            margin='10px 0'
        ))
        display(scroll_box)
        
        # حاوية لعدد الأسئلة
        questions_container = widgets.VBox([
            widgets.HTML(value='<p style="color: #f8f9f0; font-size: 16px; margin: 10px 0;">عدد الأسئلة (يجب أن يكون بين 1 و 60):</p>'),
            questions_count_input
        ], layout=widgets.Layout(margin='10px 0'))
        
        display(questions_container)
        
        # أزرار التحكم
        buttons_container = widgets.HBox([back_btn, start_exam_confirm_btn], 
                                       layout=widgets.Layout(justify_content='center', margin='20px 0'))
        display(buttons_container)

def start_exam(b):
    global exam_student, exam_questions, current_question_index, manual_scores, selected_categories, selected_questions_count, results
    
    exam_student = student_name_input.value.strip()
    if not exam_student:
        show_message('⚠️ خطأ', 'يرجى إدخال اسم الطالب')
        return
    
    selected_categories = []
    for cat_id, check in category_checks.items():
        if check.value:
            selected_categories.append(cat_id)
    
    if not selected_categories:
        show_message('⚠️ خطأ', 'يرجى اختيار حزب واحد على الأقل')
        return
    
    selected_questions_count = questions_count_input.value
    if selected_questions_count <= 0 or selected_questions_count > 60:
        show_message('⚠️ خطأ', 'يرجى إدخال عدد أسئلة صحيح بين 1 و 60')
        return
    
    # تحضير بيانات الطالب
    results = load_results()
    if exam_student not in results:
        results[exam_student] = {
            "asked_questions": {}, 
            "exam_count": 0, 
            "scores": []
        }
    
    user_data = results[exam_student]
    user_data["exam_count"] = user_data.get("exam_count", 0) + 1
    
    # توليد الأسئلة مع منع تكرار الأحزاب
    exam_questions = []
    questions_per_category = max(1, selected_questions_count // len(selected_categories))
    
    for cat_id in selected_categories:
        # الحصول على الأسئلة السابقة لهذا الحزب
        prev_questions = user_data["asked_questions"].get(str(cat_id), [])
        
        # الحصول على أسئلة عشوائية
        available_questions = [q for q in categories[cat_id]["questions"] if q not in prev_questions]
        
        if len(available_questions) == 0:
            available_questions = categories[cat_id]["questions"]
        
        # إضافة الأسئلة المتاحة
        if len(available_questions) > questions_per_category:
            selected_questions = random.sample(available_questions, questions_per_category)
        else:
            selected_questions = available_questions
        
        exam_questions.extend([(cat_id, q) for q in selected_questions])
    
    # إذا كان عدد الأسئلة أكبر من المطلوب، نختار عشوائياً
    if len(exam_questions) > selected_questions_count:
        exam_questions = random.sample(exam_questions, selected_questions_count)
    
    if not exam_questions:
        show_message('⚠️ خطأ', 'لا توجد أسئلة متاحة للاختيار')
        return
    
    # بدء الامتحان
    current_question_index = 0
    manual_scores = []
    show_all_questions()

def show_all_questions():
    global current_screen
    
    with output:
        clear_output()
        display(HTML(
            f'''
            <div class="islamic-bg fade-in">
                <div class="header-title">أسئلة امتحان الطالب: {exam_student}</div>
                <div class="subtitle">عدد الأسئلة: {len(exam_questions)}</div>
            </div>
            '''
        ))
        
        # عرض جميع الأسئلة
        for i, (cat_id, question) in enumerate(exam_questions):
            display(HTML(
                f'''
                <div class="question-box fade-in">
                    <p style="font-size: 16px; margin: 0; color: #2c5e2c; font-weight: bold;">السؤال {i+1} - {categories[cat_id]["name"]}</p>
                    <p style="font-size: 18px; margin: 10px 0; line-height: 1.4;">{question}</p>
                </div>
                '''
            ))
        
        # عرض حقول إدخال النتيجة
        display(HTML(
            '''
            <div style="background: linear-gradient(135deg, #f8f9f0 0%, #e9f5e9 100%); padding: 15px; border-radius: 10px; margin: 15px 0; text-align: center; box-shadow: 0 3px 8px rgba(0,0,0,0.08);">
                <h3 style="color: #2c5e2c; margin: 0 0 10px 0; font-size: 18px;">أدخل النتيجة النهائية للامتحان</h3>
            </div>
            '''
        ))
        
        input_box = widgets.HBox([score_input, total_input], 
                                layout=widgets.Layout(justify_content='center', margin='10px'))
        display(input_box)
        
        buttons_box = widgets.HBox([save_score_btn, back_btn], 
                                  layout=widgets.Layout(justify_content='center', margin='10px'))
        display(buttons_box)

def save_score(b):
    global current_score, current_total, results
    
    score = score_input.value
    total = total_input.value
    
    if total <= 0:
        show_message('⚠️ خطأ', 'الدرجة الكلية يجب أن تكون أكبر من صفر')
        return
    
    if score < 0 or score > total:
        show_message('⚠️ خطأ', f'الدرجة يجب أن تكون بين 0 و {total}')
        return
    
    # حساب النسبة المئوية
    percentage = (score / total) * 100
    grade = get_grade(percentage)
    
    # حفظ النتيجة مع المعلومات الإضافية
    user_data = results[exam_student]
    user_data.setdefault("scores", []).append({
        "score": score,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "type": "يدوي",
        "exam_questions": exam_questions,  # حفظ الأسئلة المعطاة للطالب
        "exam_details": {
            "questions_count": len(exam_questions),
            "categories_count": len(selected_categories),
            "categories": selected_categories
        }
    })
    
    # تحديث الأسئلة التي تم سؤالها
    for cat_id, question in exam_questions:
        cat_str = str(cat_id)
        if cat_str not in user_data["asked_questions"]:
            user_data["asked_questions"][cat_str] = []
        user_data["asked_questions"][cat_str].append(question)
    
    save_results()
    
    # عرض النتيجة النهائية
    with output:
        clear_output()
