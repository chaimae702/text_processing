# coding: utf-8
from nltk import word_tokenize
from nltk.stem.isri import ISRIStemmer

st = ISRIStemmer()
#word_list = "عرض يستخدم الى التفاعل مع المستخدمين في هاذا المجال !وعلمآ تكون الخدمه للستطلاع على الخدمات والعروض المقدمة"
word_list = "ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي وهي بدايات الجبر، ومن المهم فهم كيف كانت هذه                      الفكرة الجديدة مهمة، فقد كانت خطوة نورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر کان نظرية موحدة تتيح الأعداد الكسرية والأعداد اللا كسرية، والمقادير الهندسية وغيرها، أن تتعامل على أنها أجسام جبرية، وأعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان موجودا من قبل، وقم وسيلة للتنمية في هذا الموضوع مستقبلا. وجانب آخر مهم لإدخال أفكار الجبر وهو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل"
# Define a function
def filter(word_list):
    wordsfilter=[]
    for a in word_tokenize(word_list):
        stem = st.stem(a)
        wordsfilter.append(stem)
    print(wordsfilter)

# Call the function
filter(word_list)