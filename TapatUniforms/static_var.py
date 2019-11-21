PRODUCT_CHOICES = [
    ("20", "20"),
    ("22", "22"),
    ("24", "24"),
    ("26", "26"),
    ("28", "28"),
    ("30", "30"),
    ("32", "32"),
    ("34", "34"),
    ("36", "36"),
    ("38", "38"),
    ("40", "40"),
    ("42", "42"),
    ("44", "44"),
]

MALE = "M"
FEMALE = "F"
OTHER = "O"
GENDER_CHOICES = [(MALE, "Male"), (FEMALE, "Female"), (OTHER, "Other")]
CLASS_CHOICES = [
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
    ("IV", "IV"),
    ("V", "V"),
    ("VI", "VI"),
    ("VII", "VII"),
    ("VIII", "VIII"),
    ("IX", "IX"),
    ("X", "X"),
    ("XI", "XI"),
    ("XII", "XII"),
]
SECTION_CHOICES = [("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")]
HALFSLEEVES = "HS"
FULLSLEEVES = "FS"
HALFPANTS = "HP"
FULLPANTS = "FP"
PRODUCT_TYPE_CHOICES = [
    (HALFSLEEVES, "HALF SLEEVES"),
    (FULLSLEEVES, "FULL SLEEVES"),
    (HALFPANTS, "HALF PANTS"),
    (FULLPANTS, "FULL PANTS"),
]

PERCENTAGE = "P"
AMOUNT = "A"
OTHER = "O"

DISCOUNT_CHOICES = [(PERCENTAGE, "PERCENTAGE"), (AMOUNT, "AMOUNT"), (OTHER, "OTHER")]
