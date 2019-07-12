PRODUCT_CHOICES = [
    ('24', '24'),
    ('26', '26'),
    ('28', '28'),
    ('30', '30'),
    ('32', '32'),
    ('34', '34'),
    ('36', '36'),
    ('38', '38'),
    ('40', '40'),
]

MALE = 'M'
FEMALE = 'F'
BOTH = 'B'
GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (BOTH, 'Both')
]

HALFSLEEVES = 'HS'
FULLSLEEVES = 'FS'
HALFPANTS = 'HP'
FULLPANTS = 'FP'
PRODUCT_TYPE_CHOICES = [
    (HALFSLEEVES, 'HALF SLEEVES'),
    (FULLSLEEVES, 'FULL SLEEVES'),
    (HALFPANTS, 'HALF PANTS'),
    (FULLPANTS, 'FULL PANTS')
]

PERCENTAGE = 'P'
AMOUNT = 'A'
OTHER = 'O'

DISCOUNT_CHOICES = [
    (PERCENTAGE, 'PERCENTAGE'),
    (AMOUNT, 'AMOUNT'),
    (OTHER,'OTHER')
]
