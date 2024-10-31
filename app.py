import streamlit as st
from PIL import Image
import numpy as np
import os
import tensorflow as tf
os.chdir('C:\\Visual Studio Code\\Bird-Species-Classification-main\\Bird-Species-Classification-main\\')

def load_image(image_file):
    img = Image.open(image_file)
    return img

# Create columns
col1, col2 = st.columns([1, 2])  # Adjust the width ratio as needed

# Add heading to the first column
with col1:
    st.image("logo.png")

# Add image to the second column
with col2:
    st.title("AVEPEDIA")
    

st.title("\"Kuş Türü Tanımlamanın Kolay Yolu\"")

import tensorflow as tf

# Define your custom F1_score metric
def F1_score(y_true, y_pred):
    def recall(y_true, y_pred):
        true_positives = tf.reduce_sum(tf.round(tf.clip_by_value(y_true * y_pred, 0, 1)))
        possible_positives = tf.reduce_sum(tf.round(tf.clip_by_value(y_true, 0, 1)))
        recall = true_positives / (possible_positives + tf.keras.backend.epsilon())
        return recall

    def precision(y_true, y_pred):
        true_positives = tf.reduce_sum(tf.round(tf.clip_by_value(y_true * y_pred, 0, 1)))
        predicted_positives = tf.reduce_sum(tf.round(tf.clip_by_value(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + tf.keras.backend.epsilon())
        return precision

    precision_value = precision(y_true, y_pred)
    recall_value = recall(y_true, y_pred)
    return 2 * ((precision_value * recall_value) / (precision_value + recall_value + tf.keras.backend.epsilon()))

# Register the custom metric
tf.keras.utils.get_custom_objects().update({"F1_score": F1_score})

# Load the model with the custom object scope
with tf.keras.utils.custom_object_scope({'F1_score': F1_score}):
    model = tf.keras.models.load_model('C:\\Visual Studio Code\\Bird-Species-Classification-main\\Bird-Species-Classification-main\\CNN_best_model.h5')

# Now you can use the model as usual
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
model = tf.keras.models.load_model('C:\\Visual Studio Code\\Bird-Species-Classification-main\\Bird-Species-Classification-main\\CNN_best_model.h5')

if image_file is not None:
    #Uplaod photos
    st.image(load_image(image_file), width=250)
    image = Image.open(image_file)
    image = image.resize((224, 224))
    image_arr = np.array(image.convert('RGB'))
    image_arr.shape = (1, 224, 224, 3)
    result = model.predict(image_arr)
    ind = np.argmax(result)
    accuracy = result[0][ind] * 100
    st.write(f"Tahmin Doğruluğu: {accuracy:.2f}%")

    # Display warning if accuracy is less than 90%
    if accuracy < 90:
        st.warning("Uyarı: Modelin doğruluk oranı %90'ın altında. Görsel tanımsız veya net değil.")
    else: 
        sorted_indices = np.argsort(result[0])[::-1]
        classes = bird_species = [
    "ABBOTTS BABBLER",
    "ABBOTTS BOOBY",
    "ABYSSINIAN GROUND HORNBILL",
    "AFRICAN CROWNED CRANE",
    "AFRICAN EMERALD CUCKOO",
    "AFRICAN FIREFINCH",
    "AFRICAN OYSTER CATCHER",
    "AFRICAN PIED HORNBILL",
    "AFRICAN PYGMY GOOSE",
    "ALBATROSS",
    "ALBERTS TOWHEE",
    "ALEXANDRINE PARAKEET",
    "ALPINE CHOUGH",
    "ALTAMIRA YELLOWTHROAT",
    "AMERICAN AVOCET",
    "AMERICAN BITTERN",
    "AMERICAN COOT",
    "AMERICAN DIPPER",
    "AMERICAN FLAMINGO",
    "AMERICAN GOLDFINCH",
    "AMERICAN KESTREL",
    "AMERICAN PIPIT",
    "AMERICAN REDSTART",
    "AMERICAN ROBIN",
    "AMERICAN WIGEON",
    "AMETHYST WOODSTAR",
    "ANDEAN GOOSE",
    "ANDEAN LAPWING",
    "ANDEAN SISKIN",
    "ANHINGA",
    "ANIANIAU",
    "ANNAS HUMMINGBIRD",
    "ANTBIRD",
    "ANTILLEAN EUPHONIA",
    "APAPANE",
    "APOSTLEBIRD",
    "ARARIPE MANAKIN",
    "ASHY STORM PETREL",
    "ASHY THRUSHBIRD",
    "ASIAN CRESTED IBIS",
    "ASIAN DOLLARD BIRD",
    "ASIAN GREEN BEE EATER",
    "ASIAN OPENBILL STORK",
    "AUCKLAND SHAQ",
    "AUSTRAL CANASTERO",
    "AUSTRALASIAN FIGBIRD",
    "AVADAVAT",
    "AZARAS SPINETAIL",
    "AZURE BREASTED PITTA",
    "AZURE JAY",
    "AZURE TANAGER",
    "AZURE TIT",
    "BAIKAL TEAL",
    "BALD EAGLE",
    "BALD IBIS",
    "BALI STARLING",
    "BALTIMORE ORIOLE",
    "BANANAQUIT",
    "BAND TAILED GUAN",
    "BANDED BROADBILL",
    "BANDED PITA",
    "BANDED STILT",
    "BARN OWL",
    "BARN SWALLOW",
    "BARRED PUFFBIRD",
    "BARROWS GOLDENEYE",
    "BAR-TAILED GODWIT",
    "BAY-BREASTED WARBLER",
    "BEARDED BARBET",
    "BEARDED BELLBIRD",
    "BEARDED REEDLING",
    "BELTED KINGFISHER",
    "BIRD OF PARADISE",
    "BLACK AND YELLOW BROADBILL",
    "BLACK BAZA",
    "BLACK BREASTED PUFFBIRD",
    "BLACK COCKATO",
    "BLACK FACED SPOONBILL",
    "BLACK FRANCOLIN",
    "BLACK HEADED CAIQUE",
    "BLACK NECKED STILT",
    "BLACK SKIMMER",
    "BLACK SWAN",
    "BLACK TAIL CRAKE",
    "BLACK THROATED BUSHTIT",
    "BLACK THROATED HUET",
    "BLACK THROATED WARBLER",
    "BLACK VENTED SHEARWATER",
    "BLACK VULTURE",
    "BLACKBURNIAM WARBLER",
    "BLACK-CAPPED CHICKADEE",
    "BLACK-NECKED GREBE",
    "BLACK-THROATED SPARROW",
    "BLONDE CRESTED WOODPECKER",
    "BLOOD PHEASANT",
    "BLUE COAU",
    "BLUE DACNIS",
    "BLUE GRAY GNATCATCHER",
    "BLUE GROSBEAK",
    "BLUE GROUSE",
    "BLUE HERON",
    "BLUE MALKOHA",
    "BLUE THROATED PIPING GUAN",
    "BLUE THROATED TOUCANET",
    "BOBOLINK",
    "BORNEAN BRISTLEHEAD",
    "BORNEAN LEAFBIRD",
    "BORNEAN PHEASANT",
    "BRANDT CORMARANT",
    "BREWERS BLACKBIRD",
    "BROWN CREPPER",
    "BROWN HEADED COWBIRD",
    "BROWN NOODY",
    "BROWN THRASHER",
    "BUFFLEHEAD",
    "BULWERS PHEASANT",
    "BURCHELLS COURSER",
    "BUSH TURKEY",
    "CAATINGA CACHOLOTE",
    "CABOTS TRAGOPAN",
    "CACTUS WREN",
    "CALIFORNIA CONDOR",
    "CALIFORNIA GULL",
    "CALIFORNIA QUAIL",
    "CAMPO FLICKER",
    "CANARY",
    "CANVASBACK",
    "CAPE GLOSSY STARLING",
    "CAPE LONGCLAW",
    "CAPE MAY WARBLER",
    "CAPE ROCK THRUSH",
    "CAPPED HERON",
    "CAPUCHINBIRD",
    "CARMINE BEE-EATER",
    "CASPIAN TERN",
    "CASSOWARY",
    "CEDAR WAXWING",
    "CERULEAN WARBLER",
    "CHARA DE COLLAR",
    "CHATTERING LORY",
    "CHESTNET BELLIED EUPHONIA",
    "CHESTNUT WINGED CUCKOO",
    "CHINESE BAMBOO PARTRIDGE",
    "CHINESE POND HERON",
    "CHIPPING SPARROW",
    "CHUCAO TAPACULO",
    "CHUKAR PARTRIDGE",
    "CINNAMON ATTILA",
    "CINNAMON FLYCATCHER",
    "CINNAMON TEAL",
    "CLARKS GREBE",
    "CLARKS NUTCRACKER",
    "COCK OF THE  ROCK",
    "COCKATOO",
    "COLLARED ARACARI",
    "COLLARED CRESCENTCHEST",
    "COMMON FIRECREST",
    "COMMON GRACKLE",
    "COMMON HOUSE MARTIN",
    "COMMON IORA",
    "COMMON LOON",
    "COMMON POORWILL",
    "COMMON STARLING",
    "COPPERSMITH BARBET",
    "COPPERY TAILED COUCAL",
    "CRAB PLOVER",
    "CRANE HAWK",
    "CREAM COLORED WOODPECKER",
    "CRESTED AUKLET",
    "CRESTED CARACARA",
    "CRESTED COUA",
    "CRESTED FIREBACK",
    "CRESTED KINGFISHER",
    "CRESTED NUTHATCH",
    "CRESTED OROPENDOLA",
    "CRESTED SERPENT EAGLE",
    "CRESTED SHRIKETIT",
    "CRESTED WOOD PARTRIDGE",
    "CRIMSON CHAT",
    "CRIMSON SUNBIRD",
    "CROW",
    "CUBAN TODY",
    "CUBAN TROGON",
    "CURL CRESTED ARACURI",
    "DALMATIAN PELICAN",
    "DARJEELING WOODPECKER",
    "DARK EYED JUNCO",
    "D-ARNAUDS BARBET",
    "DAURIAN REDSTART",
    "DEMOISELLE CRANE",
    "DOUBLE BARRED FINCH",
    "DOUBLE BRESTED CORMARANT",
    "DOUBLE EYED FIG PARROT",
    "DOWNY WOODPECKER",
    "DUNLIN",
    "DUSKY LORY",
    "DUSKY ROBIN",
    "EARED PITA",
    "EASTERN BLUEBIRD",
    "EASTERN BLUEBONNET",
    "EASTERN GOLDEN WEAVER",
    "EASTERN MEADOWLARK",
    "EASTERN ROSELLA",
    "EASTERN TOWEE",
    "EASTERN WIP POOR WILL",
    "EASTERN YELLOW ROBIN",
    "ECUADORIAN HILLSTAR",
    "EGYPTIAN GOOSE",
    "ELEGANT TROGON",
    "ELLIOTS  PHEASANT",
    "EMERALD TANAGER",
    "EMPEROR PENGUIN",
    "EMU",
    "ENGGANO MYNA",
    "EURASIAN BULLFINCH",
    "EURASIAN GOLDEN ORIOLE",
    "EURASIAN MAGPIE",
    "EUROPEAN GOLDFINCH",
    "EUROPEAN TURTLE DOVE",
    "EVENING GROSBEAK",
    "FAIRY BLUEBIRD",
    "FAIRY PENGUIN",
    "FAIRY TERN",
    "FAN TAILED WIDOW",
    "FASCIATED WREN",
    "FIERY MINIVET",
    "FIORDLAND PENGUIN",
        "FIRE TAILLED MYZORNIS",
    "FLAME BOWERBIRD",
    "FLAME TANAGER",
    "FOREST WAGTAIL",
    "FRIGATE",
    "FRILL BACK PIGEON",
    "GAMBELS QUAIL",
    "GANG GANG COCKATOO",
    "GILA WOODPECKER",
    "GILDED FLICKER",
    "GLOSSY IBIS",
    "GO AWAY BIRD",
    "GOLD WING WARBLER",
    "GOLDEN BOWER BIRD",
    "GOLDEN CHEEKED WARBLER",
    "GOLDEN CHLOROPHONIA",
    "GOLDEN EAGLE",
    "GOLDEN PARAKEET",
    "GOLDEN PHEASANT",
    "GOLDEN PIPIT",
    "GOULDIAN FINCH",
    "GRANDALA",
    "GRAY CATBIRD",
    "GRAY KINGBIRD",
    "GRAY PARTRIDGE",
    "GREAT ARGUS",
    "GREAT GRAY OWL",
    "GREAT JACAMAR",
    "GREAT KISKADEE",
    "GREAT POTOO",
    "GREAT TINAMOU",
    "GREAT XENOPS",
    "GREATER PEWEE",
    "GREATER PRAIRIE CHICKEN",
    "GREATOR SAGE GROUSE",
    "GREEN BROADBILL",
    "GREEN JAY",
    "GREEN MAGPIE",
    "GREEN WINGED DOVE",
    "GREY CUCKOOSHRIKE",
    "GREY HEADED CHACHALACA",
    "GREY HEADED FISH EAGLE",
    "GREY PLOVER",
    "GROVED BILLED ANI",
    "GUINEA TURACO",
    "GUINEAFOWL",
    "GURNEYS PITTA",
    "GYRFALCON",
    "HAMERKOP",
    "HARLEQUIN DUCK",
    "HARLEQUIN QUAIL",
    "HARPY EAGLE",
    "HAWAIIAN GOOSE",
    "HAWFINCH",
    "HELMET VANGA",
    "HEPATIC TANAGER",
    "HIMALAYAN BLUETAIL",
    "HIMALAYAN MONAL",
    "HOATZIN",
    "HOODED MERGANSER",
    "HOOPOES",
    "HORNED GUAN",
    "HORNED LARK",
    "HORNED SUNGEM",
    "HOUSE FINCH",
    "HOUSE SPARROW",
    "HYACINTH MACAW",
    "IBERIAN MAGPIE",
    "IBISBILL",
    "IMPERIAL SHAQ",
    "INCA TERN",
    "INDIAN BUSTARD",
    "INDIAN PITTA",
    "INDIAN ROLLER",
    "INDIAN VULTURE",
    "INDIGO BUNTING",
    "INDIGO FLYCATCHER",
    "INLAND DOTTEREL",
    "IVORY BILLED ARACARI",
    "IVORY GULL",
    "IWI",
    "JABIRU",
    "JACK SNIPE",
    "JACOBIN PIGEON",
    "JANDAYA PARAKEET",
    "JAPANESE ROBIN",
    "JAVA SPARROW",
    "JOCOTOCO ANTPITTA",
    "KAGU",
    "KAKAPO",
    "KILLDEAR",
    "KING EIDER",
    "KING VULTURE",
    "KIWI",
    "KNOB BILLED DUCK",
    "KOOKABURRA",
    "LARK BUNTING",
    "LAUGHING GULL",
    "LAZULI BUNTING",
    "LESSER ADJUTANT",
    "LILAC ROLLER",
    "LIMPKIN",
    "LITTLE AUK",
    "LOGGERHEAD SHRIKE",
    "LONG-EARED OWL",
    "LOONEY BIRDS",
    "LUCIFER HUMMINGBIRD",
    "MAGPIE GOOSE",
    "MALABAR HORNBILL",
    "MALACHITE KINGFISHER",
    "MALAGASY WHITE EYE",
    "MALEO",
    "MALLARD DUCK",
    "MANDRIN DUCK",
    "MANGROVE CUCKOO",
    "MARABOU STORK",
    "MASKED BOBWHITE",
    "MASKED BOOBY",
    "MASKED LAPWING",
    "MCKAYS BUNTING",
    "MERLIN",
    "MIKADO  PHEASANT",
    "MILITARY MACAW",
    "MOURNING DOVE",
    "MYNA",
    "NICOBAR PIGEON",
    "NOISY FRIARBIRD",
    "NORTHERN BEARDLESS TYRANNULET",
    "NORTHERN CARDINAL",
    "NORTHERN FLICKER",
    "NORTHERN FULMAR",
    "NORTHERN GANNET",
    "NORTHERN GOSHAWK",
    "NORTHERN JACANA",
    "NORTHERN MOCKINGBIRD",
    "NORTHERN PARULA",
    "NORTHERN RED BISHOP",
    "NORTHERN SHOVELER",
    "OCELLATED TURKEY",
    "OILBIRD",
    "OKINAWA RAIL",
    "ORANGE BRESTED BUNTING",
    "ORANGE BRESTED TROGON",
    "ORCHARD ORIOLE",
    "OSPREY",
    "OSTRICH",
    "OVENBIRD",
    "OXPECKER",
    "OYSTER CATCHER",
    "PAINTED BUNTIG",
    "PALILA",
    "PALM NUT VULTURE",
    "PARADISE TANAGER",
    "PARUS MAJOR",
    "PATAGONIAN SIERRA FINCH",
    "PEACOCK",
    "PEACOCK PHEASANT",
    "PELICAN",
    "PELICAN GULL",
    "PEREGRINE FALCON",
    "PHARAOH EAGLE OWL",
    "PHEASANT COUCAL",
    "PINK ROBIN",
    "PINK SPARROW",
    "PINK-EARED DUCK",
    "POMARINE JAEGER",
    "PUFFIN",
    "PURPLE GALLINULE",
    "PURPLE MARTIN",
    "PURPLE SWAMPHEN",
    "PYGMY GOOSE",
    "QUETZAL",
    "RAINBOW LORIKEET",
    "RAZORBILL",
    "RED BEE EATER",
    "RED BILLED CHOUGH",
    "RED BILLED QUELEA",
    "RED BILLED TROPICBIRD",
    "RED BROWED FINCH",
    "RED CHEEKED CORDON BLEU",
    "RED FACED CORMORANT",
    "RED FACED WARBLER",
    "RED FODY",
    "RED HEADED DUCK",
    "RED HEADED WOODPECKER",
    "RED HONEY CREEPER",
    "RED LEGGED KITTELATE",
    "RED LEGGED SERIEMA",
    "RED LORE PARROT",
    "RED SHOULDERED HAWK",
    "RED TAILED HAWK",
    "RED TAILED THRUSH",
    "RED WINGED BLACKBIRD",
    "RED WISKERED BULBUL",
    "REGENT BOWERBIRD",
    "RESPLENDENT QUETZAL",
    "RHEA",
    "RHINOCEROS HORNBILL",
    "RIFLEMAN",
    "ROBIN",
    "ROCK DOVE",
    "ROCK PTARMIGAN",
    "ROSE BREASTED COCKATOO",
    "ROSE BREASTED GROSBEAK",
    "ROSY FACED LOVEBIRD",
    "ROUGH LEG BUZZARD",
    "ROWIS RAIL",
    "ROYAL FLYCATCHER",
    "RUFOUS KINGFISHER",
    "RUFOUS NIGHTJAR",
    "RUFOUS TAILED HUMMINGBIRD",
    "RUDDY DUCK",
    "RUDDY KINGFISHER",
    "RUDDY TURNSTONE",
    "RUFF",
    "SAGE THRASHER",
    "SANDERLING",
    "SANDHILL CRANE",
    "SANDPIPER",
    "SATYR TRAGOPAN",
    "SCARLET IBIS",
    "SCARLET MACAW",
    "SCARLET TANAGER",
    "SHOEBILL",
    "SHORT-EARED OWL",
    "SILVER GULL",
    "SINGING QUAIL",
    "SNOW BUNTING",
    "SNOW PETREL",
    "SNOWY EGRET",
    "SNOWY OWL",
    "SORA",
    "SPANGLED COTINGA",
    "SPOONBILL",
    "SPOTTED BOWERBIRD",
    "SPOTTED CATBIRD",
    "SPOTTED DOVE",
    "SPOTTED LIZARD",
    "SPOTTED OWLET",
    "SPOTTED TANAGER",
    "SPOTTED TOWHEE",
    "SRI LANKA BLUE MAGPIE",
    "STARLING",
    "STELLERS EIDER",
    "STEAMER DUCK",
    "STORK BILLED KINGFISHER",
    "STRAWBERRY FINCH",
    "STRIPPED OWL",
    "STRIPPED-TAILED HUMMINGBIRD",
    "STRIPPED-TAILED TAWNY OWL",
    "STUBBORN MALEO",
    "SULPHUR CRESTED COCKATOO",
    "SUPERB FRUIT DOVE",
    "SWINHOES PHEASANT",
    "TAIWAN BLUE MAGPIE",
    "TAKAH",
    "TANGARA",
    "TAPACULO",
    "TAVETA GOLDEN WEAVER",
    "TAXE",
    "TENNESSEE WARBLER",
    "TERRITORY BIRD",
    "THICK-BILLED PARROT",
    "THREE WATTLED BELLBIRD",
    "THRUSH",
    "TINAMOU",
    "TOUCAN",
    "TRUMPETER SWAN",
    "TUI",
    "TURQUOISE JAY",
    "TURQUOISE PARROT",
    "TWANY FROGMOUTH",
    "VARIED BUNTING",
    "VERDIN",
    "VICTORIA CROWNED PIGEON",
    "VILLAGE INDIGOBIRD",
    "VIOLET CUCKOO",
    "VIREO",
    "VULTURINE GUINEAFOWL",
    "WALL CREEPER",
    "WANDERING ALBATROSS",
    "WARBLER",
    "WATTLED IBIS",
    "WATTLED JACANA",
    "WEDGE TAIL EAGLE",
    "WESTERN BOWERBIRD",
    "WESTERN GULL",
    "WESTERN MARSH HARRIER",
    "WESTERN REEF HERON",
    "WESTERN SCRUB JAY",
    "WHITE BROWED CRAKE",
    "WHITE CHEEKED PINTAIL",
    "WHITE COLLARED MANAKIN",
    "WHITE CRESTED TURACO",
    "WHITE FACED HERON",
    "WHITE IBIS",
    "WHITE NECKED PETREL",
    "WHITE TERN",
    "WILD TURKEY",
    "WILSON BIRD OF PARADISE",
    "WILSONS PLOVER",
    "WOOD DUCK",
    "WOOD THRUSH",
    "WOODLAND KINGFISHER",
    "WRYNECK",
    "YELLOW BELLIED FLOWERPECKER",
    "YELLOW BELLIED FLYCATCHER",
    "YELLOW BELLIED SISKIN",
    "YELLOW BIRD OF PARADISE",
    "YELLOW CACIQUE",
    "YELLOW HEADED BLACKBIRD",
    "YELLOW HEADED CARACARA",
    "YELLOW LEGGED GULL",
    "YELLOW TAILED BLACK COCKATOO",
    "YELLOW THROATED WARBLER",
    "YOUNG COCOKATOO",
    "ZEBRA FINCH",
    "ZEBRA DOVE"]

        st.header(f"1. Tahmin: {classes[ind]}")
        st.write(f"2. Tahmin: {classes[sorted_indices[1]]}")
        st.write(f"3. Tahmin: {classes[sorted_indices[2]]}")
        
    