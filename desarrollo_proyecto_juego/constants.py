#tamaños
WIDTH, HEIGHT= 800, 600
PLAYER = 100
GRASS = 64
TREE = 64
SMALL_STONE = 32

# Animaciones
BASIC_FRAMES = 6
IDLE_DOWN = 0
IDLE_RIGHT = 1
IDLE_UP = 2
WALK_DOWN = 3
WALK_RIGHT = 4
WALK_UP = 5
FRAME_SIZE = 32
ANIMATION_DELAY = 100

#colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)

#barras de estados
MAX_ENERGY = 100
MAX_FOOD = 100
MAX_THIRST = 100

#Colores para barras de estado
ENERGY_COLOR = (255, 255, 0) #AMARIILO
FOOD_COLOR = (255, 165, 0) #NARANJA
THIRST_COLOR = (0, 191, 255) #AZUL CLARO
BAR_BACKGROUND = (100,100,100) #GRIS OSCURO

#Intervalo de tiempo
STATUS_UPDATE_INTERVAL = 1000


# Sistema día/noche
DAY_LENGTH = 24000 # Duracion del dia en milisegundos (24 segundos)
DAWN_TIME = 6000 # Amanecer a las 6:00
MORNING_TIME = 8000 # Mañana completa a las 8:00
DUSK_TIME = 18000 # Atardecer a las 18:00
MIDNIGHT = 24000 # Medianoche (00:00)
MAX_DARKNESS = 200 #Nivel máximo de oscuridad (0-255)

# Colores para iluminación
NIGHT_COLOR = (20, 20, 50) # Color azul oscuro para la noche
DAY_COLOR = (255, 255, 255) # Color blanco para el día
DAWN_DUSK_COLOR = (255, 193, 137) # Color anaranjado para amanecer/atardecer