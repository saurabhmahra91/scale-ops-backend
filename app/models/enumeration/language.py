from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values

class Language(Model):
    id = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db

initialize_database([Language])

_values = ['Chinese, Mandarin', 'Spanish', 'English', 'Bengali', 'Hindi', 'Portuguese', 'Russian', 'Japanese', 'German, Standard', 'Chinese, Wu', 'Javanese', 'Korean', 'French', 'Vietnamese', 'Telugu', 'Chinese, Yue', 'Marathi', 'Tamil', 'Turkish', 'Urdu', 'Chinese, Min Nan', 'Chinese, Jinyu', 'Gujarati', 'Polish', 'Arabic, Egyptian Spoken', 'Ukrainian', 'Italian', 'Chinese, Xiang', 'Malayalam', 'Chinese, Hakka', 'Kannada', 'Oriya', 'Panjabi, Western', 'Sunda', 'Panjabi, Eastern', 'Romanian', 'Bhojpuri', 'Azerbaijani, South', 'Farsi, Western', 'Maithili', 'Hausa', 'Arabic, Algerian Spoken', 'Burmese', 'Serbo-Croatian', 'Chinese, Gan', 'Awadhi', 'Thai', 'Dutch', 'Yoruba', 'Sindhi', 'Arabic, Moroccan Spoken', 'Arabic, Saidi Spoken', 'Uzbek, Northern', 'Malay', 'Amharic', 'Indonesian', 'Igbo', 'Tagalog', 'Nepali', 'Arabic, Sudanese Spoken', 'Saraiki', 'Cebuano', 'Arabic, North Levantine Spoken', 'Thai, Northeastern', 'Assamese', 'Hungarian', 'Chittagonian', 'Arabic, Mesopotamian Spoken', 'Madura', 'Sinhala', 'Haryanvi', 'Marwari', 'Czech', 'Greek', 'Magahi', 'Chhattisgarhi', 'Deccan', 'Chinese, Min Bei', 'Belarusan', 'Zhuang, Northern', 'Arabic, Najdi Spoken', 'Pashto, Northern', 'Somali', 'Malagasy', 'Arabic, Tunisian Spoken', 'Rwanda', 'Zulu', 'Bulgarian', 'Swedish', 'Lombard', 'Oromo, West-Central', 'Pashto, Southern', 'Kazakh', 'Ilocano', 'Tatar', 'Fulfulde, Nigerian', 'Arabic, Sanaani Spoken', 'Uyghur', 'Haitian Creole French', 'Azerbaijani, North', 'Napoletano-Calabrese', 'Khmer, Central', 'Farsi, Eastern', 'Akan', 'Hiligaynon', 'Kurmanji', 'Shona']

insert_enum_values(Language, _values)

