from app.core.database import db, initialize_database
from peewee import Model, CharField
from .base import insert_enum_values

class CasteCommunity(Model):
    value = CharField(unique=True, index=True, primary_key=True, null=True)

    class Meta:
        database = db


initialize_database([CasteCommunity])

_CASTES = [
    "Adaviyar",
    "Adi Andhra",
    "Agri (caste)",
    "Aheria",
    "Ahirwar",
    "Ahluwalia (caste)",
    "Ambalavasi",
    "Ambattar",
    "Andhra Vaishnavas",
    "Arora",
    "Arunattu Vellalar",
    "Asati",
    "Asur people",
    "Attar (caste)",
    "Badagas",
    "Bagal (caste)",
    "Bairagi Brahmin (caste)",
    "Baishya Kapali",
    "Baishya Saha",
    "Baiswar",
    "Balija",
    "Banai (sub-tribe)",
    "Banaphar",
    "Bandhmati",
    "Bania (caste)",
    "Barai (caste)",
    "Bari (caste)",
    "Barika (caste)",
    "Barujibi",
    "Bathudi Tribe",
    "Batwal",
    "Bauri (caste)",
    "Bedia (caste)",
    "Beldar",
    "Bengali Kayastha",
    "Bhambi",
    "Bhambi Khalpa",
    "Bhambi Rohit",
    "Bhambi Sindhi Mochi",
    "Bhandari (caste)",
    "Bhanushali",
    "Bhar",
    "Bharbhunja (Hindu)",
    "Bhat",
    "Bhatraju",
    "Bhattathiri",
    "Bhatti",
    "Bhavsar",
    "Bhil Gametia",
    "Bhil Mama",
    "Bhoi",
    "Bhottada",
    "Bhulia",
    "Bhumihar",
    "Billava",
    "Bind (caste)",
    "Binjhal",
    "Birhor people",
    "Bonda people",
    "Boom Boom Mattukaran",
    "Bot (caste)",
    "Boya (caste)",
    "Brahmin",
    "Budabukkala",
    "Bunt (community)",
    "Burud (caste)",
    "Dhobi",
    "Chakyar",
    "Chambhar",
    "Chandala",
    "Charan",
    "Chasa (caste)",
    "Chaukalshi",
    "Cherayi Panicker",
    "Chero",
    "Chettiar",
    "Chhaparband",
    "Chhipi",
    "Cholanaikkan",
    "Chozhia Vellalar",
    "Chunara",
    "Chunaru",
    "Dabgar",
    "Dahima",
    "Daivadnya",
    "Daivampadi",
    "Dangi people",
    "Desikar",
    "Deswali Majhi",
    "Devadiga",
    "Devanga",
    "Devendrakulam",
    "Dewar (caste)",
    "Dhagi",
    "Dhakar",
    "Dheevara (caste)",
    "Dhekaru",
    "Dhusia",
    "Dogra Jheer",
    "Dumal",
    "Elur Chetty",
    "Eradi",
    "Ezhava",
    "Ezhuthachan (caste)",
    "Gadhia (community)",
    "Gahoi",
    "Ganak",
    "Gandhabanik",
    "Gauda and Kunbi",
    "Gavli",
    "Gawaria",
    "Ghamaila",
    "Gharami",
    "Ghasi",
    "Ghasiara",
    "Ghirth",
    "Gihara",
    "Godha",
    "Golconda Vyapari Brahmin",
    "Golla (caste)",
    "Gollewar",
    "Gopal (caste)",
    "Goriya",
    "List of gotras",
    "Goud",
    "Gour (caste)",
    "Gowala (caste)",
    "Gowari",
    "Gudia (caste)",
    "Gudigar",
    "Guptan",
    "Gurjar",
    "Halba (tribe)",
    "Halpati",
    "Halwai",
    "Hatkar",
    "Hatwal",
    "Hebbars",
    "Heri (caste)",
    "Hilpulayan",
    "Holar caste",
    "Hoogar",
    "Hurkiya",
    "Idangai",
    "Idiga",
    "Ilayathu",
    "Isai Vellalar",
    "Iyengar",
    "Iyer",
    "Jaiswal (surname)",
    "Jalia Kaibarta",
    "Jāti",
    "Jats",
    "Jhamar (caste)",
    "Jhora",
    "Jogi (caste)",
    "Joisar",
    "Juang people",
    "Julaha",
    "Jyotish (caste)",
    "Kaarkaathaar",
    "Kadaiyar",
    "Kadia (Muslim)",
    "Kadia Kumbhar",
    "Kaikadi people",
    "Kaikalas",
    "Kalabaz",
    "Kalari Panicker",
    "Kalingi",
    "Kalita (caste)",
    "Kalwar (caste)",
    "Kamar (caste)",
    "Mukguhar",
    "Kamma (caste)",
    "Kammalar (caste)",
    "Kanakkan",
    "Kanet",
    "Kani tribe",
    "Kaniyar",
    "Kansabanik",
    "Kansara",
    "Kanyakubja Brahmin",
    "Kapariya",
    "Kapu (caste)",
    "Karmakar",
    "Kartha",
    "List of Kashmiri tribes",
    "Katesar",
    "Kathi people",
    "Kesarwani",
    "Kewat",
    "Khairaha",
    "Khant (caste)",
    "Kharol",
    "Kharwa caste",
    "Khati",
    "Khatik",
    "Khatri",
    "Kirar",
    "Kisan (caste)",
    "Koch (caste)",
    "Thakor",
    "Komati (caste)",
    "Konar (caste)",
    "Kondaikatti Vellalar",
    "Kongu Vellalar",
    "Koppula Velama",
    "Koraga people",
    "Koravar",
    "Kori (caste)",
    "Koshta",
    "Kota people (India)",
    "Kshatriya",
    "Kuchband",
    "Kudmi Mahato",
    "Kulala",
    "Kumawat",
    "Kumhar",
    "Kunbi",
    "Kuravar",
    "Kurichiya",
    "Kuruba",
    "Kushwaha",
    "Kuta (caste)",
    "Kuthaliya Bora",
    "Labana",
    "Labbay",
    "Lakhera",
    "Linga Balija",
    "Lodha",
    "Lohra (tribe)",
    "Lonari",
    "Lonaria",
    "Lonia",
    "Madiga",
    "Mahishya",
    "Mahton",
    "Mahuri",
    "Maiya",
    "Mal Muslim",
    "Mal (caste)",
    "Mala (caste)",
    "Malai Vellalar",
    "Malayarayan",
    "Mali caste",
    "Mang (caste)",
    "Manipuri Brahmin",
    "Mannan (caste)",
    "Maratha (caste)",
    "Mavilan",
    "Meenavar",
    "Cheetah Mehrat",
    "Menariya",
    "Meshuchrarim",
    "Mistri caste",
    "Hussaini Brahmin",
    "Mohyal Brahmin",
    "Moothan",
    "Motisar (caste)",
    "Mudiraju",
    "Mukkulathor",
    "Mukkuvar (India)",
    "Multani (caste)",
    "Muslim Dhobi",
    "Muthuraja",
    "Nadar (caste)",
    "Nadar climber",
    "Nador (caste)",
    "Nagarathar",
    "Nai (caste)",
    "Nair",
    "Nambiar (Ambalavasi caste)",
    "Nankudi Vellalar",
    "Narikurava",
    "Natrayat Rajputs",
    "Navnat",
    "Nayak (caste)",
    "Nethakani",
    "Niari",
    "Niyogi Brahmin",
    "Noongar (caste)",
    "Oswal",
    "Pachhimi",
    "Padhar",
    "Padmasali (caste)",
    "Padval",
    "Palayakkara Naicker",
    "Palayakkaran",
    "Pallar",
    "Panar (Kundapura)",
    "Pancha-Dravida",
    "Pancha-Gauda",
    "Panchkalshi",
    "Panikhia Jati",
    "Paniya people",
    "Pannaiyar",
    "Parahiya",
    "Paraiyar",
    "Paravar",
    "Patara (caste)",
    "Leva Patel",
    "Pathare Prabhu",
    "Pathare Prabhu (Kanchole)",
    "Patharkat",
    "Pathukudi",
    "Kadava Patidar",
    "Pattariyar",
    "Pattegar",
    "Patwa",
    "Gadaria people",
    "Pindari",
    "Purabi",
    "Puran (caste)",
    "Rajakulathor (caste)",
    "Rajapur Saraswat",
    "Rajput",
    "Raju",
    "Ramoshi",
    "Rathodia",
    "Raut (caste)",
    "Rautia",
    "Rawal (caste)",
    "Rayeen (Hindu)",
    "Relli (caste)",
    "Talk:Relli (caste)",
    "Roniaur",
    "Ror",
    "Sachora Brahmin",
    "Sadar Lingayats",
    "Sadh",
    "Sai Suthar",
    "Saini",
    "Salaat (caste)",
    "Saliya",
    "Salvi (caste)",
    "Samantan",
    "Sambandam",
    "Sansi people",
    "Sapera (Muslim)",
    "Sapera (Hindu)",
    "Sat-Sudra",
    "Satani (caste)",
    "Sathwara",
    "Sembadavar",
    "Sengunthar",
    "Shenva",
    "Shivalli Brahmins",
    "Shunri",
    "Sidh (community)",
    "Sikligar",
    "Siyal (caste)",
    "Sondhia",
    "Soni (caste)",
    "Sorathia",
    "Sundhi",
    "Sunga (caste)",
    "Sunwani",
    "Suthar",
    "Sutradhar (caste)",
    "Swakula Sali",
    "Tana Bhagats",
    "Tanti",
    "Tattama",
    "Telaga",
    "Teron",
    "Thampan",
    "Thandan (surname)",
    "Tharakan (Hindu caste)",
    "Thathagar",
    "Thathera",
    "Thigala",
    "Thirumulpad",
    "Thogata",
    "Thuluva Vellala",
    "Tili (caste)",
    "Tulu Gowda",
    "Turaiha",
    "Turi (caste)",
    "Turpu Kapu",
    "Tyagi",
    "Ulladan",
    "Uppara",
    "Vaddera",
    "Vaishya Vani",
    "Valan",
    "Valangai",
    "Vallanattu Chettiar",
    "Vannar",
    "Vanniyar",
    "Vanza",
    "Vanzha",
    "Variar",
    "Vatalia Prajapati",
    "Vathima",
    "Vatuka",
    "Velama",
    "Velar (caste)",
    "Vellalar",
    "Vettuva Gounder",
    "Vijayvargiya",
    "Yadav",
    "Yerukala people",
]

_COMMUNNITIES = [
    "Adaviyar",
    "Anariye Pirapur",
    "Are Katika",
    "Baduy people",
    "Bahun",
    "Balinese people",
    "Bamcha",
    "Banjara",
    "Bengali Hindus",
    "Bhanushali",
    "Bhil",
    "Bhumihar",
    "Bista",
    "Boudha Stupa",
    "Brittial Bania",
    "Bunt (community)",
    "Chakyar",
    "Chams",
    "Jatav",
    "Charan",
    "Charodi (community)",
    "Debbarma",
    "Devadiga",
    "Gandharv",
    "Gangota",
    "Ghasi",
    "Ghasiya",
    "Gondi people",
    "Gopa (caste)",
    "Gurjar Kshatriya Kadias",
    "Halpati",
    "Punjabi Hindus",
    "Jats",
    "Javanese Kshatriya",
    "Kabirpanthi Julaha",
    "Kadia Kumbhar",
    "Kadiya Suthar",
    "Kashmiri Hindus",
    "Kewat",
    "Khagi",
    "Khatik",
    "Koeri",
    "Krishna valley",
    "Kumbara",
    "Kushwaha",
    "Kutch Gurjar Kshatriya",
    "Lingayat Vani",
    "List of Lingayats",
    "Lonia",
    "Madhva Vaishnavas",
    "Mahyavanshi",
    "Cheetah Mehrat",
    "Mistri caste",
    "Mochi (Hindu)",
    "Hussaini Brahmin",
    "Mohyal Brahmin",
    "Nambiar (Ambalavasi caste)",
    "Nambidi",
    "Nambudiri",
    "Newar people",
    "Nishad",
    "Padharia",
    "Panika",
    "Patharkat",
    "Pathukudi",
    "Pattusali",
    "Porwal",
    "Pranami Sampradaya",
    "Rajput",
    "Rajputs in Bihar",
    "Rangrez",
    "Rattal",
    "Raval Yogi",
    "Sabar people",
    "Sai Suthar",
    "Sainthwar",
    "Samvedi",
    "Sapera (Hindu)",
    "Saryara",
    "Sindhi Hindus",
    "Siwakoti",
    "Soni (caste)",
    "Sutradhar (caste)",
    "Tamil Hindus",
    "Tana Bhagats",
    "Thakar (tribe)",
    "Tiar",
    "Tili (caste)",
    "Tripuri people",
    "Tulu Gowda",
    "Turha",
    "Valmiki caste",
    "Vankar",
    "Vatalia Prajapati",
    "Vokkaliga",
]

_OTHERS = [
    "OTHER",
]

_AGG = [*_CASTES, *_COMMUNNITIES, *_OTHERS]


insert_enum_values(CasteCommunity, _AGG)